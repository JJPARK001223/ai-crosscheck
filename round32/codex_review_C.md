# Round 32 full audit (C): HTML p.34–47

대상: `J:\Desktop\XLPR\2026_10_13_XLPR모델분석\XLPR_발표자료_수식정리.html`의 `<section class="page ...">` 순서상 p.34–47. 같은 폴더의 다른 HTML은 각각 0개/33개 section.page이므로 대상에서 제외했다. 원시 HTML의 문장, 표 행, 수식 data-tex, 제목 및 원문 쪽수·절 번호를 대조했다. HTML은 수정하지 않았다.

유일한 근거: Kyle Schmitt, *xLPR Models Subgroup Report—Crack Growth and Coalescence*, xLPR-MSGR-CGR Version 1.0, 2016-06-29, EPRI/U.S. NRC 공동 사업 보고서(학술지 논문 아님), `(ML16341B051)Crack growth and coalescence.pdf`. 아래 p.는 모두 **인쇄 쪽수**이며 PDF 페이지 번호보다 1 작다. cgr_text.txt를 검색에 이용하고 PDF 본문과 대조했다. PyMuPDF로 인쇄 p.93, 98, 101의 도식, p.109의 표 5-1, p.119의 식 6-1·6-2를 렌더링하여 육안 확인했다.

판정은 SUPPORTED / INFERENCE / WRONG / OVERSTATED로 수행하되, 요청대로 아래에는 문제만 기재한다. 보고서가 지지하는 문장의 목록은 생략한다. 원문 인용은 위 보고서에서 가져왔다.

## p.34 합체 모델이란

- **INFERENCE — 균열 크기 예시를 깊이 기준·적용 하한으로 구체화.** HTML: “공학적으로 의미 있는 큰 균열(깊이 약 1~3 mm 이상)”. 원문 p.92, §4.1: “two adjacent macro-cracks of engineering significance (e.g., 1 to 3 mm or more)”. 여기에는 **depth**라는 한정이 없고, **e.g.**라는 예시이다. 이 문장에서 깊이의 수치 하한이 정의되었다고 읽으면 안 된다. **수정안:** “이미 파괴역학에 의해 지배되는 아임계 성장 중인, 공학적으로 의미 있는 인접한 두 거시균열(예: 크기 1~3 mm 이상)이 하나로 합쳐지는 경우를 다룹니다.”

## p.35 합체 거리: 언제 합치나

## p.36 합친 뒤 균열 모양

## p.37 가정과 한계, 검증

- **WRONG — 검증 대상인 K 증폭의 시작을 증폭 자체로 바꿈.** HTML: “표면균열의 K 증폭은 최대 깊이의 일부(0.0~0.75)인 합체 거리로 잘 예측되고”. 원문 p.99, §4.2.3: “the onset of the intensification of stress intensity factor for surface cracks is well-predicted using a coalescence distance”. 검증한 것은 **증폭의 시작(onset)**이다. 합체 거리 규칙이 K 증폭량이나 증폭 과정 자체를 잘 예측한다는 진술이 아니다. p.94는 이 과정을 xLPR 2.0의 K 계산과 성장 예측에서 다루지 않고 합체 거리로 모사한다고 명시한다. 최대 깊이 비율의 0~약 0.75 범위는 p.98에서 지지된다. **수정안:** “실험 증거는 표면균열의 K 증폭이 시작되는 시점을 균열 깊이의 일부에 해당하는 합체 거리로 잘 예측할 수 있음을 시사합니다. 최대 깊이에 대한 합체 거리 비율은 0~약 0.75입니다.”

- **OVERSTATED — 같은 평면 가정의 영향을 조건·경향 없이 단정.** HTML: “누설 확률은 다소, 누설률과 파단 감수성은 크게 증가하는 쪽입니다. 겹침이 큰 균열은 누설 확률이 약간 줄고, 누설률은 약 절반으로, 파단 감수성은 다소 줄어듭니다”. 원문 p.100, §4.3: “increase susceptibility to rupture significantly depending on the degree of axial offset”; 큰 겹침의 경우에는 “would tend to result in a slightly reduced probability of leakage”라고 하며, 이어 “Further analysis would be required to quantify the effects ... more rigorously”라고 한정한다. HTML은 축방향 어긋남 정도라는 조건과 경향적 예측이라는 강도를 생략했다. **수정안:** “원주방향 겹침이 거의 없는 경우에는 누설 확률이 다소 증가하고 누설률이 크게 증가할 것으로 설명하며, 파단 감수성의 증가는 축방향 어긋남 정도에 따라 달라집니다. 겹침이 큰 경우에는 누설 확률이 약간 감소하고 누설률은 대략 절반으로, 파단 감수성은 다소 감소하는 경향을 예상합니다. 더 엄밀한 정량화에는 추가 해석이 필요합니다.”

