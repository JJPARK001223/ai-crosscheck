# Round 15 — Codex blind 독립 조사

## 조사 범위와 제한

- `PROBLEM.md`와 지정된 번역본 두 편만 먼저 읽고 조사했다. `round15/claude.md`는 읽지 않았다.
- 참고문헌 [39]의 원문은 검색하거나 열람하지 않았다.
- 아래의 7.8%와 0.4793은 모두 **사용자 Abaqus 모델에서 얻은 값**으로만 취급한다. Kwon 논문에 보고된 값이 아니다.
- 기존 라운드에서 다룬 식의 유도는 반복하지 않는다.
- 이번에는 사용자의 `.cae`/`.odb` 자체나 입력파일을 열어 메시·crack 정의를 재검사하지 않았다. 따라서 A와 B의 원인 판정은 현재 제공된 출력 양상과 문헌을 대조한 결과이며, 모델 내부 설정까지 확인한 확정 진단은 아니다.

## 결론 요약

1. **A — 조건부로 타당하다.** 20절점 이차 brick의 균열 전선에는 corner node와 midside node가 교대로 놓이며, Abaqus 공식 문서는 collapsed C3D20의 edge plane과 midplane에서 균열 특이장 재현이 달라져 균열선을 따라 국소 진동이 생길 수 있다고 명시한다. 또한 Abaqus 공식 benchmark는 첫 contour를 정확도가 낮다는 이유로 결과 평균에서 제외한다. 따라서 `Contour_1`만 홀짝 지그재그이고 바깥 contour에서 사라지는 양상은 이 아티팩트와 잘 맞는다. 다만 **노드 종류의 교대만으로 원인이 입증된 것은 아니며**, 메시·crack-front 정의·가상 균열진전방향 등의 설정을 확인하기 전에는 유일 원인으로 단정하면 안 된다.
2. **B — 정성적 경향은 타당하지만 설명 문구는 수정해야 한다.** 3차원 관통균열의 자유표면 부근에서 국소 $K$ 또는 $J$가 중앙부보다 낮아지는 현상과 자유표면 corner/vertex 경계층은 고전 3차원 파괴역학 문헌에 보고되어 있다. 사용자 모델의 7.8% 차이는 이 경향과 모순되지 않는다. 그러나 이를 단순히 “표면은 평면응력, 중앙은 평면변형률”이라고만 부르는 것은 부정확하다. 자유표면 교차점에는 2차원 $r^{-1/2}$ 장과 다른 3차원 vertex 특이장이 존재하며, 정확한 표면 끝점 값은 메시와 적분 정의에도 민감하다.
3. **C — 사용자 모델은 Kwon et al. (2024) §4의 물리적 문제와 $K\rightarrow\Upsilon$ 사용 목적을 재현하지만, 논문의 수치 절차를 그대로 복제한 모델은 아니다.** 논문은 먼저 3차원 모델로 폭 방향 거동을 조사한 뒤 최종 파괴하중 예측에는 2차원 FE와 응력장 곡선맞춤을 썼다. 사용자는 3차원 Abaqus 상호작용적분으로 $K$를 추출했다. 이는 같은 LEFM 진폭 $K$를 구하는 표준적 대안이지만, 논문이 실제 사용했다고 쓰인 방법은 아니다.

## A. Contour_1 지그재그의 원인

### A-1. 문헌·공식 문서로 확인되는 사실

이차 brick 요소의 한 edge에는 두 corner node 사이에 midside node가 하나 있다. 따라서 균열 전선이 연속된 이차 요소 edge로 구성되고 Abaqus가 요구하는 대로 전선상의 모든 노드를 순서대로 출력하면, 출력 위치는 기하학적으로 corner–midside–corner–midside 순으로 나타난다. Abaqus는 3차원 이차 요소의 crack-front node set에서 midside node를 생략해서는 안 된다고 명시한다.

