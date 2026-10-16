# round37 원문 대조 검사 — 슬라이드 35~49

검사 대상은 `round37/audit_deck.txt`의 HTML SLIDE 35~49뿐이다. HTML과 원문은 수정하지 않았다. 다른 검사자의 답은 읽지 않았다.

출처: EPRI, Schmitt, *xLPR Models Subgroup Report—Crack Growth and Coalescence*, xLPR-MSGR-CGR Ver.1.0, 2016-06-29. 아래 인용은 제공된 `cgr_text.txt`의 영어이며, 페이지는 **인쇄 쪽**이다. `=====PAGE n=====`의 본문은 인쇄 p.(n−1)로 확인했다. 식 6-1·6-2는 `pages/p120.png`(인쇄 p.119)도 직접 확인했다. 외부 문헌으로 원문을 보완하지 않았다. 원문에 없는 내용인지 여부는 이 보고서를 기준으로 판정했다.

시작 시 `git pull`을 시도했으나 `error: cannot open '.git/FETCH_HEAD': Permission denied`로 실패했다. 따라서 저장소 최신 상태와의 동기화는 확인하지 못했다. 완료 후 `git add -- round37/codex_C.md`도 `.git/index.lock` 생성 권한 오류로 실패하여 커밋·푸시는 수행하지 못했다.

## 발견 사항

### [슬라이드 35] WRONG — CONFIRMED
- 대상 문구(HTML 그대로): `합체 거리 | 이 거리보다 ligament가 짧으면 합침 | - |`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “The prediction of coalescence is contingent on the length of the smallest ID ligament”; “When this ligament length becomes less than some value—termed the coalescence distance—coalescence is said to be imminent” (p.93, §4.2.1.1).
- 문제: 원문의 판정 대상은 일반적인 ligament가 아니라 두 균열을 분리하는 **가장 짧은 ID ligament**이다. 위치와 선택 조건을 빼 일반 규칙으로 제시했다.
- 최소 교체안: `두 균열을 분리하는 가장 짧은 ID ligament의 길이가 이 거리보다 작으면 합침`.

### [슬라이드 35] OMISSION-OF-HEDGE — CONFIRMED
- 대상 문구(HTML 그대로): `합체 거리와 최대 깊이의 비는 0(균열 상호작용 없음)~약 0.75, best-estimate 0.5. 극값 0.0·0.75, 최빈값 0.5인 삼각분포 권장`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “In the absence of more detailed investigation, a triangular distribution is recommended with extremes at 0.0 and 0.75 and a mode at 0.5.” (p.98, §4.2.2).
- 문제: 삼각분포 권장의 조건인 “더 상세한 조사가 없는 경우”가 없다. 같은 조건을 보존한 슬라이드 37과도 다르다.
- 최소 교체안: `더 상세한 조사가 없는 경우, 극값 0.0·0.75, 최빈값 0.5인 삼각분포 권장`.

### [슬라이드 35] OMISSION-OF-HEDGE — CONFIRMED
- 대상 문구(HTML 그대로): `합체 거리는 사용자 지정 값이며 xLPR 대상 부품에서 0~20 in 가능.`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “Through-wall crack coalescence distances between 0 and 20 inches are possible for components of interest in xLPR, depending on the sizes of the flaws involved.” (p.94, §4.2.1.1).
- 문제: 0~20 in 가능성에 붙은 “관련 결함의 크기에 따라”라는 조건을 생략했다. 숫자와 단위 자체는 맞는다.
- 최소 교체안: `합체 거리는 사용자 지정 값이며, 관련 결함의 크기에 따라 xLPR 대상 부품에서 0~20 in가 가능.`

