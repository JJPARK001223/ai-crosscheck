# round41 독립 PPT 원문 대조

검사 대상: `J:\Desktop\XLPR\xLPR_수식 정리\2026_10_16.pptx`, 2026-10-16 15:32:06 저장, 30,679,996 bytes, **89장**. SHA-256: `47DA52F2D9963613D0FAB1BE2318D393D59470467144DF6EB3B6C9D641DF6D07`.

근거 문헌은 Kyle Schmitt, EPRI, *xLPR Models Subgroup Report—Crack Growth and Coalescence*, xLPR-MSGR-CGR Version 1.0, 2016-06-29이다. 제공된 `cgr_text.txt`와 PPT XML을 직접 읽었다. 아래 p.NN은 모두 **인쇄 쪽**이며 `=====PAGE n=====`의 n−1이다. 외부 문헌으로 주장을 보충하지 않았다. round39 결과 및 Claude 결과는 읽지 않았다. PPT와 덤프는 수정하지 않았다.

검사 방법과 한계: 1~89번 전체 본문·표·제목·쪽 표기를 확인했다. 실제 presentation.xml의 순서가 slide1~slide89 순서와 일치함을 확인했다. 덤프가 빠뜨린 Office 수식의 `m:t`도 필요한 곳에서 확인했다. 57·80번의 삽입 표 이미지는 ZIP에서 직접 읽어 시각적으로 확인했다. 전체 슬라이드를 PowerPoint로 렌더링한 검사는 수행하지 않았으므로 겹침·가려짐·화면 노출 여부는 확인 불가이다. 수식 전체를 완전 교정한 결과로 해석하면 안 된다.

**추출 중복 주의:** 6번 등에서 표가 두 번 나오는 것은 `mc:AlternateContent`의 Choice/Fallback을 덤프가 모두 읽었기 때문이다. 실제 중복 표라고 판정하지 않았다. 반대로 `Text`와 `[n] Reference`는 실제 슬라이드 객체의 텍스트로 존재한다. `Text` 객체의 상속 레이아웃 좌표는 화면 내부이나, 다른 객체에 가려지는지는 확인 불가이다.

## A. 확인된 오류 및 미완성 항목

인용은 현재 슬라이드의 문자열을 유지했다. 수식 토큰이 필요한 인용만 XML의 수식을 읽어 일반 기호로 적었으며 해당 행에 명시했다. CITE는 주장 자체의 오류와 구별하여 **그 주장 근거 쪽이 현재 출처 표기에 빠진 경우**도 포함한다. 사소한 띄어쓰기 전부를 오류로 세지는 않았다.