더 중요한 것은 단순한 노드 라벨의 교대가 아니라 **C3D20 singular mesh의 보간 특성 차이**다. Abaqus의 공식 이론/사용자 문서는 collapsed 20-node brick에서 균열 전선에 수직인 edge plane에는 square-root singularity를 만들 수 있지만, collapsed face의 midplane에서는 같은 특이성이 재현되지 않으며, 이 차이가 균열선을 따라 crack-tip 해의 국소 진동을 만든다고 설명한다. C3D27의 midface·centroid node를 포함하면 이 진동을 줄일 수 있다고도 한다. 즉 “C3D20 corner/midside 위치 사이의 교대 진동”은 실제로 알려진 수치 현상이다.

또한 Abaqus 공식 검증 예제는 첫 contour가 crack-tip에 직접 접한 요소만으로 계산되어 충분히 정확한 $J$ 추정치를 주지 못한 경험적 이유로, 보고값 평균에서 첫 contour를 제외한다. Domain integral은 바깥 contour로 갈수록 더 넓은 요소 영역을 사용하므로 국소 crack-tip 보간 오차에 덜 민감하다. 사용자의 진동이 Contour 1에서 강하고 Contour 2 이후 사라진다는 관찰은 이 설명과 일관된다.

### A-2. 판정

따라서 다음처럼 쓰는 것이 근거 수준에 맞다.

> Contour 1의 홀짝 진동은 C3D20 균열선에서 corner node와 midside node가 교대로 평가되는 구조 및 collapsed C3D20의 균열선 방향 특이장 재현 불일치와 합치되는 전형적인 **근접 contour 수치 아티팩트**다. 바깥 contour에서 진동이 소멸한다는 사실도 이 해석을 지지한다. 다만 현재 출력만으로 이 원인을 유일하게 확정할 수는 없다.

“20절점 요소이면 언제나 이런 큰 지그재그가 생긴다” 또는 “홀짝 패턴만으로 원인이 증명됐다”는 표현은 과장이다. Abaqus 문서도 해당 국소 진동이 보통은 크지 않다고 적고 있으므로, 이번 진폭이 큰 이유는 모델별 메시와 crack 정의를 별도로 점검해야 한다.

### A-3. 배제하지 못한 대안과 확인 방법

- **균열 전선 방향 메시 불균일/왜곡:** corner node 간 element 길이, 방사상 element 크기, wedge/brick의 평면성이 일정한지 확인한다. Abaqus는 crack line에 수직인 element plane의 평면성과 crack-tip element 크기가 정확도에 영향을 준다고 명시한다.
- **quarter-point 및 collapsed-node 설정:** midside node 위치가 0.25인지, collapsed face node가 선형탄성 $r^{-1/2}$ 특이장에 맞게 묶였는지 확인한다. C3D20과 C3D27 또는 전선 방향 세분화 결과를 비교하면 원인 분리가 가능하다.
- **crack-front 순서와 crack seed/edge 선택:** 21개 출력점이 실제로 한 연속 edge chain의 모든 corner/midside node인지, 중복·누락·잘못된 crack-line edge가 없는지 확인한다.
- **가상 균열진전방향 $q$ 및 표면 normal:** Abaqus는 3차원 crack front의 각 위치에서 $q$가 적절해야 하며, 외부 자유표면과 만나는 끝점에서는 표면 normal이 정확한 contour 평가에 중요하다고 설명한다.
- **하중·지지·접촉의 비대칭:** 이 요인은 실제 $K$ 분포를 바꿀 수 있다. 다만 홀짝 진동이 Contour 1에만 있고 같은 위치의 바깥 contour가 매끄럽다면, 전역 하중 자체보다는 근접 crack-tip 이산화 오차가 더 직접적인 설명이다. 이는 가능성의 우선순위이지 배제 증명은 아니다.

## B. 자유표면–중앙 $K$ 차이

### B-1. 정성적 경향

