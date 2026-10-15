# round35 A — 슬라이드 1–15 원문 대조 감사

대상은 `audit_html_all.txt`의 HTML SLIDE 1–15 마커 사이 텍스트다. HTML과 원문은 수정하지 않았다. Claude의 조사·검토 문서는 읽지 않았다.

원문: EPRI, Kyle Schmitt, *xLPR Models Subgroup Report—Crack Growth and Coalescence*, xLPR-MSGR-CGR Version 1.0, 2016-06-29. 아래 모든 영어 인용은 이 보고서에서 가져왔다. 쪽수는 인쇄 쪽이며 `=====PAGE n=====`의 n−1이다. `pages/p022, p028, p034, p035, p039, p040, p041, p043.png`를 직접 열어 식 2-1–2-6, 2-8–2-14를 확인했다. 이미지 파일명의 숫자는 인쇄 쪽보다 1 크다.

## 확인 범위와 항목 기록

확인 항목 수는 마커 구간의 비공백 텍스트 줄 수다. 한 줄에 여러 문장이 있으면 그 문장을 모두 확인했으며, 표 머리글도 한 항목으로 센다. 제목·공통 라벨도 제외하지 않았다. 슬라이드 2 끝의 다음 장 안내 3줄도 마커 구간에 포함하여 확인했다. 이 수는 주장 개수나 오류 개수가 아니다.

| 슬라이드 | 확인 항목 수 | 표 줄 수(머리글 포함) | TeX 수 | 대조한 주요 인쇄 쪽/절 |
|---|---:|---:|---:|---|
| 1 | 18 | 9 | 0 | 17–18 / §1.1 |
| 2 | 15 | 0 | 0 | 18–20 / §1.2–1.4, §2 서두·§2.1 |
| 3 | 21 | 10 | 1 | 20–25, 76, 79, 82 / §2.1, §2.2.1–2.2.1.4, §3.3, §3.3.2 |
| 4 | 16 | 6 | 1 | 22, 26–30, 82 / §2.2.1.2, §2.2.2–2.2.2.4, §3.3.2 |
| 5 | 14 | 4 | 1 | 32–35, 37, 81–82 / §2.2.3–2.2.3.4, §3.3.2 |
| 6 | 15 | 5 | 1 | 33–35, 37, 76, 81–82 / §2.2.3.1–2.2.3.4, §3.3, §3.3.2 |
| 7 | 15 | 5 | 1 | 33–34, 72 / §2.2.3.1–2.2.3.2, §3.2.1.3 |
| 8 | 13 | 3 | 1 | 33–34, 72, 81 / §2.2.3.1, §3.2.1.3, §3.3.2 |
| 9 | 14 | 4 | 1 | 38, 72, 76, 79 / §2.2.4.2, §3.2.1.3, §3.3, §3.3.2 |
| 10 | 13 | 3 | 1 | 39 / §2.3.1 |
| 11 | 13 | 3 | 1 | 39–40, 43 / §2.3.1, §2.3.2.2 |
| 12 | 14 | 4 | 1 | 39–42, 76–77, 87 / §2.3.1, §3.3, §3.3.4 |
| 13 | 15 | 3 | 1 | 39–42, 83, 86 / §2.3.1, §3.3.3, 表3-5 |
| 14 | 15 | 5 | 1 | 42–44, 71–72, 77–78, 86 / §2.3.2–2.3.2.2, §3.2.1.2–3.2.1.3, §3.3.1, 表3-5 |
| 15 | 15 | 5 | 1 | 42–44, 71–72, 77 / §2.3.2–2.3.2.2, §3.2.1.2–3.2.1.3, 表3-3 |

TeX 13개는 계수·부호·지수·첨자·곱의 인자·경우를 나누는 조건을 포함해 이미지와 일치했다. 식 2-12 뒤의 `(R≥0.10, 28 points)`는 원문 식 자체에는 없고 바로 앞 데이터 설명에 있다. 아래에서 편집 추가로 구분한다.

상단의 `원문 p.xx · §x.x`는 각 식 또는 소개 부분의 위치로는 모두 맞는다. 본문에서 별도로 붙인 p.17, 18, 19, 22, 27–30, 33–35, 37, 39–40, 42, 72, 76–77, 81–83, 86–87과 §3.3.1도 해당 내용을 실제로 포함한다. 다만 상단 한 쪽이 슬라이드 전체의 출처를 포괄하는 것은 아니다. 예를 들어 슬라이드 3의 26 heat·158점은 p.23, 검증 범위는 p.25에 있다. 상단 표시가 식의 쪽인 것을 잘못된 인용으로 판정하지 않았다.