| 슬라이드 번호 | 유형 | 슬라이드 원문 그대로 인용 | 영어 원문 구절 인용(인쇄 쪽) | 제안 수정 |
|---|---|---|---|---|
| 5 | CITE | “26개의 heat에서 얻은 158개의 측정값으로 개발했으며” / “별도 검증 범위는” / “p.21.22” | “158 measurements across 26 different material heats” (p.23); “This model validation applies for stress intensity factors between 10-80 MPa√m and operating temperatures between 280-350°C.” (p.25) | 수치 자체는 맞음. 출처에 p.23,25 추가. 21·22쪽만으로는 26 heat와 별도 검증 범위를 찾을 수 없음. |
| 6 | CITE | “같은 용해 로트 로 만든 시편 전체 민감도 보정” / “같은 heat 안에서 시편마다 다른 변동” / “p.21” | “common factor applied to all specimens fabricated from the same material heat” / “within heat factor” (p.22) | 식은 p.21, 기호 정의는 p.21~22로 표기. |
| 7 | TYPO | “나머지 계수는 선별한 데이터에 다중회귀로 맟춰” | “a linearized multiple regression statistical model was fit to the screened database” (p.28) | “맞춰”로 수정. |
| 9 | NUMBER | “검증 범위는 수소 약 10~60cc/kg 임” | “hydrogen concentrations between roughly 1 and 60 cc(STP)/kg.” (p.37) | “수소 약 1~60 cc(STP)/kg”로 수정. K 10~80 MPa√m와 혼동하지 말 것. |
| 11 | CITE | “P의 독립 데이터 검증은 이뤄지지 않음” / “p.33~35 . 76” | “Analysis has not been performed to validate the peak-to-valley ratio against independent data.” (p.37) | 문장은 맞음. 출처에 p.37 추가. |
| 17 | TYPO | “PWSCC 비슷한 SCC를 계산해야 하 때 쓰며” | “could be used to implement SCC CGR models for these materials” (p.38) | “계산해야 할 때”로 수정. |
| 19 | MISTRANSLATION | “대부분의 경우 압축이어도 인장구간이 있어” | “fatigue cycles that are mostly compressive, but include a tensile portion, can cause growth.” (p.39) | “사이클의 대부분이 압축이더라도 인장 구간을 포함하면 성장할 수 있음.” 원문의 mostly는 사이클 내 압축 비중을 뜻하며 ‘대부분의 경우’를 뜻하지 않음. |
| 25 | TYPO | “최소제곱 직선으로 맟춘 식임” / “기름 2-10 데이터 대비 약 1.27” | “A least squares linear fit” / “relative to the data in Figure 2-10 is approximately 1.27.” (p.40) | 각각 “맞춘”, “그림 2-10”으로 수정. 1.27과 1.517배는 원문과 일치함. |
| 27 | CITE | “하중 상승 시간  표면 응력 변화율이 1000psi/hr를 넘는 구간 임” / “p.42.43.44.86” | “the span of time over which the rate of change of surface stress exceeds 1000 psi/hr during a cycle” (p.78) | 수식 토큰을 포함하면 ‘하중 상승 시간 τr은’으로 읽히며 내용은 맞음. 정의의 출처 p.78 추가. |
| 32 | PLACEHOLDER | “Text여기에 수식을 입력하십시오.” | 해당 없음: 원문 식 2-15와 alloy factor 설명(p.43)에 대응하는 내용이 아님. | 남은 ‘Text’와 수식 입력 안내 필드를 삭제. 실제 XML의 mathplaceholder 필드까지 확인됨. |
| 33 | NUMBER | “Alloy 600과 28/182/132 의 피로 계산에서 사용” | “Alloy 600 and associated weld metals (Alloys 82, 182, and 132)” (p.43) | “28”을 “82”로 수정. 제목은 이미 82로 맞음. |
| 43 | DUPLICATE/STRUCTURE | “상승시간을 1초와 2000 초로 절단함” / “식 2-22 의 상승 시간 2000초 상한은 제거됨” | “truncated at 1 and 2000 seconds” (p.49); “the upper limit of 2000 seconds ... was eliminated.” (p.119) | 두 문장 각각의 근거는 있으나 동일한 사용 방법에 상충하는 지시가 병기됨. ‘기존 식(p.49)’과 ‘개정 내용(p.119, 84번)’을 구분하여 실제 적용할 버전을 명시. |
| 46 | TYPO | “EAC를 제안하는 조건을 나열하고 , 하나라도 해당하면 TCF” | “conditions for which the material is not susceptible to EAC” (p.54); “If any of the conditions that limit EAC are met, fatigue progresses as TCF.” (p.55) | “EAC를 제한하는 조건”으로 수정. ‘제안’은 뒤의 TCF 판정과도 반대 의미임. |
| 50 | TYPO | “TFC 복귀 완료” | “the TCF curve is regained” (p.55) | 제목을 “TCF 복귀 완료”로 수정. |
| 51 | TYPO | “1-TFC 환경계수를 가리킴” | “C₁ and C_upper are the environmental factors applied for TCF and in the upper transition region for EAC” (p.55) | “1—TCF 환경계수를 가리킴”으로 수정. |
| 58 | TYPO | “기준 온도를 바꾸면 도 에 맟춰 조정해야 함” | 온도·기준온도를 사용하는 식 3-1(p.72). 덤프에서 생략된 α, Qg 토큰은 XML에 있음. | “맞춰”로 수정. 수식 토큰 누락을 실제 문장 누락으로 오인하지 말 것. |
| 59 | NUMBER | 수식 XML의 전이 수소농도 분모 지수 끝: “=2.59” (`m:t` 실제 값) | 식 3-1의 분모는 `10^(0.0111(T_C)−2.59)` (p.72); 식 2-6도 `10^(0.0111T−2.59)` (p.34). | 지수 안 `=2.59`를 `−2.59`로 수정. 덤프에는 빠져 있으나 현재 PPT의 Office 수식에 실제 등호가 들어 있음. |
| 66 | MISTRANSLATION | “(positive) 거리의 합 으로 모의할 수 있음” | “can be simulated with a positive coalescence distance.” (p.94, 표면·관통 균열 설명에 각각 등장) | “양(positive)의 합체거리로 모의할 수 있음.” 두 거리를 더한다는 뜻은 원문에 없음. |
| 66 | OMISSION-QUALIFIER | “거리기준 불확실성은 분포로 주는 것을 권장함” | “Uncertainty in the coalescence prediction may be incorporated through the use of distributed coalescence distances.” (p.98) | “합체 예측의 불확실성은 분포된 합체거리를 사용해 반영할 수 있음.” epistemic 지정은 원문이 별도로 권장하므로 다음 문장과 구분. |
| 67 | OMISSION-QUALIFIER | “관통 + 관통 (길이관계)” / “길이와 대략 1:1” | “a roughly one-to-one relationship with crack length” (p.98); “This study assumed equal length for two flaws.” (p.99 각주36); “for cracks of roughly the same size” (p.121) | “비슷한 크기의 두 관통균열에 대해 합체 시 ligament 길이와 균열 길이가 대략 1:1.” ‘대략’은 유지되었지만 연구의 균열 크기 조건은 빠짐. |
| 68 | MISTRANSLATION | “표면 + 관통 두개의 ID 길이는 합친 균열의 면적이 원래 두 균열 면적의 합과 같아지도록 정하며” | “For the coalescence of one through-wall crack and one surface crack, the ID length is set such that the area of the coalesced crack is equivalent to the sum of the areas of the original two cracks.” (p.95) | “표면+관통 합체에서는 **새로 합쳐진 균열의 ID 길이**를, 그 면적이 원래 두 균열 면적의 합과 같도록 정함.” 원래 두 균열의 ID 길이를 재설정하는 규칙이 아님. |
| 70 | TYPO | “이 불확실성은 coalescence 로 이어지는 복잡한 과정의 변동성과 모델 오차 (예 – 균열 길이에 대한 체계적의존성의 부재) may reflect더 상세한 모델이” | “This uncertainty may reflect variability in the complex processes that lead to coalescence as well as model error” (p.98) | “이 불확실성은 합체로 이어지는 복잡한 과정의 변동성과 모델 오차를 반영할 수 있음. 더 상세한 모델이 …”로 완성. ‘반영할 수 없음’은 없어졌으나 영어 술어가 미번역 상태로 남음. |
| 70 | OVERSTATEMENT | “type,location,depth,ID length,OD length convention 은 논리에 뿌리를 두고 있어 큰 불확실성이 있다고 보지 않음” | “The modeling conventions for type, location, ID length, and OD length are logically rooted” (p.98). depth는 다음 별도 문장에서 “based on physical expectation”으로 설명됨(p.98~99). | 논리적 근거로 큰 불확실성이 없다고 설명하는 목록에서 depth 삭제. depth는 최대 깊이에 대한 물리적 기대 및 민감도 연구 대상으로 따로 설명. ‘모든 출력이 deterministic’이라는 첫 문장 자체는 맞음. |
| 71 | PLACEHOLDER | “[n] Reference” | 해당 없음: 실제 근거는 Schmitt/EPRI(2016), p.99. | 실제 출처로 바꾸거나 미완성 표기를 삭제. |
| 71 | OMISSION-QUALIFIER | “두 균열 사이 ligament 가 균열 길이보다 짧아질 때 까지는 ... 가능성이 낮다고 시사함” | “This study assumed equal length for two flaws. It is believed reasonable to employ the results ... [using] the maximum flaw length” (p.99 각주36) | 같은 길이의 두 균열을 가정한 연구임을 추가하고, 길이가 다를 때 최대 균열 길이로 적용하는 것은 합리적이라고 여긴 확장임을 구분. 본문의 ‘시사함’과 ‘대체로’는 이미 살아 있음. |
| 72 | MISTRANSLATION | “적용 범위” / “실험 결과와 상위 수준 모델링으로 대체로 검증됨” | “This module validation applies for the full range of crack and component geometries expected within xLPR Version 2.0.” (p.99) | “xLPR Version 2.0에서 예상되는 균열 및 부품 형상의 전체 범위에 적용됨.” 빈칸은 채웠지만 적용 범위 대신 앞선 검증 요약을 복사해 넣었음. |
| 73 | TYPO | “이런 모델링은 개별 결정론적 모의 한 번의 결과가 주된 의미를 갖지 않는 확률론적 방법과 함께 흔히 쓰이는 모델은” | “This type of modeling is often used in association with probabilistic methods ... The model includes a range of different conventions” (p.100) | “이런 모델링은 … 확률론적 방법과 함께 흔히 쓰임. 모델은 …”으로 문장을 분리. |
| 73 | DUPLICATE/STRUCTURE | “Convention-based modeling” (같은 슬라이드에 두 번) | 두 번째 항목 제목은 “Crack shape idealization” (p.100) | 두 번째 제목을 “Crack shape idealization(균열 형상 이상화)”로 변경. |
| 76 | CITE | “두 균열까지만 동시에 coalesce하면 방향은 무관하고, 세 균열 이상이 같은 시점에 coalesce할 때만 방향에 따라 달라질 수 있음” / “p.105~106” | “direction ... is irrelevant so long as no more than two cracks coalesce at the same instance in time.” (p.111) | 설명은 맞음. 직접 근거인 p.111을 출처에 추가. |
| 78 | NUMBER | “열 유형코드 0~200” | “Number of cracks represented ... 0 ≤ x ≤ 200”; “Crack type array ... −3 ≤ x < 100” (p.109, Table 5-1) | “균열 수 0~200”으로 복구. 유형코드 범위를 말하려면 별도로 `−3 ≤ x < 100`을 표기. 다음 문장의 유형코드 의미(0, −1, −2, −3, 양의 정수)와도 구별. |
| 14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,47,49,51,53,55,57,59,61,63,67,69,72,77 | PLACEHOLDER | 각 슬라이드에 “Text” 네 번 | 해당 없음: 원문 수식·기호·입력 표의 내용이 아닌 템플릿 잔존 문자열. | 해당 본문 placeholder 객체를 삭제. XML에서 29장 모두 확인. 32번의 수식 안내 문구는 위 별도 행의 추가 항목임. 화면에서 다른 객체 뒤에 가려지는지는 확인 불가. |

