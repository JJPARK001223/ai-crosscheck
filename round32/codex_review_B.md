# Round 32 전체 감사 B — HTML p.17–33

대상: `J:\Desktop\XLPR\2026_10_13_XLPR모델분석\XLPR_발표자료_수식정리.html`의 `<section class="page …">` 순서 p.17–33(전체 47쪽). HTML 원문을 직접 읽었으며 수정하지 않았다.

유일한 근거: xLPR Models Subgroup, *xLPR Models Subgroup Report—Crack Growth and Coalescence*, 제공 PDF `(ML16341B051)Crack growth and coalescence.pdf`. 여기서 p.는 PDF의 인쇄 페이지이며 PDF 페이지 번호보다 1 작다. 개인 저자·발행연도는 검토한 표지에 명시되지 않아 임의로 부여하지 않았다. 외부 문헌이나 이전 감사 결과는 사용하지 않았다.

문장·숫자·단위·표의 각 행·하첨자 설명·조건·헤더의 절/인쇄 페이지를 대조했다. 수식 2-16–2-27 및 3-1–3-3은 PyMuPDF로 렌더링한 인쇄 이미지와 직접 대조했다. 본 수식의 계수·지수·부등호·하첨자 전사는 일치한다. 아래에는 문제만 적었다. SUPPORTED 항목은 요청대로 본문 목록에서 생략했다. INFERENCE는 잘못된 계산이라는 뜻이 아니라, 보고서가 직접 서술하지 않은 작성자의 해석/계산이라는 뜻이다. 이미 해석이라고 표시한 항목도 이 분류를 적용했다.

## p.17 하중비 효과 F_R

- **INFERENCE** — HTML: “b = 0.82, p = 2.2일 때 R이 커지면 F_R이 커집니다(R=1에서도 유한)” 및 “R이 커질수록 (1−bR)이 작아져 F_R이 커집니다.” 보고서는 인쇄 p.43에 `F_R=(1−b·R)^(−p)`와 “values of 0.82 and 2.2 for b and p, respectively”를 제시한다. 단조 증가 및 R=1에서의 유한성은 식에서 도출한 결과이며 보고서의 별도 서술이 아니다. 특히 보고서의 개발 R 범위는 약 0.05–0.95이므로 R=1을 검증 범위로 읽으면 안 된다. **수정안:** “보고서는 b=0.82, p=2.2를 제시한다(p.43). [식으로부터 계산한 해석] 이 값을 대입하면 개발 범위에서 F_R은 R에 따라 증가하며, R=1에서도 수학적으로 유한하다. R=1은 제시된 개발 데이터 범위 밖이다.”

## p.18 Alloy 600 계열 온도 효과

## p.19 Alloy 690 계열 온도 효과

- **OVERSTATED** — HTML: “690 계열에서는 환경 증폭이 관찰되지 않았다는 제한된 데이터가 있습니다.” 제한된 자료라는 표현은 적절하지만 환경 조건 및 추가 확인 필요성을 빠뜨렸다. 인쇄 p.44: “Limited data for Alloy 690 and its weld metals reveal no environmental enhancement in simulated PWR conditions. However, additional tests are needed to verify these results.” 보고서의 관찰을 일반적인 환경 전체로 확대하지 않아야 한다. **수정안:** “Alloy 690과 그 용접금속의 제한된 자료에서는 모사 PWR 조건에서 환경 증폭이 관찰되지 않았으나, 이 결과를 확인하기 위한 추가 시험이 필요하다(p.44).”

## p.20 스테인리스 피로 성장률

