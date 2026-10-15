# Round 36 — PPT 텍스트와 EPRI 원문 대조

대상: round36_ppt/ppt_dump.txt의 90개 슬라이드. 근거: Kyle Schmitt, EPRI, *xLPR Models Subgroup Report—Crack Growth and Coalescence*, xLPR-MSGR-CGR Version 1.0, 2016-06-29. 모든 아래 영어 인용은 이 보고서의 제공된 cgr_text.txt에서 직접 확인했다. 외부 문헌의 원문 자체를 검증했다는 뜻은 아니다. 본문 인쇄 쪽은 PAGE 마커 값에서 1을 뺀 값으로 대조했다. 약어 목록의 실제 인쇄 쪽은 xiv(PAGE 15)이다. 표지·서명면처럼 쪽번호가 없는 면은 PAGE 번호로 표시한다. 원문 인용의 1321은 Alloy 132 뒤에 각주 번호 1이 붙은 추출 표기이다. 영어 인용은 줄바꿈을 공백으로 정리하고 행말 분리 하이픈 뒤 줄바꿈을 연결했다.

본문 문장·표 행별 판정이다. 제목·내용 구분을 위한 소제목은 대응 절과 함께 확인하고 오류가 있을 때 별도 기록했다. 빈 틀은 요청에 따라 ‘내용 없음’만 적었다. PPT의 그림·수식 이미지는 텍스트 추출본에 담긴 문장과 별개로 검증하지 않았다. 작성자·소속·발표일·마지막 인사는 원문 과학 주장에 해당하지 않는다. ‘일치’는 해당 문장 내용의 대조 결과이며 슬라이드 전체 무오류 판정은 아니다.

### [슬라이드 1] 제목 일치 / 발표 메타데이터 대조 대상 아님 — 확신도(CONFIRMED / PLAUSIBLE)
- PPT 문구: “xLPR Crack Growth and Coalescence”; 작성자·소속·발표일.
- 원문 근거: “Crack Growth and Coalescence” (서명면, PAGE 3, 절 없음).
- 문제: 제목 일치. 발표자의 성명·소속·발표일은 이 보고서에서 확인 불가(PLAUSIBLE은 미검증 표지이며 사실 확인을 뜻하지 않음).

### [슬라이드 2] 오탈자 — 확신도(CONFIRMED)
- PPT 문구: “CRACK GROWTH RATE MOUDLE”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “CRACK GROWTH RATE MODULE” (p.68, §3 제목).
- 추가 원문 근거: “This report is organized as follows: • Section 1 provides an overview of the Crack Growth Subgroup roles, responsibilities, and models. • Section 2 details the PWSCC and fatigue crack growth models including their technical bases, underlying assumptions, and mathematical descriptions. • Section 3 discusses the implementation of the CGR modules, including design, integration, and V&V. • Section 4 details the coalescence growth model. • Section 5 discusses the implementation of the coalescence module. • Section 6 provides recommendations for future work. • Section 7 provides a list of references cited in this report.” (p.19, 위 인용 절의 해당 문단).
- 문제: 오탈자: MOUDLE 철자 오류.
- 최소 교체안: CRACK GROWTH RATE MODULE

### [슬라이드 3] 의미 변경 — 확신도(CONFIRMED)
- PPT 문구: “PWSCC 성장 속도를 환경변수와 하중변수의 함수로 예측하고 불확실성을 포함하는 모듈이 기본값임”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “The foundation of the PWSCC growth model is a module that predicts PWSCC growth rate as a function of important environmental and loading variables and includes appropriate uncertainties.” (p.18, §1.2).
- 문제: 의미 변경: foundation(기반)을 기본값(default)으로 바꾸었다.
- 최소 교체안: PWSCC 성장 모델의 기반은 환경·하중변수와 불확실성을 포함해 성장 속도를 예측하는 모듈임.

### [슬라이드 3] 일치 — 확신도(CONFIRMED)
- PPT 문구: “정상 PWR 환경에서 Alloy 600과 그 용접 금속 (Alloy 82 . 182 . 132 ) 에 대한 권장 매개변수를 제시함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “The Crack Growth Subgroup has provided model parameter recommendations for PWSCC CGR predictions in Alloy 600 and its associated weld metals (Alloys 82, 182, and 1321) in normal PWR environments.” (p.18, §1.2).
- 문제: 일치

### [슬라이드 3] 일치 — 확신도(CONFIRMED)
- PPT 문구: “다른 재료 (Alloy 52 . 152 . 오스테나이트계 스테인리스 모재와 용접부 . 페라이트 강 ) 는 매개변수를 제시하지 않았는데 이런 재료에서는 PWSCC가 일어나지 않거나 Alloy 600 보다 훨씬 느리다는 증거가 충분하다고 설명함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “does not occur or occurs at substantially reduced rate relative to Alloy 600 in normal PWR environments.” (p.18, §1.2).
- 추가 원문 근거: “Model parameters appropriate for other materials or environments have not been prescribed; however, there is ample evidence that PWSCC in other common primary-side component materials—such as Alloys 52 or 152, austenitic SS base metals and welds, and ferritic steels—does not occur or occurs at substantially reduced rate relative to Alloy 600 in normal PWR environments.” (p.18, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 3] 일치 — 확신도(CONFIRMED)
- PPT 문구: “피로 성장 모델도 같은 방식의 모듈임”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Like the PWSCC growth model, the foundation of the fatigue growth model is a module that predicts fatigue growth rate as a function of important environmental and loading variables and includes appropriate uncertainties.” (p.18, §1.2).
- 문제: 일치

### [슬라이드 3] 일치 — 확신도(CONFIRMED)
- PPT 문구: “재료군별로 Ni계 합금 , 오스테나이트 스테인리스 , 페라이트강 세 가지 하위 모델을 만듬”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Distinct submodels have been developed for fatigue CGR predictions in three different material classes: Ni-based alloys, austenitic SS, and ferritic steels.” (p.18, §1.2).
- 문제: 일치

### [슬라이드 3] 오탈자 — 확신도(CONFIRMED)
- PPT 문구: “PWSCC와 피로의 CGW는 더해져서 프레임워크가 균열 성장 예측에 사용됨”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “CGR predictions for PWSCC and fatigue mechanisms are summed and utilized by the xLPR Framework to yield predictions for crack growth.” (p.18, §1.2).
- 문제: 오탈자: CGW → CGR.
- 최소 교체안: PWSCC와 피로의 CGR 예측은 합산되어 프레임워크의 균열 성장 예측에 사용됨.

### [슬라이드 4] 일치 — 확신도(CONFIRMED)
- PPT 문구: “규칙 기반 모듈로 , 같은 평면에 있는 원주방향 균열 중 공학적으로 의미 있는 크기의 균열이 종류, 형상 , 위치에 따라 합쳐지는 것을 모사함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “This module uses rule-based criteria to simulate coalescence of coplanar circumferential cracks of engineering significance based on their type, geometry, and location.” (p.19, §1.2).
- 문제: 일치

### [슬라이드 4] 일치 — 확신도(CONFIRMED)
- PPT 문구: “가까운 균열 사이의 응력확대계수 증폭 (균열간섭) 이나 둘 사이 ligament의 소성 붕괴처럼 단일 균열의 PWSCC . 피로 성장보다 훨씬 빠르게 균열이 커지는 현상을 반영함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “This simulation is intended to account for mechanisms that lead to crack extension on a time-scale significantly faster than that predicted for PWSCC and fatigue growth of a single crack, including crack tip interaction that can lead to intensified stress intensity factors and plastic collapse of a ligament separating two cracks.” (p.19, §1.2).
- 문제: 일치

### [슬라이드 4] 일치 — 확신도(CONFIRMED)
- PPT 문구: “매개변수는 실험 연구와 파괴역학 모델링으로 검증했다고 함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “The Crack Growth Subgroup has provided general coalescence model parameters and has validated them against laboratory studies and fracture mechanics modeling.” (p.19, §1.2).
- 문제: 일치

### [슬라이드 4] 일치 — 확신도(CONFIRMED)
- PPT 문구: “xLPR 2.0의 CGR 모듈은 PWR 1차계통 배관 재료 (이종금속 용접과 동종금속 용접 포함) 에서 정상 1차수 환경의 SCC와 피로 CGR을 예측하는 것이 목표임”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “The objective of the Crack Growth Module of xLPR 2.0 is to predict SCC and fatigue CGRs in normal PWR primary water environment of materials commonly located in PWR primary piping systems, including dissimilar metal welds and similar metal welds.” (p.19, §1.3).
- 문제: 일치

### [슬라이드 4] 일치 — 확신도(CONFIRMED)
- PPT 문구: “합체 모듈은 xLPR 2.0 프레임 워크가 다루는 이상화 된 균열 종류의 결합을 예측하는것이 목표임”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “The objective of the Coalescence Module of xLPR 2.0 is to predict the combination of idealized cracks of the types modeled within the xLPR 2.0 framework.” (p.19, §1.3).
- 문제: 일치

### [슬라이드 5]
내용 없음

### [슬라이드 6]
내용 없음

### [슬라이드 7]
내용 없음

### [슬라이드 8]
내용 없음

### [슬라이드 9]
내용 없음

### [슬라이드 10]
내용 없음

### [슬라이드 11]
내용 없음

### [슬라이드 12]
내용 없음

### [슬라이드 13]
내용 없음

### [슬라이드 14]
내용 없음

### [슬라이드 15]
내용 없음

### [슬라이드 16]
내용 없음

### [슬라이드 17]
내용 없음

### [슬라이드 18]
내용 없음

### [슬라이드 19]
내용 없음

### [슬라이드 20]
내용 없음

### [슬라이드 21]
내용 없음

### [슬라이드 22]
내용 없음

### [슬라이드 23]
내용 없음

### [슬라이드 24]
내용 없음

### [슬라이드 25]
내용 없음

### [슬라이드 26]
내용 없음

### [슬라이드 27]
내용 없음

### [슬라이드 28]
내용 없음

### [슬라이드 29] 일치 — 확신도(CONFIRMED)
- PPT 문구: “공기 중 피로 성장 데이터를 Paris 거듭법칙에 하중비 , 온도 합금효과를 곱한 형태로 표현함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Paris power-law exponent” (p.42, §2.3.2.1, 식 2-14).
- 추가 원문 근거: “da =C f F F (ΔK )n Ni [Eqn. 2-14] dN Ni alloy T R air where:” (p.42, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 29] 일치 — 확신도(CONFIRMED)
- PPT 문구: “Ni계 재료 (코드 1~5) 의 피로에서 식 2-13 의 첫 항과 환경항 계산의 입력으로 씀”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “• If the fatigue degradation mechanism is active and the material is a nickel-based alloy (Material Groups 1 through 5), the fatigue CGR is calculated with the CGR model given in Section 2.3.2.” (p.72, §3.2.1.3).
- 추가 원문 근거: “Fatigue CGRs for nickel-based alloys are calculated as follows: n da da  da  env = +A   τ1−n env [Eqn. 2-13] dN dN env dN r   air air da =C f F F (ΔK )n Ni [Eqn. 2-14]” (p.42, 위 인용 절의 해당 문단).
- 추가 원문 근거: “If the fatigue degradation mechanism is active and the material is a nickel-based alloy (Material Groups 1 through 5), the fatigue CGR is calculated with the CGR model given in Section 2.3.2.” (p.72, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 29] 일치 — 확신도(CONFIRMED)
- PPT 문구: “원 자료에서는 temperature effect 라고만 정의하고 단위는 적지않음”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “temperature effect” (p.42, §2.3.2.1, 식 2-14 기호 정의).
- 추가 확인: 해당 판정은 제공된 EPRI 보고서 p.42의 기호 정의에 한함. 인용된 별도 NUREG 보고서 자체를 조사한 결과가 아님.
- 문제: 일치

### [슬라이드 29] 일치 — 확신도(CONFIRMED)
- PPT 문구: “Alloy 690은 시험이 약 60개정도라 Paris 지수와 하중비 효과는 재추정 하지 않고 온도효과만 구함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “The roughly 60 tests available for Alloy 690 fatigue CGR in air were not sufficient to support estimation of the Paris power-law model or the load ratio effect. However, the temperature effect was re-estimated for Alloy 690.” (p.44, §2.3.2.2).
- 문제: 일치

### [슬라이드 30]
내용 없음

### [슬라이드 31]
내용 없음

### [슬라이드 32]
내용 없음

### [슬라이드 33]
내용 없음

### [슬라이드 34]
내용 없음

### [슬라이드 35]
내용 없음

### [슬라이드 36]
내용 없음

### [슬라이드 37]
내용 없음

### [슬라이드 38]
내용 없음

### [슬라이드 39]
내용 없음

### [슬라이드 40]
내용 없음

### [슬라이드 41]
내용 없음

### [슬라이드 42]
내용 없음

### [슬라이드 43]
내용 없음

### [슬라이드 44]
내용 없음

### [슬라이드 45]
내용 없음

### [슬라이드 46]
내용 없음

### [슬라이드 47]
내용 없음

### [슬라이드 48]
내용 없음

### [슬라이드 49]
내용 없음

### [슬라이드 50]
내용 없음

### [슬라이드 51]
내용 없음

### [슬라이드 52]
내용 없음

### [슬라이드 53]
내용 없음

### [슬라이드 54]
내용 없음

### [슬라이드 55]
내용 없음

### [슬라이드 56]
내용 없음

### [슬라이드 57] 일치 — 확신도(CONFIRMED)
- PPT 문구: “CGR | 균열 성장 속도  |”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Crack Growth Rate” (p.xiv, §약어 목록).
- 문제: 일치

### [슬라이드 57] 오탈자 — 확신도(CONFIRMED)
- PPT 문구: “Meterial Group | 모듈이 인식하는 재료 그룹과 숫자코드  / 표(3-1) |”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Material Groups Recognized by CGR Module” (p.71, §3.2.1.2, 표 3-1).
- 문제: 오탈자: Meterial → Material.
- 최소 교체안: Material Group

