# Round 4 Codex 교차검증 — `claude.md` 검토

## 검토 범위와 결론

`round4/claude.md`를 `round4/codex.md`, `round4/01_current.py`, `round4/02_current.py` 및 Kwon·Markoff·DeFisher 원문과 대조했다. Abaqus 실행 파일과 ODB가 없으므로 실행 결과는 검증하지 못했다. Abaqus 2020/2021 Scripting Reference 원문도 확보하지 못했으므로 그 버전의 Python API 서명은 여전히 **확인 불가**다. 아래에서 공개 2025 Abaqus 공식 해석 문서는 역학적 의미를 확인하는 근거로, 공개 2016 Scripting Reference는 API 형식의 보조 근거로만 사용한다.

요약하면 Claude는 반모델 하중 규약, `crackNormal`의 물리적 의미, 2D/3D 역할, 기존 무차원화 식의 오류, 구현 누락을 대체로 맞게 짚었다. 그러나 핵심적으로 (i) 경로 A 응력 성분을 `sigma_yy`로 잘못 적었고, (ii) `centerVerts`가 빈 선택이 되어 U3 구속 자체가 생략되는 실제 버그를 발견하지 못했으며, (iii) `Y=K^2/E`만으로 2D 평면응력을 확정했다. 무차원화에서 Claude가 “B가 상쇄된다”고 쓴 것은 아니다. `B=100`이 모든 케이스에서 일정하므로 `K_I sqrt(H)/P`만으로 **케이스 간 붕괴 여부를 비교할 수 있다**고 썼다. 이 제한된 주장은 맞지만, 그 양 자체는 무차원이 아니므로 완전한 형상계수에는 B가 반드시 남아야 한다.

## 1. `claude.md`가 맞게 본 점

### 1.1 반모델의 형상·경계조건과 하중 환산

Claude가 길이방향 절반 모델에서 리거먼트에 `U1=0`, 균열면은 자유, 반대쪽 롤러선에 `U2=0`, 상단 절반 패치에 총하중의 절반을 적용하는 구성을 물리적으로 타당하다고 본 것은 맞다. 전체 시편 총하중을 `P0`라 하면 반모델에 합력 `P0/2`를 적용한 해의 국부 K는 전체 시편이 `P0`를 받는 상태에 대응하므로 `K/P_total=K_output/P0`가 일관된다.

또한 `symmetric=True`가 외력이나 K를 다시 절반으로 만드는 옵션인지 의심하며 문서 확인을 요구한 태도는 적절했다. Abaqus 공식 해석 문서는 대칭면의 half-crack에 대해 가상 균열진전에 따른 퍼텐셜에너지 변화를 두 배 하여 **올바른 contour integral**을 계산한다고 명시한다. 따라서 추가로 K에 2 또는 `sqrt(2)`를 곱할 이유가 없다.

### 1.2 `crackNormal`의 의미와 방향

Claude는 `extensionDirectionMethod=CRACK_NORMAL`에서 `crackNormal`이 균열 성장방향 q가 아니라 **균열면 법선 n**이라고 정확히 보았다. 공개 Abaqus 공식 문서에 따르면 3D에서는 `q=t×n`이다. 균열전선 접선 t가 +Z, 균열면 법선 n이 +X로 정렬되면 q는 +Y가 되어 현재 형상의 의도와 맞는다. 다만 edge 순서가 반대면 t와 q의 부호가 바뀔 수 있으므로 `.dat` 출력이나 J 부호로 확인해야 한다는 `codex.md`의 조건은 그대로 유효하다.

Claude가 단일 벡터 `crackNormal=(1,0,0)`의 API 유효성을 확정하지 않고 두 점 형식 가능성을 제기한 것도 맞다. 공개 2016 Scripting Reference는 이 인자를 방향 벡터를 정하는 두 점의 sequence로 설명한다. 그러나 요구 버전인 2020/2021 원문을 확보하지 못했으므로 최종 판정은 설치본의 CAE replay 또는 로컬 Reference 확인 전까지 **확인 불가**다.

### 1.3 기존 무차원화 식의 오류 인지

Claude가 기존 `K/(P H^{-3/2})=K H^{3/2}/P`를 최종 비교량으로 쓰면 안 된다고 스스로 정정한 것은 맞다. SENB의 표준 스케일링

`K_I = [P S/(B H^(3/2))] F(a/H)`

에서 같은 `S/H`에 대해 크기와 폭을 포함한 무차원량은

