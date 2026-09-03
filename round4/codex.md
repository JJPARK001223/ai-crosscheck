# Round 4 Codex blind 독립 분석 — FE 재현 계획

## 검토 범위와 한계

- 읽은 파일: `round4/_codex_task.md`, `round4/PROBLEM.md`, `round4/FE재현계획.html`, `round4/01_current.py`, `round4/02_current.py`.
- blind 원칙에 따라 `round4/claude.md`는 열지 않았다.
- 이 환경에는 Abaqus 실행 파일과 ODB가 없어 스크립트 실행 및 수치 재현은 하지 못했다.
- Abaqus 2020/2021 **공식 Scripting Reference 원문은 공개 웹에서 접근할 수 없었다.** 따라서 그 판본에 한정한 API 서명 확인은 아래에 명시적으로 “확인 불가”로 둔다. 다만 공개된 Abaqus 공식 해석/키워드 문서와 공개 Scripting Reference의 동일 항목을 보조 근거로 구분해 사용했다.

## 판정 요약

| 항목 | 판정 | 핵심 이유 |
|---|---|---|
| 1. 논문 방법 및 ContourIntegral | **부분적 정정 필요** | 반모델 개념은 타당하나 곡선맞춤 응력 성분이 잘못됐고, `crackNormal` 형식도 공개 Scripting Reference와 불일치한다. 현재 메시/후처리는 3D crack-front별 K를 보존하지 않는다. |
| 2. 15식 및 하중 규약 | **부분적 정정 필요** | 반모델에 총하중의 절반을 적용하고 얻은 K를 총하중으로 나누는 규약은 맞다. 그러나 논문 K와 표준 KI의 `sqrt(2π)` 관계를 실제 데이터 처리에서 강제하는 절차가 없다. |
| 3. 강체구속 | **부분적 정정 필요** | 의도한 세 구속은 연속체의 6개 강체모드를 제거하지만, 현 코드의 `Z=W/2` 점은 기하학적 vertex가 아니어서 선택 실패 후 U3 BC가 조용히 생략될 가능성이 높다. |
| 4. 무차원화 | **틀림** | `K/(P H^{-3/2})=K H^{3/2}/P`는 차원은 없지만 폭비가 다른 H=50,100을 형상계수로 겹치게 하지 못한다. 표준 비교량은 `K_I B sqrt(H)/P`이다. |
| 5. 2D/3D 역할 | **부분적 정정 필요** | 논문 재현의 주 계산은 2D 4절점 모델이어야 하고, 3D는 폭 방향 균일성 확인용이어야 한다. 다만 `Y=K²/E`만으로 논문이 평면응력을 명시했다고 단정할 수는 없다. |
| 6. 누락·오류·과잉 | **부분적 정정 필요** | 반력 검산, 경로/메시 수렴, 응력 위치·평균화 통제, crack-front 위치별 출력, 기준해 비교, 실제 시험값 표가 필요하다. 임의 ±5% 기준과 단순 contour 평균은 근거가 없다. |

## 1. 논문 §4.2–4.3 방법과 ContourIntegral

### 1.1 형상·BC와 곡선맞춤

절반 길이 모델에서 `X=L/2`의 리거먼트(`Y>=a`)에 `U1=0`, 같은 면의 노치/균열면(`Y<a`)은 자유면, 반대쪽 지지선에 `U2=0`, 중앙 하중의 절반을 적용하는 구성은 대칭 3점굽힘 반모델로 물리적으로 일관된다. 다만 실제 논문 도면/본문과의 문구별 대조는 제공된 파일과 공개 논문 정보의 범위에서만 확인했으며, 실험 지그의 접촉·롤러 반경까지 재현한 것은 아니다.

계획서 경로 A의 `sigma_yy`는 현재 좌표계에서 **틀리다**. 균열면은 `X=L/2`, 개구 방향/균열면 법선은 X, 균열 성장선은 +Y이므로 균열 전방(`s=Y-a`)의 모드-I 개구 정상응력은 `sigma_xx=S11`이다. `sigma_yy=S22`는 균열 성장방향 응력이다. 따라서 경로 A는 `S11(s)` 또는 최대주응력을 쓰되 논문이 실제로 정의한 `sigma_e`와 동일한 성분인지 먼저 고정해야 한다.