### [슬라이드 35] WRONG — CONFIRMED
- 대상 문구(HTML 그대로): `균열 간섭(crack interaction)과 ligament 붕괴(ligament collapse)는 K 계산·성장·안정성 예측에서 다루지 않고 양(positive)의 합체 거리로 모의할 수 있다고 합니다.`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): 표면균열 상호작용은 “This complex process is not treated in the K-calculation and growth predictions of Version 2.0 of xLPR”; 관통균열 ligament collapse는 “These complex processes are not treated in the K-calculation, growth, or stability predictions of Version 2.0 of xLPR” (p.94, §4.2.1.1).
- 문제: 원문이 구별한 두 예측 범위를 합쳐, crack interaction에도 안정성 예측 미취급을 함께 귀속했다. 문장에 원문의 Version 2.0 한정도 없다.
- 최소 교체안: `xLPR Version 2.0은 표면균열의 crack interaction을 K 계산·성장 예측에서, 관통균열의 ligament collapse를 K 계산·성장·안정성 예측에서 다루지 않으며, 각각 양의 합체 거리로 모의할 수 있습니다.`

### [슬라이드 35] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `합체 거리: 언제 합치나`, `기호와 하첨자`, `하첨자 읽는 법`, `적용 목적`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): 해당 원문 제목은 “4.2.1.1 Prediction of Imminent Coalescence” (p.93)와 “4.2.2 Treatment of Uncertainty” (p.98)이다. p.93~94·98의 대응 본문에는 이 소제목과 하첨자 교육용 표가 없다.
- 문제: 원문의 제목을 옮긴 것이 아니라 편집자가 만든 질문형 제목·설명 라벨이다. 내용 오류와 별도로 사용자의 제목·라벨 창작 금지 규칙에 해당한다.
- 최소 교체안: 제목을 `4.2.1.1 Prediction of Imminent Coalescence`로 교체하고 나머지 창작 라벨은 삭제.

### [슬라이드 36] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `합친 뒤 균열 모양: 유형·깊이·중심·길이`, `합친 균열의 속성`, `기호와 하첨자`, `하첨자 읽는 법`, `적용 목적`, `적용 방법`, `최대 깊이를 권장하는 이유`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “4.2.1.2 Coalesced Crack Geometry” (p.94); 이어지는 p.95는 “Consistent with physical expectations, the depth of the new crack…” 등의 연속 본문으로 되어 있다. 해당 세부 소제목·기호 표는 없다.
- 문제: 설명 내용은 대체로 원문에 대응하지만 이 소제목·라벨들은 원문에 없다.
- 최소 교체안: 제목을 `4.2.1.2 Coalesced Crack Geometry`로 교체하고 추가 라벨은 삭제.

### [슬라이드 37] OMISSION-OF-HEDGE — CONFIRMED
- 대상 문구(HTML 그대로): `이 불확실성은 합체로 이어지는 복잡한 과정의 변동성과 모델 오차(예: 균열 길이에 대한 체계적 의존성이 없음)를 반영합니다.`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “This uncertainty may reflect variability in the complex processes that lead to coalescence as well as model error (e.g., the lack of a systematic dependency with respect to crack length).” (p.98, §4.2.2).
- 문제: `may reflect`가 단정적인 `반영합니다`로 바뀌었다.
- 최소 교체안: `이 불확실성은 … 변동성과 모델 오차를 반영할 수 있습니다.`

### [슬라이드 37] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `분포된 합체 거리`, `그 밖의 합체 모델링 convention`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “Uncertainty in the coalescence prediction may be incorporated through the use of distributed coalescence distances.”; “The other coalescence modeling conventions are fully deterministic.” (p.98, §4.2.2).
- 문제: 원문의 문장에 나오는 용어를 이용해 새로 만든 표의 항목명이다. 원문에는 이러한 항목 제목으로 된 표가 없다. 용어 자체의 창작 또는 내용 오류라는 뜻은 아니다.
- 최소 교체안: 원문대로 §4.2.2 아래 연속 본문으로 배치하고 새 항목명은 삭제.

