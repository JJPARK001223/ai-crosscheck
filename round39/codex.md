# round39 독립 검사 — 2026_10_16 PPT

검사 대상은 `round39/ppt_dump.txt`의 89장 전체이며, 비교본은 `round38/ppt_new_dump.txt`의 91장이다. 원문은 Kyle Schmitt, EPRI, *xLPR Models Subgroup Report—Crack Growth and Coalescence*, xLPR-MSGR-CGR Version 1.0, 2016이다. 이하 영어 인용의 출처는 모두 이 문서이며 쪽은 인쇄 쪽이다. `=====PAGE n=====`의 n−1과 블록 말미 인쇄 번호를 대조했다. Claude 파일과 이전 Codex 판정은 열람하지 않았다.

PPT를 수정하지 않았다. 그림 속 수식·한국어·참고문헌과 실제 화면에서의 텍스트 가시성은 확인 불가다. 따라서 아래의 “오류 없음”은 제공된 텍스트 및 요청 C의 제목–출처 대조 범위에 한정하며, 그림의 수식까지 검증했다는 뜻이 아니다. 제목만 추출된 장을 빈 장으로 단정하지 않았다. `Text`는 덤프에 남은 문자열로서 기록하되 실제 표시 여부는 확인 불가로 구분했다. 발표자·소속·날짜·웹주소는 원문 보고서의 검증 대상이 아니다.

## A. 확인된 지적