### [슬라이드 57] 일치 — 확신도(CONFIRMED)
- PPT 문구: “Transient component | 피로 계산에 쓰는 하중 천이 성분  |”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “The number of active transient components that are treated independently in the calculation of fatigue CGR.” (p.78, §3.3.1).
- 문제: 일치

### [슬라이드 58]
내용 없음

### [슬라이드 59]
내용 없음

### [슬라이드 60]
내용 없음

### [슬라이드 61]
내용 없음

### [슬라이드 62] 일치 — 확신도(CONFIRMED)
- PPT 문구: “피로 메커니즘이 켜져있고 재료 그룹이 사용자 정의재료 (No.10)  일 때 사용자가 cstm 하첨자가 붙은 5개 매개변수 피로 CGR을 지정하는 식임”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “3-3] dN cstm R ( 1−a R )b cstm    cstm where all variables with the subscript cstm are user-defined custom CGR model parameters. 3.2.1.4 Post-CGR Calculation A number of post-calculation operations are required to compile the outputs of the individual calls to the CGR functions, for example: • The output of the fatigue CGR functions is in terms of crack advancement per fatigue cycle.” (p.73, §3.2.1.3, 식 3-3).
- 문제: 일치

### [슬라이드 62] 일치 — 확신도(CONFIRMED)
- PPT 문구: “재료코드 10 (사용자 정의 재료) 의 피로에서만 사용”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “• If the fatigue degradation mechanism is active and the material is in a custom material (Material Group10), the fatigue CGR is calculated in accordance with the following equation: m da  ΔK  cstm =C τp cstm   [Eqn.” (p.73, §3.2.1.3).
- 문제: 일치

### [슬라이드 62] 일치 — 확신도(CONFIRMED)
- PPT 문구: “상승 시간 효과와 하중비 효과를 각각 거듭제곱으로 넣은 형태임”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “3-3] dN cstm R ( 1−a R )b cstm    cstm where all variables with the subscript cstm are user-defined custom CGR model parameters. 3.2.1.4 Post-CGR Calculation A number of post-calculation operations are required to compile the outputs of the individual calls to the CGR functions, for example: • The output of the fatigue CGR functions is in terms of crack advancement per fatigue cycle.” (p.73, §3.2.1.3, 식 3-3).
- 추가 확인: 식 3-3: da/dN = C_cstm τ_R^(p_cstm) [ΔK/(1−a_cstm R)^(b_cstm)]^(m_cstm). 상승시간과 하중비가 거듭제곱 형태로 들어감.
- 문제:  일치. 원문 이미지 pages/p074.png(인쇄 p.73)의 식 3-3도 직접 확인함.

### [슬라이드 62] 일치 — 확신도(CONFIRMED)
- PPT 문구: “5개 값은 사용자가 직접 정의함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Custom model scaling constant” (p.77, §3.3, 표 3-3).
- 추가 원문 근거: “Custom model scaling constant Ccstm (m/cyc)s-pcstm(MPa √m)-mcstm ≥ 0 real per heat / per subunit Custom model rise time exponent pcstm - ≥ 0 real -Custom model load ratio constant acstm - ≥ 0 real -Custom model load ratio exponent bcstm - ≥ 0 real -Custom model Paris law exponent mcstm - ≥ 0 real -3.3.1 Physical Inputs” (p.77, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 63]
내용 없음

### [슬라이드 64] 일치 — 확신도(CONFIRMED)
- PPT 문구: “합체 모델은 가까운 균열이 따로 자랄 때보다 빠르게 합쳐지는 현상을, 정밀한 파괴역학 계산 대신 몇 가지 규칙(convention) 으로 모의하는 것임”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “These conventions are a substitute for higher order fracture mechanics calculations that are not amenable to the xLPR probabilistic framework or that were not made a priority for Version 2.0 of xLPR.” (p.92, §4.1).
- 문제: 일치

### [슬라이드 64] 일치 — 확신도(CONFIRMED)
- PPT 문구: “균열간섭 (가까운 균열의 응력장 때문에 균열 앞의 K 가 증폭되어 성장이 빨라짐)”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Crack interaction, whereby stress intensity experienced at crack front locations are amplified due to local stress fields radiating from a nearby crack, resulting in accelerated growth;” (p.92, §4.1).
- 문제: 일치

### [슬라이드 64] 일치 — 확신도(CONFIRMED)
- PPT 문구: “ligament 붕괴 (두 관통균열 사이 재료가 높은 응력으로 완전 소성 파괴됨)”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Ligament collapse, whereby the span of material separating two through-wall cracks experiences high stresses to the point of fully plastic failure.” (p.92, §4.1).
- 문제: 일치

### [슬라이드 64] 일치 — 확신도(CONFIRMED)
- PPT 문구: “이 모델은 이미 성장 중인 공학적으로 의미 있는 큰 균열 (예 : 깊이 1~3mm 이상) 둘이 하나로 합쳐지는 경우만 다루고 , 미세균열 (micro-fissure)이 합쳐지는 초기 단계는 다루지 않음”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Instead, the purpose of the coalescence model is to account for the situation when two adjacent macro-cracks of engineering significance (e.g., 1 to 3 mm or more) that are already growing via a subcritical crack growth regime (i.e., PWSCC or fatigue crack growth) controlled by fracture mechanics (i.e., crack-tip stress intensity factor) are predicted to merge into a single, larger crack of engineering significance.” (p.92, §4.1; p.19 각주 2).
- 추가 원문 근거: “It is emphasized that the coalescence model of Version 2.0 of xLPR is not applicable to model the earlier stages of crack development that often involve coalescence of multiple short cracks (i.e., micro-fissures). Instead, the purpose of the coalescence model is to account for the situation when two adjacent macro-cracks of engineering significance (e.g., 1 to 3 mm or more) that are already growing via a subcritical crack growth regime (i.e., PWSCC or fatigue crack growth) controlled by fracture mechanics (i.e., crack-tip stress intensity factor) are predicted to merge into a single, larger crack of engineering significance. Hence, the distinct research area” (p.92, 위 인용 절의 해당 문단).
- 추가 원문 근거: “As detailed later, the term “cracks of engineering significance” is used to differentiate macro-sized cracks (e.g., 1-3 mm or more in depth) from micro-sized fissures and defects.” (p.19, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 64] 일치 — 확신도(CONFIRMED)
- PPT 문구: “같은 평면의 반 타원 표면균열,천이 관통균열,이상화 관통균열 세 종류에 적용하며 일반적으로 재료와 무관하게 적용할 수 있음”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “The conventions are generally applicable irrespective of material. 4.2.1 Model Form Development This section describes the prediction of imminent coalescence and the prediction of crack shape, size, and location after coalescence.” (p.93, §4.2).
- 추가 원문 근거: “Coalescence modeling conventions are applicable to coplanar macro-cracks of engineering significance characterized as one of the three xLPR crack types: semi-elliptical surface crack, transitioning through-wall crack, or idealized through-wall crack. The conventions are generally applicable irrespective of material.” (p.93, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 64] 오탈자 — 확신도(CONFIRMED)
- PPT 문구: “모든 규칙 (conventions)은 두 균열 사이의 pairwise colescence를 기준으로 함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “All coalescence conventions are based on pairwise coalescence between only two cracks. For rare instances of more than two cracks coalescing at the same time at the same location, pairwise coalescence conventions are applied in series.” (p.93, §4.2.1).
- 문제: 오탈자: colescence → coalescence.
- 최소 교체안: 모든 규칙은 두 균열 사이의 pairwise coalescence를 기준으로 함.

### [슬라이드 64] 일치 — 확신도(CONFIRMED)
- PPT 문구: “세 균열 이상이 같은 곳에서 동시에 합쳐지는 드문 경우에는 pairwise coalescence을 순서대로 적용함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “For rare instances of more than two cracks coalescing at the same time at the same location, pairwise coalescence conventions are applied in series.” (p.93, §4.2.1).
- 문제: 일치

### [슬라이드 64] 일치 — 확신도(CONFIRMED)
- PPT 문구: “규칙이 단순해도 되는 이유로 , 몬테카를로 해석에서는 개별 예측 하나의 중요도가 작다는 점을 듬”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Furthermore, the use of a simple convention-based approach, with overall fidelity with respect to the physical coalescence process, is justified within a Monte Carlo framework, for which a single prediction is of minor importance (due to the many other sources of significant uncertainty). Figure 4-1.” (p.93, §4.2.1).
- 문제: 일치

### [슬라이드 65] 오탈자 — 확신도(CONFIRMED)
- PPT 문구: “Prediction of lmminent Colescence”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Prediction of Imminent Coalescence” (p.93, §4.2.1.1 제목).
- 문제: 오탈자: lmminent의 첫 문자는 소문자 l이 아니라 대문자 I이며, Colescence → Coalescence.
- 최소 교체안: Prediction of Imminent Coalescence

### [슬라이드 65] 일치 — 확신도(CONFIRMED)
- PPT 문구: “이 예측은 두 균열을 가르는 가장 짧은 ID ligament의 길이에 달려있음”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Illustration of Key Terminology for Coalescence Model 4.2.1.1 Prediction of Imminent Coalescence The prediction of coalescence is contingent on the length of the smallest ID ligament (see Figure 4-1) separating two cracks.” (p.93, §4.2.1.1).
- 문제: 일치

### [슬라이드 65] 일치 — 확신도(CONFIRMED)
- PPT 문구: “이 길이가 어떤 값 (coalescence distance, 합체 거리) 보다 작아지면 합체가 임박(imminent) 했다고 하며 , xLPR프레임워크에서는 원래의 두 균열이 합쳐진 균열 하나로 대체됨”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “When this ligament length becomes less than some value—termed the coalescence distance—coalescence is said to be imminent, resulting in the replacement of the two original cracks with a single coalesced crack in the xLPR Framework.” (p.93, §4.2.1.1).
- 문제: 일치

### [슬라이드 65] 일치 — 확신도(CONFIRMED)
- PPT 문구: “ID/OD | 내면/외면 | ID – inner diameter”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “ID Inner Diameter” (p.xiv, §약어 목록(인쇄 p.xiv)).
- 추가 확인: “OD Outer Diameter” (인쇄 p.xiv, 약어 목록).
- 문제: 일치

### [슬라이드 65] 일치 — 확신도(CONFIRMED)
- PPT 문구: “ligament | 두 균열 사이에 남은 재료 | -”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Specifically, coalescence conventions may simulate two distinct modes by which cracks in proximity to one another may combine on a time scale faster than is predicted by treating growth of each crack separately: • Crack interaction, whereby stress intensity experienced at crack front locations are amplified due to local stress fields radiating from a nearby crack, resulting in accelerated growth; • Ligament collapse, whereby the span of material separating two through-wall cracks experiences high stresses to the point of fully plastic failure.” (p.92, §4.1).
- 문제: 일치

### [슬라이드 66] 의미 변경 + 오탈자 — 확신도(CONFIRMED)
- PPT 문구: “균열 간섭(crack interaction)과 ligament collaps는 K 계산 . 성장 . 안정성 예측에서 다루지 않고 (positive) 거리의 합 으로 모의할 수 있음”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “This complex process is not treated in the K-calculation and growth predictions of Version 2.0 of xLPR and instead can be simulated with a positive coalescence distance. Two conventions have been selected to determine the coalescence distance for surface cracks: in the first, the coalescence distance is set to some user-defined value, irrespective of crack sizes; in the second, the coalescence distance is calculated by scaling the maximum crack depth by some user-defined value.” (p.94, §4.2.1.1).
- 문제: 의미 변경 + 오탈자: 원문은 양의 합체거리로 모의한다고 하며 거리들을 더한다고 하지 않는다. collaps → collapse.
- 최소 교체안: 균열간섭과 ligament collapse는 각각 양의 coalescence distance로 모의할 수 있음. 균열간섭은 K·성장 계산에서, ligament collapse는 K·성장·안정성 계산에서 직접 다루지 않음.

### [슬라이드 66] 일치 — 확신도(CONFIRMED)
- PPT 문구: “표면균열 하나와 관통균열 하나의 기본값은 0임”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “For the crack pair made up of one surface crack and one through-wall crack, the coalescence distance is set to zero by default. This crack arrangement has no known ASME Code considerations (as for two surface cracks) and no true ligament formation (as for two through-wall cracks).” (p.94, §4.2.1.1).
- 문제: 일치

### [슬라이드 66] 일치 — 확신도(CONFIRMED)
- PPT 문구: “균열 유형마다 근거가 달라서 3가지로 나눠서 사용”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “For two through-wall cracks, the common physical driver of coalescence is ligament collapse, whereby the span of material separating the cracks experiences high stresses to the point of fully plastic failure.” (p.94, §4.2.1.1).
- 추가 원문 근거: “Two conventions have been selected to determine the coalescence distance for surface cracks: in the first, the coalescence distance is set to some user-defined value, irrespective of crack sizes; in the second, the coalescence distance is calculated by scaling the maximum crack depth by some user-defined value. The second convention is recommended to approximate the known dependency between crack interaction and crack depth [49].34 Furthermore, this convention is consistent with ASME Boiler and Pressure Vessel Code Section XI IWA-3000, which requires cracks separated by less than half of the maximum depth to be combined prior to stability assessment. Provided the second modeling convention, the best-fit scaling factor is half (0.5) of the maximum depth of the cracks involved in coalescence. For two through-wall cracks, the common physical driver of coalescence is ligament collapse, whereby the span of material separating the cracks experiences high stresses to the point of fully plastic failure. These complex processes are not treated in the K-calculation, growth, or stability predictions of Version 2.0 of xLPR and instead can be simulated with a positive coalescence distance. The coalescence distance in this case is set to a user-defined value. In actuality, this distance may systematically depend on crack length; however, this dependency is not implemented in the coalescence module for xLPR Version 2.0. Through-wall crack coalescence distances between 0 and 20 inches are possible for components of interest in xLPR, depending on the sizes of the flaws involved. For the crack pair made up of one surface crack and one through-wall crack, the coalescence distance is set to zero by default.” (p.94, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 66] 일치 — 확신도(CONFIRMED)
- PPT 문구: “표와 같이 균열의 종류에 따라 정함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “For the crack pair made up of one surface crack and one through-wall crack, the coalescence distance is set to zero by default.” (p.94, §4.2.1.1).
- 문제: 일치