## p.38 합체 모듈은 어떻게 불리고 동작하나

- **OVERSTATED — 인접 균열끼리만 합체한다는 보장을 정렬 단독의 효과로 설명.** HTML: “균열 배열을 원주 위치 순으로 다시 정렬하며(이렇게 해서 합체가 인접한 균열 사이에서만 일어나게 함)”. 원문 p.105, §5.2.1.2: “Enforcement of this requirement and others discussed in Section 5.2.1.3 guarantees that pairwise coalescence will only occur between adjacent cracks.” 보장은 정렬 **및 §5.2.1.3의 다른 요구사항**을 함께 적용한 결과이다. **수정안:** “균열별 배열을 원주 위치 순으로 다시 정렬합니다. 이 정렬과 §5.2.1.3의 반복 절차 요구사항을 함께 적용하여 쌍별 합체가 인접 균열 사이에서만 일어나도록 합니다.”

## p.39 반복 적용 규칙: Crack A와 Crack B

## p.40 입력 매개변수와 플래그

## p.41 속성 갱신과 출력, 오류

- **WRONG — 오류 101~115의 범위를 모델 validation 범위처럼 표기.** HTML: “101~115는 입력이 검증 범위를 벗어난 경우”. 원문 p.111, §5.3.3: “an input that is out of its range of verification”. 원문 p.109, §5.3은 “This range is different from the range over which model validation was performed”라고 명확히 구별한다. 따라서 ‘검증 범위’만 쓰면 입력 허용 범위와 모델 validation 범위를 혼동한다. **수정안:** “101~115는 입력이 표 5-1의 입력 허용 범위(range of verification)를 벗어났음을 뜻하며, 호출 측은 실행을 종료하고 범위를 벗어난 입력을 사용자에게 알려야 합니다. 이 범위는 모델 타당성 검증(validation)에 사용된 범위와 다릅니다.” 201·210의 “범위”도 동일한 verification 범위임을 명시하면 정확하다.

## p.42 Alloy 600/82/182 PWSCC 모델 보완

- **OVERSTATED — K 의존성 개발 데이터에 대한 일반적 한정을 제거.** HTML: “낮은 K(15~20 MPa√m 미만)나 높은 K(80 MPa√m 초과)를 대표하지 못하는 데이터에서 만들었습니다.” 원문 p.117, §6.1.1: “data that do not generally represent low (<15 to 20 MPa√m) or high (>80 MPa√m) values.” **generally**가 있는 진술이므로 해당 구간을 전혀 대표하지 못하는 데이터라고 단정하지 않아야 한다. 수치와 단위는 맞다. **수정안:** “현재 K 의존성은 대체로 낮은 K(<15~20 MPa√m)와 높은 K(>80 MPa√m)를 대표하지 않는 데이터로 개발되었습니다.”

- **OVERSTATED — 발생–성장 상관의 경향을 확정 효과로 표현.** HTML: “이 상관은 가장 먼저 발생한 균열의 CGR을 높이므로 위험 평가에서 중요할 수 있습니다.” 원문 p.118, §6.1.1: “it tends to result in relatively high CGRs for the earliest initiating cracks.” 중요할 수 있다는 부분은 적절하지만 CGR을 반드시 높이는 것으로 표현한 부분은 원문보다 강하다. **수정안:** “이 상관은 가장 먼저 발생하는 균열에서 상대적으로 높은 CGR을 유발하는 경향이 있어 발전소 위험 평가에 중요할 수 있습니다.”

## p.43 다른 SCC 모델

- **OVERSTATED — Alloy 690 모델 개발 희망을 필요로 격상.** HTML: “Alloy 600 다음으로 Alloy 690과 그 용접금속(Alloy 52, 152 등)의 PWSCC 모델이 필요하며”. 원문 p.118, §6.1.2: “PWSCC CGR models are desired for Alloy 690 and its associated weld metals”. **desired**이며 의무적 필요나 구현 요구사항이라고 말하지 않는다. EPRI 패널의 개발 노력에 관한 이어지는 서술은 지지된다. **수정안:** “Alloy 600과 그 용접금속에 이어, Alloy 690과 그 용접금속(Alloy 52, 152 및 변형 합금)의 PWSCC CGR 모델 개발이 바람직하다고 설명하며, EPRI 전문가 패널에서 개발 노력이 진행 중입니다.”

## p.44 식 6-1 · 오스테나이트 합금 계수 개정

## p.45 식 6-2 · Ni계 환경계수 산포 개선안

## p.46 ΔK 문턱값과 향후 검증

## p.47 복합 성장 예측과 합체 개선

문제를 찾지 못한 페이지: **p.35, p.36, p.39, p.40, p.44, p.45, p.46, p.47**.