| 슬라이드 번호 | 유형 | 슬라이드 원문 그대로 인용 | 영어 원문 구절 인용(쪽) | 제안 수정 |
|---|---|---|---|---|
| 2 | TYPO | CRACK GROWTH RATE MOUDLE | “CGR module” (p.71) | MODULE로 수정. |
| 3 | MISTRANSLATION | PWSCC 성장 속도를 환경변수와 하중변수의 함수로 예측하고 불확실성을 포함하는 모듈이 기본값임 | “The foundation of the PWSCC growth model is a module” (p.18) | “PWSCC 성장 모델의 기반은 … 모듈임”. foundation은 기본값(default)이 아니다. |
| 3 | TYPO | PWSCC와 피로의 CGW는 더해져서 프레임워크가 균열 성장 예측에 사용됨 | “CGR predictions for PWSCC and fatigue mechanisms are summed” (p.18) | CGW → CGR. |
| 10 | TYPO | ) | 대응 영어 구절 없음. p.33 본문은 PWSCC 수소 효과 모델을 설명함. | 독립된 닫는 괄호가 수식 그림과 연결되는지는 확인 불가. 불필요한 문자라면 삭제. |
| 29 | CITE | p.42 | “The roughly 60 tests available for Alloy 690 fatigue CGR in air were not sufficient…” (p.44) | Alloy 690 약 60개 시험과 재추정 설명의 출처 p.44를 추가하여 p.42,44로 표시. |
| 57 | TYPO | Meterial Group | “Material Group Numeric Code” (p.71, Table 3-1) | Material Group. |
| 64 | TYPO | pairwise colescence | “pairwise coalescence” (p.93) | pairwise coalescence. |
| 65 | TYPO | Prediction of lmminent Colescence | “Prediction of Imminent Coalescence” (p.93) | Prediction of Imminent Coalescence. 첫 글자도 대문자 I로 교정. |
| 66 | MISTRANSLATION | 균열 간섭(crack interaction)과 ligament collaps는 K 계산 . 성장 . 안정성 예측에서 다루지 않고 (positive) 거리의 합 으로 모의할 수 있음 | “can be simulated with a positive coalescence distance” (p.94) | “양의 합체 거리로 모의할 수 있음”. positive는 거리들을 더한다는 뜻이 아니다. collaps → collapse도 교정. |
| 66 | OMISSION-QUALIFIER | 거리기준 불확실성은 분포로 주는것을 권장함 | “In the absence of more detailed investigation, a triangular distribution is recommended” (p.98) | 표면균열 삼각분포 권장은 “더 상세한 조사가 없는 경우”임을 명시. 분포로 불확실성을 반영할 수 있다는 일반 설명과 특정 분포 권장의 조건을 구분. |
| 67 | OMISSION-QUALIFIER | 관통+관통 \| ligament collapse, 사용자 지정 값, 0~20 in | “between 0 and 20 inches are possible … depending on the sizes of the flaws involved” (p.94) | “대상 결함 크기에 따라 0~20 in의 합체 거리가 가능”. 고정 허용 범위로 읽히지 않도록 조건을 붙임. |
| 67 | OMISSION-QUALIFIER | 표면+표면(불확실성) \| 비는 0~약 0.75, 삼각분포 0.0 / 0.5 / 0.75 | “In the absence of more detailed investigation” (p.98) | “더 상세한 조사가 없을 때 삼각분포 권장” 추가. |
| 68 | MISTRANSLATION | 표면 + 관통 두개의 ID 길이는 합친 균열의 면적이 원래 두 균열 면적의 합과 같아지도록 정하며 | “the ID length is set such that the area of the coalesced crack is equivalent to the sum of the areas of the original two cracks” (p.95) | “표면+관통 합체 후 새 균열의 ID 길이는 … 정함”. 원래 두 균열의 ID 길이를 재설정한다는 뜻이 아니다. 69번 표는 올바르게 적혀 있음. |
| 68 | TYPO | 하용할 만한 누설 연속성 | “acceptable leakage continuity” (p.95) | “허용할 만한 누설 연속성”. |
| 70 | TYPO | 이 불확실성은 coalescence 로 이어지는 복잡한 과정의 변동성과 모델 오차 (예 – 균열 길이에 대한 체계적의존성의 부재) may reflect | “This uncertainty may reflect variability … as well as model error” (p.98) | “이 불확실성은 … 변동성과 모델 오차를 반영할 수 있음.” 부정 오역은 제거됐지만 한국어 술어가 완성되지 않음. |
| 70 | OVERSTATEMENT | 합체하는 균열마다 type,location,depth,ID length, OD length convention 은 논리에 뿌리를 두고 있어 큰 불확실성이 있다고 보지 않음 | “The modeling conventions for type, location, ID length, and OD length are logically rooted” (p.98) | 이 문장의 목록에서 depth를 제외. 깊이의 최대값 규칙은 별도 문장처럼 물리적 기대에 근거하며 민감도 검토 가능하다고 설명. “완전히 결정적”이라는 앞 문장에는 depth가 포함되는 것이 맞음. |
| 71 | PLACEHOLDER | [n] Reference | 대응 영어 구절 없음. 해당 내용은 §4.2.3 (p.99). | 실제 출처로 대체하거나 미완성 표기 삭제. |
| 71 | OMISSION-QUALIFIER | 표면균열의 응력확대계수 증대 (intensification) 가 시작되는 시점은 균열 깊이의 일부인 합체거리로 잘예측된다는 실험 증거가 있으며 | “Experimental evidence suggests that the onset … is well-predicted” (p.99) | “실험 증거는 … 잘 예측됨을 시사함”. 원문의 suggests를 보존. |
| 71 | OMISSION-QUALIFIER | 관통균열의 양 … 의 합체거리 | “This study assumed equal length for two flaws.” (p.99, 각주 36) | 해당 행에 두 결함의 길이가 같다는 연구 가정, 길이가 다르면 최대 결함 길이로 적용하는 것이 합리적이라는 저자 판단을 덧붙임. |
| 71 | TYPO | 합체 모델링 conventio은 | “coalescence modeling conventions” (p.99) | 두 곳의 conventio → convention 또는 conventions. |
| 71 | TYPO | 가능성이 낮다고 사사함 | “suggests low likelihood” (p.99) | “가능성이 낮다고 시사함”. |
| 72 | MISTRANSLATION | 적용 범위  \| 실험 결과와 상위 수준 모델링으로 대체로 검증됨 | “This module validation applies for the full range of crack and component geometries expected within xLPR Version 2.0.” (p.99) | “이 모듈 검증은 xLPR 2.0에서 예상되는 균열 및 부품 형상의 전체 범위에 적용됨.” 빈칸은 아니지만 범위 설명이 아님. |
| 72 | OMISSION-QUALIFIER | 적용 범위  \| 실험 결과와 상위 수준 모델링으로 대체로 검증됨 | “The convention for establishing location, ID length, and OD length … is generally validated” (p.99) | 적용 범위 행과 별도로 “합체 후 위치·ID 길이·OD 길이 규칙은 실험 및 상위 수준 모델링으로 대체로 검증됨” 행을 추가. 현재 일반적인 검증 문장에서 그 대상 속성이 누락됨. |
| 73 | DUPLICATE/STRUCTURE | Convention-based modeling | “Crack shape idealization” (p.100) | 두 번째 동일 소제목을 “Crack shape idealization”으로 변경. 두 번째 본문은 형상 이상화 설명임. |
| 73 | TYPO | 이런 모델링은 개별 결정론적 모의 한 번의 결과가 주된 의미를 갖지 않는 확률론적 방법과 함께 흔히 쓰이는 모델은 이 단순화에 대한 민감도를 볼 수 있도록 여러 합체 규칙(conventions)을 포함함 | “This type of modeling is often used in association with probabilistic methods … The model includes a range of different conventions” (p.100) | “… 확률론적 방법과 함께 흔히 쓰임. 모델은 … 포함함.” 두 문장을 구분. |
| 74 | CITE | p.103~105 | “Neglecting interaction between axial and circumferential cracks”; “Extension of coalescence validation to annular geometries” (모두 p.101) | p.101로 변경. 현재 인용 범위는 모듈 설명과 요구사항이며 세 가정의 출처가 아님. |
| 75 | TYPO | 간 스텝은 xLPR 2.0 기본값이 1개월이며 | “the one month time step that is the default in xLPR Version 2.0” (p.111) | “시간 스텝은 …”. |
| 76 | TYPO | oalescence distance는 | “The coalescence distance depends on” (p.106) | coalescence distance는. |
| 78 | TYPO | 열 수 0~200 … 열 유형 코드는 | “Number of cracks represented”; “Crack type array” (pp.109–110) | 각각 “균열 수”, “균열 유형 코드”. |
| 82 | TYPO | LPR 2.0은 | “xLPR Version 2.0 program” (pp.117–118) | xLPR 2.0은. |
| 83 | TYPO | 현제 구현된 식 3-1 | “currently implemented model form ([Eqn. 3-1])” (p.118) | 현재 구현된 식 3-1. |
| 83 | OMISSION-QUALIFIER | EPRI PWSCC 성장 전문가 패널에서 개발중임 | “There are efforts underway within the EPRI Expert Panel” (p.118, 2016년 보고서) | “보고서 작성 당시 EPRI … 개발 노력이 진행 중이었음”. 현재 시점의 진행 상황은 이 2016년 문서만으로 확인 불가. |
| 86 | TYPO | 실험 피로 CGR 데이더가 | “additional laboratory fatigue CGR data” (p.119) | “실험 피로 CGR 데이터가”. |
| 87 | TYPO | 향후 개선 대상으로 부품 형상2.0의 기본은 세 개의 인접 환형 재료 그룹으로 나타낸 이종금속 용접이며 | “Component geometry: xLPR Version 2.0 focuses on a dissimilar metal weld geometry” (p.120) | “향후 개선 대상에는 부품 형상이 있음. xLPR 2.0의 기본은 …”. 문장과 버전 표기를 분리. |
| 88 | TYPO | 교 균열의 교차 효과를 넣을 수 있지만 | “effects of the intersection of orthogonal cracks” (p.121) | “직교 균열의 교차 효과를 …”. |