- **OVERSTATED** — HTML: “Mills의 방대한 시험 데이터(635점)와 일치합니다.” 인쇄 p.47은 “based on an extensive compilation of test data provided by Mills”라고 하고, “in close agreement”의 대상은 작성 중인 N-809의 CGR 모델이다. 인쇄 p.49의 635점은 Figure 2-15의 산포에서 C_SS의 불확실성을 추정할 때 언급된 데이터 수다. 보고서가 635점 모두와의 일치 또는 독립 검증을 선언한 것은 아니다. **수정안:** “Mills의 광범위한 시험 자료에 근거하며, 작성 중인 N-809 모델과 근접하게 일치한다고 보고한다(p.47–48). Figure 2-15에 보고된 635점의 양쪽 극단 상대잔차 각 5개를 C_SS의 산포 추정에 사용했다(p.49).”

## p.21 스테인리스 온도 효과

## p.22 스테인리스 하중비 효과

- **OVERSTATED** — HTML: “탄소 함량이 높은 304/316은 … 저탄소(304L/316L)는 … 늘기 때문에 재료를 둘로 나눠 서로 다른 식을 씁니다.” 관찰된 차이 자체는 근거가 있으나, 탄소 함량만으로 차이가 확정적으로 설명된 듯한 표현은 줄여야 한다. 인쇄 p.49: “varied markedly from heat to heat and appeared to be correlated to the carbon content.” 보고서는 heat 간 차이와 탄소 함량과의 외관상 상관관계를 설명하고, 관찰된 재료 차이를 식에 반영한다. **수정안:** “하중비 효과는 heat마다 크게 달랐고 탄소 함량과 관련된 것으로 보였다. 304/316과 저탄소 304L/316L에서 관찰된 차이를 반영해 식 2-21을 두 재료군으로 나눴다(p.49).”

## p.23 상승 시간 효과와 절단

- **INFERENCE** — HTML: “실제 계산에는 절단된 τ_r,limit을 넣는 것으로 읽힙니다.” 인쇄 p.49의 식 2-22는 `F_τ=τ_r^0.3`과 `τ_r,limit`의 구간식을 따로 인쇄하며, 본문은 “The loading rise time is truncated at 1 and 2000 seconds”라고 한다. 본문에 근거한 해석이지만 `F_τ=τ_r,limit^0.3`이라는 직접 연결은 인쇄식에 없다. HTML의 주석은 이 점을 이미 올바르게 구별한다. **수정안:** “원문은 상승 시간을 1–2000 s로 절단한다고 설명하나, 인쇄식에서 F_τ와 τ_r,limit을 직접 연결하지 않는다(p.49). [본문에 근거한 해석] 절단된 값을 F_τ 계산에 사용하는 것으로 읽을 수 있다.” 원문 전사식 자체는 바꾸지 않는다.

## p.24 페라이트 피로 성장률과 레짐 표

- **WRONG** — HTML 표 머리글: “C_env | n_fer | n_R”, 첫 데이터 행: “공기 | 7.87E-11 | 3.07 | 1”. 머리글은 3칸인데 모든 데이터 행은 4칸이어서 레짐명이 C_env 아래, C_env 값이 n_fer 아래, n_fer 값이 n_R 아래에 놓이고 실제 n_R은 머리글 없는 네 번째 열에 놓인다. 인쇄 p.53 표 2-1의 열은 “Growth Regime | Environmental Factor C_env | Paris Power-Law Exponent n_fer | Load Ratio Exponent n_R”이다. 모든 5개 레짐 행에 해당하는 구조 오류다. **수정안:** 머리글을 “성장 레짐 | C_env | n_fer | n_R”의 4칸으로 고친다. 수치 자체는 원문과 일치한다. 공기·TCF·중간 황 EAC·높은 황 공칭 EAC의 C_env 단위는 원문 표처럼 `(m/cyc)/(MPa√m)^3.07`로 명시한다.

- **WRONG** — HTML: “레짐 (원문 표 2-1)”의 상부 천이 C_env 셀을 “식 2-27”로 표기했다. 인쇄 p.53 표 2-1의 실제 셀은 “see [Eqn. 2-26]”이다. 한편 인쇄 p.56에서 C_upper를 정의하는 실제 식은 2-27이므로 원문 내부에 참조 불일치가 있다. 이를 설명 없이 원문 표의 내용으로 바꿔 제시해서는 안 된다. **수정안:** “원문 표 2-1은 식 2-26을 참조하지만(p.53), C_upper의 직접 정의는 식 2-27이다(p.56).” 표에는 원문 참조와 실제 정의를 구분해 병기한다.

