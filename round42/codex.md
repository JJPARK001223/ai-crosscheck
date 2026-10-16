# round42 독립 PPT 검사

검사 대상: `J:\Desktop\XLPR\xLPR_수식 정리\2026_10_16.pptx`, 2026-10-16 15:44:52 저장, 30,680,352 bytes, 89장. 현재 `round42/ppt_dump.txt` 전체, 직전 `round41/ppt_dump.txt` 전체를 읽었다. 다른 라운드의 판단 결과와 Claude 결과는 읽지 않았다. PPT 및 입력 파일은 수정하지 않았다.

원문 출처: Kyle Schmitt, EPRI, *xLPR Models Subgroup Report—Crack Growth and Coalescence*, xLPR-MSGR-CGR Version 1.0, 2016-06-29. 제공된 `cgr_text.txt` 및 `pages/p073.png`(인쇄 p.72), `pages/eq225.png`를 사용했다. 이하 쪽은 모두 **인쇄 쪽**이다. `=====PAGE n=====`는 인쇄 p.(n−1)로 대조했다. 영어 인용의 줄바꿈은 읽기 쉽게 합쳤다.

덤프에서 빈칸처럼 보이는 수학 기호는 PPT XML의 OMML(`m:oMath`)로 보완 확인했다. 따라서 5번 등의 숫자·기호가 덤프에 없다는 이유만으로 누락 판정을 내리지 않았다. 표가 두 번 나타나는 경우 중 `mc:AlternateContent`의 Choice/Fallback인 것은 실제 슬라이드 중복으로 세지 않았다. 아래의 수식 지적 59번은 덤프가 아니라 PPT XML 원문에서 직접 확인한 사항이다. 그림 자체의 내용, 최종 렌더링에서의 가림·잘림·가독성은 전수 확인하지 않았으므로 **확인 불가**이다.

## A. 현재본의 확인된 수정 필요 사항

표의 인용은 슬라이드 일부를 그대로 발췌했다. 여러 유형에 걸치는 경우 주된 유형 하나로 집계한다. CITE에는 본문 주장 중 일부의 근거 쪽이 현재 출처 범위에 없는 경우도 포함했다.