### [슬라이드 66] 한정어 누락 — 확신도(CONFIRMED)
- PPT 문구: “거리기준 불확실성은 분포로 주는것을 권장함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Uncertainty in the coalescence prediction may be incorporated through the use of distributed” (p.98, §4.2.2).
- 문제: 한정어 누락: 원문은 불확실성을 분포된 거리로 반영할 수 있다고 한다(may). 이 첫 문장의 권고로의 강화는 원문 표현과 다름. 개별 분포의 권고는 뒤에서 별도로 제시됨.
- 최소 교체안: 합체 예측 불확실성은 분포된 합체거리를 사용해 반영할 수 있음.

### [슬라이드 66] 일치 — 확신도(CONFIRMED)
- PPT 문구: “더 정밀한 모델이 있으면 줄일 수 있으므로 epistemic으로 분류 권장함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “It is recommended that these uncertainties be designated as epistemic given that more detailed models would be expected to result in more precise estimates.” (p.98, §4.2.2).
- 문제: 일치

### [슬라이드 66] 일치 — 확신도(CONFIRMED)
- PPT 문구: “관통균열 합체 거리가 균열 길이에 따라 달라 질 수는 있지만 이 경우는 구현하지 않음(p.94)”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “In actuality, this distance may systematically depend on crack length; however, this dependency is not implemented in the coalescence module for xLPR Version 2.0. Through-wall crack coalescence distances between 0 and 20 inches are possible for components of interest in xLPR, depending on the sizes of the flaws involved.” (p.94, §4.2.1.1).
- 문제: 일치

### [슬라이드 67] 조건 누락 — 확신도(CONFIRMED)
- PPT 문구: “표면 + 표면 | 두 convention, 최적 계수 0.5, ASME IWA-3000 | p.94”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Provided the second modeling convention, the best-fit scaling factor is half (0.5) of the maximum depth of the cracks involved in coalescence.” (p.94, §4.2.1.1).
- 문제: 조건 누락: 0.5는 최대 깊이에 비례시키는 두 번째 규칙의 계수이다. 첫 번째는 사용자 지정 절대거리이므로 두 규칙에 공통인 계수로 적으면 안 됨.
- 최소 교체안: 두 convention: 사용자 지정 절대거리 / 최대 깊이×계수(권장). 두 번째 규칙의 best-fit 계수 0.5; ASME Section XI IWA-3000과 일관됨(p.94).

### [슬라이드 67] 일치 — 확신도(CONFIRMED)
- PPT 문구: “표면+표면(불확실성) | 비는 0~약 0.75, 삼각분포 0.0 / 0.5 / 0.75 | p.98”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “In the absence of more detailed investigation, a triangular distribution is recommended with extremes at 0.0 and 0.75 and a mode at 0.5. The coalescence distance for through-wall cracks should be roughly consistent with the lengths of cracks at the time at which coalescence is simulated.” (p.98, §4.2.2).
- 문제: 일치

### [슬라이드 67] 조건 누락 — 확신도(CONFIRMED)
- PPT 문구: “관통+관통 | ligament collapse, 사용자 지정 값, 0~20 in | p.94”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Through-wall crack coalescence distances between 0 and 20 inches are possible for components of interest in xLPR, depending on the sizes of the flaws involved. For the crack pair made up of one surface crack and one through-wall crack, the coalescence distance is set to zero by default.” (p.94, §4.2.1.1).
- 추가 원문 근거: “Through-wall crack coalescence distances between 0 and 20 inches are possible for components of interest in xLPR, depending on the sizes of the flaws involved.” (p.94, 위 인용 절의 해당 문단).
- 문제: 조건 누락: 0~20 in은 해당 부품에서 결함 크기에 따라 가능한 거리라고 설명한다. 무조건적인 사용자 입력 허용범위가 아님.
- 최소 교체안: ligament collapse 모의; 사용자 지정 거리. 대상 부품에서는 결함 크기에 따라 0~20 in의 거리가 가능(p.94).

### [슬라이드 67] 일치 — 확신도(CONFIRMED)
- PPT 문구: “관통 + 관통 (길이관계) | 길이와 대략 1:1 | p.98”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “This reflects analytical findings (after the time of model development) that the coalescence distance has a roughly one-to-one relationship with crack length [51].35 The other coalescence modeling conventions are fully deterministic.” (p.98, §4.2.2).
- 문제: 일치

### [슬라이드 67] 일치 — 확신도(CONFIRMED)
- PPT 문구: “표면+관통 / | 기본값 0 | p.94”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “For the crack pair made up of one surface crack and one through-wall crack, the coalescence distance is set to zero by default. This crack arrangement has no known ASME Code considerations (as for two surface cracks) and no true ligament formation (as for two through-wall cracks).” (p.94, §4.2.1.1).
- 문제: 일치

### [슬라이드 68] 일치 — 확신도(CONFIRMED)
- PPT 문구: “균열 유형 규칙은 xLPR 2.0이 인식하는 세 균열 유형의 제약 아래 물리적 기대와 논리적 고려에 따라 개발됨 (p.94)”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “These transitioning rules were developed based on physical expectations and logical considerations when constrained to the three crack types recognized within the Version 2.0 xLPR Framework.” (p.94, §4.2.1.2).
- 추가 원문 근거: “These transitioning rules were developed based on physical expectations and logical considerations when constrained to the three crack types recognized within the Version 2.0 xLPR Framework.” (p.94, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 68] 일치 — 확신도(CONFIRMED)
- PPT 문구: “표의 규칙으로 합친 균열의 속성을 정함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “The crack resulting from the coalescence of two original cracks requires updated geometrical attributes including type, depth, length, and location.” (p.94, §4.2.1.2).
- 문제: 일치

### [슬라이드 68] 일치 — 확신도(CONFIRMED)
- PPT 문구: “두 균열의 ID 길이를 감싸는 호의 중심이 새 균열의 중심임”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “The center of the new crack is set to the center of the arc that circumscribes the ID lengths of the” (p.95, §4.2.1.2).
- 문제: 일치

### [슬라이드 68] 의미 변경 — 확신도(CONFIRMED)
- PPT 문구: “표면 + 관통 두개의 ID 길이는 합친 균열의 면적이 원래 두 균열 면적의 합과 같아지도록 정하며  이는 합체 전후의 안정성 예측이 이어지게 하려는것임”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “For the coalescence of one through-wall crack and one surface crack, the ID length is set such that the area of the coalesced crack is equivalent to the sum of the areas of the original two cracks. This promotes continuity of the component stability prediction immediately before and after coalescence.” (p.95, §4.2.1.2).
- 문제: 의미 변경: 정하는 대상은 원래 두 균열 각각의 ID 길이가 아니라 합체 후 새 균열 하나의 ID 길이임.
- 최소 교체안: 표면+관통 합체 후 새 균열의 ID 길이는 새 균열 면적이 원래 두 균열 면적의 합과 같도록 정함. 이는 합체 직전·직후 안정성 예측의 연속성을 촉진함.

### [슬라이드 68] 오탈자 — 확신도(CONFIRMED)
- PPT 문구: “OD 길이 규칙이 물리적 기대와 일치하며 하용할 만한 누설 연속성을 가져올것이라고 설명함 (p.95)”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “This convention is consistent with physical expectations and should result in acceptable leakage continuity immediately before and after coalescence.” (p.95, §4.2.1.2).
- 추가 원문 근거: “This convention is consistent with physical expectations and should result in acceptable leakage continuity immediately before and after coalescence.” (p.95, 위 인용 절의 해당 문단).
- 문제: 오탈자: 하용할 → 허용할. ‘가져올 것’은 should result in의 기대 표현에 대응함.
- 최소 교체안: OD 길이 규칙은 물리적 기대와 일치하며 합체 직전·직후 허용할 만한 누설 연속성을 가져올 것으로 설명함(p.95).

### [슬라이드 68] 일치 — 확신도(CONFIRMED)
- PPT 문구: “표면 + 표면 상황 에서는 두 균열 사이 재진입 구간 (re-entrant sector)의 K가 합쳐진 균열이 대략 대칭의 형태를 되찾을 때까지 증폭된다는 물리적 기대에서, 최대 깊이를 권장함 (p.95)”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “However, from these selected options, the maximum depth is recommended based on the physical expectation that stress intensity factors in the “re-entrant sector” between the two original cracks will be amplified from the time crack interaction becomes significant until the coalesced crack regains a roughly symmetric shape (e.g., see Figure 4-4 from laboratories studies presented in Reference [49]).” (p.95, §4.2.1.2).
- 추가 원문 근거: “the maximum depth is recommended based on the physical expectation that stress intensity factors in the “re-entrant sector” between the two original cracks will be amplified from the time crack interaction becomes significant until the coalesced crack regains a roughly symmetric shape” (p.95, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 69] 일치 — 확신도(CONFIRMED)
- PPT 문구: “유형 | 표면+표면→ 표면 . 천이+천이→천이 . 이상화 관통 + 이상화 관통 → 이상화 관통  / 종류가 다르면 → 천이관통”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Regarding crack type after coalescence, two surface cracks form a surface crack; two transitioning cracks form a transitioning crack; two idealized through-wall cracks form an idealized through-wall crack; and the combination of cracks with dissimilar type results in a transitioning crack.” (p.94, §4.2.1.2).
- 추가 원문 근거: “Regarding crack type after coalescence, two surface cracks form a surface crack; two transitioning cracks form a transitioning crack; two idealized through-wall cracks form an idealized through-wall crack; and the combination of cracks with dissimilar type results in a transitioning crack.” (p.94, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 69] 일치 — 확신도(CONFIRMED)
- PPT 문구: “깊이 | 관통균열이 하나라도 있으면 부품 두께 . 표면 +표면은 최소 . 최대 . 평균 중 선택   / 최대 깊이 권장”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “However, from these selected options, the maximum depth is recommended based on the physical expectation that stress intensity factors in the “re-entrant sector” between the two original cracks will be amplified from the time crack interaction becomes significant until the coalesced crack regains a roughly symmetric shape (e.g., see Figure 4-4 from laboratories studies presented in Reference [49]).” (p.95, §4.2.1.2).
- 추가 원문 근거: “Consistent with physical expectations, the depth of the new crack is the component thickness for instances of coalescence involving one or more through-wall cracks. A number of options were selected for the depth of the coalesced crack resulting from two surface cracks: the minimum, maximum, or average depth of the original two cracks. These different options may be used to understand xLPR prediction sensitivity to the coalescence depth modeling convention. However, from these selected options, the maximum depth is recommended” (p.95, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 69] 일치 — 확신도(CONFIRMED)
- PPT 문구: “중심 | 두 균열의 ID 길이를 감싸는 호의 중심”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “The center of the new crack is set to the center of the arc that circumscribes the ID lengths of the original cracks.” (p.95, §4.2.1.2).
- 문제: 일치

### [슬라이드 69] 일치 — 확신도(CONFIRMED)
- PPT 문구: “OD길이 | 두 균열의 OD길이를 감싸는 호의 길이  / 표면 + 표면 이면 0  / 표면 + 관통이면 그 관통균열의 OD 길이”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “For two surface cracks, this length is zero. For one surface crack and one through-wall crack, this length is the OD length of the original through-wall crack.” (p.95, §4.2.1.2).
- 추가 원문 근거: “The OD length of the new crack is set to the length of the arc that circumscribes the OD lengths of the original cracks. For two surface cracks, this length is zero. For one surface crack and one through-wall crack, this length is the OD length of the original through-wall crack.” (p.95, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 69] 일치 — 확신도(CONFIRMED)
- PPT 문구: “ID길이 | 표면 + 표면 , 또는 관통 + 관통은 ID 길이를 감싸는 호의 길이  / 표면+관통은 합친 균열의 면적이 원래 두 균열 면적의 합과 같도록 설정”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “area of the coalesced crack is equivalent to the sum of the areas of the original two cracks.” (p.95, §4.2.1.2).
- 추가 원문 근거: “For two surface cracks or two through-wall cracks, the ID length of the new crack is set to the length of the arc that circumscribes the ID lengths of the original cracks. This is physically consistent with the simulated modes of coalescence and is believed to be logical when constrained to the three crack types recognized within the Version 2.0 xLPR Framework. For the coalescence of one through-wall crack and one surface crack, the ID length is set such that the area of the coalesced crack is equivalent to the sum of the areas of the original two cracks. This promotes continuity of the component stability prediction immediately before and after coalescence.” (p.95, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 70] 의미 변경 — 확신도(CONFIRMED)
- PPT 문구: “분포된 합체거리 |   coalescence prediction 의 불확실성은 분포된 coalescence distance(distributed coalescence distances) 를 사용해 반영할 수 있음  / 이 불확실성은 coalescence 로 이어지는 복잡한 과정의 변동성과 모델 오차 (예 – 균열 길이에 대한 체계적의존성의 부재) 를 반영할 수 없음  / 더 상세한 모델이 더 정밀한 추론을 내놓을 수 있으므로 이 불확실성들은 epistemic 으로 지정할 것이 권장됨  | p.98”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “This uncertainty may reflect variability in the complex processes that lead to coalescence as well as model error (e.g., the lack of a systematic dependency with respect to crack length).” (p.98, §4.2.2).
- 추가 원문 근거: “Uncertainty in the coalescence prediction may be incorporated through the use of distributed coalescence distances. This uncertainty may reflect variability in the complex processes that lead to coalescence as well as model error (e.g., the lack of a systematic dependency with respect to crack length). It is recommended that these uncertainties be designated as epistemic given that more detailed models would be expected to result in more precise estimates.” (p.98, 위 인용 절의 해당 문단).
- 문제: 의미 변경: ‘반영할 수 없음’은 원문의 may reflect와 정반대임. 나머지 분포거리 도입 및 epistemic 권고는 일치.
- 최소 교체안: 이 불확실성은 합체로 이어지는 복잡한 과정의 변동성과 모델 오차(예: 균열 길이에 대한 체계적 의존성의 부재)를 반영할 수 있음.

