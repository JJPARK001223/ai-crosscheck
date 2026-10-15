# DECISION — round35: 발표자료 49슬라이드 전체 원문 대조 (최종 판단: Claude)

대상: `XLPR_발표자료_수식정리.html` v23 (49슬라이드, 5~6장 수정 반영본). 원문: EPRI, K. Schmitt, *xLPR Models Subgroup Report—Crack Growth and Coalescence*, xLPR-MSGR-CGR Ver.1.0 (2016-06-29), NRC ADAMS ML16341B051. 쪽수는 인쇄 쪽.
방식: Claude 단독 감사(Codex 결과를 보기 전에 작성: `claude_audit_blind.md`)와 Codex 3구간(`codex_A/B/C.md`)을 따로 수행한 뒤, Codex만 찾은 항목은 Claude가 원문으로 다시 확인했고 Claude만 찾은 항목은 근거 구절을 다시 확인했다.
**HTML은 수정하지 않았다. 사용자 승인 전까지 바꾸지 않는다.**

## 1. 결론 요약 (개수는 아래 3장 표에서 센 값)

| 구분 | 확정 | 가능성(원문으로 완전 확정 못 함) | 합계 |
|---|---:|---:|---:|
| W: 내용이 원문과 달라진 것(의미 변경·표 결함) | 8 | 1 | 9 |
| H: 원문의 한정어·조건·hedge가 빠져 단정/범위 변경 | 38 | 2 | 40 |
| A: 원문에 없는 내 문장·해석·해설 | 17 | 4 | 21 |
| C: 인용 쪽/표시 문제 | 3 | 0 | 3 |
| **합계(제목·라벨 제외)** | **66** | **7** | **73** |

발견 경로: Codex와 Claude가 둘 다 찾은 것 22건, Codex만 찾은 것 14건, Claude만 찾은 것 37건(Codex만/Claude만 찾은 항목은 모두 상대가 원문으로 재확인). 한 항목이 여러 슬라이드나 여러 문장을 묶은 경우가 있어 “항목” 수이며 문장 수가 아니다.

- 식(TeX): 슬라이드의 모든 TeX를 원문과 대조했다(2-1~2-27, 3-1~3-3, 6-1, 6-2). Claude는 일부(2-20~2-22, 2-25, 6-1, 6-2)를 원문 이미지로, Codex는 이미지·텍스트로 확인했다. **불일치 0건.** 식 2-25의 지수 2.122와 2-22의 F_τ 표기는 원문 이미지 그대로다.
- 수치: 표 2-1, 3-1, 3-4, 3-5, 5-1 값과 본문 수치(범위·백분위·계수·시험 수·오류 코드)는 **불일치 0건**. 문제는 수치가 아니라 문장(한정어 누락, 내 해설 추가)에 있다.
- 제목·라벨 창작(T): 별도 분류. 식 슬라이드 전부에 “기호와 하첨자 / 하첨자 읽는 법 / 왜 이 식을 쓰나 / 어떤 조건에 쓰나 / 적용 방법”이 있고, 슬라이드 제목에도 원문에 없는 문구가 있다(아래 4장). Codex는 슬라이드별로 묶어 38건, Claude는 별도 목록으로 확인했다. 사용자가 “원래 구성대로, 용어만 교체”를 지시했으므로 **적용 여부를 사용자가 결정**한다.
- “합체”: 원문에 없는 내가 정한 번역어. 1~4장에 남아 있다(사용자가 “이대로”를 지시).

## 2. 확신도 기준
- 확정 = 원문 구절(영어)과 HTML 문장을 나란히 놓고 차이를 직접 확인.
- 가능성 = 원문에 비슷한 구절은 있으나 표현 차이가 해석에 달린 것.
- 출처: C=Codex가 지적, L=Claude가 지적, CL=둘 다 지적. “재확인”은 한쪽만 지적한 것을 다른 쪽이 원문으로 다시 확인했다는 뜻.

## 3. 항목표