| 슬라이드 번호 | 유형 | 슬라이드 원문 그대로 인용 | 영어 원문 구절 인용(쪽) | 제안 수정 |
|---|---|---|---|---|
| 5 | CITE | “26개의 heat에서 얻은 158개의 측정값으로 개발했으며” / “별도 검증 범위는” / “p.21.22” | “158 measurements across 26 different material heats” (p.23); “This model validation applies for stress intensity factors between 10-80 MPa√m and operating temperatures between 280-350°C.” (p.25) | p.21–23,25로 보완. 26 heat와 검증 범위 자체는 맞다. |
| 6 | CITE | “같은 용해 로트 로 만든 시편 전체 민감도 보정” / “p.21” | “common factor applied to all specimens fabricated from the same material heat” (p.22) | 기호 정의가 p.22까지 이어지므로 p.21–22로 수정. |
| 7 | TYPO | “다중회귀로 맟춰” | “a linearized multiple regression statistical model was fit to the screened database” (p.28) | “다중회귀로 맞춰”. |
| 9 | NUMBER | “검증 범위는 수소 약 10~60cc(STP)/kg 임” | “hydrogen concentrations between roughly 1 and 60 cc(STP)/kg” (p.37) | “수소 약 1~60 cc(STP)/kg”. STP 추가는 맞지만 하한 10은 여전히 틀리다. |
| 11 | CITE | “P의 독립 데이터 검증은 이뤄지지 않음” / “p.33~35 . 76” | “Analysis has not been performed to validate the peak-to-valley ratio against independent data.” (p.37) | p.37을 추가. 내용 자체는 맞다. |
| 16 | CITE | “식3-1에서 섭씨() 로 명시” / “p.34” | “T = T_C + 273.15” and “10^(0.0111(T_C)−2.59)” ([Eqn. 3-1], p.72) | p.34,72로 보완. 섭씨를 쓰는 설명은 맞다. |
| 17 | TYPO | “계산해야 하 때” | “could be used to implement SCC CGR models for these materials” (p.38) | “계산해야 할 때”. |
| 19 | MISTRANSLATION | “대부분의 경우 압축이어도 인장구간이 있어” | “fatigue cycles that are mostly compressive, but include a tensile portion, can cause growth.” (p.39) | “사이클의 대부분이 압축이어도 인장 구간이 있으면”. 원문은 대부분의 **사례**에 인장 구간이 있다는 주장이 아니라 한 사이클 내 압축 구간의 비중을 말한다. |
| 21 | NUMBER | “식(2-110) 과 재료별 피로 식의 하중비 항을 계산할 때 씀” | “[Eqn. 2-11]” (ΔK_th 모델, pp.39–40) | 문맥상 ΔK_th 계산을 말하면 “식(2-11)”로 복원. R의 정의식을 가리키려면 “식(2-10)”. 식 2-110은 없다. |
| 21 | NUMBER | “하중비 계산은 식 2-9와 같이” | “Load ratio: The load ratio calculation is also based on ASME Section XI Appendix A guidance” followed by “[Eqn. 2-10]” (p.39) | “식 2-10과 같이”. 2-9는 ΔK 정의식이다. |
| 25 | TYPO | “최소제곱 직선으로 맟춘 식임” / “기름 2-10 데이터” | “A least squares linear fit to the data of Figure 2-10” (p.40) | “맞춘”, “그림 2-10”. |
| 27 | CITE | “표면 응력 변화율이 1000psi/hr를 넘는 구간 임” / “p.42.43.44.86” | “the span of time over which the rate of change of surface stress exceeds 1000 psi/hr during a cycle” (p.78) | p.78을 추가. 값과 정의는 맞다. |
| 33 | TYPO | “3차 다항식으로 맟춤” | “A third-order polynomial fit yielded” (p.43) | “맞춤”. 재료 번호 82/182/132는 올바르게 수정됐다. |
| 43 | DUPLICATE/STRUCTURE | “상승시간을 1초와 2000 초로 절단함” / “식 2-22 의 상승 시간 2000초 상한은 제거됨” | “The loading rise time is truncated at 1 and 2000 seconds” (p.49); “the upper limit of 2000 seconds ... was eliminated” (p.119) | “초기 식 2-22: 1~2000 s로 절단. §6.2.1의 개정: 2000 s 상한 제거”로 버전을 구분. 두 문장 모두 원문에 있지만 현재 사용 지침으로 연달아 제시하면 상충한다. |
| 46 | TYPO | “5. ∆K가 (식 2-25) 위 일경우 EAC 이면 황 0.004 ~ 0.013%는 초과는” | “If any of the conditions that limit EAC are met, fatigue progresses as TCF.”; “medium sulfur materials (0.004% to 0.013% ... ) and high sulfur materials (>0.013% ...)” (p.55) | “5. ΔK가 ΔK_c(식 2-25)를 초과하면 TCF. 위 제한 조건이 없으면 EAC: 황 0.004~0.013 wt%에는 C₂, 0.013 wt% 초과에는 C₃.”로 문장을 분리. 덤프의 빠진 기호는 OMML로 확인했지만 한국어 연결부 자체는 깨져 있다. |
| 50 | TYPO | “TFC 복귀 완료” | “the TCF curve is regained” (p.55) | “TCF 복귀 완료”. |
| 51 | TYPO | “1-TFC 환경계수를 가리킴” | “C₁ ... environmental factors applied for TCF” (p.55) | “1–TCF 환경계수를 가리킴”. |
| 56 | MISTRANSLATION | “피로 계산 전에 (식2-9), 하중비 (식2-10) 사용자 입력에 따라 사이클의 최소,최대 , 평균 중 선택 , threshold값 (식2-11)을 미리 계산함” | “calculates stress intensity factor range, load ratio, temperature, and stress intensity factor range threshold” (p.71); “nominal temperature ... minimum, maximum, or average of the temperature cycle” (p.39) | ΔK(2-9), R(2-10), **공칭 온도(온도 사이클의 최소·최대·평균 중 선택)**, ΔK_th(2-11)를 별도로 열거. 현재 문장은 선택 대상인 온도를 빠뜨려 하중비를 선택하는 것처럼 읽힌다. |
| 58 | TYPO | “기준 온도를 바꾸면 도 에 맟춰 조정해야 함” | Reference temperature and scaling constant are model inputs ([Eqn. 3-1], p.72; input table p.76) | 수학 기호 α, Q_g는 XML에 있다. “기준 온도를 바꾸면 α도 Q_g에 맞춰 조정해야 함”에서 “맞춰”로 수정. |
| 59 | NUMBER | PPT 수식 XML: “0.0111”, “𝑇𝑐”, “=2.59” (같은 10의 지수 안에 존재) | denominator “10^(0.0111(T_C)−2.59)” ([Eqn. 3-1], p.72, `pages/p073.png`로도 확인) | 등호 `=2.59`를 빼기 `−2.59`로 수정. 현재 지수는 `0.0111(T_c)=2.59`여서 원문과 다르다. 단순 텍스트 추출의 착시가 아니라 `<m:t>=2.59</m:t>`가 실제로 있다. |
| 68 | OVERSTATEMENT | “합친 균열의ID 길이를 면적 합이 보존되도록 정하며” | “For the coalescence of one through-wall crack and one surface crack, the ID length is set such that the area ... is equivalent to the sum” (p.95) | “표면균열 하나와 관통균열 하나가 합체할 때는”을 복원. 표면+표면, 관통+관통에서는 두 원래 균열의 ID 길이를 감싸는 호 길이이다. 69번 표는 이 구분을 맞게 쓰고 있다. |
| 70 | MISTRANSLATION | “모델 오차 (예 – 균열 길이에 대한 체계적의존성의 부재) may reflect더 상세한 모델이” | “This uncertainty may reflect variability ... as well as model error” (p.98) | “이 불확실성은 합체에 이르는 복잡한 과정의 변동성과 모델 오차(예: 균열 길이에 대한 체계적 의존성 부재)를 반영할 수 있음. 더 상세한 모델이 …”로 완결. 기존 부정 오역은 없어졌지만 번역이 완료되지 않았다. |
| 70 | OMISSION-QUALIFIER | “관통균열의 합체 거리를 개별 프로그램 실행에서는 deterministic 으로 가정하고” | “Alternatively, ... may be assumed to be deterministic for individual program runs” (p.98, 주35) | “대안으로, 개별 실행에서는 결정론적 값으로 가정할 수도 있고”로 선택 가능성을 표시. 기본 의무 처리로 읽히지 않게 한다. |
| 70 | OVERSTATEMENT | “type,location,depth,ID length,OD length convention 은 논리에 뿌리를 두고 있어 큰 불확실성이 있다고 보지 않음” | “The modeling conventions for type, location, ID length, and OD length are logically rooted and are therefore not considered subject to significant uncertainties.” (p.98) | 이 목록에서 depth를 제외. 깊이의 최대값 convention은 바로 다음 별도 문장처럼 물리적 기대에 근거하며 실행별 민감도 검토 대상이라고 설명. ‘출력이 결정적’이라는 앞 문장의 목록에는 depth가 들어가는 것이 맞다. |
| 72 | MISTRANSLATION | “적용 범위” / “실험 결과와 상위 수준 모델링으로 대체로 검증됨” | “This module validation applies for the full range of crack and component geometries expected within xLPR Version 2.0.” (p.99) | 적용 범위 행을 “xLPR Version 2.0에서 예상되는 균열 및 부품 형상의 전체 범위”로 수정. 현재 내용은 검증 **방법·정도**를 반복하며 적용 **범위**를 설명하지 않는다. |
| 72 | TYPO | “대체로 검증됨표면균열과 관통균열의 합체를” | “are generally validated ...” and footnote 37 “While there is not experimental data involving ... a surface crack and a through-wall crack” (p.99) | “대체로 검증됨. 표면균열과 관통균열의 합체를 …”로 문장 분리. 실험 자료 부재를 명시한 내용 자체는 맞다. |
| 73 | TYPO | “확률론적 방법과 함께 흔히 쓰이는 모델은 이 단순화에 대한 민감도를 볼 수 있도록” | “This type of modeling is often used in association with probabilistic methods ... . The model includes a range of different conventions” (p.100) | “이러한 모델링은 … 확률론적 방법과 함께 흔히 쓰임. 모델은 이 단순화에 대한 민감도를 …”로 분리. 현재는 두 문장이 잘못 연결돼 있다. |
| 76 | CITE | “두 균열까지만 동시에 coalesce하면 방향은 무관하고, 세 균열 이상이 같은 시점에 coalesce할 때만 방향에 따라 달라질 수 있음” / “p.105~106” | “direction ... is irrelevant so long as no more than two cracks coalesce at the same instance in time” (p.111) | p.111을 추가. 내용은 정확하다. |
| 78 | NUMBER | “열 유형코드 0~200” | “Number of cracks represented ... 0 ≤ x ≤ 200”; “Crack type array ... −3 ≤ x < 100” (p.109, Table 5-1) | “표현되는 균열 수: 0~200개. 균열 유형 배열: −3 이상 100 미만의 정수.” 유형 코드와 균열 수를 구분. 뒤의 “열 유형 코드”도 “균열 유형 코드”로 수정. |
| 80 | TYPO | “10초 미만이여야 함” | “execution 1000 times in less than 10 seconds” (p.108) | “10초 미만이어야 함”. 성능 수치·조건은 원문과 맞다. |
| 84 | CITE | “모듈 구현 후 ASME Code Case N-809가 바뀌면서 갱신된 값임” / “스테인리스 재료 코드는 6.7.8 임” / “p.119” | “has been revised further ... since the implementation” (p.118); Material Groups 6–8 (p.71, Table 3-1) | p.71,118–119로 보완. 식 6-1의 숫자와 재료 조합은 p.119와 맞다. |
| 87 | TYPO | “향후 개선 대상으로 부품 형상2.0의 기본은” / “같은 예가 있음)을듬” | “Component geometry: xLPR Version 2.0 focuses on a dissimilar metal weld geometry” / “Subsurface flaws may arise ... lack of fusion of an overlay” (p.120) | “향후 개선 대상인 부품 형상: xLPR 2.0의 기본은 …”, “같은 예가 있음)을 듦”으로 문장 경계를 정리. |