### [슬라이드 70] 일치 — 확신도(CONFIRMED)
- PPT 문구: “표면균열 | 균열 상호작용 거리와 두 균열의 최대 깊이의 비는 0 에서 약 0.75 사이이고 best-estimate는 0.5 임 / 더 상세한 값이 없으면 0.0과0.75 최빈값 0.5인 삼각분포를 권장함  | p.98”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “For surface cracks, the ratio of the crack interaction distance (i.e., coalescence distance) to the maximum depth of the two cracks is between zero (i.e., no crack interaction) and roughly 0.75, with a best-estimate of 0.5. In the absence of more detailed investigation, a triangular distribution is recommended with extremes at 0.0 and 0.75 and a mode at 0.5.” (p.98, §4.2.2).
- 추가 원문 근거: “For surface cracks, the ratio of the crack interaction distance (i.e., coalescence distance) to the maximum depth of the two cracks is between zero (i.e., no crack interaction) and roughly 0.75, with a best-estimate of 0.5. In the absence of more detailed investigation, a triangular distribution is recommended with extremes at 0.0 and 0.75 and a mode at 0.5.” (p.98, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 70] 일치 — 확신도(CONFIRMED)
- PPT 문구: “관통균열 | 합체 거리는 합체를 모의하는 시점의 균열 길이와 대체로 일치해야 함 , 모델 개발 이후의 해석결과 , 합체 거리와 균열 길이가 대략 1:1임  / 관통균열의 합체 거리를 개별 프로그램 실행에서는 deterministic 으로 가정하고 xLPR 예측에 대한 영향을 이해하기 위한 민감도 연구에서 바꿀 수 있음  | p.98”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Alternatively, the coalescence distance for through-wall cracks may be assumed to be deterministic for” (p.98, §4.2.2 및 각주 35).
- 추가 원문 근거: “The coalescence distance for through-wall cracks should be roughly consistent with the lengths of cracks at the time at which coalescence is simulated. This reflects analytical findings (after the time of model development) that the coalescence distance has a roughly one-to-one relationship with crack length” (p.98, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 70] 의미 변경 — 확신도(CONFIRMED)
- PPT 문구: “convention | 완전히 결정적 (fully deterministic) 임  / 합체하는 균열마다 type,location,depth,ID length, / OD length convention 은 논리에 뿌리를 두고 있어 큰 불확실성이 있다고 보지 않음  / 표면균열에 원래 균열의 최대 깊이를 쓰는 convention은 물리적 기대에 근거하며 , 개별 프로그램 실행에서 바꿔 xLPR 예측에 대한 영향을 이해할 수 있음   | p.98~99”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “The modeling conventions for type, location, ID length, and OD length are logically rooted and are therefore not considered subject to significant uncertainties.” (p.98, §4.2.2; p.99 계속).
- 추가 원문 근거: “The other coalescence modeling conventions are fully deterministic. That is, for any given pair of cracks undergoing coalescence, the type, location, depth, ID length, and OD length of the resulting crack is fully determined. The modeling conventions for type, location, ID length, and OD length are logically rooted and are therefore not considered subject to significant uncertainties.” (p.98, 위 인용 절의 해당 문단).
- 추가 원문 근거: “of surface cracks is based on physical expectation; this convention may be varied for individual program runs to understand its influence on xLPR predictions.” (p.99, 위 인용 절의 해당 문단).
- 문제: 의미 변경: 원문에서 큰 불확실성에 해당하지 않는다고 열거한 것은 type/location/ID length/OD length이며 depth는 제외됨. 깊이는 다음 문장에서 별도의 물리적 기대와 민감도 대상으로 설명함.
- 최소 교체안: 다른 규칙은 주어진 균열 쌍과 선택한 규칙에 대해 결정적임. type, location, ID length, OD length 규칙은 논리에 근거해 큰 불확실성이 있다고 보지 않음. 최대 깊이 규칙은 물리적 기대에 근거하며 실행별로 바꾸어 영향을 살필 수 있음(p.98~99).

### [슬라이드 71] 오탈자 — 확신도(CONFIRMED)
- PPT 문구: “개요  | 합체 모델링 conventio은  / -논리적 물리적 기대를 반영하고 / -더 발전된 해석 . 실험 결과를 수용할 수 있도록 유연하게 개발됨  / 발표된 연구를 적용해 conventio은 대체로 검증(generally validated) 되었음 | p.99”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Through application of published research, the coalescence modeling conventions were generally validated. For instance, Bezensek et al.” (p.99, §4.2.3).
- 문제: 오탈자: conventio → convention(복수 맥락에서는 conventions). 대체로 검증되었다는 한정어는 보존되어 있음.
- 최소 교체안: 합체 모델링 conventions은 논리적·물리적 기대를 반영하고 발전된 연구 결과를 수용하도록 개발되었으며, 발표된 연구를 통해 대체로 검증됨.

### [슬라이드 71] 일치 — 확신도(CONFIRMED)
- PPT 문구: “표면균열의 K 증대  | 표면균열의 응력확대계수 증대 (intensification) 가 시작되는 시점은 균열 깊이의 일부인 합체거리로 잘예측된다는 실험 증거가 있으며 , 선택한 modeling convention 을 검증함 | p.99”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Experimental evidence suggests that the onset of the intensification of stress intensity factor” (p.99, §4.2.3).
- 추가 원문 근거: “Experimental evidence suggests that the onset of the intensification of stress intensity factor for surface cracks is well-predicted using a coalescence distance that is some fraction— e.g., somewhere between 0.0 and 0.75—of crack depth, validating the selected modeling convention.” (p.99, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 71] 오탈자 — 확신도(CONFIRMED)
- PPT 문구: “관통균열의 양  / (positive) 의 합체거리  | 상위수준 모델링은 두 균열 사이 ligament 가 균열 길이보다 짧아질 때 까지는 ligament 붕괴로 이어지는 급속한 찢김 (rapid tearing) 의 가능성이 낮다고 사사함  / 이는 관통균열에 어떤 양의 합체거리를 쓰는 것을 뒷받침 하지만 , 길이 의존성을 반영하는 더 상세한 관통균열 합체 모델링의 구현이 필요하다는 결과임  | p.99”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Higher order modeling suggests low likelihood of rapid tearing leading to ligament collapse” (p.99, §4.2.3).
- 추가 원문 근거: “Higher order modeling suggests low likelihood of rapid tearing leading to ligament collapse until the ligament between two cracks is less than the length of the cracks. This supports the use of some positive coalescence distance for through-wall cracks36. However, this finding beckons the implementation of more detailed coalescence modeling for through-wall cracks to account for length-dependency.” (p.99, 위 인용 절의 해당 문단).
- 문제: 오탈자: 사사함 → 시사함. low likelihood 및 길이 의존성 개선 필요는 일치.
- 최소 교체안: 상위 수준 모델링은 ligament가 균열 길이보다 짧아질 때까지 급속한 찢김 가능성이 낮다고 시사함.

### [슬라이드 72] 일치 — 확신도(CONFIRMED)
- PPT 문구: “두 표면균열의 최대 깊이 (convention) | 두 합체 균열의 교차 지점에서 해당 영역의 높은 응력확대계수 때문에 re-entrant sector가 경계 균열 형상에 도달할 때까지 빠르게 성장하는 것이 뒷받침됨  / 이 급속한 성장은 상위 수준 해석 모델링이 예측하고 실험에서 관찰됨 | p.99”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “This rapid growth is predicted with higher order analytical modeling and has been observed experimentally.” (p.99, §4.2.3).
- 추가 원문 근거: “The maximum depth convention for a crack resulting from two surface cracks is supported by the rapid growth of the “re-entrant sector” at the intersection of the two coalescing cracks due to elevated stress intensity factors in that region until the bounding crack shape is obtained. This rapid growth is predicted with higher order analytical modeling and has been observed experimentally.” (p.99, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 72] 일치 — 확신도(CONFIRMED)
- PPT 문구: “합체 후 균열 유형  | transitioning rules라고 부름, 실험 결과와 상위 수준 모델링으로 대체로 검증됨 / 표면균열과 관통균열의 합체를 다룬 실험 데이터는 없지만, transitioning through-wall crack 형상으로 천이하는 convention이 xLPR Version 2.0의 세 균열 유형 중 가장 적절하다고 보임 | p.99”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “there is not experimental data involving the coalescence of a surface crack and a through-wall” (p.99, §4.2.3 및 각주 37).
- 추가 원문 근거: “While there is not experimental data involving the coalescence of a surface crack and a through-wall crack, the established convention to transition to a transitioning through-wall crack shape is considered the most appropriate given the three crack type options in xLPR Version 2.0.” (p.99, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 72] 의미 변경 — 확신도(CONFIRMED)
- PPT 문구: “적용 범위  | 실험 결과와 상위 수준 모델링으로 대체로 검증됨 | p.99”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “This module validation applies for the full range of crack and component geometries expected within xLPR Version 2.0.” (p.99, §4.2.3).
- 추가 원문 근거: “The convention for establishing location, ID length, and OD length of the coalesced crack is generally validated with experimental results and higher order modeling.” (p.99, 위 인용 절의 해당 문단).
- 문제: 의미 변경: ‘적용 범위’ 행의 본문은 범위를 제시하지 않는다. 같은 쪽의 별도 검증 문장을 가져오면서 검증 대상인 location/ID length/OD length도 빠뜨림.
- 최소 교체안: 적용 범위: 이 모듈 검증은 xLPR Version 2.0에서 예상되는 균열·부품 형상의 전체 범위에 적용됨(p.99). 위치·ID 길이·OD 길이 규칙의 대체적 검증은 별도 행으로 표기.

### [슬라이드 73] 일치 — 확신도(CONFIRMED)
- PPT 문구: “가장 중요한 단순화는 합체를 역학적·현상학적으로 모델링하는 대신 단순화된 convention 기반 모델링을 쓰는 것임”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “use of simplified convention-based modeling in lieu of mechanistic or phenomenological modeling of coalescence (e.g., modeling derived from fracture mechanics or first principles).” (p.100, §4.3, Convention-based modeling).
- 문제: 일치

### [슬라이드 73] 일치 — 확신도(CONFIRMED)
- PPT 문구: “목표는 물리적 합체를 평균적이고 물리적으로 타당한 의미에서 근사하는 것이며, 상위 수준 해석 모델링과 실험 조사가 이 convention을 검증함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “The goal of the convention-based modeling is to approximate physical coalescence in an average and physically viable sense; and, indeed, higher order analytical modeling and experimental investigations validate the modeling conventions (e.g., see sections above).” (p.100, §4.3).
- 문제: 일치

### [슬라이드 73] 오탈자 — 확신도(CONFIRMED)
- PPT 문구: “이런 모델링은 개별 결정론적 모의 한 번의 결과가 주된 의미를 갖지 않는 확률론적 방법과 함께 흔히 쓰이는 모델은 이 단순화에 대한 민감도를 볼 수 있도록 여러 합체 규칙(conventions)을 포함함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “This type of modeling is often used in association with probabilistic methods where the result of any single deterministic simulation is not of primary significance. The model includes a range of different conventions, or rules, for coalescence so that the sensitivity to these simplifications can be explored.” (p.100, §4.3).
- 문제: 오탈자: ‘함께 흔히 쓰이는 모델은’에서 두 문장이 잘못 연결되어 확률론적 방법과 규칙 선택 설명의 관계가 흐려짐.
- 최소 교체안: 이런 모델링은 개별 결정론적 모의 결과가 주된 의미를 갖지 않는 확률론적 방법과 함께 흔히 쓰임. 모델은 단순화에 대한 민감도를 살필 수 있도록 여러 합체 규칙을 포함함.

### [슬라이드 73] 오탈자 — 확신도(CONFIRMED)
- PPT 문구: “균열을 반타원 표면균열, 이상화 관통균열(라디안 기준 ID·OD 길이가 같음), 천이 관통균열 중 하나로 이상화함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “• Crack shape idealization: As described earlier, cracks are idealized as one of three crack types: semi-elliptical surface cracks, idealized through-wall cracks (same ID and OD length in terms of radians), or transitioning through-wall cracks.” (p.100, §4.3, Crack shape idealization).
- 추가 원문 근거: “Crack shape idealization: As described earlier, cracks are idealized as one of three crack types: semi-elliptical surface cracks, idealized through-wall cracks (same ID and OD length in terms of radians), or transitioning through-wall cracks.” (p.100, 위 인용 절의 해당 문단).
- 문제: 오탈자: 이 문단 위 두 번째 소제목이 Convention-based modeling으로 중복되어 원문 소제목과 다름. 문단의 세 유형 설명은 일치.
- 최소 교체안: 두 번째 Convention-based modeling 소제목을 Crack shape idealization으로 교체.

### [슬라이드 73] 일치 — 확신도(CONFIRMED)
- PPT 문구: “이는 응력확대계수·균열열림변위 계산 같은 해석 모델의 개발을 다루기 쉽게 하려는 xLPR 전체의 근사(Version 2)임”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “This is an xLPR-wide approximation for Version 2 used to allow tractable development of analytical models, e.g., for stress intensity factor calculation, crack opening displacement calculation, etc.” (p.100, §4.3).
- 문제: 일치