다음은 동일 종류의 템플릿 문자열을 장마다 기록한 것이다. 영어 원문 대응은 없으며, 실제 표시 여부는 확인 불가다. 숨김 또는 마스터에서 비표시인 경우 화면상 오류로 확정하지 않는다.

| 슬라이드 번호 | 유형 | 슬라이드 원문 그대로 인용 | 영어 원문 구절 인용(쪽) | 제안 수정 |
|---|---|---|---|---|
| 14 | PLACEHOLDER | Text (4개) | 대응 없음 | 표시 여부 확인 후 불필요한 템플릿 문자열 삭제. |
| 16 | PLACEHOLDER | Text (4개) | 대응 없음 | 동일. |
| 18 | PLACEHOLDER | Text (4개) | 대응 없음 | 동일. |
| 20 | PLACEHOLDER | Text (4개) | 대응 없음 | 동일. |
| 22 | PLACEHOLDER | Text (4개) | 대응 없음 | 동일. |
| 24 | PLACEHOLDER | Text (4개) | 대응 없음 | 동일. |
| 26 | PLACEHOLDER | Text (4개) | 대응 없음 | 동일. |
| 28 | PLACEHOLDER | Text (4개) | 대응 없음 | 동일. |
| 30 | PLACEHOLDER | Text (4개) | 대응 없음 | 동일. |
| 34 | PLACEHOLDER | Text (4개) | 대응 없음 | 동일. |
| 36 | PLACEHOLDER | Text (4개) | 대응 없음 | 동일. |
| 38 | PLACEHOLDER | Text (4개) | 대응 없음 | 동일. |
| 40 | PLACEHOLDER | Text (4개) | 대응 없음 | 동일. |
| 42 | PLACEHOLDER | Text (4개) | 대응 없음 | 동일. |
| 44 | PLACEHOLDER | Text (4개) | 대응 없음 | 동일. |
| 47 | PLACEHOLDER | Text (4개) | 대응 없음 | 동일. |
| 49 | PLACEHOLDER | Text (4개) | 대응 없음 | 동일. |
| 51 | PLACEHOLDER | Text (4개) | 대응 없음 | 동일. |
| 53 | PLACEHOLDER | Text (4개) | 대응 없음 | 동일. |
| 55 | PLACEHOLDER | Text (4개) | 대응 없음 | 동일. |
| 57 | PLACEHOLDER | Text (4개) | 대응 없음 | 동일. |
| 59 | PLACEHOLDER | Text (4개) | 대응 없음 | 동일. |
| 61 | PLACEHOLDER | Text (4개) | 대응 없음 | 동일. |
| 63 | PLACEHOLDER | Text (4개) | 대응 없음 | 동일. |
| 67 | PLACEHOLDER | Text (4개) | 대응 없음 | 동일. |
| 69 | PLACEHOLDER | Text (4개) | 대응 없음 | 동일. |
| 72 | PLACEHOLDER | Text (4개) | 대응 없음 | 동일. |
| 77 | PLACEHOLDER | Text (4개) | 대응 없음 | 동일. |