## 발견 사항 — 본문·조건·표현

### [슬라이드 1] OMISSION-OF-HEDGE — CONFIRMED
- 대상 문구(HTML 그대로): `원문은 다섯 가지를 듭니다.`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “Among the criteria for selection were:” (p.17, §1.1), 뒤에 (a)–(e).
- 문제: 원문은 선정 기준 중 일부를 열거한다. HTML은 `Among`에 해당하는 비완결적 열거 표현을 생략한다. 다섯 가지가 전부라고 원문이 확정한 것은 아니다.
- 최소 교체안: `선정 기준에는 다음 다섯 가지가 포함됩니다.`

### [슬라이드 1] OMISSION-OF-HEDGE — CONFIRMED
- 대상 문구(HTML 그대로): `Alloy 600 외 재료도 넣을 수 있게 모듈을 유연하게 만들고 개선계수 항을 둠. 적절한 입력값 개발은 프로젝트 밖에서 진행 중`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “provided that appropriate model parameter inputs are developed.”; “The effort to develop appropriate and validated model parameter inputs for PWSCC in Alloys 52 and 152 is ongoing outside of the xLPR Project.” (p.18, §1.1 항목 (6)).
- 문제: 타 재료를 수용하는 데 필요한 입력값 개발 조건이 명시적으로 붙지 않았고, 진행 중인 입력 개발의 `validated`가 빠졌다. 조건부 수용과 검증된 입력 개발이라는 원문 제한을 유지해야 한다.
- 최소 교체안: `적절한 모델 매개변수 입력이 개발된다는 조건으로 Alloy 600 및 관련 용접금속 외 재료를 수용하도록 모듈을 유연하게 매개변수화하고 개선계수 항을 포함함. Alloy 52·152의 PWSCC에 적절하고 검증된 입력을 개발하는 노력은 xLPR 프로젝트 밖에서 진행 중임.`

### [슬라이드 2] OMISSION-OF-HEDGE — CONFIRMED
- 대상 문구(HTML 그대로): `즉 균열 끝 상호작용(crack tip interaction)으로 응력확대계수가 커지는 것과 두 균열을 가르는 ligament의 소성 붕괴(plastic collapse)`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “including crack tip interaction that can lead to intensified stress intensity factors and plastic collapse of a ligament separating two cracks.” (p.19, §1.2).
- 문제: `can lead to`의 가능 표현이 `커지는 것`으로 단정되었다. 또한 `including`이 `즉`으로 바뀌어 예시적 포함 관계가 동일시 설명으로 바뀐다.
- 최소 교체안: `응력확대계수 증가로 이어질 수 있는 균열 끝 상호작용과 두 균열을 가르는 ligament의 소성 붕괴를 포함한 메커니즘`

### [슬라이드 3] OMISSION-OF-HEDGE — CONFIRMED
- 대상 문구(HTML 그대로): `K 약 15 미만에서의 K 의존성은 검증되지 않았으므로`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “the dependence of CGR on K for thick-wall material was not specifically verified for lower K values.” (p.22, §2.2.1.1).
- 문제: `specifically`가 빠져 검증에 관한 진술의 강도가 달라졌다. 원문은 해당 개발 데이터에서 낮은 K 의존성을 특별히 검증하지 않았다고 말한다. 같은 슬라이드의 별도 검증 범위 K=10–80과도 구분해야 한다.
- 최소 교체안: `두꺼운 벽 재료에서 더 낮은 K 값에 대한 CGR의 K 의존성은 특별히 검증되지 않았으므로`

### [슬라이드 4] ADDED-CLAIM — CONFIRMED
- 대상 문구(HTML 그대로): `식 2-1과 같은 틀이지만 시편 계수 대신 용접 계수 4개를 곱합니다.`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “includes an alloy factor to account for the reduced PWSCC susceptibility of Alloy 82 versus Alloys 182/132”; “an orientation factor to account for the influence of crack orientation” (p.27, §2.2.2.1). 같은 쪽 정의는 “common factor applied to each unique weld”, “within-weld factor”, “alloy factor”, “crack orientation factor”.
- 문제: 원문은 네 인자를 모두 `용접 계수`라는 범주로 명명하지 않았다. heat/within-heat 인자를 weld/within-weld 인자로 대응시키는 것 외에 alloy/orientation 인자가 추가된 구조인데, 네 인자를 시편 계수의 대체물로 한꺼번에 설명한다.
- 최소 교체안: `Alloy 600 식과 유사하며, f_weld, f_ww 외에 합금 계수 f_alloy와 균열 방향 계수 f_orient를 포함합니다.`

