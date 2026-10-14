# Round 32 전수 감사 A — HTML p.1–16

대상: `J:\Desktop\XLPR\2026_10_13_XLPR모델분석\XLPR_발표자료_수식정리.html`의 47개 section.page 중 첫 16개. 원시 HTML의 문장·표·data-tex를 검사했다. HTML 수정, Git 명령, 오케스트레이션 스크립트 실행은 하지 않았다.

유일한 근거: Kyle Schmitt, *xLPR Models Subgroup Report—Crack Growth and Coalescence*, xLPR-MSGR-CGR Version 1.0, EPRI/xLPR, 2016, NRC ADAMS ML16341B051. 아래 원문 쪽수는 모두 인쇄 쪽수(PDF 물리 페이지 − 1)다. 제공된 텍스트 덤프와 PDF를 사용했다. 수식은 PyMuPDF로 렌더링한 p.21, 27, 33, 34, 38–40, 42–43과 대조했다. 그림 2-10·2-11(p.41), 모듈 식(p.72), 표 3-5(p.86)도 이미지로 확인했다.

WRONG은 원문·인용 위치·단위와의 불일치, INFERENCE는 원문에 직접 서술되지 않은 해석, OVERSTATED는 근거보다 강한 표현이나 조건의 과도한 일반화다. INFERENCE는 수학적으로 틀렸다는 뜻이 아니며, HTML이 이미 추론이라고 표시한 경우도 요청대로 분류했다. 페이지별로 문제만 적는다. 머리말은 대표 수식/주제의 위치로 대조했다.

## p.1 목적과 담당 범위

## p.2 모델 개요, 범위, 보고서 구성

## p.3 식 2-1 · Alloy 600 균열 성장 속도

- **INFERENCE — 온도에 대한 계산 해석.** HTML: “식에서 읽으면, Qg>0이고 다른 입력이 같을 때 T가 Tref보다 높을수록 지수항이 1보다 커집니다.” 원문 p.22는 “temperature dependence, implemented as the classical Arrhenius model for thermally activated processes”라고 서술하고 식 2-1(p.21)을 제시하지만 이 부등식 해석을 문장으로 적지는 않는다. **수정:** “원문은 온도 의존성을 아레니우스 항으로 표현한다(p.22). [수식 해석] Qg>0, T>Tref이면 식 2-1의 지수항은 1보다 크다.” 원문 사실만 남기려면 계산 해석을 삭제한다.

## p.4 식 2-2 · Alloy 82/182/132

- **WRONG — Kth=0의 근거 쪽수.** HTML: “데이터가 부족해 0이 아닌 K 문턱값은 넣지 않아 Kth = 0입니다(p.28–29).” 원문 **p.27**: “there were insufficient data available to include a nonzero stress intensity factor threshold.” p.82 표 3-4는 해당 모델의 threshold를 0으로 제시한다. **수정:** “0이 아닌 응력확대계수 문턱값을 포함하기에는 자료가 부족하다고 판단했다(p.27). 권장 Kth는 0 MPa√m이다(p.82, 표 3-4).”

- **WRONG — 77개 측정/19개 용접의 분석 위치.** HTML: “용접 간 변동 fweld의 분포는 19개 시험 용접의 77개 측정으로 구했습니다(p.29).” 원문 **p.28**: “Per analysis of the 77 measurements across 19 unique test welds in the MRP-115 database … weld-to-weld variability can be represented as a log-normal distributed … term.” p.29는 분포 그림 2-3의 위치다. **수정:** “19개 시험 용접에서 얻은 77개 측정값의 분석으로 용접 간 변동 분포를 구했다(p.28; 그림 2-3은 p.29).”

- **WRONG — 수소 효과 제외의 근거 쪽수.** HTML: “데이터가 부족해 용존수소(전기화학 전위) 효과는 이 식에 넣지 않았습니다(p.29).” 원문 **p.28**: “It was judged that insufficient data were available at the time to include the effects of dissolved hydrogen concentration (i.e., electrochemical potential).” **수정:** “당시 자료가 부족하다고 판단하여 용존수소 농도, 즉 전기화학 전위 효과를 포함하지 않았다(p.28).”