### [슬라이드 73] 일치 — 확신도(CONFIRMED)
- PPT 문구: “실제 PWSCC·피로 균열은 여러 규모에서 공간적으로 변하는 복잡한 형상이지만, 매개변수를 적절히 고르면 복잡한 균열 형상에 합체 모듈을 적용해도 관찰된 합체까지의 시간과 합체 이후의 깊이·길이에 대해 합리적인 결과를 줄 것으로 믿음”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Despite the simplified crack shapes required, applying the coalescence module to make predictions for complex crack geometries is believed to yield reasonable results for observed time to coalescence and observed depth / length subsequent to coalescence, provided parameters are selected appropriately. • Coplanar crack assumption: All circumferential cracks are assumed to be coplanar within the xLPR Version 2.0 framework.” (p.100, §4.3).
- 추가 원문 근거: “In reality, of course, PWSCC and fatigue cracks possess complex geometries with spatial variation on multiple different scales. Despite the simplified crack shapes required, applying the coalescence module to make predictions for complex crack geometries is believed to yield reasonable results for observed time to coalescence and observed depth / length subsequent to coalescence, provided parameters are selected appropriately.” (p.100, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 73] 일치 — 확신도(CONFIRMED)
- PPT 문구: “xLPR Version 2.0 프레임워크에서 모든 원주방향 균열은 같은 평면(coplanar)이라고 가정함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “• Coplanar crack assumption: All circumferential cracks are assumed to be coplanar within the xLPR Version 2.0 framework.” (p.100, §4.3, Coplanar crack assumption).
- 문제: 일치

### [슬라이드 73] 일치 — 확신도(CONFIRMED)
- PPT 문구: “실제로는 축방향으로 어긋나 독립적으로 남을 수 있는 균열이 합쳐진다는 뜻”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “This means that circumferential cracks that more realistically might remain offset axially and independent are combined. The conservatism of this approach varies depending on the crack configuration (e.g., see Figure 4-5).” (p.100, §4.3).
- 문제: 일치

### [슬라이드 73] 일치 — 확신도(CONFIRMED)
- PPT 문구: “보수성은 균열 배치에 따라 다릅니다(Figure 4-5). 원주방향 겹침이 거의 없는 경우(Configuration A)에는 축방향으로 어긋난 두 균열 대신 큰 균열 하나가 생겨 누설 확률은 다소, 누설률은 크게, 파단 감수성은 축방향 어긋남 정도에 따라 크게 증가”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “This would increase probability of leakage somewhat, increase leakage rates significantly, and increase susceptibility to rupture significantly depending on the degree of axial offset.” (p.100, §4.3).
- 추가 원문 근거: “The conservatism of this approach varies depending on the crack configuration (e.g., see Figure 4-5). For cracks with little to no circumferential overlap (Configuration A in Figure 4-5), this assumption will lead to a single large crack at the expense of two axially offset cracks. This would increase probability of leakage somewhat, increase leakage rates significantly, and increase susceptibility to rupture significantly depending on the degree of axial offset.” (p.100, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 73] 일치 — 확신도(CONFIRMED)
- PPT 문구: “겹침이 큰 경우(Configuration B)에는 두 균열 중 하나가 더 빨리 자랄 수 있어 누설 확률은 약간 줄고 누설률은 약 절반, 파단 감수성은 다소 줄어드는 경향입니다. 더 엄밀한 정량화에는 추가 해석이 필요합니다.”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “For cracks with substantial circumferential overlap (Configuration B in Figure 4-5), this assumption would tend to result in a slightly reduced probability of leakage as one of two cracks may grow more quickly than the other, decrease leakage rates by approximately one half, and decrease susceptibility to rupture somewhat.” (p.100, §4.3).
- 추가 원문 근거: “For cracks with substantial circumferential overlap (Configuration B in Figure 4-5), this assumption would tend to result in a slightly reduced probability of leakage as one of two cracks may grow more quickly than the other, decrease leakage rates by approximately one half, and decrease susceptibility to rupture somewhat. Further analysis would be required to quantify the effects of the coplanar assumption more rigorously.” (p.100, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 74] 일치 — 확신도(CONFIRMED)
- PPT 문구: “합체 규칙을 적용할 때 축방향 균열은 무시함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Example of Configurations Illustrating Impact of Coplanar Crack Assumption • Neglecting interaction between axial and circumferential cracks: Axial cracks are neglected when applying coalescence rules. In reality, the intersection of perpendicular cracks may result in crack blunting that arrests one of the cracks.” (p.101, §4.3).
- 문제: 일치

### [슬라이드 74] 일치 — 확신도(CONFIRMED)
- PPT 문구: “실제로는 수직 균열이 교차하면 균열 무딤(blunting)으로 한쪽이 정지할 수 있으므로, 이는 누설 확률과 안정성에 대해 보수적인 가정임”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “In reality, the intersection of perpendicular cracks may result in crack blunting that arrests one of the cracks. Therefore, this is a conservative assumption relative to probability of leakage and stability.” (p.101, §4.3).
- 문제: 일치

### [슬라이드 74] 일치 — 확신도(CONFIRMED)
- PPT 문구: “같은 평면의 축방향 균열은 Version 2.0에서 모델링하지 않으며, 부품의 원주방향 이산화 구간마다 공학적 의미가 있는 축방향 균열은 최대 하나로 모델링함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Coplanar axial cracks are not modeled in Version 2.0 of xLPR. A maximum of one axial crack of engineering significance is modeled at each circumferential discretization of the component.” (p.101, §4.3).
- 문제: 일치

### [슬라이드 74] 일치 — 확신도(CONFIRMED)
- PPT 문구: “이종 용접 모델링에서는 용접 잔류응력이 비교적 좁은 축방향 범위에서 최대가 되어 그곳에서 균열 발생이 가장 가능성 높다는 기대와 일치”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “For dissimilar weld modeling, this is consistent with the expectation that weld residual stresses will peak (and therefore initiation will be most likely) over a relatively narrow axial extent.” (p.101, §4.3).
- 문제: 일치

### [슬라이드 74] 일치 — 확신도(CONFIRMED)
- PPT 문구: “상위 수준 해석 예측은 합체 거리가 균열 길이와 부품 두께에 민감할 수 있다고 시사함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Higher order analytical predictions suggest that coalescence distance may be sensitive to crack length and component thickness, especially for coalescence of very large cracks where the ligament stress between the cracks is substantially elevated relative to the intact condition.” (p.101, §4.3).
- 문제: 일치

### [슬라이드 74] 일치 — 확신도(CONFIRMED)
- PPT 문구: “특히 균열 사이 ligament 응력이 온전한 상태보다 크게 높아진 아주 큰 균열의 합체에서 그렇게 나타남”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “• Neglecting systematic variation in coalescence distance: Higher order analytical predictions suggest that coalescence distance may be sensitive to crack length and component thickness, especially for coalescence of very large cracks where the ligament stress between the cracks is substantially elevated relative to the intact condition.” (p.101, §4.3).
- 문제: 일치

### [슬라이드 74] 일치 — 확신도(CONFIRMED)
- PPT 문구: “이 체계적 변화는 합체 모델에서 다루지 않으며, 그 결과 짧은 균열은 대체로 이르게, 긴 균열은 대체로 늦게 합쳐질 것으로 예상됩니다. 이 편향의 전체적인 보수성은 합체 거리 입력의 선택에 달려 있고 xLPR 프레임워크 안에서 민감도 연구로 살펴볼 수 있음”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “This is expected to result in generally early coalescence for short-length cracks and generally late coalescence for long-length cracks.” (p.101, §4.3).
- 추가 원문 근거: “This systematic variation is not addressed in the coalescence model. This is expected to result in generally early coalescence for short-length cracks and generally late coalescence for long-length cracks. The overall conservatism of these biases depends on the selection of the coalescence distance inputs and may be studied with sensitivity studies performed within the xLPR framework.” (p.101, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 74] 일치 — 확신도(CONFIRMED)
- PPT 문구: “사용 가능한 검증 데이터는 모두 평판(flat plate) 형상의 균열 합체에 대한 것임”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “• Extension of coalescence validation to annular geometries: All validation data available concern coalescence of cracks in flat plate geometries. In many applicable components, the characteristic length of ID curvature is much longer than typical crack lengths and therefore the extension of flat plate data is reasonable.” (p.101, §4.3).
- 문제: 일치

### [슬라이드 74] 일치 — 확신도(CONFIRMED)
- PPT 문구: “적용 대상 부품 다수에서 ID 곡률의 특성 길이가 일반적인 균열 길이보다 훨씬 길어 평판 데이터의 확장은 합리적임”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “In many applicable components, the characteristic length of ID curvature is much longer than typical crack lengths and therefore the extension of flat plate data is reasonable. For smaller radius components, such as pressurizer nozzles, or for particularly large cracks, the ID curvature may affect crack interaction and susceptibility to ligament collapse.” (p.101, §4.3).
- 문제: 일치

### [슬라이드 74] 일치 — 확신도(CONFIRMED)
- PPT 문구: “pressurizer nozzle 같은 작은 반경 부품이나 특히 큰 균열에서는 ID 곡률이 균열 상호작용과 ligament 붕괴 민감도에 영향을 줄 수 있음”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “For smaller radius components, such as pressurizer nozzles, or for particularly large cracks, the ID curvature may affect crack interaction and susceptibility to ligament collapse.” (p.101, §4.3).
- 문제: 일치

### [슬라이드 75] 일치 — 확신도(CONFIRMED)
- PPT 문구: “coalescence module은 프레임워크가 시간 스텝마다 부를 수 있고, 모든 활성 균열의 위치·모양·크기를 coalescence가 반영되도록 고침”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “At each time discretization, the Framework may call the coalescence module to update the crack configuration (i.e., location, shape, and size for all active cracks).” (p.103, §5.1).
- 문제: 일치

### [슬라이드 75] 일치 — 확신도(CONFIRMED)
- PPT 문구: “활성 균열 쌍마다 coalescence criteria에 대어 보는 반복 절차(iterative procedure)를 사용”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “To update the crack configuration, the coalescence module implements an iterative procedure whereby each pair of active cracks is assessed against coalescence criteria. If any pair of cracks does satisfy coalescence criteria, the coalescence module updates the attributes associated with this pair of cracks to result in a) a coalesced crack with attributes determined as a function of the attributes of the two original cracks and b) an absorbed crack, which is effectively ignored throughout the remainder of simulation.” (p.103, §5.1).
- 문제: 일치

### [슬라이드 75] 일치 — 확신도(CONFIRMED)
- PPT 문구: “어떤 쌍이 기준을 만족하면 coalesced crack(두 균열 속성의 함수)과 absorbed crack(이후 사실상 무시)으로 갱신하고, 기준을 만족하는 쌍이 더 이상 없을 때까지 반복한 뒤 제어를 프레임워크에 돌려줌”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “The iterative procedure continues until no pair of active cracks satisfies coalescence criteria, at which point the coalescence module returns control to the calling entity.” (p.103, §5.1).
- 추가 원문 근거: “If any pair of cracks does satisfy coalescence criteria, the coalescence module updates the attributes associated with this pair of cracks to result in a) a coalesced crack with attributes determined as a function of the attributes of the two original cracks and b) an absorbed crack, which is effectively ignored throughout the remainder of simulation. The iterative procedure continues until no pair of active cracks satisfies coalescence criteria, at which point the coalescence module returns control to the calling entity.” (p.103, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 75] 일치 — 확신도(CONFIRMED)
- PPT 문구: “프레임워크가 균열 구성, 부품 형상, coalescence model 매개변수를 입력으로 줍니다(p.103). 모듈은 먼저 모든 입력이 허용 범위 안인지 확인하고, 균열 배열을 원주 위치 순으로 다시 정렬함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “For each update, the Framework provides information about the crack configuration, component geometry, and coalescence model parameters via inputs that are detailed in Section 5.3.” (p.103, §5.1; p.105, 5.2.1.1~2).
- 추가 원문 근거: “Prior to any other operations, all arguments to the module are confirmed to be within acceptable ranges, as identified in Section 5.3. If not, the module returns control to the calling entity with an error flag to indicate which input was first found to be out of range.” (p.105, 위 인용 절의 해당 문단).
- 추가 원문 근거: “All vector arrays corresponding to crack-specific attributes are reordered in terms of circumferential location.38 Enforcement of this requirement and others discussed in Section 5.2.1.3 guarantees that pairwise coalescence will only occur between adjacent cracks.” (p.105, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 75] 일치 — 확신도(CONFIRMED)
- PPT 문구: “요구사항을 함께 적용해 coalescence가 인접한 균열 사이에서만 일어나도록 함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “5.2.1.2 Pre-Processing Requirements Before application of the iterative procedure, a number of pre-processing requirements are enforced to improve efficiency and limit complexity: • All vector arrays corresponding to crack-specific attributes are reordered in terms of circumferential location.38 Enforcement of this requirement and others discussed in Section 5.2.1.3 guarantees that pairwise coalescence will only occur between adjacent cracks. This condition is helpful for verifying the coalescence module.” (p.105, §5.2.1.2).
- 문제: 일치

### [슬라이드 75] 일치 — 확신도(CONFIRMED)
- PPT 문구: “원주방향 같은 평면 균열만 다룹니다. 축방향 균열은 coalescence에서 제외하며, 모든 균열은 세 가지 이상화 유형 중 하나라고 가정함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Flow Diagram of the Version 2.0 xLPR Crack Coalescence Module The scope of the coalescence module is limited to coplanar circumferential cracks. Axial cracks are neglected with respect to coalescence considerations.” (p.104, §5.1).
- 문제: 일치