- **WRONG** — HTML C_env 설명: “상황에 따라 C_1/C_2/C_3/C_upper 중 하나”. 같은 HTML 표에 포함한 공기 레짐의 C_env가 이 목록에서 빠졌다. 인쇄 p.53 표 2-1에는 “Air”의 C_env=`7.87E-11`이 별도로 있고, 인쇄 p.77 표 3-3의 C_1은 “Ferritic true corrosion fatigue environmental factor”이다. 공기 계수를 C_1로 대응시키면 안 된다. **수정안:** “C_env는 공기 레짐에서는 7.87E-11이고, 수중 레짐에서는 TCF의 C_1, 중간 황 EAC의 C_2, 높은 황 공칭 EAC의 C_3 또는 상부 천이의 C_upper를 사용한다(p.53, 77).”

- **OVERSTATED** — HTML: “ASME Code Case N-643-2와 일치하는 형태입니다.” 인쇄 p.52의 표현은 “The specified model is in close agreement with ASME Code Case N-643-2”이다. 완전한 동일성으로 읽히는 ‘일치’는 원문보다 강하다. **수정안:** “제시된 모델은 ASME Code Case N-643-2와 근접하게 일치한다(p.52).”

## p.25 EAC 진입 임계 속도

- **INFERENCE** — HTML: “깊이 2.5 mm 이하에서는 상수이고 그보다 깊으면 깊이에 반비례합니다.” 인쇄 p.54의 식 2-24가 이 결과의 근거지만, 보고서는 이러한 수학적 성질을 별도로 설명하지 않는다. HTML은 이미 ‘식 형태상’이라고 표시했다. **수정안:** “[식 2-24에서 도출한 해석] a≤2.5 mm에서는 V_trans가 일정하고 a>2.5 mm에서는 a에 반비례한다. 이는 보고서의 별도 해설 문장이 아니다(p.54).”

- **INFERENCE** — HTML: “이 α는 PWSCC의 α와 다른 값”. 인쇄 p.57 그림 2-18에는 “Calculate adjusted crack tip velocity, V_i = αΔa_i/Δt_i; α = 1.5”가 인쇄되어 있다. 인쇄 p.76 표 3-2의 PWSCC α는 단위가 있는 “Power-law constant”이다. 역할과 차원상 서로 다른 기호라는 판단은 가능하나 보고서에 두 α를 비교한 설명은 없다. **수정안:** “그림 2-18의 조정 계수 α는 1.5이다(p.57). [기호 대조에 따른 해석] 단위와 역할을 보면 PWSCC의 척도 상수 α(p.76)와 구분해야 한다. 보고서는 두 기호를 직접 비교하지 않는다.”

## p.26 TCF 복귀 완료 ΔK_c

- **INFERENCE** — HTML C_1 하첨자 설명: “1 = TCF 레짐 번호”. 인쇄 p.55는 “C1 and Cupper are the environmental factors applied for TCF and in the upper transition region for EAC”라고 정의하며 p.77 표 3-3도 C_1을 TCF 환경계수로 정의한다. 보고서는 ‘1번 레짐’이라는 번호 체계를 정의하지 않는다. **수정안:** “하첨자 1: TCF 환경계수를 식별하는 표기. 원문은 숫자 1의 별도 확장 의미나 레짐 번호 체계를 설명하지 않는다(p.55, 77).”

- **OVERSTATED** — HTML: “n=0.948의 선형 천이 구간”. 인쇄 p.56은 “effectively yielding a linear transition”이라고 한정한다. 정확한 선형식이라고 선언한 것이 아니며 표의 Paris 지수도 0.948이다. **수정안:** “ΔK_b와 ΔK_c 사이에서는 n_fer=0.948, n_R=1과 C_upper를 사용하며, 원문은 이를 사실상 선형 천이를 주는 것으로 설명한다(p.56).”