### [슬라이드 4] OTHER — PLAUSIBLE
- 대상 문구(HTML 그대로): `용접 wire/stick의 heat 처리와 용접 제작을 설명`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “common factor applied to each unique weld to account for weld wire/stick heat processing and for weld fabrication” (p.27, §2.2.2.1).
- 문제: `heat 처리`가 재료 heat의 가공을 뜻하는지 열처리를 뜻하는지 HTML만으로 확인 불가. 원문은 `heat treatment`라고 쓰지 않았다. 번역어 자체의 오류로 확정하지 않으며, 의미 혼동 가능성만 기록한다.
- 최소 교체안: `각 개별 용접에 적용되는 공통 계수로, 용접 wire/stick heat processing 및 용접 제작을 반영`

### [슬라이드 5] OMISSION-OF-HEDGE — CONFIRMED
- 대상 문구(HTML 그대로): `이때 Q_{g}는 실제 활성화 에너지 104 kJ/mol을 사용합니다.`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “The recommended activation energy input when using the Alloys 82/182/132 PWSCC CGR model with hydrogen adjustment (104 kJ/mol) is close to the average actual activation energy across these studies.” (p.35, §2.2.3.2). 표 3-4는 thermal activation energy를 “distributed (epistemic)”, “Normal”, “mean 104”, “stdev 20”으로 제시한다 (p.82, §3.3.2).
- 문제: `recommended`가 빠지고 104가 사용할 실제 활성화 에너지로 단정된다. 원문의 확률 입력 권고는 평균 104, 표준편차 20 kJ/mol이며 고정값 104로 한정하지 않는다.
- 최소 교체안: `수소 보정을 포함할 때 권고하는 활성화 에너지 입력은 104 kJ/mol이며 연구들의 평균 실제 활성화 에너지에 가깝습니다. 표 3-4는 평균 104, 표준편차 20 kJ/mol의 정규분포를 권고합니다.`

### [슬라이드 5] OMISSION-OF-HEDGE — CONFIRMED
- 대상 문구(HTML 그대로): `Alloy 82는 피크 위치가 어긋나 추가 시험이 필요합니다.`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “Very limited data for Alloy 82 analyzed in MRP-263 suggested a roughly Gaussian dependency relative to ECP, but exhibited a shift in the peak CGR from the estimated location of the Ni/NiO transition. Additional testing is required to resolve this apparent discrepancy.” (p.34, §2.2.3.2).
- 문제: `Very limited data`, 전이점의 `estimated location`, 불일치의 `apparent`가 빠진다. 한정된 자료에서 추정 전이 위치와 보이는 불일치를 Alloy 82의 확정된 일반 특성처럼 표현한다.
- 최소 교체안: `MRP-263에서 분석한 Alloy 82의 매우 제한된 데이터는 대략 가우스형 ECP 의존성을 시사했으나, 최대 CGR 위치가 Ni/NiO 전이의 추정 위치에서 이동해 나타났습니다. 이 겉보기 불일치를 해소하려면 추가 시험이 필요합니다.`

### [슬라이드 6] WRONG — CONFIRMED
- 대상 문구(HTML 그대로): `peak-to-valley 비: 전이점 성장 속도 ÷ 전이점에서 멀리 떨어진 곳의 성장 속도`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “The peak-to-valley ratio quantifies the modeled factor of improvement between the PWSCC CGR at the Ni/NiO transition and PWSCC CGR asymptotically far from the Ni/NiO transition.” (p.81, §3.3.2).
- 문제: 분모의 `asymptotically`를 빼면 유한한 임의의 먼 위치에서의 CGR 비도 P라고 읽힌다. 원문의 분모는 점근 CGR이다.
- 최소 교체안: `peak-to-valley 비: Ni/NiO 전이에서의 PWSCC CGR과 전이에서 점근적으로 멀리 떨어진 곳의 PWSCC CGR 사이의 모델상 개선계수`