### 미완성 템플릿 문구

다음은 PPT XML에 실제 텍스트로 남은 PLACEHOLDER이다. 영어 원문에 대응하지 않으며, 학술 내용의 오역으로 세지 않는다. 레이아웃의 body placeholder(idx=13)는 슬라이드 영역 안에 위치한다. 다만 다른 개체에 가려져 실제 발표 화면에서 보이는지는 **확인 불가**이다. 하나의 미완성 개체를 슬라이드별 1건으로 집계한다.

| 슬라이드 번호 | 유형 | 슬라이드 원문 그대로 인용 | 영어 원문 구절 인용(쪽) | 제안 수정 |
|---|---|---|---|---|
| 14 | PLACEHOLDER | “Text” (4회) | 대응 원문 없음(템플릿 잔존) | 미완성 텍스트 개체 삭제. |
| 16 | PLACEHOLDER | “Text” (4회) | 대응 원문 없음(템플릿 잔존) | 동일. |
| 18 | PLACEHOLDER | “Text” (4회) | 대응 원문 없음(템플릿 잔존) | 동일. |
| 20 | PLACEHOLDER | “Text” (4회) | 대응 원문 없음(템플릿 잔존) | 동일. |
| 22 | PLACEHOLDER | “Text” (4회) | 대응 원문 없음(템플릿 잔존) | 동일. |
| 24 | PLACEHOLDER | “Text” (4회) | 대응 원문 없음(템플릿 잔존) | 동일. |
| 26 | PLACEHOLDER | “Text” (4회) | 대응 원문 없음(템플릿 잔존) | 동일. |
| 28 | PLACEHOLDER | “Text” (4회) | 대응 원문 없음(템플릿 잔존) | 동일. |
| 30 | PLACEHOLDER | “Text” (4회) | 대응 원문 없음(템플릿 잔존) | 동일. |
| 32 | PLACEHOLDER | “Text” (4회), “여기에 수식을 입력하십시오.” | 대응 원문 없음(템플릿 잔존) | 미완성 개체 및 빈 수식 안내 삭제. |
| 34 | PLACEHOLDER | “Text” (4회) | 대응 원문 없음(템플릿 잔존) | 동일. |
| 36 | PLACEHOLDER | “Text” (4회) | 대응 원문 없음(템플릿 잔존) | 동일. |
| 38 | PLACEHOLDER | “Text” (4회) | 대응 원문 없음(템플릿 잔존) | 동일. |
| 40 | PLACEHOLDER | “Text” (4회) | 대응 원문 없음(템플릿 잔존) | 동일. |
| 42 | PLACEHOLDER | “Text” (4회) | 대응 원문 없음(템플릿 잔존) | 동일. |
| 44 | PLACEHOLDER | “Text” (4회) | 대응 원문 없음(템플릿 잔존) | 동일. |
| 47 | PLACEHOLDER | “Text” (4회) | 대응 원문 없음(템플릿 잔존) | 동일. |
| 49 | PLACEHOLDER | “Text” (4회) | 대응 원문 없음(템플릿 잔존) | 동일. |
| 51 | PLACEHOLDER | “Text” (4회) | 대응 원문 없음(템플릿 잔존) | 동일. |
| 53 | PLACEHOLDER | “Text” (4회) | 대응 원문 없음(템플릿 잔존) | 동일. |
| 55 | PLACEHOLDER | “Text” (4회) | 대응 원문 없음(템플릿 잔존) | 동일. |
| 57 | PLACEHOLDER | “Text” (4회) | 대응 원문 없음(템플릿 잔존) | 동일. |
| 59 | PLACEHOLDER | “Text” (4회) | 대응 원문 없음(템플릿 잔존) | 동일. |
| 61 | PLACEHOLDER | “Text” (4회) | 대응 원문 없음(템플릿 잔존) | 동일. |
| 63 | PLACEHOLDER | “Text” (4회) | 대응 원문 없음(템플릿 잔존) | 동일. |
| 67 | PLACEHOLDER | “Text” (4회) | 대응 원문 없음(템플릿 잔존) | 동일. |
| 69 | PLACEHOLDER | “Text” (4회) | 대응 원문 없음(템플릿 잔존) | 동일. |
| 72 | PLACEHOLDER | “Text” (4회) | 대응 원문 없음(템플릿 잔존) | 동일. |
| 77 | PLACEHOLDER | “Text” (4회) | 대응 원문 없음(템플릿 잔존) | 동일. |

