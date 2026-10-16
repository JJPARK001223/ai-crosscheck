# round40 독립 PPT 텍스트 검증

## 대상·방법·한계

- 대상: `J:\Desktop\XLPR\xLPR_수식 정리\2026_10_16.pptx`, 저장시각 2026-10-16 15:01:19, 30,680,431 bytes. PPT ZIP의 `ppt/slides/slideN.xml`을 직접 읽어 **89장**을 확인했다. PPT는 수정하지 않았다.
- 비교본: `round40/ppt_prev_dump.txt`, 현재 덤프 `round40/ppt_dump.txt`. **두 덤프 모두 89장**이다. 요청 B의 “직전본 91장”은 제공 파일과 불일치한다. 91장 버전 자체의 삭제·재배치는 확인 불가이며, 아래 비교는 제공된 89장 두 파일 기준이다.
- 원문: Kyle Schmitt, EPRI, *xLPR Models Subgroup Report—Crack Growth and Coalescence*, xLPR-MSGR-CGR Version 1.0, 2016-06-29. 아래 p.N은 모두 **인쇄 쪽**이다. `cgr_text.txt`의 PAGE N+1 블록과 블록 끝 인쇄번호를 대조했다. 원문에 요약된 다른 연구의 결과는 이 보고서의 서술과 대조했으며 원 논문을 별도 재검증한 것은 아니다.
- 중요: 제공 덤프는 그룹 안의 본문·표를 대량 누락한다. 예를 들어 덤프상 제목만 있는 5번에는 Alloy 600 설명이, 33번에는 온도 효과 설명이, 56번에는 모듈 설명이 실제로 있다. **실제 PPT XML의 모든 `a:p/a:t`를 추가로 읽어 보완**했다. 표의 반복 객체도 확인했다.
- 수식·그림 자체와 렌더링은 이번 텍스트 검사에서 검증하지 않았다. XML 텍스트 사이에서 수식 자리가 비어 보이는 것만으로는 누락 판정을 하지 않았다. `Text`·중복 표 객체의 존재는 확인했으나, 화면에서 가려졌는지·실제로 겹쳐 보이는지는 **확인 불가**다. 특히 해당 슬라이드를 “빈 슬라이드”라고 단정할 수 없다.
- round39 결과 및 Claude 답은 읽지 않았다. 자동화 스크립트는 실행하지 않았다. 보고서 외 파일은 수정하지 않았다.

## A. 현재본에서 확인한 수정 사항

인용은 현재 덤프 또는 실제 PPT XML의 문장/표 항목 그대로이며, XML에서만 확인한 항목은 비고에 명시했다. 한 행의 여러 유형은 한 원인의 중복 분류이며 각각 별도 오류로 합산하지 않는다.