## B. 직전본과의 구조·문장 비교 및 기존 문제 판정

마커 개수를 직접 세면 **91 → 89장, 순감소 2장**이다. “삭제된 3장”이라는 전제는 제공된 두 덤프와 일치하지 않는다. 앞의 1–88번은 내용 순서가 같고, 직전 89번(미래 연구 제목·Text·[n] Reference), 90번(Text·[n] Reference)이 삭제됐다. 직전 91번 “감사합니다”가 현재 89번이다. 3장이 삭제되고 새 장이 추가됐다는 증거는 덤프에서 찾지 못했다. 제목만 같은 두 장을 그림까지 같은 중복 장이라고 단정할 수 없다.

공백·슬라이드 번호·[TABLE]/[IMAGE] 마커를 제외하고 비교한 변화:

- 1번 날짜 `2026.10.15` → `2026.10.16`.
- 66번 `…구현하지 않음(p.94)` → `…구현하지 않음(p.94,98)`.
- 70번 `를 반영할 수 없음` → `may reflect`. 나머지 한국어 본문·표 내용은 동일하다. 특히 72번 적용 범위 행은 직전 덤프에서도 이미 현재와 같은 문장이며, 빈칸이 아니었다.
- 출처 추가 장: 3, 4, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 73, 74, 76, 78, 79, 81, 82, 86.
- [TABLE]/[IMAGE] 마커의 신설은 추출 표기의 차이일 수 있으므로 그림 자체가 새로 추가됐다고 판단하지 않았다.

| 기존 문제 | 현재 위치 | 판정 | 직접 대조 결과 |
|---|---|---|---|
| 70번 “반영할 수 없음” | 70 | 부분 해결 | 원문 may reflect의 부정 오역은 사라졌으나 영어 술어가 그대로 남음. A 표의 한국어로 완성 필요. |
| 72번 “적용 범위” 빈칸 | 72 | 미해결, 전제 일부 불일치 | 제공 직전본도 빈칸이 아니었음. 현재 문장은 검증의 형상 적용 범위를 설명하지 않으며 위치·ID·OD 검증 대상도 누락. |
| 66번 p.98 필요 | 66 | 해결 | p.93~98 및 본문 p.94,98이 실제 추가됨. |
| 3번 foundation → 기본값 | 3 | 미해결 | “모듈이 기본값임” 그대로임. p.18은 foundation. |
| 66번 한정어 | 66 | 미해결 | 상세 조사가 없을 때의 삼각분포 권장 조건이 여전히 없음. 다만 분포 사용 일반론 자체는 원문에서 허용됨. |
| 67번 한정어 | 67 | 미해결 | 0~20 in의 결함 크기 의존 조건 및 삼각분포 권장 조건이 없음. “대략 1:1”은 현재 보존됨. |
| 71번 한정어 | 71 | 부분 보존·잔여 문제 | 개요의 “대체로 검증(generally validated)”과 관통균열 행의 “가능성이 낮다고 … 시사” 의미는 보존됨. 실험 증거 suggests 및 각주 36의 등길이 가정은 미반영. |
| 80번 한정어 | 80 | 현재 덤프에서 해당 오류 재현 안 됨 | p.108은 “shall be capable of execution 1000 times in less than 10 seconds”; 현재도 “10초 미만이여야 함”으로 요구사항임을 보존. 최소 5개·겹침 최소 2개 조건도 보존됨. 이전에 어떤 다른 한정어가 누락됐다는 것인지는 확인 불가. ‘미만이여야’는 ‘미만이어야’로 표기 교정 가능하나 수치·의미 오류는 아님. |
| 71번 [n] Reference | 71 | 미해결 | 그대로 남음. |
| 89번 [n] Reference | 직전 89 삭제 | 해당 장 삭제로 제거 | 현재 89번은 감사 장임. |
| 90번 [n] Reference | 직전 90 삭제 | 해당 장 삭제로 제거 | 현재 90번 없음. |

