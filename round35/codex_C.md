# round35 C: 슬라이드 34–49 원문 대조

대조 원문: EPRI / Schmitt, *xLPR Models Subgroup Report—Crack Growth and Coalescence*, xLPR-MSGR-CGR Ver.1.0, 2016-06-29. 사용 파일은 지정된 `cgr_text.txt`이며, PAGE n의 인쇄 쪽은 n−1로 읽었다. 다른 작업자의 결론은 읽지 않았다. HTML 및 원문은 수정하지 않았다.

식 6-1과 6-2는 `pages/p120.png`(인쇄 p.119)로도 확인했다. 두 TeX의 계수·지수·합금 목록·구간 부등호는 원문과 일치한다. 식 6-2에서 경계점의 등호가 없는 것도 원문 그대로이므로 오류로 세지 않았다. 외부 문헌의 진위를 별도로 검증한 보고서가 아니라, 지정 보고서와 HTML의 일치 감사이다.

## 발견 사항

### [슬라이드 34] ADDED-CLAIM — CONFIRMED
- 대상 문구(HTML 그대로): `예: 깊이 1~3 mm 이상`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “two adjacent macro-cracks of engineering significance (e.g., 1 to 3 mm or more)” — p.92, §4.1.
- 문제: 원문 예시에는 크기의 방향이 지정되어 있지 않다. HTML은 이를 깊이로 한정했다.
- 최소 교체안: `예: 1~3 mm 이상`

### [슬라이드 34] OMISSION-OF-HEDGE — CONFIRMED
- 대상 문구(HTML 그대로): `합체 모델은 가까운 균열이 따로 자랄 때보다 빠르게 합쳐지는 현상을, 고차 파괴역학 계산을 대신하는 일련의 규칙(conventions)으로 모의(simulate)하는 것입니다.`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “coalescence conventions may simulate two distinct modes by which cracks in proximity to one another may combine on a time scale faster than is predicted by treating growth of each crack separately” — p.92, §4.1.
- 문제: 원문의 may simulate 및 may combine이 빠진 단정이다.
- 최소 교체안: `합체 규칙은 가까운 균열이 각각의 성장을 따로 다룬 예측보다 빠르게 합쳐질 수 있는 두 가지 모드를 모의할 수 있습니다.`

### [슬라이드 34] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `합체 모델이란` / `기호와 하첨자` / `하첨자 읽는 법` / `적용 목적` / `적용 범위` / `어떻게 적용하나`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “4.1 Model Overview”; “4.2 Coalescence Model Development”; “4.2.1 Model Form Development”; “4.2.1.1 Prediction of Imminent Coalescence” — pp.92–93.
- 문제: 위 HTML 제목·표 라벨은 해당 원문의 제목·라벨이 아니다. ‘하첨자 읽는 법’ 열은 ID/OD의 약어 풀이를 담아 하첨자 설명으로도 맞지 않는다.
- 최소 교체안: 자체 제목·라벨을 삭제하고 해당 원문 절 제목의 번역을 사용한다. ID/OD 약어 풀이는 본문에 둔다.

### [슬라이드 35] OTHER — CONFIRMED
- 대상 문구(HTML 그대로): `합체 거리는 사용자 지정 값이며 xLPR 대상 부품에서 0~20 in 가능.`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “Through-wall crack coalescence distances between 0 and 20 inches are possible for components of interest in xLPR, depending on the sizes of the flaws involved.” — p.94, §4.2.1.1.
- 문제: 0~20 in의 가능 범위가 관련 결함 크기에 따라 달라진다는 조건을 생략했다.
- 최소 교체안: `합체 거리는 사용자 지정 값이며, 관련 결함의 크기에 따라 xLPR 대상 부품에서 0~20 in가 가능합니다.`

### [슬라이드 35] OTHER — CONFIRMED
- 대상 문구(HTML 그대로): `극값 0.0·0.75, 최빈값 0.5인 삼각분포 권장`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “In the absence of more detailed investigation, a triangular distribution is recommended with extremes at 0.0 and 0.75 and a mode at 0.5.” — p.98, §4.2.2.
- 문제: 권고의 전제인 ‘더 상세한 조사가 없는 경우’가 빠졌다. 슬라이드 37에는 이 조건이 보존되어 있다.
- 최소 교체안: `더 상세한 조사가 없으면 극값 0.0·0.75, 최빈값 0.5인 삼각분포 권장`