| 슬라이드 번호 | 유형 | 슬라이드 원문 그대로 인용 | 영어 원문 구절 인용(인쇄 쪽) | 제안 수정 |
|---|---|---|---|---|
| 5 | TYPO | `ASME SEC XI  비 의무부록C, 0` | “Section XI Nonmandatory Appendices C and O” (p.21) | 숫자 0을 영문 O로 수정. XML에서 확인. |
| 5 | CITE | `p.21.22` | “158 measurements across 26 different material heats” (p.23); “This model validation applies for stress intensity factors between 10-80 MPa√m and operating temperatures between 280-350°C.” (p.25) | 개발 설명 p.21~22 외에 heat 수·불확실성 p.23, 검증 범위 p.25를 추가. 실제 본문 존재. |
| 6 | CITE | `p.21` | “T = temperature at location of crack (absolute)”; “f [heat] = common factor applied to all specimens fabricated from the same material heat” (p.22) | 기호 정의에 p.22 추가: p.21~22. XML 표에서 확인. |
| 7 | TYPO | `다중회귀로 맟추어을얻음` | “a linearized multiple regression statistical model was fit to the screened database to estimate other model parameters” (p.28) | “선별 데이터에 선형화 다중회귀 모델을 적합하여 나머지 매개변수를 추정함.” 수식 객체의 기호는 유지. |
| 8 | TYPO | `덴트라이트와 평행/수직` | “parallel or perpendicular to dendrite growth direction” (p.27) | “덴드라이트 성장 방향과 평행/수직.” |
| 9 | NUMBER | `검증 범위는 수소 약 10~60cc/kg 임` | “hydrogen concentrations between roughly 1 and 60 cc(STP)/kg” (p.37) | “검증 수소농도 범위는 약 1~60 cc(STP)/kg.” 하한 10→1. |
| 11 | CITE | `P의 독립 데이터 검증은 이뤄지지 않음` / `p.33~35 . 76` | “Analysis has not been performed to validate the peak-to-valley ratio against independent data.” (p.37) | p.37 추가. 주장은 맞지만 현재 인용 쪽에는 이 결론이 없다. |
| 12 | CITE | `Peak width, mv. 일때(최댓값 – 점근값) 차이  약 -40%` / `p.33` | “At one peak width ... CGR is reduced by approximately 40% relative to the difference between the maximum CGR ... and the asymptotic CGR” (p.81) | mV로 표기하고 “ΔECP=c에서 최대값과 점근값 차이의 약 40%만큼 CGR 감소”로 명료화, p.81 추가. ΔECP=c 수식 객체 자체는 미검증. |
| 16 | CITE | `식3-1에서 섭씨() 로명시` / `p.34` | “T = T_C + 273.15” ([Eqn.3-1], p.72) | 식 3-1을 근거로 섭씨를 설명하므로 p.72 추가. 빈 괄호의 실제 수식 표시 여부는 확인 불가. |
| 17 | TYPO | `SCC를 꼐산해야 하 때` | “could be used to implement SCC CGR models for these materials” (p.38) | “SCC를 계산해야 할 때.” |
| 21 | TYPO | `da/Dn` | “fatigue growth per cycle, da/dN” (p.39) | `da/dN`으로 수정. |
| 21 | NUMBER | `하중비 계산은 식 2-9와 같이` | “Load ratio ... [Eqn. 2-10]” (p.39) | 하중비 식 번호를 2-10으로 수정. 2-9는 ΔK 정의. |
| 25 | TYPO | `기름 2-10` / `상한은 양의 수준 , 즉 분포 중앙값의 1.517배에서 자르도록 권고함` | “Upper truncation at the positive 3-σ level (i.e., at 1.517 times the median)” (p.40 각주12) | “그림 2-10”; “양의 3σ 수준, 즉 중앙값의 1.517배에서 상한 절단.” 3σ가 그림/수식으로 따로 존재하는지는 확인 불가이므로 수치 누락 확정 대신 본문 명료화 권고. |
| 27 | TYPO | `피로 메커니즘이 커졌을때 씀` | “If the fatigue degradation mechanism is active and the material is a nickel-based alloy (Material Groups 1 through 5)” (p.72) | “피로 메커니즘이 켜졌을 때 사용함.” 커졌다는 크기 증가가 아닌 활성화 조건이다. |
| 27 | CITE | `하중 상승 시간  표면 응력 변화율이 1000psi/hr를 넘는 구간 임` / `p.42.43.44.86` | “Loading rise time ... the span of time over which the rate of change of surface stress exceeds 1000 psi/hr during a cycle” (p.78) | p.78 추가. 코드 1~5의 호출 조건은 p.72도 추가. |
| 29 | CITE | `Alloy 690은 시험이 약 60개정도라 Paris 지수와 하중비 효과는 재추정 하지 않고 온도효과만 구함` / `p.42` | “The roughly 60 tests available for Alloy 690 fatigue CGR in air were not sufficient to support estimation of the Paris power-law model or the load ratio effect.” (p.44) | p.44 추가. 파리형 식·기호는 p.42, 690 시험 근거는 p.44. |
| 32 | PLACEHOLDER | `Text여기에 수식을 입력하십시오.` | 대응하는 영어 과학 본문 없음. 원문은 “f_alloy = alloy factor” ([Eqn.2-15], p.43) | 불필요한 입력 안내 문구 제거. XML에 실제 존재하나 화면 노출 여부는 확인 불가. |
| 33 | NUMBER | `Alloy 600과 28/182/132 의 피로 계산에서 사용` | “Alloy 600 and associated weld metals (Alloys 82, 182, and 132)” (p.43) | 28→82. 제목의 82 표기와도 불일치. |
| 43 | DUPLICATE/STRUCTURE | `상승시간을 1초와 2000 초로 절단함` / `식 2-22 의 상승 시간 2000초 상한은 제거됨` | “The loading rise time is truncated at 1 and 2000 seconds” (p.49); “the upper limit of 2000 seconds ... was eliminated” (p.119) | “기존 식 2-22는 1~2000 s 절단. 모듈 업데이트에서는 2000 s 상한 제거(p.119).” 두 서술 모두 원문에 있지만 기존식/업데이트 구분이 없어 현재 사용법이 충돌한다. |
| 43 | TYPO | `실험 사승 시간` | “loading rise times available from laboratory testing” (p.49) | “실험 상승 시간.” |
| 44 | OMISSION-QUALIFIER | `1초~2000초로 잘라낸 상승 시간` | “the upper limit of 2000 seconds for loading rise time in [Eqn. 2-22] was eliminated” (p.119) | 표에 “기존 식 2-22 기준; 모듈 업데이트에서 상한 제거” 추가. 역사적 식의 기호표로 한정하면 원문 p.49와 일치한다. |
| 45 | TYPO | `계수 3개 (만상황에 따라 바꿈` / `Environmentally Assisted Crackng` | “The environmental factor, Paris power-law exponent, and sulfur-dependent load ratio exponent are varied” (p.53); “environmentally assisted cracking (EAC)” (p.48) | “환경계수·Paris 지수·하중비 지수를 상황에 따라 바꿈”; `Cracking`으로 수정. 세 매개변수라는 취지는 맞다. |
| 46 | TYPO / MISTRANSLATION | `EAC를 제안하는 조건을 나열하고` | “If any of the conditions that limit EAC are met, fatigue progresses as TCF.” (p.55) | “EAC를 제한하는 조건을 나열하고.” 뒤의 하나라도 해당하면 TCF라는 문장과 의미를 맞춘다. |
| 47 | CITE | `환경계수 , 대기중일때 7.87E-11 이고` / `p.52` | “Table 2-1. Parameters Defining Fatigue CGR Model ... Air ... 7.87E-11” (p.53) | 계수값·기호 정의가 있는 p.53 추가. p.52는 식 2-23이 시작되는 쪽이다. |
| 49 | CITE | `표 3-3의 모듈 입력 a 단위는 m` / `p.54` | “Crack depth a m >0” (Table 3-3, p.77) | p.77 추가. 식 2-24의 mm는 p.54로 맞음. |
| 50 | TYPO | `TFC 복귀 완료` | “transition from EAC back to TCF” (p.56) | TFC→TCF. |
| 51 | TYPO | `1-TFC 환경계수를 가리킴` | “C_1 ... environmental factors applied for TCF” (p.55) | TFC→TCF. 두 중복 표 객체에서 같은 오타 확인. |
| 56 | CITE | `p.61~63` | “3. CRACK GROWTH RATE MODULE” (p.68); “Routing and Pre-CGR Calculation” (p.71); “Post-CGR Calculation” (p.73) | 실제 본문 전체의 모듈 범위·호출·재료코드·후처리 근거로 p.68~73 사용. p.61~63은 일반 성장의 시간적분·균열 형상 설명으로 일부 배경에만 해당. |
| 56 | DUPLICATE/STRUCTURE | `하중비(식2-10) 사용자 입력에 따라 사이클의 최소,최대 , 평균 중 선택` | “Nominal temperature ... can be set to the minimum, maximum, or average of the temperature cycle” (p.39) | “ΔK(식2-9), 하중비(식2-10), 공칭온도(사이클 최소·최대·평균 중 선택), ΔK 문턱값(식2-11)을 계산함.” 현재 문장은 선택 대상이 하중비로 읽힌다. |
| 56 | TYPO | `매게변수` | “model parameters” (p.69) | “매개변수.” |
| 58 | TYPO | `Allou 600` | “Alloy 600” (Table 3-1, p.71) | Alloy 600. |
| 58 | CITE | `기준 온도를 바꾸면 도 에 맟춰 조정해야 함` / `p.72~76` | “as long as the power-law constant is adjusted to the specific reference temperature value using the value of the thermal activation energy” (p.79) | p.79 추가; “기준온도 변경 시 활성화에너지를 사용하여 거듭제곱 상수 α를 조정.” 수식 객체에 들어 있는 기호 자체는 미검증. |
| 59 | TYPO | `IF - improbement factor` | “Improvement factor” (p.76, p.81) | `improvement factor`. |
| 63 | TYPO | `전체 척도 사수` | “Custom model scaling constant” (p.77); user-defined parameters ([Eqn.3-3], p.73) | “전체 척도 상수.” |
| 65 | TYPO | `Prediction of lmminent Colescence` | “Prediction of Imminent Coalescence” (p.93) | `Prediction of Imminent Coalescence`. 첫 글자 I와 coalescence 철자 수정. |
| 66 | MISTRANSLATION | `(positive) 거리의 합 으로 모의할 수 있음` | “can be simulated with a positive coalescence distance” (p.94) | “양(positive)의 합체 거리로 모의할 수 있음.” 원문에는 여러 거리의 합산이 없다. |
| 66 | OMISSION-QUALIFIER | `거리기준 불확실성은 분포로 주는 것을 권장함` | “Uncertainty in the coalescence prediction may be incorporated through the use of distributed coalescence distances.” (p.98) | “합체 예측의 불확실성은 합체 거리의 분포로 반영할 수 있음.” 같은 문단의 명시적 권장은 불확실성의 epistemic 지정이다. 표면균열 삼각분포 권장과 일반 may를 구분. |
| 67 | OMISSION-QUALIFIER | `관통+관통 | ligament collapse, 사용자 지정 값, 0~20 in` | “Through-wall crack coalescence distances between 0 and 20 inches are possible ... depending on the sizes of the flaws involved.” (p.94) | “사용자 지정 값; 관심 부품에서 결함 크기에 따라 0~20 in 정도가 가능.” 보편적 허용범위나 고정 권장값으로 읽히지 않도록 조건 복원. 실제 모듈 범위는 ≥0(p.109). |
| 67 | OMISSION-QUALIFIER | `관통 + 관통 (길이관계) | 길이와 대략 1:1` | “roughly one-to-one relationship with crack length” (p.98); “This study assumed equal length for two flaws.” (p.99 각주36); “for cracks of roughly the same size” (p.121) | 대략 같은 크기 균열에 대한 해석 결과라는 조건 추가. p.99 각주36은 두 길이가 다를 때 최대길이를 쓰는 것이 합리적이라고 보는 해석도 제시한다. |
| 68 | MISTRANSLATION | `표면 + 관통 두개의 ID 길이는 합친 균열의 면적이 원래 두 균열 면적의 합과 같아지도록 정하며` | “the ID length is set such that the area of the coalesced crack is equivalent to the sum of the areas of the original two cracks” (p.95) | “표면+관통 합체 시 **새 균열의 ID 길이**를 합체 전 두 균열의 면적 합이 보존되도록 정함.” 원래 두 균열의 ID 길이를 고치는 규칙이 아니다. 69번 표는 올바르게 서술. |
| 70 | PLACEHOLDER | `이 불확실성은 coalescence 로 이어지는 복잡한 과정의 변동성과 모델 오차 (예 – 균열 길이에 대한 체계적의존성의 부재) may reflect` | “This uncertainty may reflect variability in the complex processes that lead to coalescence as well as model error” (p.98) | “이 불확실성은 합체에 이르는 복잡한 과정의 변동성과 모델 오차를 반영할 수 있음.” 현재는 영문 술어가 남은 미완성 번역. 의미 반전 ‘없음’은 현재 존재하지 않는다. |
| 70 | OMISSION-QUALIFIER | `type,location,depth,ID length,` / `OD length convention 은 논리에 뿌리를 두고 있어 큰 불확실성이 있다고 보지 않음` | “The modeling conventions for type, location, ID length, and OD length are logically rooted” (p.98) | 이 문장의 열거에서 depth 삭제. depth도 결과가 결정적이라는 앞 문장은 맞지만, 논리에 근거해 유의한 불확실성이 없다는 대상은 네 속성뿐이다. 최대깊이는 다음 문장의 물리적 기대·민감도 검토 대상으로 유지. |
| 71 | OMISSION-QUALIFIER | `잘예측된다는 실험 증거가 있으며` | “Experimental evidence suggests that the onset ... is well-predicted” (p.99) | “실험 증거는 ... 잘 예측됨을 시사하며.” 원문의 suggests를 보존. 전반 검증 문장의 generally는 이미 복원됨. |
| 71 | TYPO | `합체 모델링 conventio은` / `낮다고 사사함` | “coalescence modeling conventions”; “Higher order modeling suggests low likelihood” (p.99) | `convention은` 또는 “합체 모델링 규칙은”; “시사함.” |
| 71 | PLACEHOLDER | `[n] Reference` | 해당 표의 실제 근거는 §4.2.3 “Model Validation” (p.99) | 미완성 참조 표기 삭제하거나 완전한 보고서 서지·p.99로 교체. 각 행에 p.99가 이미 있음. |
| 72 | MISTRANSLATION / OMISSION-QUALIFIER | `적용 범위  | 실험 결과와 상위 수준 모델링으로 대체로 검증됨 | p.99` | “The convention for establishing location, ID length, and OD length ... is generally validated ...”; “This module validation applies for the full range of crack and component geometries expected within xLPR Version 2.0.” (p.99) | 현재 행을 “위치·ID/OD 길이 규칙: 실험과 상위 모델링으로 대체로 검증”으로 고치고 별도로 “검증 적용 범위: xLPR 2.0에서 예상하는 균열·부품 형상의 전체 범위”를 적을 것. 빈칸만 채우고 적용 범위 문장의 대상을 잃었다. |
| 73 | DUPLICATE/STRUCTURE | `Convention-based modeling` (두 번) | 두 번째 항목 제목은 “Crack shape idealization” (p.100) | 두 번째 제목을 “Crack shape idealization / 균열 형상 이상화”로 교체. |
| 73 | TYPO | `함께 흔히 쓰이는 모델은 이 단순화에 대한 민감도를 볼 수 있도록` | “This type of modeling is often used in association with probabilistic methods ... The model includes a range of different conventions” (p.100) | “이 모델링은 확률론적 방법과 함께 흔히 쓰임. 모델은 단순화의 민감도를 살펴볼 수 있도록 여러 합체 규칙을 포함함.” 두 문장 분리. |
| 74 | CITE | `p.103~105` | 세 항목 “Neglecting interaction between axial and circumferential cracks”, “Neglecting systematic variation in coalescence distance”, “Extension of coalescence validation to annular geometries”가 모두 p.101에 있음 | p.101로 교체. 현재 인용은 5장 모듈 설명 쪽이다. |
| 74 | OMISSION-QUALIFIER | `ID 곡률이 균열 상호작용과 ligament 붕괴 민감도에 영향을 줄 수 있음` (항목 끝) | “Uncertainty in this effect can be considered in the coalescence distance distributions.” (p.101) | 영향의 불확실성을 합체 거리 분포에 반영할 수 있다는 처리 방법 추가. 현재 문장 자체는 맞지만 이 적용 한계의 처리까지 전달하려면 보완 필요. |
| 75 | TYPO | `간 스텝은 xLPR 2.0 기본값이 1개월이며` | “the one month time step that is the default in xLPR Version 2.0” (p.111) | “시간 스텝은 ...”. 기존/현재 모두 간으로 남아 있음. |
| 75 | CITE | `입력을 줍니다(p.103). 모듈은 먼저 모든 입력이 허용 범위 안인지 확인하고, 균열 배열을 원주 위치 순으로 다시 정렬함` / `기본값이 1개월` | “Pre-Processing Requirements” (p.105); “one month time step ... default” (p.111) | 입력 제공 p.103 외에 검증·정렬 p.105, 1개월·드문 다중합체 p.111 추가. p.103은 앞 문장에만 직접 붙은 인용이므로 전체 출처 보완 사항. |
| 76 | CITE | `두 균열까지만 동시에 coalesce하면 방향은 무관하고, 세 균열 이상이 같은 시점에 coalesce할 때만 방향에 따라 달라질 수 있음` / `p.105~106` | “direction ... is irrelevant so long as no more than two cracks coalesce at the same instance in time. Coalescence of three or more cracks can lead to dependence” (p.111) | p.111 추가. 반복 절차 자체의 p.105~106은 맞음. |
| 78 | TYPO | `열 수 0~200` / `열 유형 코드는 0 = 미발생` | “Number of cracks represented ... 0 ≤ x ≤ 200” (p.109); “Crack type” (p.110) | “균열 수 0~200”, “균열 유형 코드”. heat(재료 용해 로트)로 오인할 수 있음. |
| 81 | TYPO | `lloy 82의 수소 모델 매개변수` | “the Alloy 82 hydrogen model parameters recommended are based on a database consisting of mostly Alloy 182 data” (p.117) | `Alloy 82`로 수정. XML 본문에서 확인. |
| 82 | TYPO | `LPR 2.0은` | “The xLPR Version 2.0 program does not account for the complex variation of material properties” (p.117~118) | `xLPR 2.0은`. |
| 83 | TYPO | `현제 구현된 식 3-1` | “currently implemented model form ([Eqn. 3-1])” (p.118) | “현재 구현된 식 3-1.” |
| 85 | TYPO | `log-nirmal분포` | “a log-normal distribution” (p.119) | `log-normal 분포`. XML 본문에서 확인. |
| 87 | DUPLICATE/STRUCTURE | `향후 개선 대상으로 부품 형상2.0의 기본은 세 개의 인접 환형 재료 그룹으로 나타낸 이종금속 용접이며` | “Component geometry: xLPR Version 2.0 focuses on a dissimilar metal weld geometry, represented by three material groups” (p.120) | “부품 형상: xLPR 2.0은 세 개의 인접 환형 재료 그룹으로 이종금속 용접을 나타냄. 향후 두께 방향 물성 구배·J-groove 형상 등으로 확장.” 현재형상과 향후과제 문장 접합 수정. |
| 88 | OMISSION-QUALIFIER | `균열 간섭의 2차 결정 요인이 균열 길이이고` | “the secondary determinant for crack interaction (after ligament length) is crack length” (p.120) | “ligament 길이 다음의 결정 요인은 균열 길이.” 어떤 일차 요인 다음인지 복원. 같은 문장 후반의 대략·비슷한 크기 조건은 유지되어 있음. |