또한 다음이 빠졌다.

1. 표준 LEFM의 전방응력은 `sigma_xx = K_I/sqrt(2*pi*s)`이다. 논문의 맞춤계수 `K`가 `sigma_e=K/sqrt(s)`라면 `K=K_I/sqrt(2*pi)`이다. 경로 A와 B를 비교할 때 반드시 `K_I/sqrt(2*pi)`와 `K_fit`을 비교해야 한다.
2. `s`는 팁에서 요소 중심/적분점까지의 물리 거리로 정의하고, 절점 평균(extrapolation/averaging) 여부를 고정해야 한다. 특이점 바로 위 nodal-averaged stress는 맞춤용 원자료로 부적절할 수 있다.
3. 기울기를 자유롭게 적합해 `-1/2` 근접성을 먼저 확인한 뒤, 채택 구간에서는 기울기 `-1/2` 고정 적합도 병기해야 한다. 적합창 이동과 메시 세분화에 따른 K 변화도 보고해야 한다.

### 1.2 `ContourIntegral` 인자

**Abaqus 2020/2021 공식 Scripting Reference 판본 확인: 확인 불가.** 해당 판본의 공식 온라인 Scripting Reference 페이지에 접근하지 못했으므로 그 판본의 Python 인자 형식을 확인했다고 주장하지 않는다.

다만 공개된 Abaqus 공식 해석 문서는 다음을 명확히 한다.

- `NORMAL`은 **균열면의 법선 n**이다. Abaqus는 3D에서 crack-front 접선 t와 n으로부터 가상 균열확장 방향 `q=t×n`을 계산한다. 즉 `CRACK_NORMAL`일 때 `crackNormal`은 성장방향이 아니다.
- `SYMM`은 대칭면상의 half-crack에 대해 가상 균열진전에 따른 퍼텐셜에너지 변화를 두 배 하여 올바른 contour integral을 계산한다. 따라서 `symmetric=True` 때문에 K가 절반으로 출력된다고 보고 추가 2배 또는 `sqrt(2)` 보정을 하면 안 된다.

공개된 Scripting Reference(구판 및 2019.2 API 미러)의 `ContourIntegral` 설명은 `crackNormal`을 “벡터를 정하는 두 점의 sequence of sequences”로 규정한다. 따라서 현재 `crackNormal=(1.0,0.0,0.0)`은 그 서명과 맞지 않으며, 예컨대 원점에서 +X로 향하는 두 점 `((0.0,0.0,0.0),(1.0,0.0,0.0))` 형식이어야 한다. 단, 이를 Abaqus 2020/2021 공식 판본에서 직접 확인하지 못했으므로 최종 실행 전 설치본의 `getMethod('ContourIntegral')`/CAE replay 또는 로컬 Scripting Reference로 재확인해야 한다.

물리 방향은 crack-front 접선이 +Z로 정렬됐다는 전제에서 `n=+X`이면 `q=+Y`라서 맞다. 그러나 edge의 내부 순서가 반대이면 t와 q의 부호가 바뀔 수 있으므로 `.dat`의 contour-integral crack-front/extension-direction 출력 또는 J 부호로 확인해야 한다.

`crackFront=crackRegion`, `crackTip=crackRegion` 자체는 날카로운 3D 직선 crack line에서 가능할 수 있지만, 현재 `getByBoundingBox`가 정확히 한 edge를 선택하는지 길이와 좌표를 assert해야 한다. 더 중요한 문제는 자유 C3D10 메시가 crack front를 따라 여러 절점으로 나누는데, `02_current.py`가 모든 `K1` history region을 단일 리스트로 평탄화한다는 점이다. 이 리스트는 contour 번호뿐 아니라 crack-front 위치도 섞을 수 있어 “첫 contour 제외 후 평균”이 아니다.