### [슬라이드 38] OMISSION-OF-HEDGE — CONFIRMED
- 대상 문구(HTML 그대로): `표면균열의 응력확대계수 증대(intensification)가 시작되는 시점은 균열 깊이의 일부(예: 0.0~0.75 사이)인 합체 거리로 잘 예측된다는 실험 증거가 있으며, 선택한 modeling convention을 검증합니다.`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “Experimental evidence suggests that the onset of the intensification of stress intensity factor for surface cracks is well-predicted using a coalescence distance that is some fraction—e.g., somewhere between 0.0 and 0.75—of crack depth, validating the selected modeling convention.” (p.99, §4.2.3).
- 문제: `Experimental evidence suggests`의 시사 수준이 “잘 예측된다는 실험 증거가 있으며 … 검증합니다”로 강화되었다. 0.0~0.75가 예시라는 표현은 보존되어 있다.
- 최소 교체안: `실험 증거는 표면균열의 응력확대계수 증대가 시작되는 시점이 균열 깊이의 일부(예: 0.0~0.75 사이)인 합체 거리로 잘 예측됨을 시사하며, 이는 선택한 modeling convention을 검증합니다.`

### [슬라이드 38] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `개요`, `인용된 연구`, `표면균열의 K 증대`, `관통균열의 양(positive)의 합체 거리`, `두 표면균열의 최대 깊이 convention`, `합체 후 균열 유형 convention`, `location, ID length, OD length convention`, `적용 범위`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): 원문 제목은 “4.2.3 Model Validation”; 본문은 “Specific instances of model validation are noted below:” 뒤 글머리 문장들로 구성된다 (p.99, §4.2.3).
- 문제: 각 문장을 표로 재구성하며 추가한 행 제목이다. 원문 용어를 사용한 경우도 있으나 소제목·라벨 자체는 원문에 없다.
- 최소 교체안: 원문의 제목과 글머리 문장만 남기고 새 행 제목은 삭제.

### [슬라이드 39] OMISSION-OF-HEDGE — CONFIRMED
- 대상 문구(HTML 그대로): `실제로는 축방향으로 어긋나 독립적으로 남을 수 있는 균열이 합쳐진다는 뜻입니다.`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “This means that circumferential cracks that more realistically might remain offset axially and independent are combined.” (p.100, §4.3, Coplanar crack assumption).
- 문제: `might`는 `수 있는`으로 보존되었지만, `more realistically`가 빠지고 `실제로는`이 들어가 실제 균열 상태에 대한 더 강한 표현이 되었다.
- 최소 교체안: `더 현실적인 경우에는 축방향으로 어긋나 독립적으로 남을 수도 있는 원주방향 균열이 합쳐진다는 뜻입니다.`

### [슬라이드 40] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `기호와 하첨자`, `하첨자 읽는 법`, `적용 목적`, `어떻게 동작하나`, `입력`, `범위`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “5.1 Module Scope and Limitations” (p.103), “5.2.1.1 Input Allocation, Input Verification, and Output Requirements”, “5.2.1.2 Pre-Processing Requirements” (p.105). 해당 원문에 이 설명 라벨·기호 표는 없다.
- 문제: 원문 내용을 재구성하면서 추가한 소제목과 라벨이다.
- 최소 교체안: 원문 절 제목을 사용하고 창작 라벨은 삭제.

### [슬라이드 41] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `기호와 하첨자`, `하첨자 읽는 법`, `순서`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “5.2.1.3 Iterative Application of Coalescence Rules” (p.105~106). 그 아래는 “These requirements rely on the designation of ‘Crack A’ and ‘Crack B’, as detailed below:”와 글머리 문장들이다.
- 문제: 원문에 없는 기호·하첨자 설명 구조와 소제목을 추가했다. 방향 플래그 1·2와 절차 내용 자체는 일치한다.
- 최소 교체안: 원문 절 제목과 글머리 문장만 사용하고 추가 라벨은 삭제.