## B. 두 제공 덤프의 변경 및 요청된 기존 문제 재검증

### B1. 변경 슬라이드

변경된 장은 **2, 3, 57, 64, 66, 68, 71, 75, 76, 82, 86, 88 (12장)**이다. 장 수와 번호 마커는 모두 동일하며, 제공 덤프 기준 추가·삭제·이동은 없다. 덤프에 없는 이전본 그룹 내부 텍스트 변경은 이전 PPT가 없어 확인 불가다.

| 슬라이드 | 직전→현재 변경 | 원문 대조·판정 |
|---|---|---|
| 2 | `MOUDLE`→`MODULE` | 올바른 철자 수정. 원문 3장 제목 “CRACK GROWTH RATE MODULE”(p.68)과 일치. 새 오류 없음. |
| 3 | `모듈이 기본값임`→`모듈이 기반임`; `CGW`→`CGR` | 모두 해결. “The foundation ... is a module”, “CGR predictions ... are summed”(p.18). ‘기반’은 foundation의 올바른 번역이며 default가 아니다. |
| 57 | `Meterial Group`→`Material Group` | 해결. Table 3-1의 “Material Group Numeric Code”(p.71). 새 오류 없음. |
| 64 | `pairwise colescence`→`pairwise coalescence` | 해결. “All coalescence conventions are based on pairwise coalescence”(p.93). 나머지 의미 변화 없음. |
| 66 | `ligament collaps`→`ligament collapse`; `주는것`→`주는 것` | 해당 오타·띄어쓰기 해결. “거리의 합” 오역과 일반 may를 권장으로 바꾼 부분은 **잔존**(A). p.93~98 및 문장 내 p.94,98 인용은 이번 두 덤프에서 동일하다. |
| 68 | `하용할 만한 ... 가져올것`→`사용할 만한 ... 가져올 것` | 올바른 수정. “should result in acceptable leakage continuity”(p.95). “가져올 것이라고 설명함”은 예측 성격을 유지한다. 새 오류 없음. 다만 새 균열 ID 길이의 주어 문제는 기존부터 잔존(A). |
| 71 | `발표된 연구를 적용해 conventio은`→`... convention은` | 바뀐 위치는 해결. 같은 행 앞쪽 `합체 모델링 conventio은`과 다른 행 `사사함`은 그대로 남음. “generally validated”(p.99)의 ‘대체로’는 두 제공본 모두 이미 있음. |
| 75 | `coalesce하는`→`coalesce 하는` | 의미 변화 없음. ‘시간’의 ‘시’ 누락은 두 제공본 모두 잔존. default 1개월은 p.111과 맞음. |
| 76 | `oalescence distance`→`coalescence distance` | 해결. p.106의 “The coalescence distance depends on the crack types and geometries”와 일치. 새 오류 없음. 방향의 2개/3개 구분 출처 p.111은 추가 필요. |
| 82 | `모재로`→`모재 로` | 원문 의미 변화 없음. 띄어쓰기는 “모재로”가 맞으므로 문장 품질은 되돌리는 것이 좋음. 용접금속→모재 모델 전환 설명은 p.118과 일치. 신규 과학 오류는 없음. |
| 86 | 경어체→보고체; `만하다고`→`만 하다고`; `데이더`→`데이터` | p.119의 재료 공통 ΔK 문턱 모델·독립 실험자료 필요성과 일치. 데이터 오타 해결, 신규 의미 오류 없음. |
| 88 | `교 균열의 교차 효과`→`균열의 교차 효과` | 불필요한 ‘교’ 삭제는 올바름. p.121의 “effects of the intersection of orthogonal cracks”에 부합. 신규 오류 없음. ‘2차’의 일차 기준 누락은 이전부터 잔존(A). |