### [슬라이드 75] 오탈자 — 확신도(CONFIRMED)
- PPT 문구: “간 스텝은 xLPR 2.0 기본값이 1개월이며, 세 균열 이상이 같은 스텝에 coalesce하는 일은 드물다고 봄”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Cases of three or more cracks coalescing during the same time step is believed to be rare for the one month time step that is the default in xLPR Version 2.0.” (p.111, §5.3.2).
- 추가 원문 근거: “Coalescence of three or more cracks can lead to dependence on the direction of the coalescence procedure. Cases of three or more cracks coalescing during the same time step is believed to be rare for the one month time step that is the default in xLPR Version 2.0.” (p.111, 위 인용 절의 해당 문단).
- 문제: 오탈자: 간 스텝 → 시간 스텝. 기본값 1개월 및 세 균열 이상 합체가 드물다는 서술은 일치.
- 최소 교체안: 시간 스텝은 xLPR 2.0 기본값이 1개월이며, 세 균열 이상이 같은 스텝에 합체하는 일은 드물다고 봄.

### [슬라이드 76] 일치 — 확신도(CONFIRMED)
- PPT 문구: “일반적으로 “Crack B”의 가장 왼쪽 끝이 “Crack A”의 두 끝 사이에 있거나, “Crack A”의 가장 오른쪽 끝에서 시계 방향으로 coalescence distance보다 가까우면 기준이 만족됨”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “These requirements rely on the designation of “Crack A” and “Crack B”, as detailed below: • In general, the crack coalescence criteria are satisfied when the leftmost tip (relative to an observer standing on the origin of the pipe cross-section) of “Crack B” is between the tips of “Crack A” or if the leftmost tip of “Crack B” is less than the coalescence distance from the 38 This requirement is facilitated by the Index Transformation array described later.” (p.105, §5.2.1.3; p.106 계속).
- 추가 원문 근거: “In general, the crack coalescence criteria are satisfied when the leftmost tip (relative to an observer standing on the origin of the pipe cross-section) of “Crack B” is between the tips of “Crack A” or if the leftmost tip of “Crack B” is less than the coalescence distance from the” (p.105, 위 인용 절의 해당 문단).
- 추가 원문 근거: “rightmost tip of “Crack A” in the clockwise direction. The coalescence distance depends on the crack types and geometries of “Crack A” and “Crack B”. See Section 5.2.1.4.” (p.106, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 76] 오탈자 — 확신도(CONFIRMED)
- PPT 문구: “oalescence distance는 두 균열의 종류와 형상에 따라 달라짐”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “The coalescence distance depends on the crack types and geometries of “Crack A” and “Crack B”.” (p.106, §5.2.1.3).
- 문제: 오탈자: oalescence → coalescence.
- 최소 교체안: coalescence distance는 두 균열의 종류와 형상에 따라 달라짐.

### [슬라이드 76] 일치 — 확신도(CONFIRMED)
- PPT 문구: “구간 1에서 시작한 균열이 처음의 “Crack A” 로 지정”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “• The crack that initiated in subunit 1 is the first crack designated as “Crack A”. • Each time a crack is designated as “Crack A”, each other crack is iteratively designated as “Crack B”, beginning immediately clockwise of “Crack A” and proceeding in the clockwise direction.” (p.106, §5.2.1.3).
- 문제: 일치

### [슬라이드 76] 일치 — 확신도(CONFIRMED)
- PPT 문구: “어떤 균열이 “Crack A”가 될 때마다 나머지 균열을 “Crack A” 바로 시계 방향 옆에서 시작해 시계 방향으로 차례로 “Crack B”로 지정”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Each time a crack is designated as “Crack A”, each other crack is iteratively designated as “Crack B”, beginning immediately clockwise of “Crack A” and proceeding in the clockwise direction.” (p.106, §5.2.1.3).
- 문제: 일치

### [슬라이드 76] 일치 — 확신도(CONFIRMED)
- PPT 문구: “현재 “Crack A”가 어떤 균열과도 조건을 만족하지 않으면 바로 시계 방향 옆의 균열이 새 “Crack A”가 됨”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “If the current “Crack A” does not satisfy the coalescence criteria with any other crack, the crack immediately clockwise of the current “Crack A” is designated as the new “Crack A”.” (p.106, §5.2.1.3).
- 문제: 일치

### [슬라이드 76] 일치 — 확신도(CONFIRMED)
- PPT 문구: “조건을 만족하면 “Crack A”는 coalesced crack의 속성을, “Crack B”는 absorbed crack의 속성을 받고, 조건을 만족하는 쌍이 없어질 때까지 반복”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “• If the coalescence criteria are satisfied, “Crack A” receives updated attributes corresponding with the coalesced crack and “Crack B” receives updated attributes corresponding with the absorbed crack.” (p.106, §5.2.1.3).
- 문제: 일치

### [슬라이드 76] 일치 — 확신도(CONFIRMED)
- PPT 문구: “coalescence가 두 번 이상 필요한 배치에서는 순회 방향에 따라 갱신된 균열 구성이 달라질 수 있다는 우려가 있어, 순회 방향을 뒤집을 수 있게 제작함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “This capability was built-in to investigate the concern that—for configurations requiring more than one instance of pairwise coalescence—the iterative coalescence rules may give different updated crack configurations depending on directionality of the iterative procedure. 5.2.1.4 Defining Coalescence Distance A number of requirements are enforced to define the coalescence distance—the distance between two cracks below which those cracks will coalesce—in accordance with the modeling conventions of Section 4.2, for example: • If both cracks are surface cracks, two possible conventions have been implemented: in the first, the coalescence distance is set to a user-defined input, irrespective of crack sizes; in the second, the coalescence distance is calculated by scaling the maximum crack depth by a user-defined input.” (p.106, §5.2.1.3).
- 추가 원문 근거: “The directionality of the iterative coalescence procedure (as stated above) may be reversed using a module flag (the Coalescence Direction flag). This capability was built-in to investigate the concern that—for configurations requiring more than one instance of pairwise coalescence—the iterative coalescence rules may give different updated crack configurations depending on directionality of the iterative procedure.” (p.106, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 76] 일치 — 확신도(CONFIRMED)
- PPT 문구: “두 균열까지만 동시에 coalesce하면 방향은 무관하고, 세 균열 이상이 같은 시점에 coalesce할 때만 방향에 따라 달라질 수 있음”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Coalescence of three or more cracks can lead to dependence on the direction of the coalescence procedure.” (p.111, §5.3.2).
- 문제: 일치

### [슬라이드 77] 일치 — 확신도(CONFIRMED)
- PPT 문구: “Coalescence direction | 반복 절차의 순회 방향 플래그 | 시계 방향 (1) / 반시계 방향 (2)”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “The following parameter inputs fully define the behavior of the coalescence module: • Coalescence direction: The coalescence direction flag determines whether the iterative coalescence procedure is applied in a clockwise (1) or counter-clockwise direction (2). The 40 The coalescence module performs updates to crack type due to coalescence.” (p.110, §5.3.2).
- 문제: 일치

### [슬라이드 77] 일치 — 확신도(CONFIRMED)
- PPT 문구: “Surface crack coalescence distance rule | 표면균열 coalescence distance를 절대 거리로 볼지 최대 깊이 비율로 볼지 | 절대 거리 (1) / 최대 깊이 비율 (2, 권장)”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “• Surface crack coalescence distance rule: This input selects the rule applied to determine if the coalescence distance is defined as an absolute distance (1) or as a ratio of the maximum depth of the cracks involved in potential coalescence (2).” (p.111, §5.3.2).
- 추가 원문 근거: “Surface crack coalescence distance rule: This input selects the rule applied to determine if the coalescence distance is defined as an absolute distance (1) or as a ratio of the maximum depth of the cracks involved in potential coalescence (2). The latter convention is recommended in order to capture the depth-dependence of crack interaction discussed in Section 4.2.” (p.111, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 77] 일치 — 확신도(CONFIRMED)
- PPT 문구: “Surface crack coalescence distance rule modifier | 규칙 1이면 coalescence distance 자체, 규칙 2이면 coalescence distance ÷ 최대 깊이 | 규칙 2이면 삼각분포 0.0 / 0.5 / 0.75 권장”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “As discussed in Section 4.2, provided a distance rule of 2, the surface crack coalescence distance rule modifier should be sampled from a triangular distribution with extremes at 0.0 and 0.75 and a mode at 0.5 to represent variability observed in laboratory studies.” (p.111, §5.3.2).
- 추가 원문 근거: “Surface crack coalescence distance rule modifier: For a distance rule value of 1, this value is the coalescence distance—absolute distance between two surface cracks at the time that they are predicted to coalesce. For a distance rule value of 2, this value is the ratio of the coalescence distance to the maximum crack depth.” (p.111, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 77] 일치 — 확신도(CONFIRMED)
- PPT 문구: “Through-wall crack coalescence distance rule modifier | 두 관통균열의 coalescence distance | 균열 길이와 대략 맞는 분포, 예: 0~20 in 균일분포”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “For components of interest, this distribution might be achieved roughly with a uniform distribution between zero and 20 inches.” (p.111, §5.3.2).
- 추가 원문 근거: “Through-wall crack coalescence distance rule modifier: This value is the coalescence distance for two through-wall cracks. The coalescence distance for through-wall cracks is used predominantly to mimic ligament collapse. As discussed in Section 4.2, the through-wall crack coalescence distance rule modifier should be sampled from a distribution roughly consistent with the lengths of cracks at the time at which coalescence is simulated to represent a dependence on crack length that is otherwise unmodeled. For components of interest, this distribution might be achieved roughly with a uniform distribution between zero and 20 inches.” (p.111, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 77] 일치 — 확신도(CONFIRMED)
- PPT 문구: “Coalescence depth rule | coalesced crack 깊이를 정하는 규칙 | 최대 (1, 권장) / 최소 (2) / 평균 (3)”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “• Coalescence depth rule: The coalescence depth rule specifies whether the depth of the coalesced surface crack is the maximum (1), minimum (2), or average (3) of the original crack depths.” (p.111, §5.3.2).
- 추가 원문 근거: “Coalescence depth rule: The coalescence depth rule specifies whether the depth of the coalesced surface crack is the maximum (1), minimum (2), or average (3) of the original crack depths. A value of 1 is recommended based on findings presented in Section 4.2.” (p.111, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 78] 일치 — 확신도(CONFIRMED)
- PPT 문구: “coalescence model은 몇 개의 입력 매개변수와 플래그로 동작이 완전히 정해지도록 만들었음”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “The following parameter inputs fully define the behavior of the coalescence module: • Coalescence direction: The coalescence direction flag determines whether the iterative coalescence procedure is applied in a clockwise (1) or counter-clockwise direction (2).” (p.110, §5.3.2).
- 문제: 일치

### [슬라이드 78] 일치 — 확신도(CONFIRMED)
- PPT 문구: “아래 표의 입력을 설정합니다. surface crack coalescence distance rule 값이 2이면 계수는 삼각분포(0.0, 0.5, 0.75)에서 뽑도록 권장하고, through-wall crack coalescence distance는 coalescence가 모의되는 시점의 균열 길이와 대략 맞는 분포에서 뽑도록 권장”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “As discussed in Section 4.2, the through-wall crack coalescence distance rule modifier should be sampled from a distribution roughly consistent with the lengths of cracks at the time at which coalescence is simulated to represent a dependence on crack length that is otherwise unmodeled.” (p.111, §5.3.2).
- 문제: 일치

### [슬라이드 78] 일치 — 확신도(CONFIRMED)
- PPT 문구: “입력 단위는 모듈에 내장되어 있어 그대로 지켜야 합니다. 허용 범위를 벗어나면 치명적 오류로 실행이 멈추며, 이 범위는 모델을 검증한 범위와 다름”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “This range is different from the range over which model validation was performed.” (p.109, §5.3).
- 추가 원문 근거: “Required unit: Assumed units are built into the coalescence module calculations and therefore must be upheld by input arguments. • Range of verification: A critical error (requiring program termination) is generated for inputs outside of the range of verification. In general, these ranges prevent unrealistic or non-meaningful inputs. This range is different from the range over which model validation was performed.” (p.109, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 78] 오탈자 — 확신도(CONFIRMED)
- PPT 문구: “열 수 0~200, 균열 중심 0 이상 2π rad 미만, ID·OD 입력은 반길이(m), surface crack coalescence distance rule modifier는 규칙 1이면 m이고 규칙 2이면 무차원, through-wall crack coalescence distance는 m이며 거리는 모두 0 이상임”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Number of cracks represented” (p.109, §5.3, 표 5-1).
- 추가 원문 근거: “Number of cracks represented - 0 ≤ x≤ 200 Crack type array - -3 ≤ x < 100 Depth array m 0 < x ≤ thickness Center location array rad 0 ≤ x< 2π ID half-length array m 0 < x≤ π*inner radius OD half-length array m 0 ≤ x≤ π*outer radius Crack orientation array - 1 ≤ x ≤ 2 Index transformation array - 1 ≤ x < 100 Component inside radius m x> 0 Component thickness m x> 0 Coalescence direction - 1 ≤ x ≤ 2 Surface crack coalescence distance - 1 ≤ x ≤ 2 rule value (DistanceRule) Surface crack coalescence distance meter if DistanceRule=1 x ≥ 0 rule modifier unitless if DistanceRule=2 Through-wall crack coalescence m x≥ 0 distance rule modifier Coalescence depth rule value - 1 ≤ x ≤ 3 Error flag” (p.109, 위 인용 절의 해당 문단).
- 문제: 오탈자: 열 수 → 균열 수. 나머지 0~200, 중심각 범위, 반길이 m, 거리계수의 단위·비음수 조건은 일치.
- 최소 교체안: 균열 수 0~200, 균열 중심 0 이상 2π rad 미만. ID·OD 입력은 반길이(m), 거리 규칙 1의 계수는 m, 규칙 2의 계수는 무차원, 관통균열 합체거리는 m이며 거리계수는 0 이상임.