| ID | 슬라이드 | 유형 | 확신 | 출처 | 내용 (HTML → 원문) |
|---|---|---|---|---|---|
| W1 | 5 | W | 확정 | CL | “Q_g는 실제 활성화 에너지 104 kJ/mol을 사용” → p.35 “The recommended activation energy input … (104 kJ/mol) is close to the average actual activation energy”; 표 3-4(p.82)는 평균 104, 표준편차 20의 분포 |
| W2 | 6 | W | 확정 | CL | P 정의 “전이점 성장 속도 ÷ 전이점에서 멀리 떨어진 곳의 성장 속도” → p.81 “between the PWSCC CGR at the Ni/NiO transition and PWSCC CGR **asymptotically** far from” (asymptotically 누락) |
| W3 | 19 | W | 확정 | C, 재확인 | “Alloy 690 계열은 약 60개 시험뿐” → p.44 “roughly 60 tests available for Alloy 690 fatigue CGR **in air**” (계열·in air) |
| W4 | 24 | W | 확정 | C, 재확인(HTML) | 표 2-1 머리글이 3칸(C_env, n_fer, n_R)인데 데이터 행은 4칸(레짐 포함) → 머리글이 한 칸씩 어긋남. 원문 표 2-1은 Growth Regime / Environmental Factor / Paris Power-Law Exponent / Load Ratio Exponent |
| W5 | 35 | W | 확정 | L | “균열 간섭과 ligament 붕괴는 K 계산·성장·안정성 예측에서 다루지 않고” → p.93~94: 표면균열 간섭은 “K-calculation and growth”, 관통균열 ligament collapse는 “K-calculation, growth, or stability” (두 현상에 안정성을 모두 적용) |
| W6 | 42 | W | 확정 | L | “구성 요소별로는 0~20 in의 균일분포 정도” → p.111 “For components of interest, this distribution **might** be achieved roughly with a uniform distribution between zero and 20 inches” (components of interest=관심 대상 부품; might) |
| W7 | 44 | W | 확정 | L | 냉간가공 항목에서 원문 “it may be appropriate to develop a cold work dependency or develop different models for different ranges of cold work. However, …”의 앞 권고가 빠지고 “However” 이하만 남음 (p.117) |
| W8 | 44 | W | 확정 | L | “프랑스 연구자들은 Alloy 182에 개선계수 2.0을 권장” → p.117 “…when modeling the PWSCC CGR for Alloy 182 **exposed to post-weld heat treatment of adjacent carbon/low-alloy steel material**” (조건 누락) |
| W9 | 12 | W | 가능성 | L | “N-643-2의 문턱 곡선 형태” → p.40 “This model form is based on ASME Code Case N-643-2, which presents a fatigue CGR curve for ferritic steels in PWR water environments” (문턱 곡선이라는 표현은 원문에 없음) |
| H1 | 1 | H | 확정 | CL | “원문은 다섯 가지를 듭니다” → p.17 “**Among** the criteria for selection were” |
| H2 | 1 | H | 확정 | C, 재확인 | 항목 (6): “provided that appropriate model parameter inputs are developed”, “appropriate and **validated** model parameter inputs … ongoing outside of the xLPR Project” (p.18) 조건·validated 누락 |
| H3 | 1 | H | 확정 | L | 항목 (1) “deemed largely acceptable through **careful assessment**”, (4) “three material-specific fatigue CGR models **applicable to PWR environments**”, (7) “**Extensive** V&V” 누락 (p.17~18) |
| H4 | 2 | H | 확정 | CL | “즉 … 응력확대계수가 커지는 것과 … 소성 붕괴” → p.19 “**including** crack tip interaction that **can lead to** intensified stress intensity factors and plastic collapse” |
| H5 | 2 | H | 확정 | L | PWSCC 문단: 원문 “**such as** Alloys 52 or 152, austenitic SS …”(예시)와 “… relative to Alloy 600 **in normal PWR environments**” 누락 (p.18) |
| H6 | 2 | H | 확정 | L | 범위: “materials **commonly located** in PWR primary piping systems” → “commonly located” 누락 (p.19) |
| H7 | 3 | H | 확정 | CL | “검증되지 않았으므로” → p.22 “was not **specifically** verified” |
| H8 | 3 | H | 가능성 | L | Alloy 600 수소 모델 미제시 이유: 원문은 세 가지(설치 safe end 적음, 신규 플랜트 미사용, 82/182/132보다 효과 작음)인데 하나만 적음 (p.23) |
| H9 | 4 | H | 확정 | L | “linearized multiple regression”의 linearized 누락(p.28), 각주 7 “in the **unusual** case” 누락 |
| H10 | 5 | H | 확정 | CL | Alloy 82: p.34 “**Very limited data** … a shift in the peak CGR from the **estimated** location … resolve this **apparent** discrepancy” 누락 |
| H11 | 8 | H | 확정 | CL | “계산한다고” → p.34 “**may be** calculated using the following fit” |
| H12 | 9 | H | 확정 | CL | “SCC에 민감하지 않다고 보아” → p.38 “**ordinarily** considered not to be susceptible … (**especially relative to** Alloys 600/82/182/132)” |
| H13 | 12 | H | 확정 | C, 재확인 | “이 한 식을 씁니다” → p.42 “selected that the same ΔK_th model be used for all three material classes **unless additional data that refute this approach are produced or identified**” |
| H14 | 12 | H | 확정 | CL | “약 30%” → p.40 “biased low by 30%” (원문에 없는 “약” 추가) |
| H15 | 17 | H | 확정 | L | b=0.82, p=2.2: p.43 “Best fits to individual data sets for air fatigue of **Alloy 600 in constant temperature environment**” (대상·조건 누락) |
| H16 | 18, 19 | H | 확정 | C, 재확인 | p.43~44 “yielded the following **best-estimate** temperature effect” → best-estimate 누락(2곳) |
| H17 | 24 | H | 확정 | C, 재확인 | 코드 9 설명: p.52 “**generally** applicable to carbon steels and low-alloy steels and their associated weld metals”, p.54 “Until other more specific models are developed … considered acceptable” 한정 누락 |
| H18 | 24 | H | 확정 | L | 온도 효과: 원문 “A temperature effect has not been included, **despite experimental evidence to the contrary**” 누락 (p.53) |
| H19 | 24 | H | 확정 | L | 각주 15 “… exhibited **for some combinations of loading, metallurgical, and environmental conditions**” 누락 |
| H20 | 24 | H | 확정 | L | 각주 16 “predictions … **may be unreliable**” → “불확실합니다”(hedge·출처 [35] 누락) |
| H21 | 24 | H | 확정 | L | 조건 ④: p.54 “Currently available data show that rapid transients cause little to no EAC … for **relatively low material sulfur** content. **It is hypothesized** that …” → “EAC가 유지되지 않음”(단정) |
| H22 | 24 | H | 확정 | L | 개발 범위 “황 약 0.004~0.02%”, “상승시간 주로 30 s” ← p.54 “sulfur contents from **very low (e.g., 0.004 %wt)** to 0.02 %wt”, “a **diversity** of loading rise times (although predominantly at 30 seconds)” |
| H23 | 29 | H | 확정 | C, 재확인 | “시간 적분합니다”, “조건을 갱신하고” → p.62 “**In general**, it is this net CGR that is integrated”, “**generally** account for time-variant properties”; 시간 스텝: p.61 “(within the tolerance needed for analysis)”, “a satisfactory value depends on the exact input conditions including fatigue cycling frequencies” 누락 |
| H24 | 29 | H | 확정 | L | 표면균열 “한쪽만 계산한 뒤 2배” → 각주 23은 “Growth asymmetry … can occur … the updated crack is assumed to remain symmetric, but its center location is shifted”라는 경우의 구현. 맥락 누락(일반 규칙처럼 서술) |
| H25 | 30, 31 | H | 확정 | L | 표 3-4: p.79 “should only be modified in parallel **with careful assessment**” → S30 “병행 수정해야 함”, S31 “한 열에서 일부만 바꾸지 않습니다”(금지로 변경) |
| H26 | 34 | H | 확정 | CL | “모의하는 것입니다” → p.92 “coalescence conventions **may simulate** two distinct modes by which cracks … **may combine**”; 원문의 이유 “higher order fracture mechanics calculations that are not amenable to the xLPR probabilistic framework or that were not made a priority” 누락 |
| H27 | 35 | H | 확정 | C, 재확인 | “0~20 in 가능” → p.94 “…are possible for components of interest in xLPR, **depending on the sizes of the flaws involved**” |
| H28 | 35 | H | 확정 | C, 재확인 | 삼각분포 권장: p.98 “**In the absence of more detailed investigation**” 누락(슬라이드 37에는 있음) |
| H29 | 37 | H | 확정 | CL | “반영합니다” → p.98 “This uncertainty **may reflect**” |
| H30 | 38 | H | 확정 | CL | “실험 증거가 있으며” → p.99 “Experimental evidence **suggests**” |
| H31 | 39 | H | 확정 | CL | Configuration A: “증가합니다” → p.100 “This **would** increase probability of leakage somewhat, …” |
| H32 | 43 | H | 확정 | C, 재확인 | 소제목 “5.2.1.7 Performance” → 원문 “5.2.1.7 Performance Requirements”(Requirements 누락) |
| H33 | 44 | H | 확정 | C, 재확인 | “계획된 실험이 도움이 될 수 있다” → p.118 “**Carefully** planned **laboratory** experiments may help quantify this correlation” |
| H34 | 44 | H | 확정 | L | “원문은 … 영역을 나열합니다” → p.117 “Refinements and extensions … are **desired** for several areas. … **For instance:**”(예시, desired) |
| H35 | 45 | H | 확정 | C, 재확인 | “Alloy 600 다음으로 Alloy 690과…” → p.118 “After Alloy 600 **and its associated weld metals**” |
| H36 | 47 | H | 확정 | CL | “후속 버전에서 쓰려는 안입니다” → p.119 “This model **could be improved** in a later version of xLPR by implementing …”; 원문 “good agreement with data scatter has been achieved using a log-normal distribution with a median of 4.4x10^-7 (m/cyc-s)^(1-0.33)”도 누락 |
| H37 | 47 | H | 확정 | CL | “고정 log-σ = 1.2를 권장합니다(p.45 각주 14)” → 각주 14 “…is recommended **at the risk of incorporating excessive variability at high CGRs**” 누락 |
| H38 | 48 | H | 확정 | L | 6.2.4: 원문 “To the extent that these can be identified, **they should be used to bolster the fatigue CGR model validation**” 누락 |
| H39 | 49 | H | 확정 | L | 6.3.1 “을 듭니다” ← “More complex geometries constitute extensive development efforts … **For instance:**”; 6.3.2 “secondary determinant … (**after ligament length**)” 누락 |
| H40 | 42 | H | 가능성 | L | “동작이 완전히 정해지도록 만들었습니다” ← p.110 “parameterized to improve flexibility. The following parameter inputs fully define the behavior” |
| A1 | 1 | A | 확정 | L | “한 줄 요약” 문장 전체(원문에 없는 HTML 요약: “…과정을 정리한 보고서입니다”) |
| A2 | 3 | A | 확정 | L | 아연: “균열 발생 모델에**만** 반영” → 원문 “included in the initiation model”(only 없음) (p.23) |
| A3 | 4 | A | 확정 | CL | “시편 계수 대신 용접 계수 4개를 곱합니다”(원문 해설 아님; 원문은 alloy factor, orientation factor가 추가된다고만 서술) |
| A4 | 6 | A | 확정 | C, 재확인 | “식 2-3과 함께 82/182/132의 수소 효과를 켤 때**만** 씁니다” |
| A5 | 7 | A | 확정 | CL | “식 2-4를 쓸 때마다 같이 씁니다” (원문 p.34는 “All the modeling presented in MRP-263 used [Eqn. 2-5] and [Eqn. 2-6]”, 다른 형태도 문헌에 있다고 서술) |
| A6 | 7, 8, 15, 23 | A | 확정 | L | “원문은 log의 밑을 적지 않았는데…”, “원문 식 2-6에는 단위가 적혀 있지 않고…”, “원문은 F_T를 temperature effect라고만 정의하고 단위는 적지 않았습니다”, “원문은 F_τ … 따로 적었습니다” (원문에 없는 해설 4곳; 사용자 규칙 위반 유형) |
| A7 | 9 | A | 확정 | CL | f_comp “(재료 그룹)”, f_flaw “결함 위치마다”, “사용자가 필요하면 값을 넣어 쓸 수 있도록”, “PWSCC 비슷한 SCC”(원문: “component-to-component variation”, “within-component variation”, “could be used to implement SCC CGR models for these materials”) |
| A8 | 10, 11 | A | 확정 | L | S10 “규정을 따랐습니다”(원문 “guidance”), “(경수로 환경 피로 균열 성장)”(원문은 “for LWR environments”뿐); S11 “음수 R을 쓰지 않습니다” |
| A9 | 13 | A | 확정 | CL | TeX 줄에 “(R≥0.10, 28 points)” 덧붙임(식 2-12 자체에는 없음), “주의” 단락(p.83·p.86·p.42를 HTML이 나란히 배치) |
| A10 | 14 | A | 확정 | L | da/dN 단위 “m/cycle”(원문 식 2-13 변수 설명에는 단위 없음) |
| A11 | 29 | A | 확정 | L | 제목 “시간 적분 규칙 (원문에 번호식 없음)” |
| A12 | 30 | A | 확정 | L | 표 3-1에 “PWSCC / 피로” 열과 식 연결(식 3-1, 2-13/2-14, 2-19, 2-23, “f=2.0”, “P=1” 등)을 넣고 “원문 표 3-1”이라 표시. 원문 Table 3-1은 Material Group, Numeric Code 두 열뿐; “코드 6~9 ‘미개발’은 … 뜻입니다” 해석 |
| A13 | 31 | A | 확정 | L | “식 2-1, 2-2, 2-3을 한 식으로 합친 구현용 식입니다” (원문: “flexible to accommodate all PWSCC CGR models presented in Section 2.2”) |
| A14 | 33 | A | 확정 | L | “(식 속의 a는 균열 깊이가 아니라 상수)”, “거듭제곱으로 넣은 형태입니다” |
| A15 | 34 | A | 확정 | L | “합체 거리와 합친 뒤 모양은 다음 두 페이지에서 설명합니다”, S35 “균열 유형 쌍마다 근거가 달라서 세 가지로 나눕니다” |
| A16 | 47 | A | 확정 | L | “구간별 값은 식 6-2에 적힌 대로입니다.”(내용 없는 HTML 문장) |
| A17 | 표지·서두·푸터 | A | 확정 | CL | “Contents … 순서와 표기를 그대로 따랐습니다”(원문 목차는 7. REFERENCES 포함, 슬라이드는 6장까지); 푸터 “영문 철자(MODULE, MODULE, RECOMMENDATIONS)는 그대로 두었습니다”(원문 목차에 오타 없음 → 의미 불명); “설명 문장은 새로 썼고” |
| A18 | 3, 7, 26, 40 | A | 가능성 | L | 식 해설: “K_th 이하이면 0, 넘으면 (K−K_th)^β에 비례”, “수소 농도 비의 로그에 비례하는 형태”, “(ΔK가 크면)”, Crack A/B “기준 균열 / 상대 균열” |
| A19 | 6, 7 | A | 가능성 | L | “T는 절대온도입니다”(식 2-5 where절에 T 정의 없음; 식 안 “298.15 [K]”로 추론), P−1/“변동 계수” 번역어 |
| A20 | 25 | A | 가능성 | L | 식 2-24의 a를 “균열 깊이”로 정의(원문 식 2-24에는 a 정의 없음; 표 3-3 p.77에 Crack depth a가 있어 연결은 가능) |
| A21 | 28 | A | 가능성 | L | C_EAC를 “(C_3)”로 표기(원문은 “previously stated environmental factor for EAC of high sulfur material”; C_3는 표 3-3의 고황 EAC 계수) |
| C1 | 31 | C | 확정 | CL | 인용: “재료마다 파라미터 값만 바꾼다”는 원문 p.79(§3.3.2)에 있는데 HTML은 (p.72)로 표기; 기준온도 문장의 근거도 p.79(HTML은 (p.76, 80)) |
| C2 | 43 | C | 확정 | CL | 소제목 “5.2.1.5 Updating Crack Attributes”가 제목과 소제목으로 2번 표시됨(내가 이번에 만든 중복) |
| C3 | 34 | C | 확정 | C(부분), 재확인 | “예: 깊이 1~3 mm 이상” 인용이 p.92인데 “in depth”는 p.19 각주 2에만 있음. Codex는 ADDED-CLAIM이라 했으나 원문 p.19 각주 2 “(e.g., 1-3 mm or more in depth)”가 있으므로 내용 오류는 아니고 인용 쪽만 맞지 않음 |