## B. 직전본 대비 변화와 지정 문제 재판정

### 실제 구조와 모든 텍스트 변경

round41과 round42의 마커를 세면 **각각 89장**이다. 요청의 “직전본 91장”은 제공된 직전 덤프와 일치하지 않는다. 해당 91장 파일은 제공되지 않아 삭제된 장의 내용·번호 대응은 **확인 불가**이다. 제공된 두 덤프 사이에서는 장 추가·삭제가 없고, 같은 장 번호를 대응시킬 수 있다.

두 덤프의 차이는 아래 8개 장에 있다. 아래 이외의 텍스트 차이는 없었다. 추출 방식 차이 때문에 두 덤프에 잡히지 않은 내용의 변경까지 없다고 단정하지 않는다.

| 현재 슬라이드 | 직전 → 현재 | 원문 대조 판정 |
|---|---|---|
| 9 | “반영할때” → “반영할 때”; “약 10~60cc/kg” → “약 10~60cc(STP)/kg” | 띄어쓰기·STP는 적절. 하한은 여전히 1이어야 함(p.37). |
| 21 | “식(2-11)” → “식(2-110)” | 새 식 번호 오류 발생. p.39–40의 식은 2-10,2-11이다. |
| 33 | “Alloy 600과 28/182/132” → “Alloy 600과 82/182/132” | **해결**. p.43의 적용 재료와 일치. |
| 46 | “EAC를 제안하는 조건” → “EAC를 제한하는 조건” | **해결**. p.55의 “conditions that limit EAC”와 일치. 남은 문장 연결 문제는 A에 별도 기록. |
| 66 | “(positive) 거리의 합” → “양의(positive) 합체 거리” | **해결**. p.94의 “positive coalescence distance”와 일치. |
| 68 | “표면 + 관통 두개의 ID 길이는” → “합친 균열의ID 길이를” | **새 오류**. 면적 보존 규칙의 적용 대상(표면+관통)이 사라짐(p.95). |
| 71 | “[n] Reference” 삭제; “잘예측” → “잘 예측” | **해결**. 본문 의미 변화 없음. |
| 73 | 두 번째 “Convention-based modeling” → “Crack shape idealization” | **해결**. p.100의 소제목 및 해당 내용과 일치. |