### B2. 요청에 열거된 과거 문제의 현재 상태

| 과거 문제의 내용 기준 식별 | 현재 위치·판정 | 직접 근거 |
|---|---|---|
| 70 “반영할 수 없음” | **부분 해결**. 현재에는 ‘없음’이 없다. 그러나 한국어 문장이 `may reflect`로 끝나 번역 미완성. 제공된 직전 덤프도 이미 동일하여 이번 저장에서 고친 것은 아님. | p.98 “This uncertainty may reflect ...”; A의 70번. |
| 72 “적용 범위” 빈칸 | **부분 해결/대체 내용 오류**. 현재 빈칸은 아니지만 위치·ID/OD 길이 규칙 검증 문장에 해당하는 내용을 범위 행에 적었다. 실제 검증 범위와 세 속성 검증 모두 정리해야 함. 제공 직전본도 동일. | p.99 마지막 두 문장; A의 72번. |
| 66 인용에 p.98 필요 | **현재 해결**. 하단 `p.93~98`, 마지막 문장 `(p.94,98)` 확인. 두 제공본 모두 이미 포함. | 불확실성은 p.98, 길이 의존성 미구현은 p.94. |
| 3 foundation→기본값 | **이번 수정으로 해결**. 기반임으로 변경. | p.18 “The foundation ... is a module”. |
| 66 한정어 누락 | **부분 잔존**. 길이 의존성 ‘달라질 수는’은 may를 보존. 불확실성 반영 수단의 may를 ‘권장’으로 단정한 부분은 남음. | p.94 “may systematically depend”; p.98 “may be incorporated”. |
| 67 한정어 누락 | **잔존**. 0~20 in의 결함 크기 의존 조건, 약 1:1 해석의 비슷한 크기 조건이 필요. ‘대략’ 자체는 이미 있음. | p.94; p.98; p.99 각주36; p.121. |
| 71 한정어 누락 | **부분 해결**. 개요의 generally는 ‘대체로’로 보존. 표면 K 증대의 “evidence suggests”는 단정적으로 옮김. ‘가능성이 낮다’는 p.99 원문과 일치. | p.99; A의 71번. |
| 80 한정어 누락 | **현재 발견되지 않음**. 현재 문장에는 최소 5개, 최소 2개 겹침, 임의 유형·깊이·길이, 1000회, 10초 미만, 요구조건 ‘~이어야 함’이 모두 있음. 메모리 30 kB 이하도 맞음. 요구사항을 실제 측정 성능으로 오해하면 안 되지만 현재 문장은 요구로 작성됨. | p.108 “at least five cracks of arbitrary type, depth, and length—subject to at least two instances of overlapping cracks”; “shall be capable ... 1000 times in less than 10 seconds”. 현재/직전 동일. |
| 71 `[n] Reference` | **잔존**. 실제 XML과 덤프 모두 존재. | A의 71번. |
| 과거 89·90 `[n] Reference` | **현재 없음, 과거 번호 매핑 확인 불가**. 현재 89는 감사 인사이고 90은 존재하지 않음. 현재 실제 89장 전체에서 `[n] Reference`는 71번만 검출. 91장 이전본이 제공되지 않아 삭제인지 재번호인지 단정 불가. | 제공 두 덤프 89장 및 실제 PPT 89장 확인. |