덧붙여 52번의 p.73 ‘300급 오류’와 p.87 ‘203’은 **원문 자체에 함께 존재**하므로 PPT의 번호 오류로 지적하지 않는다. 원문 내부 충돌로 남겨야 하며 임의로 하나로 통일하면 안 된다. 85번의 `1.2 -8에서 0`도 덤프만 보면 수치가 깨져 보이지만 실제 XML 수식과 합치면 `log10(CGR_air)=−12에서 1.2, −8에서 0`이라는 맞는 설명이다.

## B. 직전본 대비 및 지정 수정 재검증

비교 입력인 **round40/ppt_dump.txt도 89장**이다. 지시 B의 ‘직전본 91장’은 이 파일과 일치하지 않는다. 따라서 제공되지 않은 91장본의 삭제·이동 내역을 추정하지 않았다. 현재 90·91번은 존재하지 않는다.

round40은 python-pptx 추출로 그룹 본문을 놓쳤고 round41은 XML 전체 추출이다. 예컨대 5~63번의 많은 설명 및 81·84·85번 본문이 round41에 새로 보이지만 이것만으로 실제 추가라고 할 수 없다. 제공된 직전 PPT 원본을 별도로 특정할 수 없어 그룹·수식 내부의 실제 편집 이력은 **확인 불가**이다. 표의 `[TABLE]` 표시 소실, 행/셀의 줄 분리, Choice/Fallback의 중복, 대부분의 공백 차이는 구조 개편으로 세지 않았다.