### [슬라이드 35] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `합체 거리: 언제 합치나` / `기호와 하첨자` / `하첨자 읽는 법` / `적용 목적`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “4.2.1.1 Prediction of Imminent Coalescence” — pp.93–94; “4.2.2 Treatment of Uncertainty” — p.98.
- 문제: 자체 제목·라벨이다. ‘합체 거리’는 하첨자가 있는 기호도 아니다.
- 최소 교체안: 원문 절 제목의 번역으로 교체하고 자체 기호 표의 제목·하첨자 열을 삭제한다.

### [슬라이드 36] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `합친 뒤 균열 모양: 유형·깊이·중심·길이` / `합친 균열의 속성` / `기호와 하첨자` / `하첨자 읽는 법` / `적용 목적` / `적용 방법` / `최대 깊이를 권장하는 이유`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “4.2.1.2 Coalesced Crack Geometry”; “The various conventions for modeling the updated attributes are discussed below.” — pp.94–95, §4.2.1.2.
- 문제: 원문 절 제목은 Coalesced Crack Geometry이다. 나열한 소제목·표 라벨은 원문에 없는 재구성이다. 표의 유형·깊이·중심·ID/OD 길이 규칙 자체는 원문과 일치한다.
- 최소 교체안: 제목을 `합체된 균열의 형상`으로 하고 자체 소제목 및 하첨자 표를 삭제한다.

### [슬라이드 37] OMISSION-OF-HEDGE — CONFIRMED
- 대상 문구(HTML 그대로): `이 불확실성은 합체로 이어지는 복잡한 과정의 변동성과 모델 오차(예: 균열 길이에 대한 체계적 의존성이 없음)를 반영합니다.`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “This uncertainty may reflect variability in the complex processes that lead to coalescence as well as model error” — p.98, §4.2.2.
- 문제: may reflect를 반영한다고 단정했다.
- 최소 교체안: `이 불확실성은 … 변동성과 모델 오차를 반영할 수 있습니다.`

### [슬라이드 38] OMISSION-OF-HEDGE — CONFIRMED
- 대상 문구(HTML 그대로): `표면균열의 응력확대계수 증대(intensification)가 시작되는 시점은 균열 깊이의 일부(예: 0.0~0.75 사이)인 합체 거리로 잘 예측된다는 실험 증거가 있으며, 선택한 modeling convention을 검증합니다.`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “Experimental evidence suggests that the onset of the intensification of stress intensity factor for surface cracks is well-predicted using a coalescence distance that is some fraction” — p.99, §4.2.3.
- 문제: 실험 증거가 ‘시사한다’는 표현을 직접적인 검증 단정으로 강화했다.
- 최소 교체안: `실험 증거는 … 합체 거리로 잘 예측됨을 시사하며, 선택한 modeling convention을 검증합니다.`

### [슬라이드 37] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `분포된 합체 거리` / `그 밖의 합체 모델링 convention`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “Uncertainty in the coalescence prediction may be incorporated through the use of distributed coalescence distances.”; “The other coalescence modeling conventions are fully deterministic.” — p.98, §4.2.2.
- 문제: 원문 문장의 일부를 떼어 새 표의 항목 라벨로 만들었다. 해당 원문에는 이 두 항목 제목이 없다. 용어 자체의 오역이라는 지적은 아니다.
- 최소 교체안: 표의 자체 라벨을 삭제하고 원문의 문단 구조를 따른다.

### [슬라이드 38] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `개요` / `인용된 연구` / `적용 범위`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “4.2.3 Model Validation”; “Specific instances of model validation are noted below”; “This module validation applies for the full range of crack and component geometries expected within xLPR Version 2.0.” — p.99, §4.2.3.
- 문제: 원문은 도입 문단·검증 사례 목록·마지막 적용 문장으로 되어 있다. HTML은 자체 항목 제목을 추가했다.
- 최소 교체안: 자체 라벨을 삭제하고 §4.2.3의 문단 및 목록 구조를 따른다.