66번의 “거리의 합”, 70번 논리적 규칙 목록에 depth 포함, 74번 잘못 추가된 쪽 번호 등은 기존 항목의 해결 여부와 별도로 남는 지적이다. 77번 0~20 in 균일분포는 p.111에 예시가 실제로 있으므로 근거 없는 추가 주장으로 판정하지 않았다. 62번 사용자 정의 피로 매개변수 5개도 p.73 식 3-3의 C, p, m, a, b에 대응한다.

## C. 본문 없는 장의 쪽 대조

한국어 본문이 추출되지 않은 장은 요청대로 제목과 출처 쪽의 주제 일치만 검사했다. “CRACK GROWTH MODELS”는 PWSCC·피로 식과 변수·불확실성·입력 쪽을 포괄하는 넓은 제목이므로, 보다 좁은 개별 식의 출처 적정성을 그림을 보지 않고 단정하지 않았다.

- 5–28번, 30–55번 중 제목/쪽 중심 장: 인용된 p.21–57 및 p.72–87 등은 균열 성장 모델·매개변수·구현과 관련됨. 46번 표 2-1은 원문 p.52에 존재함. 주제 수준에서 불일치 확인 안 됨.
- 56번 p.61~63은 §2.4의 CGR 시간 적분·균열 형상 갱신이다. 제목 “CRACK GROWTH RATE MODELS”와 일반 주제는 관련되나 CGR 모듈의 §3 시작 쪽이라는 뜻으로 사용한다면 맞지 않는다. 제목만으로 그 의도는 확인 불가이므로 CITE 오류로 확정하지 않음.
- 58–61번 p.72~76/p.72, 63번 p.73은 CGR 함수·사용자 정의 모델과 관련됨.
- 81번 p.117~118, 84·85번 p.119는 실제 미래 연구 권고 절에 해당함. 84·85번은 텍스트 제목·쪽만 동일하다. 그림 내용의 중복 여부는 확인 불가이며 삭제 권고를 확정하지 않음.
- 1·89번 표지·감사 장은 원문 쪽 대조 대상에서 제외. 14번 등의 Text 표기는 A 표와 별도 상태로 기록함.

오류 없음으로 판단한 슬라이드 번호(제공 텍스트와 위 제한 범위):

1, 4, 5, 6, 7, 8, 9, 11, 12, 13, 15, 17, 19, 21, 23, 25, 27, 31, 32, 33, 35, 37, 39, 41, 43, 45, 46, 48, 50, 52, 54, 56, 58, 60, 62, 79, 80, 81, 84, 85, 89.

## 건수 요약 및 실행 상태

주요 지적 표는 35행이다. Text 템플릿 잔존은 별도 28행이며 실제 표시 여부 확인 불가다. 그림·수식 검증 미수행을 “오류 없음”으로 환산하지 않았다. 구조 비교는 2장 삭제, 1장 이동이며, 기존 문제는 항목별 판정을 위 표에 기록했다.

시작 시 git pull을 실행했으나 `cannot open '.git/FETCH_HEAD': Permission denied`로 실패했다. 이 작업에서 결과 파일 이외의 파일은 수정하지 않았다. git add는 `.git/index.lock` 생성 권한 오류로 실패했다. 뒤이은 파일 지정 commit도 미등록 파일이라는 pathspec 오류로 실패했으며, git push 역시 GitHub HTTPS 연결 실패로 완료하지 못했다. 보고서는 로컬에 저장되어 있다.

__DONE__
