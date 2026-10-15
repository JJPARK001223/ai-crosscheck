# Claude 단독 감사 (blind, round35) — 게시본 v23 vs 원문
(S=슬라이드. 쪽수는 인쇄쪽. 유형: W=오류, H=hedge/한정 누락, A=원문에 없는 주장·해석, T=원문에 없는 제목·라벨, C=인용쪽, E=식)

## 표지/목차
- T: 표지 “XLPR 균열 성장·합체 발표자료 정리”, ch 부제 “§1 · 목적, 모델 개요, 범위 (한국어 요약)” 등 — 원문 제목 아님. “합체”는 원문에 없는 한국어(내가 정한 번역).
## S1 (p.17–18, §1.1)
- T: “목적과 담당 범위: 무엇을 하려고 만든 보고서인가”(원문 1.1 Crack Growth Subgroup Objectives), “한 줄 요약”, “모델을 고른 기준”, “모듈 개발” 라벨.
- A: “한 줄 요약” 문장 전체가 원문에 없는 요약(“…과정을 정리한 보고서입니다”).
- H: (1) 원문 “deemed largely acceptable through careful assessment” → “careful assessment” 누락. (4) “three material-specific fatigue CGR models applicable to PWR environments” → “PWR 환경에 적용” 누락. (7) “Extensive V&V” → “Extensive” 누락. 기준 목록: 원문 “Among the criteria for selection were”(그중 일부) → “원문은 다섯 가지를 듭니다”는 가능하나 “Among” 누락.
- A: (3) “피로 CGR 계산의 구조를 다른 소그룹과 함께 만듦” — 원문은 K-Calculation Models Subgroup, Inputs Group, Framework Group와 협력해 “a structure to enable the treatment of fatigue growth(하중 천이 정의·천이→K 변환·피로 CGR 계산 포함)”를 개발. 구조의 내용 범위가 달라 보임. “다른 소그룹”은 Group 포함.
## S2 (p.18–19, §1.2–1.4)
- T: 제목 “모델 개요, 범위, 보고서 구성”(원문: 1.2 Models and Inputs / 1.3 Scope / 1.4 Report Organization).
- H: PWSCC: “다른 재료(Alloy 52·152, 오스테나이트 SS…, 페라이트강)” — 원문은 “such as”(예시) + “in normal PWR environments” 누락; “includes appropriate uncertainties”의 appropriate 누락.
- H/A: 합체 모델: 원문 “mechanisms …, including crack tip interaction that can lead to intensified SIF and plastic collapse of a ligament” → HTML “즉 … 응력확대계수가 커지는 것과 … 소성 붕괴”: “including”(예시) → “즉”(전부), “can lead to” → 단정.
- H: 범위: “materials commonly located in PWR primary piping systems” → “commonly located” 누락.
## 공통 패턴 (S3~S33 식 슬라이드 전부)
- T: 소제목 “왜 이 식을 쓰나 / 어떤 조건에 쓰나 / 적용 방법”, “기호와 하첨자”, “하첨자 읽는 법” 열은 원문에 없는 라벨(식 슬라이드마다). “주의”(S13) 등.
- A: 각 슬라이드 “어떤 조건에 쓰나/적용 방법” 중 원문 문장이 아닌 사용 안내(예: “식 2-4를 쓸 때마다 같이 씁니다”, “수소 효과를 넣으려면 식 2-3을 씁니다”).
## S3 식 2-1 (p.21)  TeX 일치
- H: “검증되지 않았으므로” ← 원문 “not specifically verified”(specifically 누락). 수소: Alloy 600 수소 모델 미제시 이유 3가지 중 하나만(“작고 우선순위가 낮다”), 나머지 둘(설치 safe end 적음, 신규 플랜트 미사용) 누락.
- A: 아연 “균열 발생 모델에만 반영” — 원문은 “included in the initiation model”(only 없음). “K_th 이하 성장 0, 넘으면 (K−K_th)^β에 비례” 식 해설. “시뮬레이션에서 대수정규분포로 뽑아” 중 “시뮬레이션에서 뽑아”는 원문 표현 아님. α “전체 크기를 맞추는 상수”(원문: scaling constant). 
## S4 식 2-2 (p.27)  TeX 일치
- A: “시편 계수 대신 용접 계수 4개를 곱합니다” — 원문에 없는 해설. “수소 효과를 넣으려면 식 2-3을 씁니다”. 
- H: fn7 “unusual case” 누락. “linearized multiple regression” → “다중회귀”(linearized 누락).
- 확인 필요: “권장값 표 3-4 p.82” (아래 3장 대조에서 확인)
## S5 식 2-3 (p.33)  TeX 일치
- W/H: “실제 활성화 에너지 104 kJ/mol을 사용합니다” ← 원문 p.35 “recommended activation energy (104 kJ/mol) is close to the average actual activation energy”(104가 ‘실제 활성화 에너지’라는 서술 아님). “Alloy 82는 피크 위치가 어긋나 추가 시험이 필요” ← 원문 “Very limited data … apparent discrepancy”(very limited, apparent 누락).
## S6 식 2-4 (p.33)  TeX 일치
- A: P 정의 “전이점 성장 속도 ÷ 전이점에서 멀리 떨어진 곳의 성장 속도” — 원문은 “peak-to-valley ratio”만. c “ΔECP = c일 때 … 약 40% 줄어듦” — 자체 계산(원문에서 확인 안 됨).
- A: “P−1은 대수정규분포” — 원문은 “shifted log-normally distributed peak-to-valley ratio”. “변동 계수” ← “CGR variability terms”.
## S7 식 2-5 (p.33) TeX 일치
- A(원문은~않았다 식 해설): “원문은 log의 밑을 적지 않았는데…”. “T는 절대온도입니다”(식 2-5 where절에 T 정의 없음). “수소 농도 비의 로그에 비례하는 형태”.
## S8 식 2-6 (p.34) TeX 일치
- A: “원문 식 2-6에는 단위가 적혀 있지 않고…”. H: “may be calculated” → “계산한다고”(may 누락).
## S9 식 2-8 (p.38) TeX 일치
- A: f_comp “부품(재료 그룹)마다”, f_flaw “결함 위치마다” — 원문은 “component-to-component / within-component variation”뿐. “사용자가 필요하면 값을 넣어 쓸 수 있도록”, “PWSCC 비슷한 SCC”. H: “ordinarily”.
## S10~11 식 2-9, 2-10 (p.39) TeX 일치
- C/A: S10 “ASME … 규정을 따랐습니다”(원문 guidance), “경수로 환경 피로 균열 성장” (원문은 “LWR environments”만). S11 “음수 R을 쓰지 않습니다” 추가. 
## S12 식 2-11 (p.40) TeX 일치
- W: “N-643-2의 문턱 곡선”(원문: N-643-2는 ferritic steels PWR 환경의 fatigue CGR curve), “약 30%”(원문 30%).
## S13 식 2-12 (p.40) TeX 일치 / S14~16 TeX 일치
- A: S14 단위 “m/cycle” 원문 미기재. S15 “원문은 F_T를 temperature effect라고만 정의하고 단위는 적지 않았습니다”(해설).
- 확인 필요: p.87 플래그(평균1/최소2/최대3), p.76–77 per heat, p.83, p.86 Table 3-5 log-μ 0.239, §3.3.1 1000 psi/hr (3장 대조에서)
## S17 식 2-16 (p.43) TeX 일치
- H: 원문 “Best fits to individual data sets for air fatigue of Alloy 600 in constant temperature environment yielded 0.82 and 2.2” → HTML “원문은 b = 0.82, p = 2.2를 제시”(대상 데이터·조건 누락). A: “b = 0.82, p = 2.2를 넣어 F_R을 계산”(원문은 best fit 결과 서술). 따옴표 “선례에 따라, 공기 중 데이터와 잘 맞도록”은 번역문인데 인용부호 사용.
## S18~19 식 2-17/2-18 TeX 일치. S18 “표 3-3 … T_min/T_max 단위 °C (p.77)” 확인 필요.
## S20 식 2-19 (p.48) TeX 일치; 값/범위 일치(2.25, 635점, 0.5/2.0, DO 2 ppb·5–500 ppb, 371°C, 1–30000 s, R 0.1–0.95). 
- A: “공기와 환경을 따로 나누지 않고 모두 한 식에 합쳤습니다”. (원문 p.49의 원래 alloy factor 값 1.39E-8/9.10E-9/7.28E-9은 슬라이드에 없음 — 식 6-1 값만 제시 → 누락)
## S21 식 2-20 (p.49) TeX 일치. A: “반드시 K로”(원문: “where temperature, T, is in units Kelvin”).
## S22 식 2-21 TeX 일치. H/A: 원문 “nominal carbon contents (up to 0.08%)” vs “탄소 함량이 높은”; “(0.748은 식 안의 상수)” 해설.
## S23 식 2-22 TeX는 원문 표기와 동일하나 원문 표기 자체가 F_τ=τ_r^0.3 / τ_r,limit 로 모호 → 이미지 확인 필요. A: “원문은 F_τ … 따로 적었습니다”(해설).
## S24 식 2-23 (p.52) TeX·표 2-1 수치 일치(7.87E-11, 2.76E-10, 1.17E-9, 1.42E-7, 3.07/0.948, 1/2.166).
- H: 온도 효과 “despite experimental evidence to the contrary” 누락. 개발 범위 “황 약 0.004~0.02%” ← 원문 “from very low (e.g., 0.004 %wt) to 0.02 %wt”, “상승시간 주로 30 s” ← “a diversity of loading rise times (although predominantly at 30 s)”. fn15 “for some combinations of loading, metallurgical, and environmental conditions” 누락. fn16 “may be unreliable” → “불확실합니다”(hedge·출처 [35] 누락). ④ 조건: 원문은 “It is hypothesized …”, “little to no EAC … for relatively low material sulfur” → HTML “EAC가 유지되지 않음”(단정).
- T: “TCF로 가는 조건 / EAC로 가는 조건”. A: “아래 이어지는 식 2-24~2-27 페이지에서 … 설명합니다”.
- 확인 필요: C_1/C_2/C_3 정의(p.77), p.73 영구 메모리 문장, 표 2-1 행 라벨에 “(0.004~0.013%)”, “(>0.013%)”, “ΔK_b~ΔK_c” 추가(원문 표에는 없음 → 표 2-1 라벨 변경).
## S25 식 2-24 (p.54) TeX 일치. A: a=“균열 깊이”(원문 2-24는 a 정의 없음). 확인: p.77 a 단위 m, 그림 2-18 내용(V_i=αΔa_i/Δt_i, α=1.5, V_in)은 이미지로 확인 필요.
## S26 식 2-25 (p.55): 원문 이미지(pages/eq225.png)로 TeX 확인 → 일치 [ΔK_c=(C_upper/C_1)^2.122 θ^0.326 (2.88−R)]. 문제 없음(해설 A: “(ΔK가 크면)”).
## S27 식 2-26 (p.56) TeX 일치. 확인 필요: p.73(ΔK_b<ΔK_th 300급 오류), p.87(오류 203).
## S28 식 2-27 (p.56) TeX 일치. “C_EAC … (C_3)” p.77 확인 필요. “사실상 선형 천이”에 인용부호(번역문).
## S29 §2.4 (p.61–63): T: “시간 적분 규칙 (원문에 번호식 없음)”(원문 2.4.1 Time Integration / 2.4.2 Crack Shape and Size / 2.4.2.1 Special Considerations), “특수 규칙”. 
- H: fn23 “Growth asymmetry … updated crack assumed to remain symmetric, center shifted” 맥락 누락 → 일반 규칙처럼 서술. “other probabilistic crack simulations for PWR components”→“다른 PWR 확률 계산”. 
- 확인 필요: Δt EFPY·N_TS 1~20·플래그 I_mechanism (p.76–77).
### 정정 (S6): “ΔECP=c에서 약 40% 줄어듦”은 원문 p.81에 있음(“reduced by approximately 40% relative to the difference between the maximum CGR … and the asymptotic CGR”) → 문제 없음. “P−1 대수정규”는 Table 3-4 Note 2(p.82)에 있음 → 문제 없음. p.76/p.82/0.714 인용 확인됨. (P 정의 “전이점 ÷ 멀리 떨어진 곳”은 원문 “factor of improvement between … CGR at the Ni/NiO transition and … asymptotically far” 와 표현 상이 — 경미)
## S30 (p.68–73) 3장 개요
- T: 제목 “CGR 모듈은 식을 어떻게 불러 쓰나”, 소제목 “적용 목적 / 한 번 호출될 때 하는 일 / 재료 코드 / 후처리 / 모듈이 하지 않는 일 / 표를 읽을 때 주의 / 관련 근거”.
- A(표 구성): “표 3-1 재료 코드와 쓰이는 식 (원문 표 3-1 …)” — 원문 Table 3-1은 Material Group·Numeric Code 두 열뿐. “PWSCC/피로” 열과 식 연결(식 3-1, 2-13/2-14, 2-19, 2-23, ‘f=2.0’, ‘P=1’ 등)은 HTML이 §3.2.1.3·§2·표 3-4를 조합한 것. 
- A: “‘미개발’은 … 뜻입니다”(해석, 원문 인용 아님), “PWSCC 함수는 한 번”(원문은 fatigue function이 transient component마다 1회라고만).
- H: “병행 수정해야 함(p.79)” ← 원문 “should only be modified in parallel with careful assessment”(careful assessment 누락). “모듈이 하지 않는 일”: “bookkeeping operations” 맥락, “require the use of”→“맡습니다”.
- 확인됨: p.71 표 3-1, p.73 200번대 오류·영구 메모리, p.68 근거 문헌, p.82 표 3-4, p.70 “hardwired”.
## S31 식 3-1 (p.72) TeX 일치(ΔECP 포함).
- A: “원문은 … 재료마다 파라미터 값만 바꾼다고 설명합니다”(원문은 “flexible to accommodate all PWSCC CGR models presented in Section 2.2”뿐), “식 2-1, 2-2, 2-3을 한 식으로 합친 구현용 식입니다”.
- H/A: “주의”의 “한 열에서 일부만 바꾸지 않습니다” ← 원문 “should only be modified in parallel with careful assessment”(금지로 바뀜). 
## S32 식 3-2: TeX 일치. “사용자가 입력하는 상수”(원문: p.85 사용자 정의 모델 매개변수) 
## S33 식 3-3 (p.73): TeX 일치. A: “(식 속의 a는 균열 깊이가 아니라 상수)”, “거듭제곱으로 넣은 형태” 해설.
## 확인된 인용(문제 없음): S12 p.87 플래그(평균1/최소2/최대3), p.76–77 per heat, S13 p.83·p.86·p.42, S14 §3.3.1 1000 psi/hr·표3-5 0.25–0.33, S18 p.77 °C, S24 C1/C2/C3 p.77, S27 오류 203 p.87·300급 p.73, S29 플래그 1/2/3·EFPY·N_TS 1–20.
## 4장 (S34~39, p.92–101) — 수치·인용쪽 전부 일치. 지적:
- T: S34 “합체 모델이란”, “적용 목적/적용 범위/어떻게 적용하나”; S35 “합체 거리: 언제 합치나”, “적용 목적”; S36 “합친 뒤 균열 모양: 유형·깊이·중심·길이”, “적용 목적/적용 방법”, “최대 깊이를 권장하는 이유”; 장 부제 “합체 규칙: 합체 거리, 합친 뒤 모양, 가정”. “합체”는 원문 용어(coalescence) 아님.
- H: S34 “may simulate two distinct modes” → “두 가지 경우를 듭니다”(may 누락); 원문의 “higher order fracture mechanics calculations that are not amenable to the xLPR probabilistic framework or that were not made a priority” 이유 누락.
- A/W: S35 적용 목적 “균열 간섭과 ligament 붕괴는 K 계산·성장·안정성 예측에서 다루지 않고” — 원문은 표면균열(crack interaction)은 “K-calculation and growth predictions”, 관통균열(ligament collapse)은 “K-calculation, growth, or stability predictions”로 구분 → 두 현상 모두에 ‘안정성’ 적용. “균열 유형 쌍마다 근거가 달라서 세 가지로 나눕니다(p.94)”, “다음 두 페이지에서 설명합니다”(S34)는 HTML 자체 문장.
- H: S37 “이 불확실성은 … 반영합니다” ← 원문 “This uncertainty may reflect”(may 누락). “이 불확실성을 epistemic으로” ← “these uncertainties”. S38 “실험 증거가 있으며” ← “Experimental evidence suggests”(suggests 누락). S39 Coplanar: “큰 균열 하나가 생겨 … 증가합니다” ← “This would increase … would”(조건/가정법 누락).
- 경미: S36 “하려는 것입니다”(원문 “promotes continuity”), S35 “합침”(원문 imminent→replacement).
## 5~6장 (S40~49, p.103–121) — Claude 단독 감사 (Codex 결과를 보기 전에 작성)
- 쪽수·수치·식(6-1, 6-2)·오류코드·표 5-1 값 일치. 지적:
- T: S40 “적용 목적/어떻게 동작하나/입력/범위”, S41 “coalescence criteria/순서”(원문 문장 일부 용어), S42 “입력 매개변수와 플래그/적용 목적/적용 방법/단위와 허용 범위/coalescence distance를 정하는 규칙”, S44 “K 의존성/수소 의존성/기계적 성질, 냉간가공, 열처리/재료 경계면, 발생-성장 상관”(여러 bullet 합친 라벨), S45 “내용”, S48·49 일부 라벨(“축방향 균열과 미세균열” 합침).
- A: S43 소제목이 슬라이드 제목과 동일하게 중복 표시(“5.2.1.5 Updating Crack Attributes” 2회) — 내가 방금 만든 중복. S47 “구간별 값은 식 6-2에 적힌 대로입니다.”(원문에 없는 내용 없는 문장). 푸터 “슬라이드 목차의 영문 철자(MODULE, MODULE, RECOMMENDATIONS)는 그대로 두었습니다”(원문 Contents에는 오타 없음 — 의미 불명한 자체 문장), 서두 “Contents … 표기를 그대로 따랐습니다”(원문 Contents는 7. REFERENCES 포함, 슬라이드는 6장까지).
- W: S42 “구성 요소별로는 0~20 in의 균일분포 정도가 한 예입니다” ← 원문 “For components of interest, this distribution might be achieved roughly with a uniform distribution between zero and 20 inches”(components of interest=관심 대상 부품; “구성 요소별”로 의미 변경, “might” 누락).
- H: S44 “원문은 현재 모델의 보완이 필요한 영역을 나열합니다” ← 원문 “Refinements and extensions … are desired for several areas … For instance:”(desired, 예시). 냉간가공 bullet: 원문 “it may be appropriate to develop a cold work dependency or … different models for different ranges of cold work. However …” 중 앞 권고가 빠지고 “However” 이하만 남음. “프랑스 연구자들은 Alloy 182에 개선계수 2.0을 권장했습니다” ← 원문은 “when modeling PWSCC CGR for Alloy 182 exposed to post-weld heat treatment of adjacent carbon/low-alloy steel”(조건 누락). 
- H: S47 “후속 버전에서 쓰려는 안입니다” ← 원문 “This model could be improved in a later version…”(could→계획처럼 서술). fn14 “at the risk of incorporating excessive variability at high CGRs” 누락. 원문 “good agreement with data scatter … median of 4.4x10^-7 (m/cyc-s)^{1-0.33}” 누락.
- H: S48 6.2.4 “they should be used to bolster the fatigue CGR model validation” 누락. S49 “For instance:”(예시) → “을 듭니다”, 6.3.1 “More complex geometries constitute extensive development efforts” 누락; “(after ligament length)” 누락.
- 경미: S42 “동작이 완전히 정해지도록 만들었습니다”(원문 “parameterized to improve flexibility … inputs fully define the behavior”).
- 누락(오류 아님): 5.4, 5.5, 표 5-2 슬라이드 없음.