- **INFERENCE** — HTML 주석 전체의 대수/수치 부분: “교점은 (C_upper/C_1)^(1/2.122)(2.88−R)”, “ΔK_b ≈ 12.28, C_upper ≈ 3.42E-7, 교점 ≈ 62.5 MPa√m … 인쇄식은 약 2.4E7”. 인쇄 p.55의 실제 식 2-25는 `(C_upper/C_1)^2.122 θ^0.326(2.88−R)`이고, p.53 표 및 p.56 식 2-26·2-27은 비교 계산에 사용한 식과 계수를 제시한다. 보고서는 이 교점 계산·대표 조건·수치 결과·정정식을 제시하지 않는다. 독립 재계산으로 HTML의 근삿값은 재현되지만 원문 진술은 아니다. **수정안:** “인쇄식 2-25는 원문 그대로 전사한다(p.55). [작성자의 별도 대수 검토] 표 2-1 및 식 2-26·2-27과 비교하면 교점 계산에 불일치가 나타난다. 이는 원문 정정이 아니며 원문만으로 오기 여부를 확정하지 못한다.” 수치 검토를 남긴다면 원문 설명과 분리하고 작성자 계산이라는 표지를 유지한다.

## p.27 TCF 복귀 시작 ΔK_b

- **INFERENCE** — HTML: “θ의 지수가 양수라 다른 입력이 같을 때 상승 시간이 길수록 ΔK_b가 커집니다.” 인쇄 p.56의 식 2-26은 `ΔK_b=C_Kb θ^0.326(2.88−R)^2.69`, 최적값 C_Kb=0.498을 제시한다. 증가 방향은 식에서 도출한 해석이며 별도 보고서 문장이 아니다. **수정안:** “[식 2-26에서 도출한 해석] C_Kb와 R을 고정하면 θ^0.326 때문에 ΔK_b가 θ에 따라 증가한다(p.56).”

## p.28 상부 천이 계수

- **INFERENCE** — HTML: “지수 차 3.07−0.948 = 2.122, 하중비 지수 차 2.166×3.07−0.948 ≈ 5.702로 ΔK_b에서 C_3 곡선에 거의 연속으로 접속하는 것으로 읽힙니다”. 인쇄 p.56은 식 2-27과 “effectively yielding a linear transition”만 제시하며, 지수 차나 연속 접속의 설계 이유는 설명하지 않는다. p.53 표 값에서 직접 계산하면 두 번째 차는 5.70162로 HTML의 근사는 재현된다. **수정안:** “원문은 C_upper가 상승 시간과 하중비의 함수이며 사실상 선형 천이를 준다고 설명한다(p.56). [별도 대수 해석] 표 2-1의 지수 차와 식 2-27을 비교하면 ΔK_b에서 높은 황 EAC 곡선에 거의 연속으로 이어지는 것으로 읽힌다. 보고서가 그 설계 목적을 명시한 것은 아니다.”

## p.29 시간 적분 규칙

- **INFERENCE** — HTML의 번호 없는 수식 전체: `a(t+Δt)=a(t)+ȧ_netΔt`, `ȧ_net=ȧ_PWSCC+Σȧ_fat,i`, `ȧ_fat,i=(da/dN)|_i N_cyc,i/Δt`. 인쇄 p.61은 “explicit fixed-time forward Euler method”, p.62는 “multiplying by the number of cycles per unit time” 및 “sum of the PWSCC CGR and the fatigue CGRs for each active transient component”를 서술한다. HTML처럼 번호 없는 수식으로 정식화한 것은 작성자의 작업이며 보고서의 인쇄식은 아니다. 제목에서 이를 밝힌 점은 적절하다. 또한 HTML 표가 Δt 입력을 EFPY로 제시하는 반면 PWSCC α의 입력 단위는 m/s 기반이다(p.76–77). 공통 시간 단위로 변환하지 않고 이 식을 그대로 계산에 사용해서는 안 된다. **수정안:** “[원문 절차를 작성자가 수식화한 표현] 성장률과 Δt를 같은 시간 단위로 환산한 뒤 전진 오일러 갱신을 적용한다. Δt의 모듈 입력 단위는 EFPY이고, PWSCC 척도 상수는 m/s 기반이므로 시간 단위의 일치가 필요하다(p.61–62, 76–77).”