### [슬라이드 6] ADDED-CLAIM — CONFIRMED
- 대상 문구(HTML 그대로): `식 2-3과 함께 82/182/132의 수소 효과를 켤 때만 씁니다.`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “If the PWSCC degradation mechanism is active, the following functional form is used to calculate PWSCC CGR for all materials besides the custom material (Material Group 10)” (p.72, §3.2.1.3, 식 3-1에 같은 수소 인자 포함). “the peak-to-valley ratio should be set to unity to omit the hydrogen effect on the model prediction.” (p.81, §3.3.2).
- 문제: `때만`이라는 배타적 사용 조건을 추가했다. 원문의 공통 구현식은 해당 인자를 포함하고, 수소 효과를 생략할 때에도 P=1을 지정한다. 수소 효과를 켜는 경우만으로 구현식의 사용을 제한하지 않는다.
- 최소 교체안: `Alloy 82/182/132 수소 효과 모델의 수소 계수입니다. 수소 효과를 생략하려면 P를 1로 설정합니다.`

### [슬라이드 7] ADDED-CLAIM — CONFIRMED
- 대상 문구(HTML 그대로): `식 2-4를 쓸 때마다 같이 씁니다.`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “All the modeling presented in MRP-263 used [Eqn. 2-5] and [Eqn. 2-6]”; “Though different forms of these relationships exist in literature” (p.34, §2.2.3.2).
- 문제: 원문의 `MRP-263에 제시된 모든 모델링`이라는 범위를 지우고 식 2-4를 쓰는 모든 경우에 대한 무조건적 사용 규칙으로 바꿨다. 원문은 다른 관계식 형태가 문헌에 있음을 명시한다.
- 최소 교체안: `MRP-263의 모든 모델링에서는 식 2-5와 2-6을 각각 ECP 차이와 Ni/NiO 전이 수소 농도 계산에 사용했습니다.`

### [슬라이드 8] OMISSION-OF-HEDGE — CONFIRMED
- 대상 문구(HTML 그대로): `원문은 Ni/NiO 전이에 해당하는 수소 농도가 온도에 의존하며 이 적합식으로 계산한다고 설명합니다(p.34).`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “The concentration of dissolved hydrogen corresponding to the potential Ni/NiO transition is temperature dependent, and may be calculated using the following fit presented in Reference [12]:” (p.34, §2.2.3.1).
- 문제: `may be calculated`가 `계산한다고`로 바뀌어 가능 표현이 빠졌다.
- 최소 교체안: `원문은 Ni/NiO 전이에 해당하는 용존수소 농도가 온도에 의존하며, 참고문헌 [12]의 다음 적합식으로 계산할 수 있다고 설명합니다(p.34).`

### [슬라이드 9] OMISSION-OF-HEDGE — CONFIRMED
- 대상 문구(HTML 그대로): `오스테나이트 스테인리스와 페라이트강은 정상 PWR 환경에서 SCC에 민감하지 않다고 보아 이 보고서는 모델을 만들지 않았습니다.`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “These materials are ordinarily considered not to be susceptible to SCC under normal PWR conditions (especially relative to Alloys 600/82/182/132).” (p.38, §2.2.4.2).
- 문제: `ordinarily` 및 특히 Alloy 600/82/182/132 대비라는 상대적 한정이 빠졌다. 통상적인 평가를 조건 없는 비감수성 판단처럼 옮겼다.
- 최소 교체안: `이 재료들은 정상 PWR 조건에서, 특히 Alloy 600/82/182/132와 비교하여 통상 SCC에 민감하지 않은 것으로 간주됩니다. xLPR 2.0을 지원하기 위한 SCC CGR 모델은 개발하지 않았습니다.`

### [슬라이드 9] ADDED-CLAIM — CONFIRMED
- 대상 문구(HTML 그대로): `모델이 정해지지 않은 재료에서 PWSCC 비슷한 SCC를 계산해야 할 때 쓰며, 값은 사용자가 입력합니다.`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “a general material model of the form shown in [Eqn. 2-8] is included in xLPR and could be used to implement SCC CGR models for these materials” (p.38, §2.2.4.2). “This equation is modeled after the CGR equations developed in MRP-55 and MRP-115.” (동일 쪽·절).
- 문제: 원문은 앞서 명시한 재료의 SCC CGR 모델 구현 가능성을 말한다. `모델이 정해지지 않은 재료`라는 일반적 적용 조건과 `PWSCC 비슷한 SCC`라는 현상 분류는 원문에 없다. `could be used`도 `쓰며`로 강화됐다. 입력을 사용자가 지정한다는 부분 자체는 §3.3.2에 근거가 있다.
- 최소 교체안: `오스테나이트 스테인리스와 페라이트강의 SCC CGR 모델을 구현하는 데 사용할 수 있는 일반 재료 모델입니다.`