`K_I B sqrt(H)/P = (S/H) F(a/H)`

이다. 기존 `K H^(3/2)/P`는 이 표준량에 `H/B`가 더 곱해져, `B=100` 고정 상태에서 H=100 결과를 H=50 결과보다 인위적으로 두 배 이동시킨다.

### 1.4 2D/3D 역할과 구현 누락

Claude가 논문 재현의 본체는 2D 4절점 6케이스이고 3D는 폭방향 K 균일성 확인용이라고 정정한 것은 원문 §4.2–4.3과 일치한다. 원문은 3D 모델로 폭방향 거동을 검토한 뒤 파괴하중 예측용 K를 2D FEA와 식 (3)의 곡선맞춤으로 구했다고 명시한다. 따라서 현 `01_current.py`의 3D C3D10 3케이스만으로는 논문 본체 방법을 재현하지 못한다.

Claude가 다음 누락을 열거한 것도 타당하다.

- 2D 본 계산 스크립트 부재
- 경로 A의 path 추출 및 곡선맞춤 코드 부재
- 케이스 4 보정, 나머지 예측 및 Fig. 11 비교 코드 부재
- 실험 파괴하중 원자료의 정확한 확정 부재
- J-K 변환의 유효탄성률/평면가정 확인 부재

## 2. `claude.md`가 틀리거나 근거가 부족한 점

### 2.1 경로 A stress 성분: `sigma_yy`는 틀림

Claude는 경로 A를 `sigma_yy(s)=Khat/sqrt(s)`라고 명시했다. 현재 스크립트 좌표계에서는 균열면이 `X=L/2`, 그 법선과 개구방향이 X, 균열 성장방향 및 거리 s가 +Y이다. 따라서 균열 전방의 모드-I 개구 정상응력은 `sigma_xx=S11`이고, `sigma_yy=S22`는 성장방향 성분이다. 이 점에서 Claude와 Codex는 명백히 충돌하며 **Codex 판정이 맞다**.

다만 원문 식 (3)은 특정 전역 성분을 직접 쓰지 않고 `sigma_e`를 쓴다. 원문 §2는 취성·준취성 등방재의 유효응력으로 보통 최대정규응력을 사용한다고 설명한다. 따라서 구현은 우선 `S11`을 모드-I 성분으로 추출하되, 논문의 실제 후처리가 최대주응력인지 전역 `S11`인지 원문 그림·데이터로 더 확인해야 한다. 확인 전 `S11`과 `sigma_e`를 무조건 동일시해서도 안 된다.

### 2.2 “지수 부호가 틀려 차원이 틀림”이라는 설명은 부정확

Claude는 `K H^(3/2)/P`를 두고 “차원이 틀림 (지수 부호)”이라고 썼다. 이는 **틀린 설명**이다. `K_I`의 차원은 응력×길이^(1/2), 즉 힘×길이^(-3/2)이므로 `K_I H^(3/2)/P`는 실제로 무차원이다. 문제는 차원이 아니라 SENB 식에 필요한 폭 B가 빠져 있어 서로 다른 `B/H`의 형상 유사성을 보존하지 못한다는 것이다.

Claude가 대안으로 함께 쓴 `K H^(-1/2)/P`는 차원적으로도 틀리다. `K sqrt(H)/P`는 차원이 `1/길이`이며, 여기에 B를 곱한 `K B sqrt(H)/P`가 무차원이다. 따라서 정확한 정정은 “부호만 고친다”가 아니라 **`K_I B sqrt(H)/P`로 바꾼다**이다.

### 2.3 B 상쇄 여부: 제한적으로 맞지만 표현을 엄밀히 해야 함

사용자가 지정한 점을 문언 그대로 확인하면, Claude는 **“B가 상쇄된다”고 쓰지 않았다**. `B(=W)=100`과 `S/H=4`가 여섯 케이스에서 모두 같으므로 `K_I sqrt(H)/P`로 비교해도 H 간 스케일이 제거된다고 썼다.

이 주장은 목적을 나누어 판정해야 한다.

- H=50과 100 결과가 같은 `a/H`에서 겹치는지만 비교: 맞다. `K_I sqrt(H)/P=4F/B`이고 B가 동일하므로 두 군에 공통인 상수 `1/B`를 생략해도 붕괴 여부는 같다.
- 무차원 형상계수의 정의: 틀리거나 불완전하다. `K_I sqrt(H)/P`는 `1/길이` 차원을 가지므로 B는 상쇄된 것이 아니라 **고정된 공통 척도로 생략**되었을 뿐이다. 보고·검증에는 `K_I B sqrt(H)/P` 또는 이를 `S/H`로 나눈 F를 써야 한다.