## 4. 제목·라벨 창작(T) — 구조 문제, 별도
- 식 슬라이드(3~29, 31~33쪽 해당 식)마다: “기호와 하첨자”, “하첨자 읽는 법”(열), “왜 이 식을 쓰나”, “어떤 조건에 쓰나”, “적용 방법”. 이 5개 라벨 구조는 원문에 없다.
- 슬라이드·장 제목: 표지 “XLPR 균열 성장·합체 발표자료 정리”, 장 부제 6개(예: “§1 · 목적, 모델 개요, 범위 (한국어 요약)”, “§4 · 합체 규칙: 합체 거리, 합친 뒤 모양, 가정”), S1 “목적과 담당 범위: 무엇을 하려고 만든 보고서인가”, S2 “모델 개요, 범위, 보고서 구성”, S6 “(가우스형 피크)”, S12 “(N-643-2 형태)”, S13 “실측 최소제곱 식”·“주의”, S15 “(Paris형)”, S24 “TCF로 가는 조건 / EAC로 가는 조건”, S29 “특수 규칙”, S30 “CGR 모듈은 식을 어떻게 불러 쓰나”와 소제목 7개, S31 “주의”, S34 “합체 모델이란”, S35 “합체 거리: 언제 합치나”, S36 “합친 뒤 균열 모양: 유형·깊이·중심·길이”와 “최대 깊이를 권장하는 이유”, S37 “분포된 합체 거리”·“그 밖의 합체 모델링 convention”, S38 “개요/인용된 연구/적용 범위”, S40~42의 “적용 목적/어떻게 동작하나/입력/범위/…”, S44 “기계적 성질, 냉간가공, 열처리”·“재료 경계면, 발생-성장 상관”, S45 “내용”, S46·S47 “개정”, S49 “축방향 균열과 미세균열” 등.
- 이번 수정에서 원문 제목으로 바꾼 것(5.1, 5.2.1.3, 5.2.1.5, 5.2.1.6, 5.3.3, 6.2.1, 6.2.2, 6.2.3, 6.2.4, 6.3, 6.3.1, 6.3.2)은 Codex·Claude 모두 원문 제목과 일치함을 확인했다. 단 “5.2.1.7 Performance”는 원문이 “Performance Requirements”다(H32).