- **INFERENCE** — HTML: “프레임워크는 양끝의 조건을 평균해 한쪽만 계산한 뒤 2배로 반영하며, 이상화 관통균열도 같은 방식”. 인쇄 p.62 각주 23은 표면균열의 두 surface tip 평균/2배 처리를, p.63 각주 25는 이상화 관통균열의 ID 및 OD tip 평균/2배 처리를 각각 설명한다. 사이에 있는 천이 관통균열에도 동일 구현을 적용한다고 직접 서술하지는 않는다. HTML의 무조건적인 일반 표현은 이를 세 균열형 모두로 확대해 읽게 한다. **수정안:** “표면균열에는 p.62 각주 23의 평균/2배 처리, 이상화 관통균열에는 p.63 각주 25의 ID·OD별 평균/2배 처리가 명시되어 있다. 천이 관통균열의 동일 처리 여부는 이 두 각주에서 직접 확인되지 않는다.”

## p.30 CGR 모듈 개요

- **OVERSTATED** — HTML 코드 2 행: “수소 끔 = 식 2-2 값, 켬 = 식 2-3 값(활성화 에너지, 척도, 불확실성 입력도 해당 권장 값 세트로 바뀜)”. 권장 입력 세트가 다르다는 것은 인쇄 p.82 표 3-4로 확인되지만, P를 바꾸면 나머지 입력이 자동으로 교체된다고 보고서는 말하지 않는다. 인쇄 p.79: “allows the user to specify PWSCC CGR model parameters” 및 “inter-dependent and should only be modified in parallel with careful assessment.” **수정안:** “수소 효과 포함/제외에 따라 표 3-4의 권장 α, Q_g, 변동계수 분포가 다르므로 사용자가 일관된 입력 세트를 지정해야 한다(p.79, 82). P만 바꾸면 다른 입력까지 자동 변경된다는 의미는 아니다.”

- **WRONG** — HTML 전처리 문단 끝의 근거: “(p.68–70)”. 해당 문단의 ③ “§2.3.1에 따라 ΔK … 하중비 … 온도 … ΔK 문턱값을 미리 계산”의 직접 근거는 인쇄 p.71 §3.2.1.2: “calculates stress intensity factor range, load ratio, temperature, and stress intensity factor range threshold”. 사이클 온도의 최소/최대/평균 선택은 p.87에 설명되어 있다. p.68–70만으로 문단의 모든 항목을 뒷받침하지 못한다. **수정안:** 문단 근거를 “p.68–71; 온도 선택 플래그는 p.87”로 고친다.

- **WRONG** — HTML: “식의 매개변수 상당수는 소스 코드에 박혀 있지 않고 사용자 입력입니다(p.71).” 실제 문장은 인쇄 p.70: “Numerous parameters … are user inputs … (i.e., they are not hardwired into the source code).” p.71은 라우팅·전처리 및 재료 코드 표이다. **수정안:** 내용은 유지하고 인용 페이지를 “p.70”으로 고친다.

## p.31 모든 재료 공통 PWSCC 식