- **WRONG — 수소 체적 기준과 검증 K 단위 누락.** HTML: “수소 25~50 cc/kg … 별도 검증 범위는 K 10~80, 280~350°C”. 원문 p.27: “hydrogen concentrations from 25 to 50 cc(STP)/kg”; p.30: “stress intensity factors between 10-80 MPa√m and operating temperatures between 280-350°C.” **수정:** “개발 데이터의 용존수소 농도는 25–50 cc(STP)/kg이다(p.27). 별도 검증 범위는 K=10–80 MPa√m, 280–350°C이다(p.30).”

- **OVERSTATED — 방향계수를 사용하지 않는 이유의 절대화.** HTML: “실제로는 덴드라이트 방향을 모르므로 모델에서 쓰지 않습니다.” 원문 p.28: “the dendrite growth direction at any given location in the weldment is **usually not reliably known**”. **수정:** “용접부 각 위치의 덴드라이트 성장 방향은 통상 신뢰성 있게 알기 어려우므로, 이 모델의 실제 적용에서는 방향계수를 사용하지 않는다(p.28).”

## p.5 식 2-3 · 수소 효과를 포함한 CGR

- **WRONG — 검증 K 단위와 수소 체적 기준 누락.** HTML: “검증 범위는 K 10~80, 280~350°C, 수소 약 1~60 cc/kg입니다.” 원문 p.37: “stress intensity factors between 10-80 MPa√m, operating temperatures between 280-350°C, and hydrogen concentrations between roughly 1 and 60 cc(STP)/kg.” **수정:** “검증 범위는 K=10–80 MPa√m, 280–350°C, 용존수소 농도 약 1–60 cc(STP)/kg이다(p.37).”

## p.6 식 2-4 · 수소 보정 계수

- **WRONG — 가우스형 의존성 설명의 인용 쪽수.** HTML: “원문은 이 항이 ECP에 대해 가우스형 의존성을 가져, 전이점에서 수소 농도가 높은 쪽이든 낮은 쪽이든 멀어지면 CGR 예측이 줄어든다고 설명합니다(p.33).” 실제 문장은 **p.34**: “The term has a Gaussian dependence relative to ECP such that the CGR prediction is reduced at both high and low hydrogen concentrations away from the Ni/NiO transition.” **수정:** 인용을 “p.34”로 바꾼다. p.33에는 식 2-4가 있다.

- **OVERSTATED — 표본추출 절차의 조건 누락.** HTML: “시뮬레이션마다 P와 c를 확률분포에서 뽑아 넣습니다.” 원문 p.35: “A positive correlation of 0.714 between the underlying normal deviates was used for peak width and peak-to-valley ratio samples.” p.76 표 3-2는 P와 c의 빈도를 모두 “per heat”로 지정하며, 같은 쪽은 이를 각 독립 시뮬레이션의 각 distinct material group당 한 번으로 정의한다. p.82 표 3-4 주 2의 분포 모수는 **P 자체가 아니라 P−1**에 지정한다. 단순히 두 분포에서 뽑는다는 설명만으로는 권장 절차를 재현하지 못한다. **수정:** “각 독립 시뮬레이션에서 재료 그룹마다 P와 c를 표본추출한다. P−1의 대수정규분포와 c의 정규분포에 대해 기저 정규변수의 상관계수 0.714를 적용한다(p.35, 76, 82).”

- **INFERENCE — 세 식을 비교한 설명.** HTML: “이 대괄호가 식 2-4와 같은 형태이고, 식 2-3은 기본 성장항에 이 보정을 곱한 형태입니다(식을 비교해 읽은 것).” 근거: p.33 식 2-3·2-4와 p.34 식 2-7. 원문 p.34는 “The MRP-263 model for hydrogen dependence assumed the following form”이라고 식 2-7을 제시하지만 세 식의 대괄호를 비교하는 이 문장은 직접 쓰지 않는다. **수정:** “[수식 비교 해석] 식 2-7의 대괄호는 식 2-4와 같으며, 식 2-3은 기본 성장항에 fH2를 곱한다(p.33–34).” 원문 서술만 남기려면 삭제한다.

## p.7 식 2-5 · 전기화학 전위 차