따라서 `codex.md`의 “B가 같아서 상쇄되는 것이 아니다”도 문맥 없이 읽으면 지나치게 단정적이다. 형상계수 정의에서는 맞는 지적이지만, 동일 B 데이터의 상대적 collapse 비교에서는 Claude의 생략이 허용된다. 이 부분은 억지 합의가 아니라 **목적별 판정의 분리**다.

### 2.4 평면응력 확정은 근거 부족

Claude는 논문의 `Y=K^2/E`를 근거로 2D를 평면응력으로 확정하자고 했다. 그러나 논문 K는 표준 `K_I`와 `sqrt(2*pi)`가 다른 정의일 수 있고, 저자가 유효탄성률 `E'` 표기를 생략했을 가능성과 FE 요소의 plane stress/plane strain 선택은 별개다. 원문의 정확한 요소명 또는 두께/평면가정 명시 없이 평면응력으로 확정할 수 없다. 이 항목은 `codex.md`처럼 **확인 불가**로 두고, 원문 요소를 확인하거나 3D 중앙부 K/P와 두 가정을 비교해야 한다.

### 2.5 강체회전 불완전 주장과 ZSYMM 우월성은 입증되지 않음

Claude는 한 점 `U3=0`만으로 X/Y축 회전 구속이 불완전할 수 있다고 했으나, 세 구속이 의도대로 존재한다면 강체운동 `u=t+omega×r`에 직접 대입했을 때 6개 강체모드는 모두 제거된다. 리거먼트 면의 `U1=0`이 `t1, omega2, omega3`, 지지선의 `U2=0`이 `t2, omega1`, 그 선 위 한 점의 `U3=0`이 남은 `t3`를 제거한다. 따라서 “조대 메시라 수치 불안정”이라는 일반론만으로 구속 불충분이라 판정할 근거는 없다.

ZSYMM 폭 절반 모델은 대칭 하중·재료에서 계산비를 줄이는 유효한 대안이지만 무조건 더 낫지는 않다. 전폭 모델의 자유표면 양쪽 거동을 직접 확인하려는 목적이라면 한 점 U3 최소구속이 정보를 더 보존한다. 반폭 모델을 쓰면 한쪽 자유표면과 중앙면을 보존하도록 `0..W/2` 범위를 정확히 잡아야 한다.

## 3. `claude.md`가 놓친 점

### 3.1 `centerVerts` 버그를 인지하지 못함

Claude는 `round4/01_current.py` 97–108행을 보고 “롤러 edge + 1점 최소구속이 조대 메시에서 불안정할 수 있다”고만 썼다. 그러나 실제 핵심 버그는 103–108행의 선택 로직이다.

압출 직육면체의 `X=0, Y=0` 지지 edge에는 통상 Z=0과 Z=W 끝 vertex만 있고 Z=W/2에는 기하학적 vertex가 없다. 따라서

`centerVerts = inst.vertices.getByBoundingBox(... z=W/2 ...)`

가 빈 배열이 되고, 뒤의 `if len(centerVerts)>0:` 때문에 `Support-AntiRigid` BC가 **경고 없이 생성되지 않을 가능성이 높다**. 그러면 남은 폭방향 강체병진 `t3` 때문에 singular matrix가 발생할 수 있다. Claude는 이 빈 선택/조용한 생략을 발견하지 못했으므로 사용자가 지정한 `centerVerts` 버그를 **인지하지 못했다**고 판정한다.

수정은 지지 edge를 Z=W/2에서 partition한 뒤 vertex가 정확히 하나인지 assert하거나, 반폭 모델과 ZSYMM을 쓰는 것이다. 다른 bounding-box 선택에도 예상 개수와 좌표/길이 assert가 필요하다.

### 3.2 경로 A와 Contour K의 정규화 관계

Claude는 경로 A의 응력 성분 오류뿐 아니라 논문 맞춤 K와 Abaqus 표준 `K_I`의 변환을 명시하지 않았다. 전방응력이 `sigma=K_I/sqrt(2*pi*s)`이고 논문 식 (3)이 `sigma_e=K/sqrt(s)`라면

`K_paper = K_I/sqrt(2*pi)`.