### [슬라이드 39] OMISSION-OF-HEDGE — CONFIRMED
- 대상 문구(HTML 그대로): `겹침이 거의 없는 경우(Configuration A)에는 축방향으로 어긋난 두 균열 대신 큰 균열 하나가 생겨 누설 확률은 다소, 누설률은 크게, 파단 감수성은 축방향 어긋남 정도에 따라 크게 증가합니다.`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “This would increase probability of leakage somewhat, increase leakage rates significantly, and increase susceptibility to rupture significantly depending on the degree of axial offset.” — p.100, §4.3, Coplanar crack assumption.
- 문제: 원문은 would로 예상 영향을 설명한다. HTML은 증가한다고 단정한다.
- 최소 교체안: `… 증가할 것으로 봅니다.`

### [슬라이드 39] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `CONTENTS 5 / 6` / `§5 · coalescence module의 절차, 입력, 출력`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “5. CRACK COALESCENCE MODULE”; “Section 5.1 provides an overview of the module, including a description of its scope and limitations.” — p.103, §5 도입.
- 문제: CONTENTS 번호 및 §5의 부제는 HTML에서 만든 라벨이다. CRACK COALESCENCE MODULE 자체는 원문 제목이다.
- 최소 교체안: `5. CRACK COALESCENCE MODULE`만 남긴다.

### [슬라이드 40] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `기호와 하첨자` / `하첨자 읽는 법` / `적용 목적` / `어떻게 동작하나` / `입력` / `범위`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “5.1 Module Scope and Limitations” — pp.103–104; “5.2.1.1 Input Allocation, Input Verification, and Output Requirements”; “5.2.1.2 Pre-Processing Requirements” — p.105.
- 문제: 자체 소제목·표 라벨이다. Crack A/B와 absorbed crack은 하첨자가 아니다.
- 최소 교체안: 자체 라벨을 삭제하고 인용한 원문 절 제목을 사용한다.

### [슬라이드 41] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `기호와 하첨자` / `하첨자 읽는 법` / `coalescence criteria` / `순서`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “5.2.1.3 Iterative Application of Coalescence Rules”; “These requirements rely on the designation of ‘Crack A’ and ‘Crack B’, as detailed below” — p.105, §5.2.1.3.
- 문제: 원문 본문 용어 coalescence criteria를 별도 소제목으로 승격했고, 나머지도 자체 라벨이다. Coalescence Direction flag는 하첨자가 아니다. 순회·판정 내용은 원문과 일치한다.
- 최소 교체안: §5.2.1.3 제목 아래 본문으로 합치고 자체 라벨을 삭제한다.

### [슬라이드 42] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `입력 매개변수와 플래그` / `coalescence module 입력` / `적용 목적` / `적용 방법` / `단위와 허용 범위(표 5-1)` / `coalescence distance를 정하는 규칙`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “5.3.2 Coalescence Model Parameters and Flags” — pp.110–111; “5.3 Module Inputs and Outputs”; “Table 5-1. Coalescence Subroutine Arguments” — p.109; “5.2.1.4 Defining Coalescence Distance” — p.106.
- 문제: 첫 제목은 원문 절 제목에서 ‘합체 모델’이 빠졌고, 나머지는 자체 소제목이다.
- 최소 교체안: `5.3.2 합체 모델 매개변수와 플래그`, `표 5-1. 합체 서브루틴 인수`, `5.2.1.4 합체 거리 정의` 등 해당 원문 제목의 번역을 사용하고 자체 소제목을 삭제한다.

### [슬라이드 43] OTHER — CONFIRMED
- 대상 문구(HTML 그대로): `5.2.1.5 Updating Crack Attributes` (연속 두 번)
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “5.2.1.5 Updating Crack Attributes” — p.107, §5.2.1.5(한 번).
- 문제: 추출된 게시본에서 같은 절 제목이 중복된다. 내용 오류는 아니지만 원문 구조와 다르다.
- 최소 교체안: 중복 한 개 삭제.

### [슬라이드 43] OTHER — CONFIRMED
- 대상 문구(HTML 그대로): `5.2.1.7 Performance`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “5.2.1.7 Performance Requirements”; “the following runtime and memory requirements were imposed” — p.108, §5.2.1.7.
- 문제: 원문 제목에서 Requirements를 누락했다. 요구 성능과 실측 성능의 구별에 중요한 단어이다. 본문은 ‘이어야 합니다’로 요구사항임을 보존하고 있다.
- 최소 교체안: `5.2.1.7 Performance Requirements`