근거: Dassault Systèmes, *Abaqus Analysis Guide—Contour Integral Evaluation* (공개 2025 문서, 정의는 해당 기능의 기본식), `https://docs.software.vt.edu/abaqusv2025/English/SIMACAEANLRefMap/simaanl-c-contintegral.htm`; Dassault Systèmes, *Abaqus Keywords Reference—*CONTOUR INTEGRAL*, `https://docs.software.vt.edu/abaqusv2025/English/SIMACAEKEYRefMap/simakey-r-contourintegral.htm`; Dassault Systèmes, *Abaqus Scripting User's Reference Guide*, §19.3.1 (공개 2016 PDF), `https://ceae-server.colorado.edu/v2016/pdf_books/SCRIPT.pdf`. 마지막 자료는 2020/2021 판본이 아니므로 형식 확인의 보조자료일 뿐이다.

## 2. 15식 경로와 하중 환산

하중 규약은 **맞다**. 전체 시편의 중앙 총하중을 `P0`라 정의하면, 길이방향 절반 모델에는 잘린 하중 패치의 합력이 `P0/2`가 되도록 압력을 적용한다. 이 해의 국부 K는 전체 시편이 총하중 `P0`를 받을 때의 물리적 K와 같다. `symmetric=True`는 crack energy 계산을 보정하는 옵션이지 외력 또는 K를 다시 절반으로 만드는 옵션이 아니다. 그러므로 `K/P_total = K_output/P0`가 일관되며, `K_output/(P0/2)`로 나누면 2배 오류다.

식 10의 “무차원 거리를 쓰면 `sqrt(ell0)`를 복원” 지적은 맞지만, 실제 추가 스크립트가 없으므로 구현된 것은 아니다. 식 12–14도 경로 A의 논문 K와 경로 B의 표준 KI를 구별하는 열/변수명과 자동 변환이 필요하다. 현재 `02_current.py`의 `K1_avg`를 그대로 논문 K로 역산하면 `2*pi` 계수 오류가 생긴다.

`DECISION.md §7.2`와의 대조는 이번 blind 입력 범위에 포함되지 않아 하지 않았다. 제공된 계획서 내부의 15식 매핑만 독립 검토했다.

## 3. 강체이동 구속

**Abaqus 2020/2021 공식 Scripting Reference에 의한 확인: 확인 불가.** 경계조건 조합의 충분성은 API 서명 문제가 아니라 연속체 강체모드의 선형독립성 문제이며, 해당 판본 공식 문서 원문에도 접근하지 못했다. 아래 판정은 강체운동 `u=t+omega×r`에 직접 대입한 역학 검산이다.

의도대로 적용된다면 충분하다. 리거먼트의 2D 면에 `U1=0`은 `t1, omega2, omega3`을, `X=0,Y=0` 폭 전체 선의 `U2=0`은 `t2, omega1`을 제거하고, 그 선 위 한 점의 `U3=0`은 남은 `t3`를 제거한다. 즉 6개 강체모드가 모두 제거된다. 한 점 U3는 폭방향 포아송 변형을 과도하게 막지 않는 최소 구속이다.

그러나 현 코드는 의도대로 적용될 가능성이 낮다. 압출 직육면체의 `X=0,Y=0` edge에는 보통 `Z=0,W` 끝의 vertex만 있고 `Z=W/2`에는 vertex가 없다. `centerVerts=getByBoundingBox(...Z=W/2...)`는 빈 배열이 될 수 있으며, 코드는 `if len(centerVerts)>0` 때문에 경고 없이 BC를 생략한다. 그러면 폭방향 강체병진 `t3`가 남아 singular matrix가 된다.

수정은 둘 중 하나다.

- 지지 edge를 `Z=W/2`에서 분할해 실제 vertex를 만든 뒤 정확히 1개인지 assert하고 U3=0을 준다.
- 더 안정적으로 `Z=W/2` 폭대칭면까지 잘라 1/4 모델을 만들고 그 면에 ZSYMM(`U3=0`)을 준다. 하중과 형상·재료가 폭방향 대칭이므로 성립한다. 다만 3D 목적이 자유표면부터 중앙면까지 K(z) 확인이라면 폭의 절반(`0..W/2`)을 모델링해 한쪽 자유표면과 중앙 대칭면을 모두 보존해야 한다.

`symFaces`, `supportEdges`, `loadFaces`, `crackEdges`도 각각 예상 개수를 assert하지 않으면 bounding-box 과선택/무선택이 조용히 통과할 수 있다.