### 기존 문제 목록 재판정

| 지정 문제 | 현재본 판정 | 직접 확인한 근거 |
|---|---|---|
| 70 “반영할 수 없음” vs “may reflect” | **부분 해결, 미완료** | 부정 문장은 없어졌지만 “may reflect더”가 번역되지 않은 채 남음. p.98은 “반영할 수 있음”. |
| 72 “적용 범위” 빈칸 | **빈칸만 해소, 내용 미해결** | 채워 넣은 문구가 “대체로 검증됨”. p.99의 실제 적용 범위는 예상되는 균열·부품 형상의 전체 범위. |
| 66 출처 p.98 필요 | **해결** | 현재 출처 p.93~98이고 본문에도 “(p.94,98)”가 있음. 분포·epistemic 논거는 p.98에서 확인. |
| 3 foundation → “기본값” | **해결** | 현재 “모듈이 기반임”; p.18 “The foundation ... is a module”. 현재 “기본값”은 없음. |
| 66 한정어 누락 | **현재 문구는 적절** | “모의할 수 있음”, “달라 질 수는 있지만”, “권장함”으로 can/may/recommended를 보존. “양의 합체 거리” 수정도 정확(p.94,98). |
| 67 한정어 누락 | **현재 표에서 추가 오류 확인하지 못함** | “0~약 0.75”, “길이와 대략 1:1”, “기본값 0”은 p.94,98과 부합. 0~20 in도 p.94에 가능한 범위로 나옴. 설명이 짧다는 이유로 없는 오류를 확정하지 않음. 템플릿 Text는 별도. |
| 71 한정어 누락 | **해결/현재 표현 적절** | “대체로 검증(generally validated)”, “가능성이 낮다고 시사함”으로 p.99의 generally/suggests low likelihood를 보존. 실험 증거에 관한 문장도 원문의 의미와 일치. |
| 80 한정어 누락 | **해당 없음/성능 조건 정확** | p.108은 성능 **요구사항**이다. “shall be capable”, 최소 5개 균열, 최소 2건 중첩, 1000회, 10초 미만, 메모리 ≤30 kB를 정확히 옮김. may/generally를 임의로 넣을 근거 없음. 오탈자 1건은 A 참조. |
| 71 “[n] Reference” | **해결** | round41에는 있으나 round42에서는 삭제됨. |
| 구 89·90 “[n] Reference” | **현재본 잔존 없음; 구 번호 대응 확인 불가** | 현재 89는 “감사합니다”, 90은 존재하지 않음. 현재 전체 덤프에 “[n] Reference” 없음. 제공된 round41도 89장이므로 구 91장본과의 대응은 확정할 수 없음. |