### 추가 지시의 10개 슬라이드

| 현재 번호 | 직전 덤프 대비 실제 확인되는 내용 | 원문 대조 판정 |
|---|---|---|
| 2 | 여섯 목차 항목은 직전에도 동일. 공백·줄바꿈 차이만 확인됨. | **정상/해결 상태 유지.** CGR Module과 Coalescence Module의 구분 및 순서가 원문 장 1~6과 맞음(p.19). 새로운 의미 오류 없음. |
| 3 | foundation 관련 “모듈이 기반임”은 직전에도 이미 있었음. “CGR는”→“CGR은”. | **해결 상태 유지.** foundation을 기본값으로 번역하지 않음. PWSCC·피로 모듈 및 CGR 합산 설명은 p.18과 일치. 새 오류 없음. |
| 57 | CGR·Material Group·Transient component 정의는 직전과 같음. 직전의 표(3-1) 줄바꿈은 추출 차이. | **내용 정상.** 삽입 이미지의 Table 3-1을 직접 확인했고 재료코드 1~10이 p.71과 일치. 다만 `Text` 4개 잔존은 미해결. 다른 의미 오류 없음. |
| 64 | 설명과 p.92~93은 직전과 같음. | **내용 정상.** generally에 대응하는 ‘일반적으로’, pairwise·드문 다중 합체 조건이 보존됨(p.92~93). ‘깊이 1~3mm 이상’도 p.19 각주2가 명시하므로 추가 주장으로 지적하지 않음. 새 오류 없음. |
| 66 | 본문, ‘달라 질 수는 있지만’, `(p.94,98)`, 하단 `p.93~98` 모두 직전에도 이미 있었음. | **부분 해결 상태 유지.** p.98 출처와 길이 의존성의 may는 적절함. ‘거리의 합’ 오역과 분포 반영 may→권장 변화는 여전히 남음(A표). 새로 고쳐졌다고 판정할 근거는 없음. |
| 68 | ID 길이·OD 연속성·최대 깊이 문장 모두 직전과 같음. | **부분 정상, 오역 잔존.** 최대 깊이 근거 및 OD 길이 규칙의 물리적 기대는 p.95와 맞음. ‘표면+관통 두개의 ID 길이’는 새 균열 하나의 ID 길이를 정한다는 원문과 다름(A표). |
| 71 | `conventio은`→`convention은`, `사사함`→`시사함`. | **두 오탈자 해결.** ‘대체로’·‘시사함’도 정상 유지. `[n] Reference`와 p.99 각주36의 동길이 조건 누락은 잔존. 새 의미 오류는 발견하지 못함. |
| 76 | 핵심 문장과 p.105~106은 직전과 같음. | **내용 정상.** generally→‘일반적으로’, A/B 반복 순서·방향성 설명 일치(p.105~106,111). 마지막 방향성 문장의 근거 p.111은 출처에 추가 필요. |
| 86 | 문장·수치·쪽은 직전과 같고 공백 차이만 있음. | **정상/해결 상태 유지.** acceptable, 독립성 한계, 한 주기 이상 현장 관측 설명 모두 p.119에 근거. 새 오류 없음. |
| 88 | 문장은 직전과 같고 마지막 제어문자·공백 차이만 있음. | **정상/해결 상태 유지.** ‘최근 검증 연구’, ‘대략’, ‘비슷한 크기의 균열’, ‘일 수 있음’이 p.120~121의 한정성을 유지함. 새 오류 없음. |