### [슬라이드 12] OMISSION-OF-HEDGE — CONFIRMED
- 대상 문구(HTML 그대로): `Ni계, 오스테나이트, 페라이트 모두 이 한 식을 씁니다(Ni계는 데이터가 적어 같은 식을 선택).`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “Therefore, it was selected that the same ΔKth model be used for all three material classes unless additional data that refute this approach are produced or identified.” (p.42, §2.3.1; ΔKth는 추출 텍스트의 흩어진 첨자를 한 기호로 연결).
- 문제: `unless ...`라는 채택 조건이 빠졌다. 원문은 이 접근을 반박하는 추가 데이터가 생성되거나 확인되지 않는다는 조건으로 공통 모델을 선택했다.
- 최소 교체안: `이 접근을 반박하는 추가 데이터가 생성되거나 확인되지 않는 한 세 재료군에 같은 ΔK_th 모델을 사용하도록 선택했습니다.`

### [슬라이드 12] ADDED-CLAIM — CONFIRMED
- 대상 문구(HTML 그대로): `낮은 R에서 약 30%, 높은 R에서 2배 낮게 예측`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “biased low by 30% at low load ratios and by a factor of two at high load ratios, relative to the data in Figure 2-10.” (p.40, §2.3.1).
- 문제: 원문이 수치 30%에 붙이지 않은 `약`을 추가했다. 과학적 타당성 판단이 아니라 사용자가 지정한 원문 한정어 유지 규칙에 따른 지적이다.
- 최소 교체안: `그림 2-10 데이터에 비해 낮은 하중비에서 30%, 높은 하중비에서 2배 낮게 예측`

### [슬라이드 13] OTHER — CONFIRMED
- 대상 문구(HTML 그대로): `[EQUATION TeX] \Delta K_{th}=7.0\cdot(1-0.693R)\quad(R\ge0.10,\ 28\ \text{points})`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “A least squares linear fit to the data of Figure 2-10 for R≥0.10 (28 data points) provided the following best-fit equation (in units MPa√m):” (p.40, §2.3.1). 이미지 p041의 식 2-12에는 `ΔK_th=7.0·(1−0.693R)`만 있다.
- 문제: 수식 자체는 일치하고 괄호 안 정보도 원문에 있다. 다만 원문의 식에 없는 데이터 집합 설명을 번호식과 같은 TeX 줄에 덧붙였다. 식의 적용 범위 조건과 적합 데이터 범위를 혼동할 수 있으므로 편집 추가임을 구분해야 한다. 수식 오류(EQUATION)로 세지 않는다.
- 최소 교체안: TeX는 `\Delta K_{th}=7.0\cdot(1-0.693R)`로 두고, 별도 문장에 `그림 2-10의 R≥0.10인 28개 데이터에 대한 최소제곱 직선 적합식입니다.`를 둔다.

## 발견 사항 — 원문에 없는 제목·라벨

아래 COINED-TITLE은 기술 내용의 오류를 뜻하지 않는다. 사용자가 원문에 없는 소제목·라벨도 별도 표시하도록 요구했으므로, 편집자가 재구성한 질문형 라벨 등을 슬라이드별 한 건으로 묶었다. 원문의 영어 제목을 한국어로 옮긴 것만으로는 지적하지 않았다. 반복되는 네 라벨은 `기호와 하첨자`, `왜 이 식을 쓰나`, `어떤 조건에 쓰나`, `적용 방법`이다. 제목 부재 판단의 범위는 위 표에서 읽은 관련 절·쪽이며 보고서 전체의 모든 단어 검색으로 부재를 증명했다는 뜻은 아니다.

### [슬라이드 1] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `목적과 담당 범위: 무엇을 하려고 만든 보고서인가`; `한 줄 요약`; `모델을 고른 기준`; `모듈 개발`; 표 머리글 `| 번호 | 업무 | 결과`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “1.1 Crack Growth Subgroup Objectives”; “Specific responsibilities ... are stated below and are discussed as they relate to the final work products presented in this report” (p.17, §1.1).
- 문제: 원문은 §1.1 본문과 (1)–(8) 목록이다. 질문형 제목·한 줄 요약·독립 소제목·업무/결과 표의 열 이름은 HTML 편집 구조다.
- 최소 교체안: `1.1 균열 성장 소그룹의 목적`을 사용하고 나머지 자체 라벨·열 머리글은 삭제하여 원문의 목록 구조로 제시한다.