### [슬라이드 43] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `CONTENTS 6 / 6` / `§6 · PWSCC·피로·coalescence의 향후 과제와 개정 식 6-1, 6-2`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “6. RECOMMENDATIONS FOR FUTURE WORK”; “This section identifies several areas for improvement within the context of crack growth and coalescence” — p.117, §6 도입.
- 문제: 목차 번호와 설명형 부제가 원문에 없다. RECOMMENDATIONS FOR FUTURE WORK는 원문 제목이다.
- 최소 교체안: `6. RECOMMENDATIONS FOR FUTURE WORK`만 남긴다.

### [슬라이드 44] OTHER — CONFIRMED
- 대상 문구(HTML 그대로): `정량화에는 계획된 실험이 도움이 될 수 있다고 합니다.`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “Carefully planned laboratory experiments may help quantify this correlation.” — p.118, §6.1.1, Initiation-growth correlation.
- 문제: carefully와 laboratory를 생략했다. ‘계획된 실험’은 원문에서 요구한 신중한 계획과 실험실이라는 한정을 보존하지 못한다.
- 최소 교체안: `신중하게 계획한 실험실 실험이 이 상관의 정량화에 도움이 될 수 있다고 합니다.`

### [슬라이드 44] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `기계적 성질, 냉간가공, 열처리` / `재료 경계면, 발생-성장 상관`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “Mechanical properties”; “Cold work”; “Heat treatment”; “Material interfaces”; “Initiation-growth correlation” — pp.117–118, §6.1.1.
- 문제: 원문에서 독립된 다섯 항목을 두 개의 새 복합 제목으로 만들었다. 각각의 한국어 번역어 자체는 지적하지 않는다.
- 최소 교체안: 원문처럼 다섯 항목으로 각각 표시한다.

### [슬라이드 45] OTHER — CONFIRMED
- 대상 문구(HTML 그대로): `Alloy 600 다음으로 Alloy 690과 그 용접금속(Alloy 52, 152 등)의 PWSCC CGR 모델 개발이 바람직하다고 설명하며`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “After Alloy 600 and its associated weld metals, PWSCC CGR models are desired for Alloy 690 and its associated weld metals” — p.118, §6.1.2.
- 문제: 선행 대상으로 명시한 Alloy 600의 관련 용접금속을 생략했다.
- 최소 교체안: `Alloy 600과 그 관련 용접금속 다음으로 …`

### [슬라이드 45] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `내용`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “6.1.2 Other SCC Models”; “Some specific conditions of interest are noted below” — p.118, §6.1.2.
- 문제: 원문에 없는 소제목이다. Alloy 690 및 BWR 소제목은 원문 항목에 대응하므로 지적하지 않는다.
- 최소 교체안: `내용` 삭제.

### [슬라이드 46] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `개정` / `기호와 하첨자` / `하첨자 읽는 법`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “6.2.1 Updated Fatigue Crack Growth Relations for Austenitic SS” — pp.118–119; “f” (하첨자 alloy) “= alloy factor” — p.48, §2.3.3.1.
- 문제: ‘개정’이라는 분류 제목과 기호 표 라벨은 원문에 없다. 합금 계수 정의와 식 자체는 맞는다.
- 최소 교체안: 자체 분류·표 라벨을 삭제하고 §6.2.1 제목 및 원문 정의를 본문으로 둔다.

### [슬라이드 47] OMISSION-OF-HEDGE — CONFIRMED
- 대상 문구(HTML 그대로): `Ni계 피로의 식 2-13에서 A_{env}를 샘플할 때 후속 버전에서 쓰려는 안입니다.`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “This model could be improved in a later version of xLPR by implementing an environmental factor whose dispersion could vary with the fatigue CGR prediction in air.” — p.119, §6.2.2. “The more detailed treatment is recommended for future work in Section 6.” — p.45, 각주 14, §2.3.2.
- 문제: 원문의 개선 가능성·향후 작업 권고를 후속 버전에서 사용하려는 의도로 표현했다. 확정된 채택 의도는 원문이 말하지 않는다.
- 최소 교체안: `식 2-13의 환경계수 산포가 공기 중 피로 CGR 예측에 따라 달라지도록 구현하면 후속 버전에서 모델을 개선할 수 있으며, 이 상세 처리는 향후 작업으로 권고됩니다.`