### [슬라이드 42] OMISSION-OF-HEDGE — CONFIRMED
- 대상 문구(HTML 그대로): `Through-wall crack coalescence distance rule modifier | 두 관통균열의 coalescence distance | 균열 길이와 대략 맞는 분포, 예: 0~20 in 균일분포 |`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “the through-wall crack coalescence distance rule modifier should be sampled from a distribution roughly consistent with the lengths of cracks at the time at which coalescence is simulated”; “For components of interest, this distribution might be achieved roughly with a uniform distribution between zero and 20 inches.” (p.111, §5.3.2).
- 문제: 표에는 균열 길이의 기준 시점인 “합체가 모의되는 시점”이 없고, 0~20 in 균일분포에 대한 `might be achieved roughly`도 단순 `예`로 바뀌었다. 아래 본문의 시점 설명은 표 자체의 생략과 구별해야 한다.
- 최소 교체안: `합체가 모의되는 시점의 균열 길이와 대략 맞는 분포에서 표본 추출 권장. 대상 부품에서 이 분포는 0~20 in 균일분포로 대략 구현될 수도 있음`.

### [슬라이드 42] OMISSION-OF-HEDGE — CONFIRMED
- 대상 문구(HTML 그대로): `구성 요소별로는 0~20 in의 균일분포 정도가 한 예입니다(p.111).`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “For components of interest, this distribution might be achieved roughly with a uniform distribution between zero and 20 inches.” (p.111, §5.3.2).
- 문제: `components of interest`는 “구성 요소별”이 아니라 “관심 대상 부품”이다. 또한 원문의 가능성 표현 `might`가 없다. 앞의 표와 별도로 본문에서도 발생한다.
- 최소 교체안: `관심 대상 부품에서는 이 분포를 0~20 in의 균일분포로 대략 구현할 수도 있습니다(p.111).`

### [슬라이드 42] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `입력 매개변수와 플래그`, `coalescence module 입력`, `적용 목적`, `적용 방법`, `단위와 허용 범위(표 5-1)`, `coalescence distance를 정하는 규칙`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “5.3 Module Inputs and Outputs” (p.109), “Table 5-1. Coalescence Subroutine Arguments” (p.109), “5.3.2 Coalescence Model Parameters and Flags” (p.110), “5.2.1.4 Defining Coalescence Distance” (p.106).
- 문제: 여러 절을 합친 뒤 원문 제목과 다른 제목·라벨을 붙였다. 원문 제목을 번역한 범위를 넘어선 편집 라벨은 엄격한 규칙상 별도 지적 대상이다.
- 최소 교체안: 대응 원문 절·표 제목을 그대로 사용하고 `적용 목적`·`적용 방법`은 삭제.

### [슬라이드 44] WRONG — CONFIRMED
- 대상 문구(HTML 그대로): `현재 K 의존성은 대체로 낮은 K(80 MPa√m)를 대표하지 않는 데이터로 개발되었습니다.`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “The currently implemented stress intensity factor dependency has been developed from data that do not generally represent low (<15 to 20 MPa√m) or high (>80 MPa√m) values.” (p.117, §6.1.1).
- 문제: 저 K 범위 `<15 to 20 MPa√m`와 고 K 범위 `>80 MPa√m`가 모두 소실되고, 80 MPa√m가 저 K의 값처럼 제시되었다. 단순 요약이 아니라 범위·부등호·분류 오류다. 원본 HTML의 원인까지는 확인하지 않았다.
- 최소 교체안: `현재 K 의존성은 대체로 낮은 K(<15~20 MPa√m) 또는 높은 K(>80 MPa√m)를 대표하지 않는 데이터로 개발되었습니다.`

### [슬라이드 44] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `기계적 성질, 냉간가공, 열처리`, `재료 경계면, 발생-성장 상관`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): 원문은 “Mechanical properties:”, “Cold work:”, “Heat treatment:”, “Material interfaces:”, “Initiation-growth correlation:”라는 **개별** 항목이다 (p.117~118, §6.1.1).
- 문제: 서로 다른 원문 항목을 합쳐 만든 복합 소제목이다. 각 번역어 자체를 문제 삼는 것이 아니다.
- 최소 교체안: 원문처럼 다섯 개의 개별 항목명으로 분리.