- **INFERENCE — 전이 농도에서 0이라는 대입 계산.** HTML: “식에 대입하면, 수소 농도가 전이 농도와 같을 때 로그가 0이라 ΔECP = 0입니다.” 근거: p.33 식 2-5의 log([H2]/[H2]Ni/NiO). 원문은 식과 농도 정의를 제시하며 이 대입 계산은 직접 서술하지 않는다. **수정:** “[수식 해석] [H2]=[H2]Ni/NiO를 식 2-5에 대입하면 ΔECPNi/NiO=0이다(p.33).” 원문 사실만 남기려면 삭제한다.

## p.8 식 2-6 · Ni/NiO 전이 수소 농도

- **INFERENCE — 온도에 대한 단조 증가 해석.** HTML: “식의 온도 계수가 양수이므로 온도가 오르면 전이 농도도 커집니다(식에서 읽은 것).” 원문 p.34는 “temperature dependent”라고 하며 식 2-6 `[H2]Ni/NiO=10^(0.0111T−2.59)`을 제시한다. 증가 방향의 문장은 직접 없다. **수정:** “원문은 전이 수소 농도가 온도에 의존하며 식 2-6으로 계산할 수 있다고 설명한다(p.34).” 증가 방향을 남기려면 “[수식 해석]”으로 구분한다.

## p.9 식 2-8 · 그 밖의 재료용 일반 SCC 식

## p.10 식 2-9 · 응력확대계수 범위

## p.11 식 2-10 · 하중비

## p.12 식 2-11 · 피로 문턱값

- **OVERSTATED — 온도 입력의 재료 범위 누락.** HTML: “Ni계, 오스테나이트, 페라이트 모두 이 한 식을 씁니다 … 공칭 온도는 사이클의 평균(플래그 1), 최소(2), 최대(3) 중 사용자가 선택합니다.” 세 재료 공통 설명과 이어져 온도 선택 역시 세 재료 공통 요건처럼 읽힌다. 원문 p.39: “The fatigue CGR models for **Ni-based alloy and austenitic SS** require a temperature input.” 플래그 값은 p.87과 일치한다. **수정:** “식 2-11은 세 재료군에 공통 적용한다(p.42). 별도로 온도 입력이 필요한 Ni계·오스테나이트 SS의 피로 계산에서는 공칭 온도를 평균(1), 최소(2), 최대(3) 중 선택한다(p.39, 87).”

- **OVERSTATED — 표본추출 단위와 권고 강도.** HTML: “CKth는 시뮬레이션당 1회 샘플링하는 epistemic 변수입니다.” 원문 p.40: “should be sampled once **per component simulation**”; p.77 표 3-3은 CKth의 빈도를 “per heat”로 지정하고, p.76은 이를 각 독립 시뮬레이션의 각 재료 그룹당 한 번으로 정의한다. 전체 시스템 시뮬레이션에서 무조건 하나의 공통 표본을 쓰라는 뜻은 아니다. **수정:** “문턱값 불확실성은 epistemic으로 취급하며, 부품 시뮬레이션당 한 번 표본추출하도록 권고한다(p.40). 모듈 입력 빈도는 재료 그룹별 per heat이다(p.76–77).”

## p.13 식 2-12 · 문턱값 실측 최소제곱 식

- **WRONG — 수식과 기호표의 단위 누락.** HTML: `ΔKth=7.0·(1−0.693R)` 및 기호표 “피로 성장이 무시되는 ΔK 문턱값”. 이 페이지 어디에도 ΔKth의 단위가 없다. 원문 p.40은 직전에 “the following best-fit equation (**in units MPa√m**)”이라고 명시한다. **수정:** 기호표에 “ΔKth: 응력확대계수 범위 문턱값, MPa√m”를 명시한다. R≥0.10과 28개 점은 원문의 수식 본체가 아닌 적합 자료 조건이므로 별도 설명으로 두면 원식과의 구분도 명확하다.

- **INFERENCE — 절편과 기울기 계산.** HTML: “식에서 계산하면 R=0에서 7.0, R에 대한 기울기는 −7.0×0.693 = −4.851입니다(괄호 안의 0.693은 계수이며 R=0은 데이터 범위 밖의 절편).” 원문 p.40은 “A least squares linear fit … for R≥0.10 (28 data points)”라고 하며 식 2-12를 제시한다. 절편·전개 기울기 수치는 직접 설명하지 않는다. **수정:** “식 2-12는 R≥0.10인 28개 측정점의 최소제곱 적합식이다(p.40). [수식 해석] 외삽 절편은 7.0 MPa√m이고 R에 대한 기울기는 −4.851 MPa√m이다.” 원문 사실만 남기려면 계산 부분을 삭제한다.