같은 비교에서 추가로 분명한 변경은 다음과 같다. 74번 출처 `p.103~105`→`p.101`은 **정확히 해결**되었다. 75번 `간 스텝`→`시간 스텝`, 82번 `LPR`→`xLPR`, 83번 `현제`→`현재`도 해결되었다. 78번 `열 수 0~200`→`열 유형코드 0~200`은 **새 수치-변수 대응 오류**를 만들었다. 87번은 첫 문장이 두 줄로 나뉘었지만 핵심 의미 변화는 없다. 70·72번의 문제 문장은 이미 round40 덤프에도 현재와 동일하게 있었으므로 이번 저장에서 수정된 것으로 볼 수 없다.

### B항에 주어진 기존 문제 목록의 현재 상태

| 기존 지적 | 현재 상태 | 직접 근거 |
|---|---|---|
| 70 ‘반영할 수 없음’ ↔ may reflect | **부분 해결/미완성.** 부정 오역은 없어졌으나 `may reflect`가 한국어 술어 없이 잔존. | p.98 “This uncertainty may reflect ...”; 현재/round40 모두 `... may reflect더 상세한 ...`. |
| 72 ‘적용 범위’ 빈칸 | **빈칸만 해결, 내용 미해결.** 일반 검증 문장을 넣었으며 실제 범위를 쓰지 않음. | p.99 마지막 본문 문장은 xLPR 2.0의 예상 균열·부품 형상 전체 범위를 명시함. |
| 66 출처 p.98 필요 | **해결 상태 유지.** | 본문 `(p.94,98)` 및 하단 `p.93~98`. round40에도 동일. |
| 3 foundation→기본값 | **해결 상태 유지.** | 현재 ‘모듈이 기반임’; p.18 “The foundation ... is a module ...”. |
| 66 한정어 | **부분 해결.** 길이 의존 may는 ‘달라 질 수는 있지만’으로 유지. 분포 반영 may는 권장으로 바뀌어 남음. | p.94,98 및 A표. |
| 67 한정어 | **부분 해결.** ‘약 0.75’, ‘대략 1:1’은 있음. 동등·유사 길이 조건은 없음. | p.98, p.99 각주36, p.121. `0~20 in` 자체는 p.94에 존재하며 수치 오류 아님. |
| 71 한정어 | **부분 해결.** 본문 generally·suggests는 ‘대체로’·‘시사함’으로 있음. 각주36의 연구 조건은 없음. | p.99. |
| 80 한정어 | **현재 오류 아님.** | p.108 요구사항은 ‘최소 5개’, ‘겹침 최소 2회’, ‘1000번, 10초 미만’, ‘30 kB 이하’를 그대로 명시. 현재는 요구사항으로 적었으므로 실측 성능을 단정한 것도 아님. |
| 71 `[n] Reference` | **미해결.** | 현재 XML에 실제 TextBox로 존재. |
| 과거 89·90 `[n] Reference` | **과거 번호 매핑 확인 불가.** 현재 89번에는 없고 90번은 없음. | 현재 전체 XML에서 이 문자열이 남은 곳은 71번뿐. 과거 91장본을 보지 않고 번호만으로 삭제·이동을 추정하지 않음. |