### [슬라이드 45] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `내용`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “6.1.2 Other SCC Models” 뒤 곧바로 “In addition to refinement of the CGR models for PWSCC…”라는 본문이 이어진다 (p.118, §6.1.2).
- 문제: 해당 위치에 `내용`이라는 원문 소제목은 없다. `다른 SCC 모델`, `Alloy 690과 용접금속`, `BWR 환경`은 각각 원문 제목·항목의 번역에 대응하므로 지적하지 않는다.
- 최소 교체안: `내용` 라벨만 삭제.

### [슬라이드 46] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `개정`, `기호와 하첨자`, `하첨자 읽는 법`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “6.2 Fatigue Crack Growth Rates”, “6.2.1 Updated Fatigue Crack Growth Relations for Austenitic SS” (p.118), “The material groupings for the SS alloy effect were changed to:” 및 식 6-1 (p.119).
- 문제: `개정`이라는 별도 구획명과 하첨자 교육용 표는 원문에 없다. 식 6-1 수치와 재료 조합은 일치한다.
- 최소 교체안: 구획명은 `6.2 Fatigue Crack Growth Rates`로 바꾸고 추가 기호·하첨자 라벨은 삭제.

### [슬라이드 47] EQUATION — CONFIRMED
- 대상 문구(HTML 그대로): `[EQUATION TeX] \text{log-}\sigma=\begin{cases}0&CGR_{air}>10^{-8}\\-2.4-0.3\log_{10}(CGR_{air})&10^{-12}기호와 하첨자`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): 식 직전 “a log-σ parameter determined as follows:” (p.119, §6.2.2); 식 6-2는 이미지 `pages/p120.png`에서 다음 세 분기로 직접 확인: `0` if `CGR_air > 10^-8`; `−2.4−0.3 log_10(CGR_air)` if `10^-12 < CGR_air < 10^-8`; `1.2` if `CGR_air < 10^-12`.
- 문제: TeX가 둘째 행의 `10^{-12}`에서 잘려 중간 범위의 두 부등호와 변수, 마지막 분기, cases 종료가 모두 없다. 이어지는 본문 `기호와 하첨자`가 수식 줄에 붙어 있다. 검사 대상 텍스트가 완전한 원문 식을 담지 못한다는 것은 확정이며, 실제 DOM·렌더러의 고장 원인은 이 입력만으로 확인 불가다. 원문은 경계값 등호를 쓰지 않으므로 교체안에 임의로 등호를 추가하지 않았다.
- 최소 교체안:

```tex
\text{log-}\sigma=\begin{cases}
0&CGR_{air}>10^{-8}\\
-2.4-0.3\log_{10}(CGR_{air})&10^{-12}<CGR_{air}<10^{-8}\\
1.2&CGR_{air}<10^{-12}
\end{cases}
```

### [슬라이드 47] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `개정`, `기호와 하첨자`, `하첨자 읽는 법`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “6.2.2 Enhancements to Probabilistic Model for Nickel-Based Alloys” (p.119); 본문은 “As discussed in Section 2.3.2, there is considerable scatter…”로 시작한다. 이 구획명과 교육용 표는 없다.
- 문제: 원문에 없는 소제목·설명 라벨을 넣었다. `log-σ`, `CGR_air` 자체는 원문 용어다.
- 최소 교체안: 원문 §6.2와 §6.2.2 제목만 사용하고 창작 라벨은 삭제.