Raju와 Newman의 3차원 유한요소 연구는 여러 유한두께 관통균열 시험편에서 표면의 응력확대계수가 중앙면보다 상당히 낮고, 검토한 대부분 형상에서 최대값이 중앙면에 나타났다고 보고했다. Nakamura와 Parks는 자유표면과 crack front의 교차점 근처가 quarter-infinite crack의 corner singularity로 기술되며, 국소 $J$가 두께 방향으로 변한다고 밝혔다. 3점굽힘 형상 자체에 대해서도 Tseng의 3차원 탄성 FE 연구는 $K$가 두께와 자유표면 효과에 의존함을 다뤘다.

따라서 “자유표면 쪽 $K$가 낮고 중앙이 높은” 사용자의 분포는 3차원 파괴역학에서 알려진 방향과 일치한다. 그러나 문헌의 백분율은 형상 $a/H$, 두께비, Poisson 비, crack-front 형상, 표면 교차각, $K$ 추출법과 표면에서 얼마나 떨어진 위치를 비교했는지에 따라 달라진다. 이번 조사로 **모든 3점굽힘 시편에 적용되는 보편적 ‘수 %~십수 %’ 범위는 확정할 수 없었다.** 그러므로 사용자 모델의 7.8%는 “문헌의 정성적 경향과 양립하며 비현실적으로 보이지 않는다”까지만 말할 수 있고, “문헌이 예측한 정확한 감소율”이라고 써서는 안 된다.

### B-2. 권장되는 물리적 표현

다음 표현이 더 정확하다.

> 중앙부와 자유표면 부근의 $K$ 차이는 두께 방향 구속도의 변화와 crack front–free surface 교차점의 3차원 corner/vertex 특이장으로 생기는 자유표면 경계층 효과와 일관된다.

“자유표면은 평면응력이고 중앙은 평면변형률”은 직관적 요약으로는 쓸 수 있지만, 엄밀한 원인 설명으로는 부족하다. Nakamura와 Parks의 탄성해석에서는 crack front에 충분히 가까운 내부점에서 국소적으로 plane-strain형 장이 우세하고, 정확한 자유표면 교차점에서는 별도의 corner singularity가 지배한다. 따라서 표면에서 중앙까지 2차원 평면응력 해에서 평면변형률 해로 단순 보간된다고 단정해서는 안 된다.

또한 F1/F21이 정확한 자유표면 끝점이라면 그 값은 물리적 vertex 효과와 수치적 끝점 민감도가 함께 들어갈 수 있다. Abaqus는 외부 자유표면 근처에 정제된 메시가 필요하고, crack line 끝의 surface normal과 $q$ 방향이 정확해야 한다고 명시한다. 그러므로 7.8%를 물리 효과로 확정하려면 다음 검증이 필요하다.

- Contour 2–8에서 중앙/표면 비가 안정적인지 확인한다.
- 자유표면 근처의 두께 방향 메시를 독립적으로 세분화하고 F1뿐 아니라 F2, F3의 수렴도 본다.
- 양쪽 표면의 대칭성(F1 대 F21)을 확인한다.
- crack-front 끝점의 surface normal, $q$, 전선 접선 보간을 점검한다.
- 중앙값과 끝점값의 차이를 재료 고유 특성으로 해석하지 않는다. 이는 주어진 형상·경계조건·메시의 3차원 구조해석 결과다.

## C. 선행연구 1·3과 사용자 모델의 연결

### C-1. Kwon (2021)의 이론적 출발점

지정 번역본의 Kwon (2021) §2, 사례 2(원문의 세부 절 번호로는 §2.2에 해당)는 중앙균열 무한평판에 대해 균열 끝단 응력을 식 (4)의 $1/\sqrt{r}$ 특이장으로 쓰고 $K$를 응력확대계수로 정의한다. 이어 식 (5)–(7)에서 이를 응력구배 파괴값 및 $K_{IC}$와 연결한다. 사용자 모델이 계산하는 $K_1$의 일반적인 LEFM 의미는 이 부분과 연결된다.