### [슬라이드 2] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `모델 개요, 범위, 보고서 구성`; `PWSCC 성장 모델`; `피로 성장 모델`; `합체 모델`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “1.2 Models and Inputs”; “1.3 Scope”; “1.4 Report Organization” (pp.18–19, §1.2–1.4).
- 문제: 전체 제목은 세 절을 합쳐 새로 만든 것이고, 세 모델의 독립 소제목은 §1.2의 문단을 HTML에서 나눠 붙인 라벨이다. 모델 명칭 자체는 원문에 존재한다.
- 최소 교체안: 원문 절 제목 `모델과 입력`, `범위`, `보고서 구성`을 각각 사용하고 §1.2의 자체 소제목은 삭제한다.

### [슬라이드 3] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `기호와 하첨자`; `하첨자 읽는 법`; `왜 이 식을 쓰나`; `어떤 조건에 쓰나`; `적용 방법`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “2.2.1.1 Mathematical Description”; “where:” (p.21); “2.2.1.2 Model Development” (p.22); “2.2.1.3 Treatment of Uncertainty” (p.23); “2.2.1.4 Model Validation” (p.24).
- 문제: 원문은 위 구분으로 설명한다. 질문형·사용법·첨자 읽기 라벨은 원문 소제목이 아니다.
- 최소 교체안: `수학적 설명`, `모델 개발`, `불확실성 처리`, `모델 검증` 중 해당 원문 구분을 사용하고 첨자 읽기 라벨은 삭제한다.

### [슬라이드 4] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `기호와 하첨자`; `하첨자 읽는 법`; `왜 이 식을 쓰나`; `어떤 조건에 쓰나`; `적용 방법`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “2.2.2.1 Mathematical Description”; “2.2.2.2 Model Development” (p.27); “2.2.2.3 Treatment of Uncertainty” (p.28); “2.2.2.4 Model Validation” (p.30).
- 문제: 원문 절에 없는 자체 설명 라벨이다.
- 최소 교체안: 해당 원문의 `수학적 설명`, `모델 개발`, `불확실성 처리`, `모델 검증` 구분으로 대체하고 첨자 읽기 라벨은 삭제한다.

### [슬라이드 5] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `기호와 하첨자`; `하첨자 읽는 법`; `왜 이 식을 쓰나`; `어떤 조건에 쓰나`; `적용 방법`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “2.2.3.1 Mathematical Description” (p.33); “2.2.3.2 Model Development” (p.34); “2.2.3.4 Model Validation” (p.37).
- 문제: 여러 원문 절에서 가져온 설명을 원문에 없는 질문형·사용법·첨자 라벨로 재분류했다.
- 최소 교체안: 해당 원문 절 제목으로 바꾸고 첨자 읽기 라벨은 삭제한다.

### [슬라이드 6] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `식 2-4 · 수소 계수(hydrogen factor) f_{H2} (가우스형 피크)`; `기호와 하첨자`; `하첨자 읽는 법`; `왜 이 식을 쓰나`; `어떤 조건에 쓰나`; `적용 방법`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “fH2 = hydrogen factor”, “c = peak width parameter” (p.33, §2.2.3.1; 흩어진 첨자를 연결); “The term has a Gaussian dependence relative to ECP” (p.34, §2.2.3.1); “2.2.3.3 Treatment of Uncertainty” (p.35).
- 문제: 가우스 의존성이라는 내용은 원문에 있지만 `가우스형 피크`는 식 제목으로 붙인 자체 라벨이다. 나머지 질문형·사용법·첨자 라벨도 원문 제목이 아니다.
- 최소 교체안: 식 제목은 `식 2-4 · 수소 계수`로 두고, 자체 라벨은 삭제하거나 해당 원문의 `수학적 설명`, `모델 개발`, `불확실성 처리`, `모델 검증` 제목을 사용한다.

### [슬라이드 7] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `기호와 하첨자`; `하첨자 읽는 법`; `왜 이 식을 쓰나`; `어떤 조건에 쓰나`; `적용 방법`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “2.2.3.1 Mathematical Description”; “The difference in ECP ... is calculated as follows” (p.33); “3.2.1.3 CGR Calculation” (p.72).
- 문제: 원문 식·정의·구현 설명을 자체 소제목으로 재구성했다.
- 최소 교체안: 자체 라벨을 삭제하고 필요한 구분은 `수학적 설명`, `CGR 계산`으로 둔다.

### [슬라이드 8] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `기호와 하첨자`; `하첨자 읽는 법`; `왜 이 식을 쓰나`; `어떤 조건에 쓰나`; `적용 방법`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “may be calculated using the following fit” (p.34, §2.2.3.1); “3.2.1.3 CGR Calculation” (p.72); “Peak-to-valley ratio:” (p.81, §3.3.2).
- 문제: 원문에 없는 질문형·사용법·첨자 설명 소제목이다.
- 최소 교체안: 자체 라벨을 삭제하고 `수학적 설명`, `CGR 계산`, `PWSCC CGR 모델 매개변수` 등 실제 원문 제목을 사용한다.

