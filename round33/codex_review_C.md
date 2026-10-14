# Round 33 — C: 보고서 직접 진술 대조

검토 대상: `XLPR_발표자료_수식정리.html`의 순서상 34–47페이지. 본문 문장, 기호·하첨자 설명, 모든 표 셀과 수식을 대조했다. 유일한 근거는 `xLPR Models Subgroup Report—Crack Growth and Coalescence`(ML16341B051)이며, 아래 p.는 보고서의 인쇄 쪽수다. 식 6-1·6-2와 표 5-1은 PyMuPDF로 렌더링한 원문 이미지도 확인했다.

## HTML 36페이지

1. **INFERENCE/DERIVED/JUDGMENT — 계산을 계속하기 위한 필수 조건이라는 설명 추가**
   - 대상: “합쳐진 균열은 xLPR가 인식하는 세 가지 이상화 균열 중 하나로 다시 정의되어야 계속 계산할 수 있습니다.”
   - 원문: p.94는 “These transitioning rules were developed based on physical expectations and logical considerations when constrained to the three crack types recognized within the Version 2.0 xLPR Framework.”라고 설명한다. p.104는 세 이상화 균열 유형이 다른 계산에도 필요하다고 설명하지만, 합친 균열을 다시 정의해야 계산을 계속할 수 있다는 절차·목적 문장은 직접 제시하지 않는다.
   - 최소 교체: “합체 후 균열 유형 규칙은 xLPR 2.0이 인식하는 세 균열 유형의 제약 아래 물리적 기대와 논리적 고려에 따라 개발되었습니다(p.94).”

2. **INFERENCE/DERIVED/JUDGMENT — 예상 결과를 목적 설명으로 변경**
   - 대상: “OD 길이 규칙은 합체 전후 누설이 이어지게 하려는 것입니다(p.95).”
   - 원문: p.95는 “This convention is consistent with physical expectations and should result in acceptable leakage continuity immediately before and after coalescence.”라고 한다. 허용할 만한 누설 연속성이 예상된다는 진술이며, 그 목적을 위해 규칙을 만들었다고 직접 말하지 않는다.
   - 최소 교체: “원문은 OD 길이 규칙이 물리적 기대와 일치하며 합체 직전과 직후에 허용할 만한 누설 연속성을 가져올 것으로 설명합니다(p.95).”

## HTML 42페이지

1. **OVERSTATED — ‘대부분의 관심 부품’이라는 적용 범위를 삭제**
   - 대상: “PWSCC 성장은 냉간가공 수준에 의존하는 것으로 알려져 있으나, 두꺼운 벽의 가공 Alloy 600은 관심 부품에서 예상되는 것보다 높은 냉간가공이 있어야 CGR이 크게 빨라진다고 설명합니다.”
   - 원문: p.117는 “cold work levels greater than that expected for most components of interest are necessary for the cold work to result in a substantial acceleration of the CGR.”라고 한다. 모든 관심 부품으로 일반화하지 않고 ‘most’로 한정한다.
   - 최소 교체: “PWSCC 성장은 냉간가공 수준에 의존하며, 두꺼운 벽의 가공 Alloy 600에서는 대부분의 관심 부품에서 예상되는 것보다 높은 냉간가공 수준이 있어야 CGR이 크게 빨라진다고 설명합니다(p.117).”

## HTML 44페이지

1. **쪽수 인용 — 적용 식과 재료 코드의 근거 쪽수 누락**
   - 대상: “스테인리스 피로(코드 6, 7, 8)에서 식 2-19의 f_alloy 자리에 넣습니다.” / 페이지 상단 “원문 p.119 · §6.2.1”.
   - 원문: p.119는 식 6-1의 개정 합금 그룹·값을 제시한다. 식 2-19의 오스테나이트 스테인리스 피로 모델은 p.48, 재료 코드 6·7·8은 p.71 표 3-1에 있다. 해당 적용 설명 전체의 근거를 p.119만으로 표시할 수 없다.
   - 올바른 쪽수: p.48, p.71 표 3-1, p.119.
   - 최소 교체: “오스테나이트 스테인리스 피로 모델의 식 2-19에는 f_alloy가 포함되며(p.48), 스테인리스 재료 코드는 6·7·8입니다(p.71, 표 3-1). 개정 합금 계수는 식 6-1에 제시됩니다(p.119).”

2. **INFERENCE/DERIVED/JUDGMENT — 두 식의 구현 상태를 비교한 작성자 종합**
   - 대상: “식 6-2(향후 개선안)와 구현 상태가 다릅니다.”
   - 원문: p.118–119의 §6.2.1은 모듈 업데이트를 설명하고, p.119의 §6.2.2는 후속 버전의 개선 가능성을 설명한다. 두 식의 ‘구현 상태가 다르다’는 비교 문장은 직접 제시하지 않는다.
   - 최소 교체: **DELETE**. 앞 문장의 모듈 업데이트 설명과 다음 페이지의 향후 개선안 설명만 유지한다.