### C-2. Kwon, Markoff와 DeFisher (2024)의 시멘트 페이스트 절차

지정 번역본에서 확인되는 정확한 연결은 다음과 같다.

- §2 식 (3)은 균열 근방 등가응력을 $\sigma_e=K/\sqrt{s}$로 쓰고, 식 (4)는 $\Upsilon=K^2/E$로 둔다. 이는 Kwon (2021)의 균열 끝단 특이장 아이디어를 다른 기호·정규화로 다시 사용한 것이다. 두 논문의 식에 나타나는 $2\pi$ 계수와 파괴값 기호가 같지 않으므로 식을 문자 그대로 동일하다고 쓰기보다, **동일한 $1/\sqrt{\text{distance}}$ LEFM 특이장과 그 진폭 $K$를 사용한다**고 표현하는 편이 정확하다.
- §4.1은 폭 방향 관통균열, 균열 깊이 $a$, 3점굽힘 시험을 정의한다.
- §4.2는 처음에 절반 대칭 3차원 솔리드 모델을 만들고 폭 방향 응력분포가 매우 유사함을 확인한 뒤, 계산 절감을 위해 최종 파괴하중 예측을 2차원 4절점 사각형 요소 모델로 수행했다고 명시한다.
- §4.3은 2차원 FE 응력에 식 (3)을 곡선맞춤해 $K$를 정하고, 식 (4)로 $\Upsilon$ 및 파괴하중을 연결했다고 명시한다.

따라서 사용자 모델은 “Kwon et al. (2024) §4의 3점굽힘 관통균열 문제를 3차원으로 구현하고, 동일한 물리량 $K$를 구해 식 (3)·(4)의 파괴기준에 연결하기 위한 재현/확장 모델”이라고 설명할 수 있다. 반대로 “논문과 동일한 FE 차원·요소·$K$ 추출법을 그대로 복제했다”고 쓰면 사실과 다르다.

### C-3. Abaqus contour/interaction integral의 위치

Kwon et al. (2024) 번역본에는 Abaqus, contour integral 또는 interaction integral을 사용했다는 기술이 없다. §4.3에 명시된 $K$ 추출법은 **균열 끝단 바로 근처 FE 응력의 부정확성을 피하기 위한 식 (3) 곡선맞춤**이다.

Abaqus의 $K$-factor 계산은 보조 순수모드 crack-tip field와 실제장 사이의 interaction integral을 3차원 domain integral로 평가하여 crack front 각 위치의 $K_I,K_{II},K_{III}$를 구하는 표준 방법이다. 그러므로 보고서에는 다음처럼 구분해야 한다.

> 원 논문은 근접 응력장 곡선맞춤으로 $K$를 추출했다. 본 Abaqus 모델은 같은 LEFM 진폭 $K$를 보다 직접적으로 평가하는 표준 상호작용적분(domain-integral) 대안을 사용했다. 따라서 목적과 이론적 $K$는 연결되지만, 수치 추출 절차는 논문과 동일하지 않다.

### C-4. 사용자 고유 결과의 해석 경계

- 7.8%는 사용자 3차원 모델의 두께방향 $K$ 분포이며 Kwon 논문의 결과가 아니다. 특히 Kwon et al. (2024)은 3차원 폭 방향 변화가 매우 유사하다고 판단해 2차원 모델로 전환했으므로, 이 논문을 7.8%의 직접 검증값으로 인용할 수 없다.
- 0.4793은 사용자 모델의 $K/P$ 기울기다. 선형탄성·고정 형상·비례하중 조건에서 $K\propto P$인 것은 중첩원리와 일치하지만, 그 계수 0.4793은 해당 모델의 기하·단위·하중 정의에 종속된 값이며 논문 상수가 아니다.
- $K/P$ 일정성은 해석의 선형 스케일링을 검증하지만 메시 수렴, crack-front 정의, 절대 $K$ 정확도까지 독립적으로 보증하지는 않는다.

## 최종 판정 문구