## 4. H=50 대 H=100 무차원화

`K/(P H^{-3/2}) = K H^{3/2}/P`는 단위상 무차원이다(`K`의 차원은 힘·길이^(-3/2)). 그러나 이것은 표준 SENB 형상계수가 아니다. SENB의 대표식은

`K_I = [P S/(B H^(3/2))] F(a/H)`

이므로 같은 `a/H`와 `S/H`에서 크기·폭비와 무관한 비교량은

`K_I B sqrt(H)/P = (S/H) F(a/H)`

이다. 필요하면 `(K_I B sqrt(H)/P)/(S/H)`를 써서 `F(a/H)` 자체를 비교한다. 여기서 `B=W=100 mm`는 두 군 모두 수치상 같지만 `B/H`는 2와 1로 달라진다. 따라서 B가 “같아서 상쇄”되는 것이 아니다. 기존 `K H^(3/2)/P`는 표준량에 `H/B`가 곱해져 H=100 결과가 H=50보다 인위적으로 2배 이동한다. 계획서 마지막 판정 기준은 위 식으로 교체해야 한다.

## 5. 2D와 3D의 역할

논문 방법의 재현이 목적이면 6케이스 주 계산은 논문과 같은 2D 4절점 요소, 3D는 대표 케이스 1개 이상에서 K의 폭방향 균일성과 자유표면 영향을 확인하는 역할로 나누는 편이 맞다. 현 `01_current.py`의 3D C3D10 자유메시 6회는 논문과 요소·차원·추출법이 동시에 달라 직접 재현이 아니라 별도 모델 검증이다. 계산비용도 불필요하게 크다.

다만 `Y=K^2/E`라는 식만 보고 2D를 평면응력으로 **확정**하는 것은 부족하다. 그 식의 K가 논문 정의 `K=K_I/sqrt(2*pi)`인지, 저자들이 유효탄성률 `E'`를 생략했는지와 별개로 FE 요소의 plane stress/strain 선택은 논문 §4.2의 요소명·가정으로 확인해야 한다. 제공 자료만으로는 **확인 불가**다. 우선 논문의 정확한 4절점 요소/두께 규약을 확인하고, 명시가 없으면 3D 중앙부와 `K/P`가 맞는 가정을 선택하되 두 가정의 민감도를 보고해야 한다.

## 6. 구체적 수정사항과 빠진 필수 절차

### `round4/FE재현계획.html`

1. §4 경로 A의 `sigma_yy`를 현 좌표계 기준 `sigma_xx=S11`로 고치고, 논문 `sigma_e`의 정확한 정의를 원문에서 재확인한다.
2. `K_fit=K_I/sqrt(2*pi)` 변환, 적분점 응력 사용, 평균화 설정, 자유기울기/고정기울기 적합, 적합창·메시 수렴을 명시한다.
3. 경로 B의 `crackNormal`을 균열 성장방향이 아니라 균열면 법선으로 설명하고, Python 인자는 두 점 형식으로 수정한다. 2020/2021 설치 문서 확인을 실행 전 게이트로 둔다.
4. “첫 1–2 contour 제외 후 나머지 평균”을 자동 규칙으로 두지 말고, crack-front 위치별로 contour plateau를 확인해 경로독립 구간을 선택한다.
5. §7의 무차원량을 `K_I W sqrt(H)/P`(또는 이를 `S/H`로 나눈 F)로 교체한다.
6. 주 워크플로우를 “2D 6케이스 + 3D 대표 케이스”로 바꾸고, 3D에서는 `K(z)`를 자유표면과 중앙면 위치별로 보존한다.
7. 반력 합계가 `P0/2`인지, 전체 시편 환산 반력이 `P0`인지 검산하는 단계를 넣는다.
8. Fig. 11 눈대중 값이 아니라 Karihaloo 원 데이터의 정확한 케이스 조합·폭·스팬·파괴하중을 표로 확정한다. 이 입력이 확정되지 않으면 정량 재현 판정은 할 수 없다.
9. 임의의 “±5% 일치”를 문헌 기반 허용오차 또는 메시/데이터 불확도 예산으로 대체한다.

### `round4/01_current.py`