- **WRONG** — HTML f_comp, f_flaw 행의 하첨자 설명: “comp = 부품 간, flaw = 결함 간”. 인쇄 p.76 표 3-2 및 p.80의 정의는 각각 “Component-to-component CGR variation factor”와 “Within-component CGR variation factor”이다. f_flaw는 결함마다 독립적으로 부여하는 결함 간 변동이 아니라 동일 부품/연속 재료군 내부 공간 구간의 변동이다. HTML의 ‘하위 구간별 샘플’ 설명과도 서로 충돌한다. **수정안:** “f_comp: 부품 간 변동계수, 재료군별·시뮬레이션별 샘플. f_flaw: 부품 내 공간 변동계수, 공간 하위 구간별 샘플. flaw라는 기호 이름을 ‘결함 간’이라는 통계적 정의로 번역하지 않는다(p.76, 80).”

- **OVERSTATED** — HTML IF 행: “예: Alloy 82는 2.6”. 인쇄 p.28 각주 7: “should only be applied in the unusual case in which it is confirmed that the PWSCC as modeled is exclusively located in Alloy 82 material.” p.30 HTML에는 이 제한이 있으나 p.31의 독립적인 기호표에는 빠졌다. **수정안:** “Alloy 82의 IF=2.6은 모델링하는 PWSCC가 Alloy 82 용접금속 내부에만 위치한다고 확인된 특수 경우에 한해 적용한다(p.28 각주 7; 권장값 표는 p.82).”

- **OVERSTATED** — HTML: “f_alloy·f_orient 대신 IF로 합금 보정을 넣습니다.” 인쇄 p.72: “may be used to mimic the falloy and forient terms”. 보고서는 IF가 두 항의 효과를 모사하는 데 사용될 수 있다고 설명하며, 언제나 두 보정을 대신 적용하라고 단정하지 않는다. f_orient도 합금 종류 보정이 아니라 균열 방향 보정이다(p.27). **수정안:** “IF는 식 2-3의 합금 계수 f_alloy와 방향 계수 f_orient의 효과를 모사하는 데 사용할 수 있다(p.27, 72). 적용 여부와 값은 별도로 정한다.”

## p.32 사용자 정의 PWSCC

- **WRONG** — HTML: “f_comp, f_flaw … 부품 간, 결함 간 변동”. p.31과 같은 정의 오류다. 인쇄 p.76 표 3-2의 f_flaw는 “Within-component CGR variation factor”, p.80은 “sampled for each spatial discretization of each contiguous material group”라고 한다. **수정안:** “f_comp는 부품 간 변동, f_flaw는 부품 내 공간 위치 간 변동을 나타낸다(p.76, 80).”

- **INFERENCE** — HTML: “정해진 모델이 없는 재료에서 사용자가 직접 PWSCC를 정의하기 위한 식”. 인쇄 p.72는 “For custom materials (Material Group 10), by which xLPR users can specify their own growth characteristics”라고 한다. 사용자 정의 기능은 확인되지만, 이미 정해진 모델이 없는 경우에만 쓰거나 그 경우를 위해 만들었다는 조건/목적은 명시하지 않는다. **수정안:** “재료 그룹 10에서 사용자가 자신의 성장 특성을 지정할 수 있도록 제공되는 PWSCC 식이다(p.72).”

## p.33 사용자 정의 피로

- **INFERENCE** — HTML: “Ni계, 스테인리스, 페라이트 모델이 맞지 않는 재료를 위해”. 인쇄 p.73의 적용 조건은 “fatigue degradation mechanism is active”이면서 “custom material (Material Group10)”인 경우이며, 이어서 모든 cstm 하첨자 변수가 사용자 정의 매개변수라고 설명한다. 기존 세 모델이 ‘맞지 않음’을 요구하거나 이를 개발 목적이라고 설명하지는 않는다. **수정안:** “피로 메커니즘이 활성이고 재료 그룹이 사용자 정의 재료(10)일 때, 사용자가 5개 cstm 매개변수로 피로 CGR을 지정하는 식이다(p.73).”

문제 미발견 페이지: **p.18, p.21**. 이는 원문과의 대조에서 위 세 유형의 문제를 찾지 못했다는 뜻이며, 원문의 물리적 타당성이나 실제 코드 구현을 추가로 검증했다는 뜻은 아니다.