따라서 경로 A와 B를 직접 같은 숫자로 비교하면 안 되며, CSV 변수명과 후속 보정식에서 두 K를 분리해야 한다. 현 `02_current.py`의 `K1_avg`를 논문 K로 바로 쓰면 `2*pi` 계수 오류가 생긴다.

### 3.3 3D crack-front 위치와 contour 번호가 섞이는 후처리 버그

`02_current.py`는 모든 history region의 `K1` 마지막 값을 단일 리스트에 append한 후 앞 한 개를 버리고 평균한다. 3D에서는 history region이 contour 번호뿐 아니라 crack-front 위치별로 존재할 수 있으므로 이 리스트 순서를 contour 순서라고 보장할 수 없다. 서로 다른 z 위치와 contour가 섞인 평균일 수 있다. `(z 또는 front node, contour number)`로 파싱해 위치별 plateau를 보존해야 한다. Claude는 일반적인 “Contour Integral 인자 검증 미완”은 적었지만 이 구체적인 후처리 오류를 짚지 못했다.

### 3.4 추가로 빠진 검증 게이트

Claude의 누락 목록에도 다음은 명시되지 않았다.

- 선택 면적×압력이 실제 `P0/2`인지와 해석 후 RF2 합계 검산
- 팁 적분점 응력, nodal averaging 설정, 자유기울기 후 `-1/2` 고정 적합, 적합창 이동 및 메시 3수준 수렴
- 한 2D 케이스를 표준 SENB 폐형식과 비교해 하중·폭·두께·K 정규화 검증
- `crackEdges`, `symFaces`, `supportEdges`, `loadFaces`의 예상 개수·좌표 assert
- “첫 contour 제외 후 평균” 대신 위치별 contour plateau와 경로독립성 확인

## 최종 교차검증 판정

| 쟁점 | Claude 판정에 대한 결론 |
|---|---|
| 경로 A stress 성분 | **틀림** — `sigma_yy`가 아니라 현 좌표계의 모드-I 성분은 `S11=sigma_xx`; 원문 `sigma_e` 정의는 추가 확인 필요 |
| 반모델 하중 및 `symmetric=True` | **대체로 맞음** — `P0/2` 입력, K는 `P0` 상태, 추가 2배/`sqrt(2)` 보정 불필요 |
| `crackNormal` 의미 | **맞음** — 균열면 법선; 단일 벡터 API 형식은 2020/2021 설치본 확인 전 확정 불가 |
| 무차원화 오류 인지 | **결론은 맞으나 설명 일부 틀림** — 기존 양도 차원은 없으며 문제는 B 누락; `K H^(-1/2)/P`는 오답 |
| “B 상쇄” 주장 여부 | **그렇게 쓰지 않음** — 동일 B의 비교에서 공통상수를 생략했을 뿐; 무차원 형상계수에는 B 필수 |
| `centerVerts` 버그 | **놓침** — Z=W/2 vertex 부재 → 빈 선택 → U3 BC 조용히 생략 가능 |
| 강체구속 자체 | **Claude의 불완전 우려는 근거 부족** — 세 BC가 실제 적용되면 6 강체모드는 제거됨 |
| 2D/3D 역할 | **맞음** — 2D 6케이스가 본체, 3D는 폭방향 검증용 |
| 평면응력 확정 | **근거 부족** — 요소/평면가정 원문 확인 전 확인 불가 |

## 근거 자료

- Kwon, Y. W.; Markoff, E. K.; DeFisher, S., “Unified Failure Criterion Based on Stress and Stress Gradient Conditions,” *Materials*, 17, 569 (2024), doi:10.3390/ma17030569. 원문 공개본: https://pmc.ncbi.nlm.nih.gov/articles/PMC10856633/
- Dassault Systèmes, *Abaqus Analysis Guide: Contour Integral Evaluation*, 공개 2025 온라인판. n, q, `q=t×n`, 대칭 half-crack의 에너지 보정 및 3D crack-front 정의 근거: https://docs.software.vt.edu/abaqusv2025/English/SIMACAEANLRefMap/simaanl-c-contintegral.htm
- Dassault Systèmes, *Abaqus Scripting User's Reference Guide*, §19.3.1, 공개 2016 PDF. `crackNormal` 두 점 형식의 보조 근거: https://ceae-server.colorado.edu/v2016/pdf_books/SCRIPT.pdf (2020/2021 판본이 아니므로 버전별 API 확정 근거로 사용하지 않음)