### [슬라이드 47] OTHER — CONFIRMED
- 대상 문구(HTML 그대로): `고정 log-σ = 1.2를 권장합니다(p.45 각주 14).`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “a fixed log-σ parameter of 1.2 is recommended at the risk of incorporating excessive variability at high CGRs.” — p.45, 각주 14, §2.3.2.
- 문제: 권고에 붙은 높은 CGR에서 과도한 변동성을 포함할 위험이라는 유보를 생략했다.
- 최소 교체안: `높은 CGR에서 과도한 변동성을 포함할 위험이 있으나 고정 log-σ = 1.2를 권장합니다.`

### [슬라이드 47] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `개정` / `기호와 하첨자` / `하첨자 읽는 법`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “6.2.2 Enhancements to Probabilistic Model for Nickel-Based Alloys” — p.119, §6.2.2.
- 문제: 원문에 없는 분류 제목·표 라벨이다. log-σ에 대한 하첨자 풀이도 해당하지 않는다.
- 최소 교체안: 자체 라벨을 삭제하고 원문 절 제목과 본문 정의만 사용한다.

### [슬라이드 49] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `축방향 균열과 미세균열`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “Axial crack coalescence”; “Micro-fissure coalescence” — p.121, §6.3.2.
- 문제: 별개 항목 두 개를 원문에 없는 하나의 제목으로 합쳤고 각 항목의 coalescence도 제목에서 빠졌다.
- 최소 교체안: `축방향 균열 합체`와 `미세균열 합체`를 각각 표시한다.

### [슬라이드 49] OTHER — PLAUSIBLE
- 대상 문구(HTML 그대로): `설명 문장은 새로 썼고 원문 저작권은 EPRI에 있습니다. 슬라이드 목차의 영문 철자(MODULE, MODULE, RECOMMENDATIONS)는 그대로 두었습니다.`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “5. CRACK COALESCENCE MODULE” — p.103, §5; “6. RECOMMENDATIONS FOR FUTURE WORK” — p.117, §6. 해당 구절들은 목차의 영문 철자만 확인한다.
- 문제: 집필 방식·저작권 귀속·편집 이력은 지정 대조 범위의 기술 본문으로 확인할 수 없다. 특히 ‘설명 문장은 새로 썼다’는 원문 대조만으로 작성 이력을 확정할 수 없다. 저작권 귀속이 틀렸다고 판정한 것은 아니다. 보고서 한 편을 근거로 삼았다는 편집자 고지까지 원문의 과학 주장과 동일하게 판단하지 않는다.
- 최소 교체안: 원문만 말해야 하는 엄격한 조건을 적용한다면 이 편집자 고지를 기술 설명과 분리하거나 삭제한다. 저작권 귀속은 확인 불가로 남긴다.

## 전체 대조 기록

확인 단위는 마커를 제외한 비어 있지 않은 추출 줄이다. 제목·문단·표의 각 행·수식 줄·쪽수/절 인용을 모두 포함한다. 한 문단에 있는 여러 문장·수치·조건도 각각 대조했으나 별도 수로 부풀리지 않았다. 표 행 수에는 헤더 행을 포함한다. 아래 ‘추가 지적 없음’은 위 발견 외의 항목에 관한 것이다.