### [슬라이드 49] WRONG — CONFIRMED
- 대상 문구(HTML 그대로): `overlay/onlay는 네 번째 재료 그룹으로 모델링할 수 있습니다. 이후 두께 방향 재료 구배와 J-groove 용접 등을 개발할 것으로 기대합니다`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “It is expected that later versions of xLPR will introduce more complicated geometries, e.g., to allow for through-wall material gradients. Furthermore, geometries are expected to be developed to represent other susceptible components such as J-groove welds used for head penetration nozzles.” (p.120, §6.3.1).
- 문제: 원문이 개발 대상으로 말한 것은 구배를 허용하거나 J-groove 용접을 **나타내는 형상(geometries)**이다. HTML은 `형상`을 생략해 재료 구배와 용접 자체를 개발한다고 읽힌다. `head penetration nozzles`라는 J-groove 용접 적용 한정도 생략했다. 기대한다는 양태는 보존되어 있다.
- 최소 교체안: `이후 버전에서는 두께 방향 재료 구배를 허용하는 등의 더 복잡한 형상과, 헤드 관통 노즐의 J-groove 용접 같은 취약 부품을 나타내는 형상이 개발될 것으로 기대합니다.`

### [슬라이드 49] OTHER — CONFIRMED
- 대상 문구(HTML 그대로): `미세균열(micro-fissure) coalescence는 보통 발생 과정의 일부로 보며 발생 소그룹의 향후 과제로 봅니다(p.121).`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “It is not applicable to simulation of micro-fissure coalescence”; “The simulation of micro-fissure coalescence is considered a potential area of future work for the Initiation Subgroup.” (p.121, §6.3.2).
- 문제: 이 항목의 핵심 적용 제한인 현 coalescence module의 micro-fissure coalescence 모의 불가가 빠졌다. `potential area`도 단순한 `향후 과제`로 축약되었다. 슬라이드 전체에 이 제한의 다른 명시가 없다.
- 최소 교체안: `현 coalescence module은 micro-fissure coalescence 모의에 적용할 수 없습니다. 이는 흔히 발생 과정의 일부로 간주되며, 그 모의는 발생 소그룹의 잠재적 향후 작업 분야로 봅니다(p.121).`

### [슬라이드 49] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `축방향 균열과 미세균열`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “Axial crack coalescence:”와 “Micro-fissure coalescence:”는 별개 항목이다 (p.121, §6.3.2).
- 문제: 원문에는 없는 두 항목의 통합 제목이다.
- 최소 교체안: `Axial crack coalescence`와 `Micro-fissure coalescence`로 분리.

## 전체 대조 기록

본문의 모든 문장, 표의 모든 데이터 행, 두 `[EQUATION TeX]` 줄과 모든 인용을 대조했다. 제목·기호표는 별도 열에 기록했다. 본문에 명시된 수치·단위·조건도 함께 확인했다. 다음의 “일치”는 위에서 지적한 부분을 제외한 내용에 대한 것이다. 문제가 없는 슬라이드는 마지막에 확인한 문장 수도 명시했다.