- 24–26, 39행: `H_LIST=(50,100)` 이중 루프로 바꾸고 H로부터 L, a, 원거리 메시, 스트립을 케이스 내부에서 계산한다. job/model/tag에 H를 포함한다.
- 70–78행: 논문 주 재현은 별도 2D 4절점 모델로 작성한다. 3D contour 검증 모델은 crack-front 주위 구조화/집중 메시와 최소 3단계 메시 수렴을 사용한다. 단순 `seedEdgeBySize` 뒤 전역 free C3D10만으로 “팁 0.3 mm 요소”가 보장되는지 확인할 수 없다.
- 90–94행: `symFaces`의 개수와 면의 중심/범위를 assert한다.
- 97–108행: `centerVerts`가 정확히 1개인지 assert하고, 없다면 edge를 Z 중앙에서 partition한다. 현재처럼 빈 선택을 묵살하지 않는다. 권장안은 폭 절반 모델과 ZSYMM이다.
- 110–116행: 선택 면적을 계산해 실제 합력 `pressure*area=P0/2`를 assert하고, 해석 후 RF2 합계도 검산한다. 압력 부호도 확인한다.
- 119–132행: `crackEdges`가 의도한 직선 하나/연속 crack front인지 검증한다. `crackNormal=((0,0,0),(1,0,0))`처럼 두 점으로 바꾸되 Abaqus 2020/2021 설치본 서명을 먼저 확인한다. 생성 후 `.dat`에서 q가 +Y인지 확인한다.
- 134–136행: `kFactor=ON`의 K1뿐 아니라 J도 출력해 `J=K_I^2/E'` 검산을 추가한다.

### `round4/02_current.py`

- 15, 54행: H와 a/H의 6개 tag를 읽도록 변경한다.
- 29–49행: history-region 이름을 파싱해 `(front position, contour number)`로 구조화한다. 현재 append 순서는 contour 순서라는 보장이 없으며 서로 다른 crack-front 절점의 K가 섞인다.
- 43–44행: 앞 N개를 기계적으로 버리고 전체를 평균하지 않는다. 각 front 위치마다 contour 수렴표를 내고 plateau의 평균·범위·변동계수를 저장한다.
- 60행: Abaqus/Python 버전에 따라 `csv`와 binary mode 조합이 달라질 수 있으므로 설치 Python 버전에 맞춘다. Python 3이면 `open(...,'w',newline='')`가 필요하다.
- CSV에는 `H`, `a/H`, `z/W`, contour 번호, `K1`, `J`, `K1/sqrt(2*pi)`, `K1/P_total`, 수렴판정을 각각 저장한다.

### 최소 검증 순서

1. 무균열 또는 매우 얕은 균열 모델의 반력·변형 대칭 검산.
2. 한 2D 케이스를 표준 SENB 폐형식과 비교해 형상·하중·두께·K 정규화를 검증.
3. 같은 케이스에서 메시 3수준 및 맞춤창 이동으로 `K_fit`과 contour K 수렴 확인.
4. 3D 대표 케이스에서 `K(z)`를 출력하여 중앙부 plateau와 자유표면 영향을 정량화.
5. 검증된 2D 절차를 6케이스에 적용하고 정확한 실험값으로 케이스 4를 1회 보정한 뒤 나머지 5개를 예측.

## 참고문헌·문서

- Kwon, Y. W.; Markoff, E. K.; DeFisher, S., “Unified Failure Criterion Based on Stress and Stress Gradient Conditions,” *Materials*, 17, 569 (2024), doi:10.3390/ma17030569, PMC10856633.
- Dassault Systèmes, *Abaqus Analysis Guide: Contour Integral Evaluation*, 공개 2025 온라인판. (기능의 n, q, SYMM 정의 확인)
- Dassault Systèmes, *Abaqus Keywords Reference: CONTOUR INTEGRAL*, 공개 2025 온라인판. (NORMAL, SYMM 데이터 정의 확인)
- Dassault Systèmes, *Abaqus Scripting User's Reference Guide*, §19.3.1, 공개 2016 PDF. (`crackNormal` 두 점 형식의 보조 확인; 요구된 2020/2021 판본은 접근 불가)