## C. 제목만 보이는 슬라이드·그림·구조 점검

1. **제공 덤프에서 본문이 비어 보이는 것과 실제 제목 전용 슬라이드를 구분했다.** 5~28, 30~55, 56, 58~61, 63, 81, 84~85 등에 실제 한국어 본문/기호표가 있다. 따라서 해당 장을 덤프만 보고 빈 슬라이드로 지적하지 않았다. 실제 텍스트의 인용 불일치는 A에 기록했다. 실제 표지를 제외하고 이들 가운데 단순 제목 전용으로 판정한 장은 없다.
2. 덤프상 제목·p.NN만 보이는 장들의 큰 절 제목과 참조 쪽의 관계는 대체로 맞는다. CRACK GROWTH MODELS에 붙은 p.21~63, p.72~87, p.119는 성장 모델 또는 구현·개정값을 다루므로 다른 과학 분야로 잘못 연결된 것은 아니다. 다만 **본문별 세부 근거**로 보면 5, 6, 11, 12, 16, 27, 29, 47, 49, 56, 58 등의 인용은 부족하거나 잘못되어 A에 별도 지적했다. 74는 본문 항목의 실제 쪽과 명백히 다르다.
3. 실제 XML에서 같은/유사한 기호표가 두 개씩 있는 장: **6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 47, 49, 51, 53, 55, 59, 61, 63, 84**. 객체 중복은 확인했으나 화면에서 두 표가 보이는지 또는 한 표를 가리는지는 **확인 불가**. 시각적 중복 오류 건수에는 넣지 않았다.
4. 실제 XML의 `Text` 네 줄이 있는 장: **14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 47, 49, 51, 53, 55, 57, 59, 61, 63, 67, 69, 72, 77**. 원문 과학 내용에 대응하지 않는 객체이며 발표 전 불필요 객체 제거 점검 대상이다. 화면 노출은 **확인 불가**. 32의 명시적 입력 안내는 A에 독립 기록했다.
5. 10번의 단독 `)`와 85번의 수식이 빠져 보이는 문자열은 수식/그림의 조합까지 확인하지 않았으므로 수식 오류나 미완성 문장으로 확정하지 않았다. 85번의 log-normal 철자 오류만 확정했다. 그림 속 식·표의 수치/기호 일치는 **확인 불가**.