| 슬라이드 | 대조한 본문·표·수식 | 제목·기호표 | 인용 대조 결과 및 나머지 확인 내용 |
|---|---|---|---|
| 35 | 본문 전체, 주 표 5행 | 창작 제목·라벨 및 기호표 1행 확인 | p.93~94 §4.2.1.1, p.98 §4.2.2 모두 해당 내용 있음. 표의 p.94·98 맞음. 두 표면균열 convention, 0.5, ASME IWA-3000, 관통균열의 길이 의존성 미구현, 약 1:1, 표면+관통 기본값 0 확인. 세부 지적은 위 참조. |
| 36 | 주 표 5행, 본문 전체 | 창작 제목·라벨 및 기호표 2행 확인 | p.94~95 §4.2.1.2 맞음. 같은/다른 유형 조합, 관통균열 포함 시 두께, 표면균열 최소·최대·평균, 최대 권장, 중심·OD·ID arc, 면적 보존, 안정성 연속성, re-entrant K 증폭·대략 대칭 회복, leakage continuity 표현 대조. 내용상 추가 지적 없음. |
| 37 | 주 표 4행(각 행 전체 문장 대조) | §4.2.2는 원문 제목과 일치, 새 행 라벨 확인 | p.98~99 §4.2.2 맞음. 분포·epistemic 권장·비율 범위·조건부 삼각분포·약 1:1·각주 35·결정적 속성 5개·최대 깊이 convention 변경 가능 확인. `may reflect` 외 내용상 추가 지적 없음. |
| 38 | 주 표 8행(각 행 전체 문장 대조) | §4.2.3는 원문 제목과 일치, 새 행 라벨 확인 | p.99 §4.2.3 맞음. Bezensek [49], Huh [52], Chang [51], Suga [53], 0.0~0.75 예시, low likelihood, rapid tearing, maximum depth, generally validated, 각주 36·37, full range 확인. `suggests` 외 내용상 추가 지적 없음. |
| 39 | 도입 문구, 주 표 6행(각 행 전체 문장 대조) | §4.3 및 6개 영어 항목명은 원문과 일치 | p.100~101 §4.3 맞음. 반타원·세 유형·ID/OD 라디안 동일, A/B 배치, 누설·파단 영향의 정도와 조건, 약 절반, 추가 해석 필요, 보수성, 축방향 최대 하나, may-sensitive·generally early/late, 평판 검증·작은 반경·곡률 불확실성 확인. 위 양태 지적 외 추가 지적 없음. |
| 40 | 본문 전체 | 기호표 2행·소제목 확인 | p.103~104 §5.1, p.105 §5.2.1.1~.2, 인접 조건 §5.2.1.3, p.111 §5.3.2 모두 해당 내용 있음. 호출 가능, 반복 종료, absorbed crack, 입력·정렬·제외·활성 2개 미만 반환, coplanar·세 유형, 1개월·3개 이상 드묾 확인. 내용상 지적 없음. |
| 41 | 본문 전체 | 기호표 1행·소제목 확인 | p.105~106 §5.2.1.3, p.110~111 §5.3.2 맞음. 원점 관찰자·좌/우 tip·시계 방향·거리 미만, subunit 1, A/B 지정과 갱신, 방향 반전 가능, 2개 이하 방향 무관·3개 이상 방향 의존 가능 확인. 내용상 지적 없음. |
| 42 | 주 표 5행, 본문 전체 | 창작 제목·라벨 확인 | 헤더 p.106,109~111 및 §5.2.1.4·§5.3·§5.3.2 맞음. 숫자 플래그 1/2 및 깊이 1/2/3, 삼각분포 0/0.5/0.75, 0~20 in, 표 5-1의 0~200·[0,2π) rad·반길이 m·modifier 단위와 비음수, crack type 0/−1/−2/−3/양의 정수·orientation 1/2, verification/validation 구별 확인. 위 조건·양태 외 추가 지적 없음. |
| 43 | 본문 전체 | §5.2.1.5·.6·.7 및 §5.3.3 제목과 대응 확인 | p.107~108 §5.2.1.5~.7 및 p.111~112 §5.3.3 맞음. 각주 39의 initiation time index, type·geometry, 미관여 균열 불변, 출력 재정렬, 오류 0·101~115·201/210·301 및 종료 여부, 빈도 추적·역방향 재실행, 30 kB·최소 5개·겹침 최소 2건·1000번·10초 미만 모두 일치. |
| 44 | 도입 포함 본문 전체 | §6.1.1 제목 번역 및 항목 통합 라벨 확인 | 헤더의 p.117~118 §6.1.1은 맞음. 다만 `재료 경계면, 발생-성장 상관` 단락의 내용은 p.118에 있음(해당 단락은 p.117~118로 넓게 인용하므로 틀린 쪽수라고 판정하지 않음). K 문턱값·Alloy 82/182 수소자료·Alloy 600 수소 분석·hybrid/yield stress·cold work 조건·heat treatment 2.0·경계 모델 전환·현장 관찰·상관값 미권장·위험 중요 가능성 대조. 저/고 K 오류 외 추가 내용 지적 없음. |
| 45 | 본문 전체 | §6.1.2와 두 원문 항목명 대응 확인 | p.118 §6.1.2 맞음. Alloy 600/82/182/132·PWR·식 3-1·대안 형태 가능·Alloy 690/52/152·패널 개발 중·BWR·SS IGSCC·실험 기반 구현 가능 모두 일치. `내용` 라벨 외 지적 없음. |
| 46 | 본문 전체, 수식 1줄 | 기호표 1행·라벨 확인 | p.119 §6.2.1, p.118~119, p.48 식 2-19, p.71 표 3-1 모두 해당 내용 있음. 식 6-1 두 수치 9.10×10^-9/1.39×10^-8와 304·316/304L·316L·304LE, 재료코드 6·7·8, N-809 개정, 식 2-22의 2000 s 상한 제거 확인. 수식은 이미지와도 일치. |
| 47 | 본문 전체, 수식 1줄 | 기호표 2행·라벨 확인 | p.119 §6.2.2, p.45 §2.3.2.2 및 각주 14 인용 맞음. median 4.4×10^-7 (m/cyc-s)^(1−0.33), log-normal, CGR_air, log10의 −12/−8·1.2/0.0, v2.0 미구현·고정 1.2 권장·높은 CGR 과다 변동 위험 모두 일치. 수식 손상 별도 지적. |
| 48 | 본문 전체 | 두 영어 절 제목 모두 원문과 일치 | p.119 §6.2.3·§6.2.4 맞음. 재료 공통 fatigue ΔK threshold·acceptably validated·ASME Section XI 재료별 시험·향후 참조, alternative equation/software 중심·일부 비독립·독립 실험자료 필요, 현장 검사에서 fatigue 진전 확인·한 주기 이상 잔류·일부 추정 가능 모두 일치. |
| 49 | 본문 전체 | §6.3·§6.3.1·§6.3.2 대응 및 통합 라벨 확인 | p.120~121 §6.3.1~.2 맞음. annular 3그룹·overlay/onlay 4번째 가능·대칭 세 유형·coplanar·subsurface 미모델링·공동 작업, K-solutions/안정성의 미취급·FM 해·길이 의존 가능 개선·secondary determinant·roughly same size와 약 1:1, mixed orientation 과제 대조. 위 세 지적 외 추가 지적 없음. |