### 사용자가 지정한 10개 슬라이드 재검증

| 슬라이드 | 판정 | 원문 근거 및 남은 사항 |
|---|---|---|
| 2 | 현재 목차 적절, round41 대비 변화 없음 | p.19의 report organization과 순서·주제가 일치. 참고문헌을 목차에 따로 싣지 않은 것은 내용 오류로 보지 않음. |
| 3 | foundation 오역 **해결**, round41 대비 변화 없음 | p.18과 부합. “모듈이 기반임”은 맞고, PWSCC·피로 합산 및 세 재료군 설명도 맞음. |
| 57 | 추출된 한국어 의미 적절, round41 대비 변화 없음 | CGR 정의와 Material Group/표3-1 설명은 pp.68–71과 맞음. 삽입 그림의 표 숫자 전수 검증은 **확인 불가**. Text 4개는 남음. |
| 64 | 일반적 재료 독립성 한정어 적절, round41 대비 변화 없음 | “일반적으로 재료와 무관하게”는 p.93 “generally applicable irrespective of material”. 1~3 mm의 예, 미세균열 제외, pairwise 적용은 pp.92–93 및 p.19 주2와 부합. |
| 66 | “거리의 합” 수정 **해결**, 새 의미 오류 확인하지 못함 | pp.94,98. 출처 범위·가능성 표현도 맞음. |
| 68 | 수정 후 **새 범위 확대 오류** | p.95에서 면적 보존은 표면+관통 조합에 한정. 기존 문장이 갖고 있던 조합 조건이 빠짐. |
| 71 | reference 삭제 및 띄어쓰기 **해결** | p.99와 부합. generally·suggests가 유지됨. |
| 76 | 순회 순서·방향성 설명 정확, round41 대비 변화 없음 | pp.105–106,111. 내용의 새 오류는 없으나 출처에 p.111 보완 필요. |
| 86 | 독립 데이터 및 현장 검증 설명 적절, round41 대비 변화 없음 | p.119: 다른 예측에 predominantly 의존, 일부 not independent, 현장 균열 one or more cycles. 현재 문장이 이를 정확히 반영. |
| 88 | 본문 적절, round41 대비 변화 없음 | pp.120–121: crack length가 ligament length 다음의 secondary determinant; 비슷한 크기의 균열에서 붕괴 ligament와 균열 길이가 roughly one-to-one. 현재 “비슷한 크기의 균열” 및 “대략 1:1” 유지. |