## 이번 텍스트 대조에서 확정 오류를 찾지 못한 슬라이드

1, 2, 3, 4, 10, 13, 14, 15, 18, 19, 20, 22, 23, 24, 26, 28, 30, 31, 34, 35, 36, 37, 38, 39, 40, 41, 42, 48, 52, 53, 54, 55, 57, 60, 61, 62, 64, 69, 77, 79, 80, 84, 86, 89

위 번호는 텍스트의 명백한 오류 미발견이라는 뜻이다. 그림·수식·레이아웃 및 위 C의 화면 노출 미확인까지 정상이라는 보증은 아니다. 개별 띄어쓰기는 의미 혼동을 일으키거나 수정 검증 대상인 경우를 중심으로 기록했다.

## 건수와 작업 상태

- A 확정 수정·보완 사항: **60행, 45개 슬라이드**. 한 행에 복수 유형이 붙어도 1건으로 계산. 한정어/문맥 보완과 인용 쪽 보완도 포함한다.
- 확정 오류 미발견: **44장**. 두 집합 합계 89장이다. C의 객체 중복·Text 노출 여부는 미확인으로 별도 관리하며 A 건수에 가산하지 않았다.
- 제공 직전본 대비 변경: **12장**, 장 수 변경 **0장**. 요청에 적힌 91장 이전본의 구조 변화는 확인 불가.
- PPT와 덤프·원문은 수정하지 않았다. 이 파일만 작성했다.
- 시작 시 `git pull` 실행은 `error: cannot open '.git/FETCH_HEAD': Permission denied`로 실패했다. 작성 후 `git add -- round40/codex.md`도 `fatal: Unable to create 'J:/Desktop/공학/ai-crosscheck/.git/index.lock': Permission denied`로 실패했다. `.git` 쓰기 제한으로 스테이징·커밋·푸시를 완료하지 못했다. 다른 기존 변경은 건드리지 않았다.

__DONE__