슬라이드 43: 지적 없음(본문 13문장, 절 제목·인용 및 그 안의 모든 수치·조건 확인).

슬라이드 48: 지적 없음(본문 6문장, 절 제목 2개·인용 및 그 안의 모든 수치·조건 확인).

## 유형별 요약

발견 단위는 위 `### [슬라이드 N] 유형 — 확신도` 제목 1개이며, 한 슬라이드의 창작 라벨 여러 개는 하나로 묶었다. 표와 본문의 같은 생략은 실제 출현별로 분리했다. 페이지 머리의 `페이지 N / 49` 및 표의 일반 열 이름은 탐색·표 구조 정보로 보아 과학적 주장으로 세지 않았다.

| 유형 | CONFIRMED | PLAUSIBLE | 합계 |
|---|---:|---:|---:|
| WRONG | 4 | 0 | 4 |
| OMISSION-OF-HEDGE | 7 | 0 | 7 |
| ADDED-CLAIM | 0 | 0 | 0 |
| COINED-TITLE | 12 | 0 | 12 |
| CITATION | 0 | 0 | 0 |
| EQUATION | 1 | 0 | 1 |
| OTHER | 1 | 0 | 1 |
| 합계 | 25 | 0 | 25 |

ADDED-CLAIM은 별도 중점 확인했으나, 새로운 과학적 주장·자체 수치 계산으로 확정할 항목은 찾지 못했다. 이는 무오류 선언이 아니다. 원문 범위의 확대는 WRONG, 양태·조건 생략은 OMISSION-OF-HEDGE, 추가 제목은 COINED-TITLE로 중복 없이 분류했다. 특히 슬라이드 35의 예측 범위 확대와 슬라이드 44의 K 범위 변경은 내용 오류로 기록했다.

__DONE__