| 슬라이드 | 확인한 추출 줄 | 표 행 | 수식 | 대조 쪽(인쇄) 및 결과 |
|---|---:|---:|---:|---|
| 34 | 14 | 3 | 0 | pp.92–93, §4.1–4.2.1.1. 위 3건 외 추가 지적 없음. ID/OD, ligament 정의는 해당 문맥과 부합. |
| 35 | 14 | 8 | 0 | pp.93–94, 98, §4.2.1.1·4.2.2. 위 3건 외 추가 지적 없음. 0.5, 0.75, 0~20 in 및 ASME 문맥 확인. |
| 36 | 19 | 9 | 0 | pp.94–95, §4.2.1.2. 위 1건 외 추가 지적 없음. 다섯 속성 및 각 균열 조합 확인. |
| 37 | 7 | 5 | 0 | pp.98–99, §4.2.2 및 각주 35. 위 2건 외 추가 지적 없음. 삼각분포·epistemic·결정적 convention 확인. |
| 38 | 11 | 9 | 0 | p.99, §4.2.3 및 각주 36–37. 위 2건 외 추가 지적 없음. 네 연구의 역할·generally·적용 범위 확인. |
| 39 | 13 | 7 | 0 | pp.100–101, §4.3; 말미 목차는 p.103 §5. 위 2건 외 추가 지적 없음. 6개 가정의 내용과 약 절반 등의 수치 확인. |
| 40 | 14 | 3 | 0 | pp.103–105, §5.1·5.2.1.1–.2, p.111 §5.3.2. 위 1건 외 추가 지적 없음. 1개월과 3개 이상 합체의 희소성은 p.111에 있음. |
| 41 | 10 | 2 | 0 | pp.105–106, §5.2.1.3; pp.110–111 §5.3.2. 위 1건 외 추가 지적 없음. A/B 순서·방향 flag 1/2·기준 확인. |
| 42 | 17 | 6 | 0 | p.106 §5.2.1.4, pp.109–111 §5.3–5.3.2, 표 5-1. 위 1건 외 추가 지적 없음. 입력 다섯 행·단위·명시된 범위·코드 모두 확인. |
| 43 | 13 | 0 | 0 | pp.107–108 §5.2.1.5–.7, pp.111–112 §5.3.3; 말미 목차 p.117 §6. 위 3건 외 추가 지적 없음. 101~115, 201과 210, 301, 30 kB, 5개/2사례, 1000회/10초 확인. |
| 44 | 11 | 0 | 0 | pp.117–118, §6.1.1. 위 2건 외 추가 지적 없음. K 구간·계수 2.0·재료/계면·상관 확인. |
| 45 | 8 | 0 | 0 | p.118, §6.1.2. 위 2건 외 추가 지적 없음. 식 3-1 언급·합금 52/152·BWR IGSCC 확인. |
| 46 | 9 | 2 | 1 | pp.118–119 §6.2.1, p.48 §2.3.3.1, p.71 표 3-1. 위 1건 외 추가 지적 없음. 식 6-1은 이미지로 일치 확인. 2000 s 상한 제거도 p.119에 있음. |
| 47 | 10 | 3 | 1 | p.119 §6.2.2, p.45 §2.3.2 및 각주 14. 위 3건 외 추가 지적 없음. 식 6-2는 이미지로 일치 확인. −12/−8에서 1.2/0.0 선형 변화도 p.45에 있음. |
| 48 | 5 | 0 | 0 | 슬라이드 48: 지적 없음(확인한 항목 수 5). p.119, §6.2.3–6.2.4의 모든 문장과 두 절 제목·인용 확인. |
| 49 | 9 | 0 | 0 | pp.120–121, §6.3.1–6.3.2. 위 2건 외 추가 지적 없음. 3/4 재료 그룹·대칭·비동일평면·표면 아래 결함·1:1 조건·축방향/미세균열 확인. |

모든 명시된 인쇄 쪽수와 절 번호를 확인했다. 슬라이드 34의 넓은 절 인용은 세부 §4.2.1.1의 상위 절을 포함하므로 CITATION 오류로 세지 않았다. 슬라이드 46의 §6.2.1 도입은 p.118이며 본문에서 p.118–119를 별도로 명시한다. 슬라이드 43의 ‘201과 210’은 원문 그대로이고 201~210으로 고치면 안 된다. 슬라이드 42에서 ‘거리는 모두 0 이상’은 앞서 열거한 합체 거리 입력을 지칭하는 문맥으로 읽었다. 이를 ID 반길이의 허용 범위로 확대해서는 안 된다(표 5-1은 ID 반길이 >0).

## 유형별 개수

한 발견 제목을 한 건으로 집계했다. 동일 슬라이드의 자체 제목·라벨 여러 개는 한 건으로 묶었다.

| 유형 | CONFIRMED | PLAUSIBLE | 합계 |
|---|---:|---:|---:|
| WRONG | 0 | 0 | 0 |
| OMISSION-OF-HEDGE | 5 | 0 | 5 |
| ADDED-CLAIM | 1 | 0 | 1 |
| COINED-TITLE | 15 | 0 | 15 |
| CITATION | 0 | 0 | 0 |
| EQUATION | 0 | 0 | 0 |
| OTHER | 7 | 1 | 8 |
| 합계 | 28 | 1 | 29 |

저장소 작업: 시작 시 `git pull`을 시도했으나 `.git/FETCH_HEAD: Permission denied`로 실패했다. `git add -- round35/codex_C.md`도 `.git/index.lock: Permission denied`로 실패했다. 따라서 커밋과 푸시는 완료하지 못했다. 이 세션의 파일 시스템 권한에서 `.git`은 읽기 전용이다. 기존 다른 작업물은 수정하지 않았다.

ROUND35C DONE