### [슬라이드 9] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `기호와 하첨자`; `하첨자 읽는 법`; `왜 이 식을 쓰나`; `어떤 조건에 쓰나`; `적용 방법`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “2.2.4.2 Other SCC-Resistant Materials” (p.38); “3.2.1.3 CGR Calculation” (p.72).
- 문제: 실제 원문 절을 질문형·사용법·첨자 라벨로 바꿨다.
- 최소 교체안: `기타 SCC 저항성 재료`, `CGR 계산` 등 원문 제목을 사용하고 자체 라벨은 삭제한다.

### [슬라이드 10] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `기호와 하첨자`; `하첨자 읽는 법`; `왜 이 식을 쓰나`; `어떤 조건에 쓰나`; `적용 방법`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “2.3.1 General Considerations”; “Stress intensity factor range:” (p.39, §2.3.1).
- 문제: 원문에는 응력확대계수 범위라는 본문 라벨이 있고 질문형·사용법·첨자 소제목은 없다.
- 최소 교체안: `일반 고려사항 — 응력확대계수 범위`로 두고 자체 소제목은 삭제한다.

### [슬라이드 11] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `기호와 하첨자`; `하첨자 읽는 법`; `왜 이 식을 쓰나`; `어떤 조건에 쓰나`; `적용 방법`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “2.3.1 General Considerations”; “Load ratio:” (p.39, §2.3.1).
- 문제: 원문의 하중비 설명에 없는 편집 소제목이다.
- 최소 교체안: `일반 고려사항 — 하중비`를 사용하고 자체 소제목은 삭제한다.

### [슬라이드 12] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `식 2-11 · 응력확대계수 범위 문턱값 ΔK_{th} (N-643-2 형태)`; `기호와 하첨자`; `하첨자 읽는 법`; `왜 이 식을 쓰나`; `어떤 조건에 쓰나`; `적용 방법`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “Stress intensity factor range threshold:” (p.39, §2.3.1); “This model form is based on ASME Code Case N-643-2” (p.40, 같은 절).
- 문제: N-643-2에 기초한 내용은 맞지만 `(N-643-2 형태)`를 제목으로 붙인 것은 편집 라벨이다. 나머지 소제목도 원문에 없다.
- 최소 교체안: `응력확대계수 범위 문턱값`을 제목으로 사용하고 N-643-2 근거는 본문에 둔다. 자체 소제목은 삭제한다.

### [슬라이드 13] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `식 2-12 · ΔK_{th} 실측 최소제곱 식`; `기호와 하첨자`; `하첨자 읽는 법`; `왜 이 식을 쓰나`; `어떤 조건에 쓰나`; `적용 방법`; `주의`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “A least squares linear fit ... provided the following best-fit equation” (p.40, §2.3.1); “Threshold stress intensity factor range scaling factor:” (p.83, §3.3.3); “Table 3-5. Recommended Values and Distributions for Fatigue CGR Subroutine Inputs” (p.86).
- 문제: 원문 식 2-12에 독립적인 `실측 최소제곱 식` 제목은 없다. 최소제곱 직선 적합이라는 내용 자체는 맞는다. `주의` 및 반복 질문형 라벨은 원문 서술들을 재배치해 만든 구조다.
- 최소 교체안: `식 2-12`와 원문 본문 설명을 사용하고 자체 제목·라벨은 삭제한다. p.83·86의 서로 다른 값은 각 출처를 붙인 문장으로 유지한다.

### [슬라이드 14] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `기호와 하첨자`; `하첨자 읽는 법`; `왜 이 식을 쓰나`; `어떤 조건에 쓰나`; `적용 방법`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “2.3.2.1 Mathematical Description” (p.42); “2.3.2.2 Model Development” (p.43); “Fatigue in PWR environment:” (p.44).
- 문제: 원문에는 위 구분이 있고 HTML의 질문형·사용법·첨자 소제목은 없다.
- 최소 교체안: `수학적 설명`, `모델 개발`, `PWR 환경에서의 피로` 등 실제 원문 구분을 사용한다.