## 5. 이 검증에서 확인된 오판 (Claude/Codex)
- Claude 정정: 슬라이드 6 “ΔECP=c에서 약 40% 감소”는 내 계산이 아니라 원문 p.81에 있다. 처음 내가 A로 의심했다가 원문으로 확인하고 철회했다. “P−1은 대수정규분포”도 표 3-4 주 2(p.82)에 있다.
- Claude 정정: 슬라이드 31 “재료마다 파라미터 값만 바꾼다”는 원문 p.79에 있다(내용은 원문). 인용 쪽만 틀렸다(C1).
- Codex 오판(부분): 슬라이드 34 “깊이 1~3 mm”를 원문에 없다고 판정했으나 p.19 각주 2에 있다(C3).
- Codex 누락: 슬라이드 10, 11, 14, 15, 48을 “추가 지적 없음”으로 보았으나 Claude는 10(규정), 11(음수 R), 14(단위), 15(해설), 48(bolster)에서 문제를 찾아 원문으로 확인했다.
- Claude 누락: Codex만 찾은 항목은 H2, H13, H16, H17, H23(일부), H27, H28, H32, H33, H35, W3, W4, A4, C3(부분)이며 모두 원문으로 재확인했다.
- 도구: Codex 실행 환경은 `.git`이 읽기 전용이라 git pull/add/commit이 모두 실패했다. 결과 파일은 Claude가 커밋했다(824da14).

## 6. 수정안(승인 전 적용 안 함)
1. 확정 항목 중 사실상 단서 복원(H), 의미 복원(W), 내 해설 삭제(A), 인용 보정(C)은 위 표의 “원문” 열 문구로 교체한다.
2. 표 2-1 머리글에 “성장 레짐(Growth Regime)” 열을 추가한다(W4).
3. 슬라이드 43의 중복 소제목을 한 번만 둔다(C2).
4. T(제목·라벨 구조)는 사용자 결정: (a) 그대로, (b) 원문 절 제목으로 교체, (c) 라벨 삭제.
5. 1~4장 “합체”를 coalescence로 교체할지는 사용자 결정.
6. 수정 후 해당 슬라이드만 Codex 재검증(round36).