### [슬라이드 78] 오탈자 — 확신도(CONFIRMED)
- PPT 문구: “열 유형 코드는 0 = 미발생, −1 = 표면, −2 = 천이, −3 = 이상화 관통, 양의 정수 = 흡수된 균열이고, 균열 방향 배열은 원주 1, 축 2임”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “0 corresponds to a crack that has not yet initiated; -1 corresponds to a surface crack; -2 corresponds to a transitioning crack; -3 corresponds to an idealized through-wall crack; and any positive integer corresponds to a crack that was previously absorbed by coalescence.” (p.110, §5.3.1).
- 추가 원문 근거: “Crack orientation: The crack orientation array designates cracks as either circumferential (1) or axial (2). Axial cracks are neglected” (p.110, 위 인용 절의 해당 문단).
- 문제: 오탈자: 열 유형 → 균열 유형. 유형·방향 코드의 값과 의미는 일치.
- 최소 교체안: 균열 유형 코드는 0=미발생, −1=표면, −2=천이, −3=이상화 관통, 양의 정수=흡수됨. 균열 방향은 원주 1, 축 2.

### [슬라이드 78] 일치 — 확신도(CONFIRMED)
- PPT 문구: “두 표면균열은 사용자 지정 거리 또는 최대 깊이에 사용자 값을 곱한 거리, 두 관통균열은 사용자 지정 거리, 표면+관통은 0임”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “• If both cracks are through-wall cracks, the coalescence distance is set to a user-defined input.” (p.106, §5.2.1.4).
- 추가 원문 근거: “If both cracks are surface cracks, two possible conventions have been implemented: in the first, the coalescence distance is set to a user-defined input, irrespective of crack sizes; in the second, the coalescence distance is calculated by scaling the maximum crack depth by a user-defined input. Either option may be invoked by varying a model flag (the Surface Crack Coalescence Distance Rule flag). • If both cracks are through-wall cracks, the coalescence distance is set to a user-defined input. • If one crack is a surface crack and the other is a through-wall crack, the coalescence distance is set to zero.” (p.106, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 79] 일치 — 확신도(CONFIRMED)
- PPT 문구: “흡수된 균열은 균열 유형 값에 양의 정수를 넣어 표시함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “By convention in xLPR Version 2.0, positive integers designate absorbed cracks.39 • A coalesced crack resulting from coalescence between any two dissimilar crack types is a Transitioning Crack.” (p.107, §5.2.1.5).
- 문제: 일치

### [슬라이드 79] 일치 — 확신도(CONFIRMED)
- PPT 문구: “그 값은 coalescence 상대인 Crack A의 발생 시점 번호이며 실행 후 진단에 도움이 됨”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Specifically, absorbed cracks are given a crack type equal to the initiation time index of the crack with which it coalesces (i.e., “Crack A”).” (p.107, §5.2.1.5, 각주 39).
- 문제: 일치

### [슬라이드 79] 일치 — 확신도(CONFIRMED)
- PPT 문구: “coalescence에 관여하지 않은 균열의 속성은 바뀌지 않음”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “5.2.1.6 Output Requirements Several requirements pertain to the output of the coalescence module, for example: • Cracks not involved in coalescence do not have their attributes updated by the coalescence module.” (p.107, §5.2.1.6).
- 문제: 일치

### [슬라이드 79] 일치 — 확신도(CONFIRMED)
- PPT 문구: “모듈이 돌려주는 인수가 허용 범위를 벗어나면 어느 출력이 문제인지 오류 플래그로 알림”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “If not, the module returns control to the calling entity with an error flag to indicate which output was found to be out of range. • If the number of pairwise coalescences exceeds one during a single call to the coalescence module, the error flag is set to 301.” (p.108, §5.2.1.6).
- 문제: 일치

### [슬라이드 79] 일치 — 확신도(CONFIRMED)
- PPT 문구: “한 번의 호출에서 pairwise coalescence가 한 번을 넘으면 오류 플래그가 301이 되며, xLPR에서 300번대 오류는 프로그램을 끝내지 않으며 run file에 기록함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “If the number of pairwise coalescences exceeds one during a single call to the coalescence module, the error flag is set to 301.” (p.108, §5.2.1.6).
- 추가 원문 근거: “If the number of pairwise coalescences exceeds one during a single call to the coalescence module, the error flag is set to 301. By definition within xLPR, a 300-level error does not result in termination of the program instance, but is logged to a run file for the benefit of the user or reviewers.” (p.108, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 79] 일치 — 확신도(CONFIRMED)
- PPT 문구: “균열별 벡터 출력은 균열 발생 시간 순서로 다시 정렬됨”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “All vector array outputs containing crack-specific attributes are reordered and returned with the order corresponding to crack initiation times.” (p.108, §5.2.1.6).
- 문제: 일치

### [슬라이드 79] 일치 — 확신도(CONFIRMED)
- PPT 문구: “0은 정상, 101~115는 입력이 표 5-1의 허용 범위(range of verification, 모델 타당성 검증(validation)에 쓴 범위와는 다름, p.109)를 벗어난 경우로 실행을 끝내야 하며 프레임워크의 알 수 없는 오류를 뜻함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Error codes 101 through 115 communicate an input that is out of its range of verification.” (p.111, §5.3.3; p.109, 5.3).
- 추가 원문 근거: “The default error code is 0, indicating no errors or anomalies. • Error codes 101 through 115 communicate an input that is out of its range of verification. For these error codes, the calling entity should terminate the run and notify the user which input is out of range. These error codes indicate an unknown error in the Computational Framework.” (p.111, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 79] 일치 — 확신도(CONFIRMED)
- PPT 문구: “201과 210은 모듈 출력이 허용 범위를 벗어난 경우로 역시 실행을 끝내야 하며 모듈의 알 수 없는 오류를 뜻함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Error codes 201 and 210 communicate that a calculated output of the coalescence module is out of its range of verification.” (p.112, §5.3.3).
- 추가 원문 근거: “Error codes 201 and 210 communicate that a calculated output of the coalescence module is out of its range of verification. For these error codes, the calling entity should terminate the run and notify the user which input is out of range. These error codes indicate an unknown error in the coalescence module.” (p.112, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 79] 일치 — 확신도(CONFIRMED)
- PPT 문구: “301은 한 번의 호출에서 pairwise coalescence가 한 번을 넘은 경우로 실행을 끝내지는 않지만, 프레임워크가 발생 빈도를 추적해야 함. 자주 일어나면 coalescence direction 입력을 반대로 해 다시 실행해서 편향이 없었는지 확인하라고 지시. 모듈은 갱신된 배열 외에 pairwise coalescence 횟수도 돌림”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “If it occurs frequently, the run should be repeated with the Coalescence Direction input set to apply the coalescence procedure in the reverse direction to ensure that there was no bias during the run.” (p.112, §5.3.3; p.111 시작).
- 추가 원문 근거: “Error code 301 communicates that the number of pairwise coalescences exceeded one during a single call to the coalescence module. This error code does not terminate the realization, but should be tracked by the Framework to ensure that the condition is relatively rare across all realizations. If it occurs frequently, the run should be repeated with the Coalescence Direction input set to apply the coalescence procedure in the reverse direction to ensure that there was no bias during the run.” (p.112, 위 인용 절의 해당 문단).
- 추가 원문 근거: “In addition to the updated crack type and geometry arrays, two other output arguments are used to convey additional information about the call to the coalescence module. First, the number of pairwise coalescences is returned.” (p.111, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 80] 일치 — 확신도(CONFIRMED)
- PPT 문구: “실행중 메모리 30kB 이하 , 임의유형 . 깊이 . 길이의 균열이 최소 5개이고 겹치는 사례가 최소 2개인 구성에서 1000번 실행이 10초 미만이여야 함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “5.2.1.7 Performance Requirements To motivate efficient module design, the following runtime and memory requirements were imposed: • The coalescence module memory does not exceed 30 kB during runtime. • For a case with the existence of at least five cracks of arbitrary type, depth, and length— subject to at least two instances of overlapping cracks—the coalescence module shall be capable of execution 1000 times in less than 10 seconds.” (p.108, §5.2.1.7).
- 추가 원문 근거: “For a case with the existence of at least five cracks of arbitrary type, depth, and length— subject to at least two instances of overlapping cracks—the coalescence module shall be capable of execution 1000 times in less than 10 seconds.” (p.108, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 81]
내용 없음

### [슬라이드 82] 오탈자 — 확신도(CONFIRMED)
- PPT 문구: “LPR 2.0은 용접 경계의 복잡한 물성 변화(모재 HAZ, 용접금속 희석 영역)를 모델링하지 않음”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “material properties that exists at weld material interfaces, e.g., base metal heat affected zone (HAZ) and weld metal dilution zone.” (p.118, §6.1.1; p.117 시작).
- 추가 원문 근거: “The xLPR Version 2.0 program does not account for the complex variation of” (p.117, 위 인용 절의 해당 문단).
- 문제: 오탈자: LPR → xLPR.
- 최소 교체안: xLPR 2.0은 용접 경계의 복잡한 물성 변화(모재 HAZ, 용접금속 희석 영역)를 모델링하지 않음.

### [슬라이드 82] 일치 — 확신도(CONFIRMED)
- PPT 문구: “용접금속 안에 있는 균열 끝은 용접금속 모델로, 모재로 들어가는 순간부터 모재 모델로 예측”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “immediately after the crack tip extends into the base metal, growth would be predicted with the base metal model.” (p.118, §6.1.1).
- 문제: 일치

### [슬라이드 82] 일치 — 확신도(CONFIRMED)
- PPT 문구: “배관 맞대기 용접의 현장 PWSCC 경험에서 저 Cr 재료와의 계면 가까운 Alloy 82/182 용접금속에 균열이 몰리는 뚜렷한 경향은 보이지 않았다고 덧붙임”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “While a specific weld interface / dilution zone model has not been developed, plant PWSCC experience for piping butt weld locations has not indicated any apparent preference for cracking to occur in the Alloys 82/182 weld metal close to interfaces with lower-chromium materials.” (p.118, §6.1.1).
- 문제: 일치

### [슬라이드 82] 일치 — 확신도(CONFIRMED)
- PPT 문구: “PWSCC 발생 민감도와 성장을 상관시키는 기능이 있지만 정확한 값은 권장하지 않았으며, 정량화에는 계획된 실험이 도움이 될 수 있다고 함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “• Initiation-growth correlation: Currently, xLPR Version 2.0 includes the ability to correlate susceptibility to PWSCC initiation and PWSCC growth; however, with the current state of knowledge, no precise value is recommended for this correlation. This correlation can be important for assessing plant risks because it tends to result in relatively high CGRs for the earliest initiating cracks.” (p.118, §6.1.1).
- 추가 원문 근거: “Initiation-growth correlation: Currently, xLPR Version 2.0 includes the ability to correlate susceptibility to PWSCC initiation and PWSCC growth; however, with the current state of knowledge, no precise value is recommended for this correlation. This correlation can be important for assessing plant risks because it tends to result in relatively high CGRs for the earliest initiating cracks. Carefully planned laboratory experiments may help quantify this correlation.” (p.118, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 82] 일치 — 확신도(CONFIRMED)
- PPT 문구: “이 상관은 가장 먼저 발생하는 균열에서 상대적으로 높은 CGR을 유발하는 경향이 있어 위험 평가에서 중요할 수 있음”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “This correlation can be important for assessing plant risks because it tends to result in relatively high CGRs for the earliest initiating cracks.” (p.118, §6.1.1).
- 문제: 일치

### [슬라이드 83] 일치 — 확신도(CONFIRMED)
- PPT 문구: “Alloy 600 /82/182/132 의 PWR PWSCC 모델 개선과 함께 다른 재료 , 환경의 CGR 모델 개발이 유용 할 수 있음”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “6.1.2 Other SCC Models In addition to refinement of the CGR models for PWSCC of Alloys 600/82/182/132 in PWR environments, it may be useful to develop CGR models for other materials and other environments.” (p.118, §6.1.2).
- 문제: 일치

### [슬라이드 83] 오탈자 — 확신도(CONFIRMED)
- PPT 문구: “이런 모델이 현제 구현된 식 3-1의 형태에 들어가길 바라지만 다른 형태가 필요 할 수도 있음”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “3-1]), but alternative model forms may be required. Some specific conditions of interest are noted below: • Alloy 690 and associated weld metals: After Alloy 600 and its associated weld metals, PWSCC CGR models are desired for Alloy 690 and its associated weld metals (e.g., Alloy 52, 152, and variants).” (p.118, §6.1.2).
- 문제: 오탈자: 현제 → 현재. 식 3-1 및 대안 형식의 가능성은 일치.
- 최소 교체안: 이런 모델이 현재 구현된 식 3-1 형태에 들어가길 바라지만 다른 형태가 필요할 수도 있음.

### [슬라이드 83] 일치 — 확신도(CONFIRMED)
- PPT 문구: “Alloy 600 다음으로 Alloy 690과 그 용접금속 (Alloy 52,152 등) 의 PWSCC CGR 모델 개발이 바람직하다고 설명하며, EPRI PWSCC 성장 전문가 패널에서 개발중임”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “There are efforts underway within the EPRI Expert Panel on PWSCC Growth to develop such models.” (p.118, §6.1.2).
- 추가 원문 근거: “Alloy 690 and associated weld metals: After Alloy 600 and its associated weld metals, PWSCC CGR models are desired for Alloy 690 and its associated weld metals (e.g., Alloy 52, 152, and variants). There are efforts underway within the EPRI Expert Panel on PWSCC Growth to develop such models.” (p.118, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 83] 일치 — 확신도(CONFIRMED)
- PPT 문구: “xLPR 이 더 다양한 부품을 다루게 되면 BWR 환경의 SCC모델이 필요 할 수도 있음”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “• BWR environments: As xLPR progresses to take on a more diverse set of component types, it may be required to implement SCC CGR models for BWR environments. For instance, IGSCC CGR models for SS have been developed from laboratory data and could be implemented.” (p.118, §6.1.2).
- 문제: 일치