### [슬라이드 15] COINED-TITLE — CONFIRMED
- 대상 문구(HTML 그대로): `식 2-14 · 공기 중 da/dN (Paris형)`; `기호와 하첨자`; `하첨자 읽는 법`; `왜 이 식을 쓰나`; `어떤 조건에 쓰나`; `적용 방법`
- 원문 근거(영어 그대로 인용 + 인쇄 쪽 + 절): “2.3.2.1 Mathematical Description” (p.42); “This model includes conventional fatigue dependencies on stress intensity factor range (i.e., Paris power-law) and load ratio.”; “Fatigue in air:” (p.43, §2.3.2.2).
- 문제: Paris 거듭제곱 의존성은 원문 내용이지만 `(Paris형)`은 식 제목에 새로 붙인 라벨이다. 질문형·사용법·첨자 라벨도 원문 소제목이 아니다.
- 최소 교체안: `식 2-14` 또는 원문의 `공기 중 피로`를 사용하고 자체 라벨은 삭제한다.

## 지적하지 않은 사항 및 확인 한계

- 슬라이드 10·11·14·15: 본문·수치·표·식·인용에서 추가 지적 없음. 확인 항목 수는 각각 13, 13, 15, 15이다. 위 COINED-TITLE 지적은 별도로 남긴다. 다른 슬라이드도 위에 적지 않은 확인 항목에서는 불일치를 발견하지 못했다.
- 슬라이드 6의 `ΔECP=c`에서 약 40% 감소한다는 설명은 자체 계산이 아니다. 원문 p.81 §3.3.2에 그대로 있는 설명이다. `P=1`로 수소 효과를 생략하는 것도 같은 쪽에 명시되어 있다.
- 슬라이드 7·8의 Kelvin/Celsius 구분은 식 3-1(p.72, §3.2.1.3)에서 확인했다. 식 2-6 자체에는 온도 단위가 쓰여 있지 않은 점도 이미지에서 확인했다.
- 슬라이드 12의 온도 플래그 1/2/3은 p.87 §3.3.4와 일치한다. `per heat`가 재료 그룹별·독립 시뮬레이션별이라는 것은 p.76에 명시되어 있다. p.40의 부품 시뮬레이션별 권고와 p.76–77의 모듈 입력 표를 HTML이 구분해 제시한 것은 오류로 판정하지 않았다.
- 슬라이드 13의 p.83 중앙값 1, p.86 표의 log-μ=0.239, p.42 중앙값 1.27 및 대안 1.0은 각각 실제 원문에 있다. 이 차이를 임의로 통합하거나 HTML이 잘못 옮긴 것으로 판정하지 않았다. 3σ 상한의 중앙값 배수 1.517도 p.40 각주 12에 직접 있다.
- 슬라이드 14·15의 재료 코드 1–5는 p.71 표 3-1 및 p.72 §3.2.1.3과 일치한다. 상승 시간의 1000 psi/hr 기준은 p.78 §3.3.1에 있다. 환경 지수 0.25–0.33은 p.86 표 3-5의 균등분포 최소·최대와 일치한다. Alloy 690의 약 60개 공기 중 시험과 온도 효과 재추정은 p.44에 있다.
- `열처리`와 `heat processing`의 혼동 가능성은 위 PLAUSIBLE 한 건으로만 기록했다. 원문으로 의미가 확정되지 않는 번역 오류를 확정 사실로 쓰지 않았다.

## 유형별 개수

각 `### [슬라이드 N] 유형 — 확신도` 블록을 1건으로 센다. 같은 슬라이드의 반복 편집 라벨은 한 COINED-TITLE 블록으로 묶었으므로 개별 라벨 개수와 다르다.

| 유형 | CONFIRMED | PLAUSIBLE | 합계 |
|---|---:|---:|---:|
| WRONG | 1 | 0 | 1 |
| OMISSION-OF-HEDGE | 9 | 0 | 9 |
| ADDED-CLAIM | 5 | 0 | 5 |
| COINED-TITLE | 15 | 0 | 15 |
| CITATION | 0 | 0 | 0 |
| EQUATION | 0 | 0 | 0 |
| OTHER | 1 | 1 | 2 |
| 합계 | 31 | 1 | 32 |

작업 시작 시 `git pull`을 시도했으나 `cannot open '.git/FETCH_HEAD': Permission denied`로 실패했다. 이 실행 환경의 .git 쓰기 제한으로 동기화되지 않은 로컬 자료를 대조했다. 결과 파일 작성 후 `git add -- round35/codex_A.md`도 `.git/index.lock: Permission denied`로 실패했다. 따라서 커밋·push는 수행할 수 없었으며 결과는 로컬 파일로 남겼다.

ROUND35A DONE