- **WRONG — 상한 절단의 기준 누락.** HTML: “상한 절단 1.517배는 작은 데이터 집합에 없는 비보수적 값을 막기 위한 것입니다”. 원문 p.40 각주 12: “at **1.517 times the median**”. 1.517은 절대 상한 CKth가 아니라 중앙값의 배수다. p.86 표 3-5에는 log-μ=0.239와 upper truncation=1.927이 있다. **수정:** “상한은 양의 3σ 수준, 즉 선택한 분포 **중앙값의 1.517배**에서 절단하도록 권고한다(p.40 각주 12). 표 3-5의 상한 1.927은 해당 표의 log-μ=0.239인 분포에 대한 값이다(p.86).”

## p.14 식 2-13 · 환경 효과를 포함한 da/dN

- **OVERSTATED — 데이터 적합을 ‘그대로 표현’한다고 서술.** HTML: “NUREG/CR-6721의 방대한 데이터(공기, 모의 PWR 환경)를 그대로 표현하기 위해서입니다.” 원문 p.43: “based most notably on analysis presented in NUREG/CR-6721”; p.44: “A least squares fit to data … yielded best-fit estimates”. 원문은 회귀 모델이며 모든 데이터를 그대로 재현한다고 하지 않는다. p.44는 일부 용접금속 데이터의 신뢰성이 확정적이지 않다고 하며 독립 MHI 자료에는 환경 지수 0.25에서 더 정확한 예측을 얻었다고 명시한다. **수정:** “NUREG/CR-6721에서 분석한 공기 중 및 모사 PWR 환경의 피로 CGR 자료를 토대로, 환경 효과를 포함한 성장 관계를 나타내기 위해 사용한다(p.43–44).”

- **INFERENCE — 상승시간에 대한 단조성 유도 및 조건 누락.** HTML: “식에서 읽으면, 0<nenv<1(표 3-5의 0.25~0.33)이고 다른 입력이 같을 때 τr이 길수록 환경항이 커집니다.” 근거는 식 2-13(p.42), 표 3-5(p.86)이며 원문은 이 조건부 단조성 문장을 직접 쓰지 않는다. 또한 p.77 표 3-3은 Aenv=0도 허용한다. 이 경우 환경항은 0으로 일정하므로 무조건 ‘커진다’고 할 수 없다. **수정:** “[수식 해석] Aenv>0, 공기 중 성장량>0, 0<nenv<1이고 다른 입력이 같으면 상승시간 증가에 따라 환경항이 증가한다. Aenv=0이면 환경항은 항상 0이다(식 2-13, p.42; 입력 범위 p.77).”

## p.15 식 2-14 · 공기 중 da/dN

- **INFERENCE — FT의 차원/척도 추정.** HTML: “계수 크기(약 1E-14)와 식 2-14의 다른 항을 함께 보면 성장량 척도가 들어 있는 것으로 읽히지만 원문이 명시한 것은 아닙니다.” 원문 p.42의 정의는 “FT = temperature effect”; p.43–44 식 2-17·2-18은 수치 계수를 제시한다. ‘성장량 척도가 들어 있다’는 문장은 원문에 없다. 이미 추론이라고 표시되어 있어 사실 오기와는 구별된다. **수정:** “원문은 FT를 온도 효과로 정의하고 식 2-17·2-18을 제시한다(p.42–44). 계수 단위는 해당 위치에 따로 표기하지 않는다.” 차원 해석을 남기려면 별도의 “[수식의 차원 해석]”으로 구분한다.

## p.16 식 2-15 · 합금 보정

문제가 발견되지 않은 페이지: **p.1, p.2, p.9, p.10, p.11, p.16**. 대조 근거는 각각 원문 p.17–18, p.18–19, p.38·72·80, p.39, p.39–40·43·49·53, p.43–44·83·86이다. 나머지 페이지에서도 목록에 들지 않은 문장·수치·표 항목 및 대표 수식·머리말은 대조 범위에서 SUPPORTED로 판단했다. 원문 내부의 불일치(p.83의 CKth 중앙값 1 대 p.86 표 3-5의 log-μ=0.239)는 HTML 오류로 판정하지 않았다.