## HTML 45페이지

1. **OVERSTATED — 구간별 식을 제한 없는 증가 관계로 일반화**
   - 대상: “보고서의 제안 모델은 공기 중 CGR이 작을수록 log-σ를 크게 둡니다.”
   - 원문: p.119 식 6-2는 CGR_air > 10⁻⁸에서 0, 10⁻¹² < CGR_air < 10⁻⁸에서 −2.4 − 0.3 log₁₀(CGR_air), CGR_air < 10⁻¹²에서 1.2를 제시한다. 양쪽 바깥 구간은 상수다. p.45는 log₁₀(CGR_air) = −12에서 1.2, −8에서 0.0까지 선형으로 변한다고 직접 설명한다.
   - 최소 교체: “log-σ는 log₁₀(CGR_air) = −12에서 1.2, −8에서 0.0까지 선형으로 변합니다(p.45).”

2. **OVERSTATED — 권장값을 실제 사용값으로 단정**
   - 대상: “이 보고서(xLPR 2.0)에서는 구현할 수 없어 고정값 1.2를 씁니다.”
   - 원문: p.45 각주 14는 “An environmental factor distribution parameter that varies as a function of air fatigue CGR cannot be implemented in Version 2.0 of xLPR. Instead, a fixed log-σ parameter of 1.2 is recommended at the risk of incorporating excessive variability at high CGRs.”라고 한다. ‘1.2를 권장’하는 진술이며 해당 값이 모든 실행에서 실제 사용된다고 단정하지 않는다.
   - 최소 교체: “xLPR 2.0에서는 공기 중 피로 CGR에 따라 변하는 환경계수 분포 매개변수를 구현할 수 없어, 고정 log-σ = 1.2를 권장합니다(p.45, 각주 14).”

3. **쪽수 인용 — xLPR 2.0의 구현 제약·고정값 근거는 p.119가 아님**
   - 대상: 페이지 상단 “원문 p.119 · §6.2.2”와 그 아래의 “이 보고서(xLPR 2.0)에서는 구현할 수 없어 고정값 1.2를 씁니다.”
   - 원문: p.119는 후속 버전 개선안과 식 6-2를 제시한다. 구현 불가와 고정 1.2 권장은 p.45 각주 14에 있다. p.83 각주 30에도 현재 프로그램에서 변동하는 분포 표준편차를 구현할 수 없어 경계 입력을 권장한다고 설명한다.
   - 올바른 쪽수: 식 6-2는 p.119; 구현 제약과 고정 1.2 권장은 p.45 각주 14.
   - 최소 교체: 상단을 “원문 p.119 · §6.2.2 (관련: p.45 각주 14)”로 바꾸고, 구현 제약 문장에는 위 항목의 교체문처럼 p.45 각주 14를 붙인다.

4. **INFERENCE/DERIVED/JUDGMENT — 식 표기에 대한 작성자의 결손 관찰**
   - 대상: “경계값 10⁻⁸, 10⁻¹²에 등호가 없고 CGR_air 단위도 명시되어 있지 않습니다(원문 표기).”
   - 원문: p.119 식 6-2의 부등호에 등호가 없고 식 옆에 CGR_air 단위가 별도로 표기되지 않은 것은 이미지로 확인된다. 그러나 보고서가 경계값·단위의 누락에 관해 직접 진술하지는 않는다. 이 문장은 보고서 내용의 인용·의미 보존형 바꿔쓰기가 아니라 작성자의 표기 관찰이다.
   - 최소 교체: **DELETE**. 식 6-2 자체의 원문 부등호는 그대로 유지한다.

## HTML 46페이지

1. **INFERENCE/DERIVED/JUDGMENT — 원문의 ‘cycles’를 ‘운전 주기’로 특정**
   - 대상: “또한 피로로 진전 중임이 확인된 균열이 한 번 이상 운전 주기 동안 사용된 사례를 가동 중 검사 보고서에서 찾으면 현장 조건의 피로 CGR을 추정하는 데 쓸 수 있다고 제안합니다(p.119).”
   - 원문: p.119는 “cracks verified to be advancing by fatigue were left in service for one or more cycles, thus allowing some estimation of fatigue CGR in field conditions.”라고 한다. 여기서는 ‘cycles’를 ‘운전 주기’라고 별도로 정의하거나 특정하지 않는다.
   - 최소 교체: “가동 중 검사 보고서에서 피로로 진전 중임이 확인된 균열이 한 주기 이상 사용된 사례를 찾으면, 현장 조건의 피로 CGR을 어느 정도 추정할 수 있다고 설명합니다(p.119).”

## 문제를 찾지 못한 HTML 페이지

- 34, 35, 37, 38, 39, 40, 41, 43, 47.