## C. 제목만 있는 슬라이드와 쪽 표기

현재본에서 p.NN이 있으면서 **실제 본문·표·수식이 없는 제목만의 슬라이드는 확인되지 않았다.** 직전 덤프에서 제목만처럼 보인 81·84·85번 등은 현재 실제 그룹 본문과 수식이 있다. 특히 84·85번의 p.119는 각각 식 6-1, 6-2 및 해당 절의 내용과 맞는다. 1·2·89번은 표지·목차·끝 인사이며 검증 대상인 p.NN 표기가 없다. 덤프의 수식 공백이나 그룹 누락을 근거로 빈 슬라이드라고 판단하지 않았다.

## 오류를 발견하지 못한 슬라이드

1, 2, 3, 4, 8, 10, 12, 13, 15, 21, 23, 29, 31, 35, 37, 39, 41, 45, 48, 52, 54, 56, 60, 62, 64, 65, 74, 75, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89

위 목록은 요청 범위의 본문·표 의미 및 출처 대조에서 오류를 발견하지 못했다는 뜻이다. 수식 전부 또는 화면 배치의 무결성을 보증하지 않는다. `Text`만 문제인 장은 이 목록에서 제외했다.

## Git 인계와 건수

시작 시 `git pull` 실행은 `error: cannot open '.git/FETCH_HEAD': Permission denied`로 실패했다. 현재 세션은 `approval_policy=never`이며 `.git`은 읽기 전용이므로 권한 승인 요청 재실행을 지원하지 않는다. 일반 재시도나 샌드박스 해제 우회는 하지 않았다. 이 결과 파일만 대상으로 `git add -- round41/codex.md`를 실행했으나 `fatal: Unable to create 'J:/Desktop/공학/ai-crosscheck/.git/index.lock': Permission denied`로 실패했다. 다른 수정·미추적 파일은 건드리지 않았다. **Git 인계 미완료: 커밋 생성 및 push 미수행, 커밋 ID와 원격 반영 확인 불가.** 자동 승인 심사의 거부가 아니라, 이 세션의 승인 요청 기능 미지원 및 파일시스템 쓰기 차단이다.

건수: A표 **31개 지적 행**(공통 `Text` 잔존 29장을 한 행으로 묶음), 이 중 NUMBER 4행, MISTRANSLATION 4행, OMISSION-QUALIFIER 3행, OVERSTATEMENT 1행, CITE 5행, PLACEHOLDER 3행, DUPLICATE/STRUCTURE 2행, TYPO 9행. 같은 슬라이드의 다른 문제는 별도 행이다. 오류·미완성 대상은 **50장**, 오류 미발견은 **39장**으로 합계 89장이다. 검증 불가 사항은 과거 91장본의 이동 내역, 추출 누락 구간의 실제 편집 이력, 전체 화면 렌더링 상태이며 오류 건수에 넣지 않았다.

__DONE__