‘round41 대비 변화 없음’은 제공된 두 텍스트 덤프의 비교 결과이다. 사용자가 그보다 앞선 파일에서 수정했는지, 그림·렌더링이 바뀌었는지는 그 말로 판단하지 않는다.

## C. 제목만 있는 슬라이드와 확인 한계

현재 89장 중, 내용이 없는 제목 슬라이드에 p.NN만 달린 사례는 텍스트·XML 검사에서 확인되지 않았다. 표지 1, 목차 2, 마지막 89에는 논문 본문과 대조할 인용 쪽이 없다. 70·71 등은 제목 아래 표가 있으므로 제목만 있는 슬라이드가 아니다. 57도 표·그림이 있으므로 빈 슬라이드로 처리하지 않았다.

수식의 OMML 전수 텍스트를 읽어 기호 공백을 보완했지만, 수식 전체의 모든 괄호·위첨자·렌더링을 원문 이미지와 전수 대조한 검사는 아니다. 따라서 이 보고서의 “오류 없음”은 **한국어 본문·표·출처 및 확인 가능한 기호 범위에서 추가 오류를 찾지 못함**을 뜻하며 그림 내용까지 완전 검증했다는 뜻이 아니다. 원문 자체의 p.73(300급 오류)과 p.87(203 오류) 설명 차이는 52번이 두 쪽을 구분해 그대로 소개하므로 PPT 오역으로 세지 않았다. p.49와 p.119의 상승시간 상한 변경도 원문에 실제로 존재하며, A의 43번 지적은 이 버전 구분을 분명히 하자는 것이다.

## 오류 없음으로 판단한 슬라이드

1, 2, 3, 4, 8, 10, 12, 13, 15, 23, 29, 31, 35, 37, 39, 41, 45, 48, 52, 54, 60, 62, 64, 65, 66, 71, 74, 75, 79, 81, 82, 83, 85, 86, 88, 89

## Git 인계

시작 시 `git pull`을 실행했으나 `error: cannot open '.git/FETCH_HEAD': Permission denied`로 실패했다. 결과 작성 후 지정 파일만 대상으로 `git add -- round42/codex.md`를 실행했으나 `.git/index.lock: Permission denied`로 실패했다. 현재 실행 환경은 `approval_policy=never`이며 `sandbox_permissions`를 제공할 수 없어 권한 승인 재시도 기능이 지원되지 않는다. 같은 일반 명령을 반복하거나 샌드박스를 우회하지 않았다. 따라서 커밋·푸시는 수행하지 못했으며 Git 인계는 미완료, 커밋 ID·원격 반영은 확인되지 않았다. 다른 작업의 수정·삭제·미추적 파일은 건드리지 않았다.

## 건수 요약

집계는 A의 표 행 기준이며, B의 해결·재판정 행은 중복 집계하지 않는다.

- 총 89장 중 수정 필요 53장, 추가 오류를 찾지 못한 슬라이드 36장.
- 수정 필요 **61건**: 본문·수치·출처·오탈자 등 32건 + 템플릿 개체 잔존 29건.
- 유형별: NUMBER 5, MISTRANSLATION 4, OVERSTATEMENT 2, OMISSION-QUALIFIER 1, CITE 7, DUPLICATE/STRUCTURE 1, TYPO 12, PLACEHOLDER 29, ADDED-CLAIM 0.
- 두 덤프 모두 89장. 변경된 텍스트가 있는 장 8개. 실제 중복 장·빈 장은 확인되지 않음.
- 그림 내용·가독성 전수 검사 및 구 91장본의 장 번호 대응은 확인 불가. Git 커밋·푸시 인계 미완료.

__DONE__