- **A:** “타당한 우선 가설이며 Abaqus 공식 문서의 직접 근거가 있다. 다만 메시와 crack 정의를 보지 않고 유일 원인으로 확정해서는 안 된다.”
- **B:** “중앙보다 자유표면 부근 $K$가 낮은 정성적 경향은 문헌과 일치한다. 명칭은 단순 평면응력–평면변형률 전이보다 ‘3차원 자유표면 corner/vertex 경계층과 구속도 변화’가 정확하다. 7.8%는 사용자 모델값이며 보편적 문헌값이 아니다.”
- **C:** “물리 문제와 $K\rightarrow\Upsilon$ 연결은 Kwon et al. (2024) §2·§4에 근거한다. $K$의 LEFM 출발점은 Kwon (2021) §2의 균열 사례에 있다. 다만 사용자 3D Abaqus 상호작용적분은 원 논문의 2D 곡선맞춤을 대체한 표준 수치기법이지, 논문이 사용했다고 확인된 방법은 아니다.”

## 참고문헌 및 확인 자료

1. Kwon, Y. W., “Revisiting Failure of Brittle Materials,” *Journal of Pressure Vessel Technology*, 143(6), 064503, 2021. DOI: 10.1115/1.4050989. 지정 번역본 §2, 사례 2, 식 (4)–(7) 확인.
2. Kwon, Y. W., Markoff, E. K., and DeFisher, S., “Unified Failure Criterion Based on Stress and Stress Gradient Conditions,” *Materials*, 17(3), 569, 2024. DOI: 10.3390/ma17030569. 지정 번역본 §2 식 (3)–(4), §4.1–4.3 확인.
3. Dassault Systèmes SIMULIA, “Contour Integral Evaluation,” *Abaqus 2025 Documentation*, 2025. 3차원 이차 요소 crack-front node 정의, domain integral, 자유표면 normal, C3D20의 균열선 방향 국소 진동 및 C3D27에 의한 완화에 관한 공식 문서. https://docs.software.vt.edu/abaqusv2025/English/SIMACAEANLRefMap/simaanl-c-contintegral.htm
4. Dassault Systèmes SIMULIA, “Stress Intensity Factor Extraction,” *Abaqus 2025 Documentation*, 2025. interaction integral과 crack-front nodal interpolation에 관한 공식 이론 문서. https://docs.software.vt.edu/abaqusv2025/English/SIMACAETHERefMap/simathe-c-stressintfact.htm
5. Dassault Systèmes SIMULIA, “Test 1.1: Center Cracked Plate in Tension,” *Abaqus 2025 Benchmarks Guide*, 2025. 첫 contour의 부정확성 때문에 평균에서 제외한다는 공식 검증 예. https://docs.software.vt.edu/abaqusv2025/English/SIMACAEBMKRefMap/simabmk-c-2dlefracturetest1-1.htm
6. Nakamura, T. and Parks, D. M., “Three-Dimensional Stress Field Near the Crack Front of a Thin Elastic Plate,” *Journal of Applied Mechanics*, 55(4), 805–813, 1988. DOI: 10.1115/1.3173725. 자유표면 corner singularity와 3차원 경계층 확인.
7. Raju, I. S. and Newman, J. C., Jr., *Three-Dimensional Finite-Element Analysis of Finite-Thickness Fracture Specimens*, NASA TN D-8414, 1977. 유한두께 관통균열의 두께방향 $K$ 분포와 표면 저하 경향 확인. https://ntrs.nasa.gov/citations/19770018633
8. Tseng, A. A., “A Three-Dimensional Finite Element Analysis of the Three-Point Bend Specimen,” *Engineering Fracture Mechanics*, 13(4), 939–943, 1980. DOI: 10.1016/0013-7944(80)90023-5. 3점굽힘 시험편의 두께·Poisson 비·자유표면 효과에 관한 3차원 탄성 FE 연구.

> 참고문헌 [39] 원문은 본 조사에서 사용하지 않았다.