### [슬라이드 83] 일치 — 확신도(CONFIRMED)
- PPT 문구: “스테인리스의 IGSCC CGR 모델은 실험 데이터로 개발된 것이 있어 구현이 가능함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “IGSCC CGR models for SS have been developed from laboratory data and could be implemented.” (p.118, §6.1.2).
- 문제: 일치

### [슬라이드 84]
내용 없음

### [슬라이드 85] 일치 — 확신도(CONFIRMED)
- PPT 문구: “현재 xLPR 모델은 재료에 상관없이 같은 피로 ΔK 문턱값 모델을 씁니다. 재료별로 받아들일 만하다고 검증되었지만, ASME Section XI를 위해 재료별 threshold 시험으로 모델을 만드는 작업이 진행 중이므로 이후 개정 때 참고해야 한다고 함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “The current xLPR model uses the same fatigue stress intensity factor range threshold model, irrespective of material.” (p.119, §6.2.3).
- 추가 원문 근거: “While this model has been validated as acceptable across different materials, there are efforts underway to develop models from material-specific stress intensity factor range threshold testing for ASME Section XI. These models should be consulted for future revisions of the xLPR program.” (p.119, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 85] 일치 — 확신도(CONFIRMED)
- PPT 문구: “피로CGR 모델의 검증은 주로 다른 식이나 소프트웨어의 예측에 의존했고 , 일부는 모델 개발과 독립적이지 않음”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “The validation performed for the fatigue CGR models was based predominantly on alternative equation or software predictions. In some cases, these alternative predictions were not independent from the development efforts underlying the xLPR fatigue CGR models.” (p.119, §6.2.4).
- 문제: 일치

### [슬라이드 85] 오탈자 — 확신도(CONFIRMED)
- PPT 문구: “모델 개발과 독립적인 실험 피로 CGR 데이더가 더 필요함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “For future validation efforts, additional laboratory fatigue CGR data—independent from model development—is needed for validation that is more thorough.” (p.119, §6.2.4).
- 문제: 오탈자: 데이더 → 데이터.
- 최소 교체안: 모델 개발과 독립적인 실험 피로 CGR 데이터가 더 필요함.

### [슬라이드 85] 일치 — 확신도(CONFIRMED)
- PPT 문구: “또한 가동중 검사 보고서에서 피로로 진전중임이 확인된 균열이 한 주기 이상 사용된 사례를 찾으면, 현장 조건의 피로 CGR을 어느 정도 추정 할 수 있다고 설명함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Alternatively, review of in-service examination reports may lead to instances in which cracks verified to be advancing by fatigue were left in service for one or more cycles, thus allowing some estimation of fatigue CGR in field conditions.” (p.119, §6.2.4).
- 추가 원문 근거: “Alternatively, review of in-service examination reports may lead to instances in which cracks verified to be advancing by fatigue were left in service for one or more cycles, thus allowing some estimation of fatigue CGR in field conditions.” (p.119, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 86] 오탈자 — 확신도(CONFIRMED)
- PPT 문구: “xLPR 2.0은 단순화된 균열·부품 형상에 의존합니다. 향후 개선 대상으로 부품 형상2.0의 기본은 세 개의 인접 환형 재료 그룹으로 나타낸 이종금속 용접이며 overlay/onlay는 네 번째 재료 그룹으로 모델링할 수 있음”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “For instance: • Component geometry: xLPR Version 2.0 focuses on a dissimilar metal weld geometry, represented by three material groups, each an annular shape, adjacent to one another. Weld overlay or onlay may be modeled with a fourth material group.” (p.120, §6.3.1).
- 추가 원문 근거: “Component geometry: xLPR Version 2.0 focuses on a dissimilar metal weld geometry, represented by three material groups, each an annular shape, adjacent to one another. Weld overlay or onlay may be modeled with a fourth material group.” (p.120, 위 인용 절의 해당 문단).
- 문제: 오탈자: ‘향후 개선 대상으로 부품 형상2.0의 기본은’은 소제목과 본문이 잘못 연결됨. 세 환형 재료 그룹 및 네 번째 그룹 설명은 일치.
- 최소 교체안: xLPR 2.0은 단순화된 균열·부품 형상에 의존함. 부품 형상: 현재 기본은 인접한 세 환형 재료 그룹으로 나타낸 이종금속 용접이며 overlay/onlay는 네 번째 그룹으로 모델링할 수 있음.

### [슬라이드 86] 일치 — 확신도(CONFIRMED)
- PPT 문구: “이후 두께 방향 재료 구배와 J-groove 용접 등을 개발할 것으로 기대”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “It is expected that later versions of xLPR will introduce more complicated geometries, e.g., to allow for through-wall material gradients.” (p.120, §6.3.1).
- 추가 원문 근거: “Furthermore, geometries are expected to be developed to represent other susceptible components such as J-groove welds used for head penetration nozzles.” (p.120, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 86] 일치 — 확신도(CONFIRMED)
- PPT 문구: “비대칭 균열 성장(세 이상화 균열 형상은 모두 대칭), 같은 평면이 아닌 균열(현재 모든 원주균열은 같은 평면이라 가정), 표면 아래 결함(발생·성장·coalescence·안정성 예측이 없으며 overlay의 융합 불량 같은 예가 있음)을듬”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “• Subsurface flaws: xLPR Version 2.0 does not include initiation, growth, coalescence, or stability predictions for subsurface flaws.” (p.120, §6.3.1).
- 추가 원문 근거: “Asymmetric crack growth: All three idealized crack shapes in xLPR Version 2.0 are symmetric, precluding the possibility of asymmetric growth that may arise, for instance, from off-axis bending loads, within-weld growth susceptibility variation, etc. While idealized (non-complex) crack shapes will probably remain necessary in later versions, it is recommended that asymmetric variations be developed. • Non-coplanar cracks: All circumferential cracks in Version 2.0 of xLPR are assumed to be coplanar, while in reality, circumferential cracks may be offset. As discussed in Section 4.3, the conservatism of this modeling convention is difficult to determine for any given case. While a coordinated effort between the Computational Framework and Models Groups would be required to eliminate the coplanar assumption, this would improve the predictive fidelity of xLPR.” (p.120, 위 인용 절의 해당 문단).
- 추가 원문 근거: “Subsurface flaws: xLPR Version 2.0 does not include initiation, growth, coalescence, or stability predictions for subsurface flaws. Subsurface flaws may arise from various mechanisms (e.g., lack of fusion of an overlay) and can influence plant risks.” (p.120, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 86] 일치 — 확신도(CONFIRMED)
- PPT 문구: “비동일평면 균열과 표면 아래 결함을 다루려면 프레임워크 그룹과 모델 그룹의 공동 작업이 필요”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “A coordinated effort between the Computational Framework and Models Groups would be required to introduce treatment for subsurface flaws.” (p.120, §6.3.1).
- 문제: 일치

### [슬라이드 86] 일치 — 확신도(CONFIRMED)
- PPT 문구: “K-solution 모듈은 인접 균열의 응력장 상호작용을 고려하지 않고, 안정성 모듈은 두 균열 사이 ligament 붕괴를 고려하지 않음”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “6.3.2 Crack Coalescence The prediction of crack coalescence in later versions of xLPR could be improved, for instance: • Crack interaction: Currently, the K-solutions modules do not account for the interaction of stress fields for adjacent cracks, which can lead to increased stress intensity factors.” (p.120, §6.3.2; p.121 계속).
- 추가 원문 근거: “Ligament collapse: Currently, the stability modules do not account for the collapse of ligaments between two cracks. Instead, this collapse is simulated by the coalescence module using a distributed input variable to define the ligament length at the time of collapse.” (p.121, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 86] 일치 — 확신도(CONFIRMED)
- PPT 문구: “이 둘을 coalescence module이 단순한 규칙으로 흉내 냄”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Instead, this interaction, which can lead to accelerating crack growth for cracks in close proximity, is simulated by the coalescence module using simple modeling conventions. More precise predictions would be achieved using fracture mechanics based solutions implemented in the K-solutions modules.” (p.120, §6.3.2; p.121 계속).
- 추가 원문 근거: “Instead, this collapse is simulated by the coalescence module using a distributed input variable to define the ligament length at the time of collapse.” (p.121, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 87] 일치 — 확신도(CONFIRMED)
- PPT 문구: “파괴역학 기반 해를 K-solution이나 안정성·coalescence 모듈에 넣으면 더 정밀해지며, 또는 균열 길이 의존성을 coalescence 규칙에 도입하면 크게 개선될 수 있다고 함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “More precise predictions would be achieved using fracture mechanics based solutions implemented in the K-solutions modules.” (p.120, §6.3.2; p.121 계속).
- 추가 원문 근거: “More precise predictions would be achieved using fracture mechanics based solutions implemented in the stability or coalescence modules. Alternatively, recent validation work (based on analytical modeling) has suggested that ligament length at the time of collapse is roughly one-to-one with crack length (for cracks of roughly the same size). Revisions to the simple modeling conventions implemented by the current coalescence module to introduce crack length-dependence could significantly improve the simulation of ligament collapse.” (p.121, 위 인용 절의 해당 문단).
- 추가 원문 근거: “Revisions to the simple modeling conventions implemented by the current coalescence module to introduce crack length-dependence could significantly improve the simulation of crack interaction.” (p.120, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 87] 일치 — 확신도(CONFIRMED)
- PPT 문구: “최근 검증 연구는 균열 간섭의 2차 결정 요인이 균열 길이이고, ligament 붕괴 시 ligament 길이가 비슷한 크기의 균열에서는 균열 길이와 대략 1:1이라고 시사함”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Alternatively, recent validation work [50] has suggested that the secondary determinant for crack interaction (after ligament length) is crack length.” (p.120, §6.3.2; p.121 계속).
- 추가 원문 근거: “Alternatively, recent validation work (based on analytical modeling) has suggested that ligament length at the time of collapse is roughly one-to-one with crack length (for cracks of roughly the same size).” (p.121, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 87] 일치 — 확신도(CONFIRMED)
- PPT 문구: “coalescence module은 축방향과 원주방향 균열의 상호작용을 무시”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “• Axial crack coalescence: The interaction of axial and circumferential cracks is ignored by the current coalescence module.” (p.121, §6.3.2).
- 문제: 일치

### [슬라이드 87] 오탈자 — 확신도(CONFIRMED)
- PPT 문구: “교 균열의 교차 효과를 넣을 수 있지만 혼합 방향 균열의 처리는 다른 모듈에 더 큰 과제일 수 있음”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “Coalescence modeling could be updated to account for the effects of the intersection of orthogonal cracks; however, the treatment of mixed orientation cracks is likely more of a challenge for other modules.” (p.121, §6.3.2).
- 문제: 오탈자: 교 균열 → 직교 균열.
- 최소 교체안: 직교 균열의 교차 효과를 넣을 수 있지만 혼합 방향 균열의 처리는 다른 모듈에 더 큰 과제일 수 있음.

### [슬라이드 87] 일치 — 확신도(CONFIRMED)
- PPT 문구: “미세균열(micro-fissure) coalescence는 보통 발생 과정의 일부로 보며 발생 그룹의 향후 과제로 봄”
- 원문 근거(영어 인용 + 인쇄 쪽 + 절): “It is not applicable to simulation of micro-fissure coalescence, a step commonly considered to be part of the initiation process.” (p.121, §6.3.2).
- 추가 원문 근거: “The simulation of micro-fissure coalescence is considered a potential area of future work for the Initiation Subgroup.” (p.121, 위 인용 절의 해당 문단).
- 문제: 일치

### [슬라이드 88]
내용 없음

### [슬라이드 89]
내용 없음

### [슬라이드 90] 발표 마무리 — 확신도(PLAUSIBLE)
- PPT 문구: “감사합니다”; “remsys.seoultech.ac.kr”.
- 원문 근거: 해당 없음(발표 마무리 및 연구실 주소).
- 문제: 원문 과학 내용 대조 대상 아님. 웹 주소의 유효성은 확인하지 않음.

## 유형별 개수

문장·표 행 기록 단위로 집계한다. 하나의 기록에 두 유형이 함께 있는 경우 복합 유형 한 건으로 표시하므로, 오탈자의 개별 철자 개수와 다르다. 같은 슬라이드의 반복 출현은 해당 기록에 묶었다.

- 오탈자: 19건
- 의미 변경: 5건
- 일치: 122건
- 의미 변경 + 오탈자: 1건
- 한정어 누락: 1건
- 조건 누락: 2건

- 검토 기록 합계: 150건(표지·마무리 2건 별도).
- 내용 없음: 60개 슬라이드.
- PPT에 명시된 인용 쪽 확인: 슬라이드 66 p.94; 67 p.94/p.98; 68 p.94/p.95; 70 p.98/p.98~99; 71 p.99; 72 p.99; 75 p.103; 79 p.109. 해당 쪽에서 관련 근거를 확인했다. 쪽 자체가 틀린 사례는 발견하지 못했으며, 72의 적용 범위 행은 쪽 오류가 아닌 내용·대상 오류로 기록했다.
- 수치·단위 자체의 불일치: 발견하지 못함. 67의 0.5와 0~20 in은 조건 누락으로 별도 기록함.
- 원문에 없는 내용 추가: 단독 유형 0건(66의 거리 합 표현은 의미 변경에 포함).

Git 작업: 시작 시 git pull을 시도했으나 .git/FETCH_HEAD 쓰기 권한 거부로 실패했다. 이 환경의 .git 쓰기 제한으로 git add/commit도 완료할 수 없었다. push 결과는 실행 후 기록한다.

ROUND36 DONE
