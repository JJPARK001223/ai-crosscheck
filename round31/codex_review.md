# Round 31 Codex 교차검증

대상: `J:\Desktop\XLPR\2026_10_13_XLPR모델분석\XLPR_발표자료_수식정리.html`의 원시 HTML. `<section class="page">` 47개, `<div class="chap">` 6개를 확인했다. 신규 감사 대상은 p1, p2, p30, p34–p43, p46, p47의 15페이지다. p3–p29, p31–p33, p44–p45의 기존 수식·설명은 심층 재감사하지 않았다. 장 구분과 헤더는 별도로 확인했다.

유일한 내용 근거: Kyle Schmitt, EPRI, *xLPR Models Subgroup Report—Crack Growth and Coalescence*, xLPR-MSGR-CGR Version 1.0, 2016-06-29, NRC ADAMS ML16341B051. 아래 p.는 모두 **인쇄 쪽수**이며 PDF의 물리적 페이지 번호는 +1이다. 제공된 `cgr_text.txt`와 PDF에서 새로 추출한 layout 텍스트를 대조했고, Table 3-1(PDF 72 / 인쇄 71)과 Table 5-1(PDF 110 / 인쇄 109)을 렌더링하여 확인했다. 외부 자료·외부 지식은 사용하지 않았다. 보고서가 설명하는 구현·시험 결과를 확인한 것이며 실제 Fortran 코드 실행이나 성능 실측을 했다는 뜻은 아니다.

판정: **SUPPORTED** = 원문에 직접 근거가 있음; **INFERENCE** = 설명상 해석·축약·범위 확대이고 그 표현 자체의 직접 근거는 없음; **WRONG** = 원문과 불일치. 한 문장 안에 다른 판정이 있으면 주장 단위로 분리했다. 일반 제목·“아래 표” 같은 편집 지시문은 기술 주장과 구별했다. 문장별 전체 판정은 부록에 기록했다.

## 1 틀린 점

### W1. p30: 전처리 전체를 “식 2-9~2-12”로 설명한 것은 부정확 — WRONG

HTML: “피로 계산 전에 ΔK, 하중비, 온도, ΔK 문턱값을 식 2-9~2-12로 미리 계산합니다.”

원문 §3.2.1.2, p.71의 정확한 설명:

> In preparation for the fatigue CGR function, the module calculates stress intensity factor range, load ratio, temperature, and stress intensity factor range threshold in accordance with the descriptions given in Section 2.3.1.

§2.3.1 p.39–40에서 ΔK는 식 2-9, 하중비는 식 2-10, ΔK 문턱값은 식 2-11이다. **명목 온도는 식 2-9~2-12에 없다.** p.39의 명목 온도 문단은 사용자 입력에 따라 온도 사이클의 최소·최대·평균을 고른다고 설명한다. 식 2-12는 28개 자료에 대한 별도 선형 적합식이며, 공통 구현 문턱값 식으로 선택한 것은 식 2-11이다(§2.3.1 p.42). 수정안: “§2.3.1에 따라 ΔK(2-9), 하중비(2-10), 명목 온도(최소·최대·평균 선택), ΔK 문턱값(2-11)을 전처리한다.”

### W2. p30: 모듈 반환값을 “성장량”이라고 부름 — WRONG(물리량 명칭)

HTML: “모듈이 돌려준 성장량을 적분해 …”

§3.1 p.69의 원문:

> The sum of all CGRs is returned to the Framework for integration.

§3.2.1.4 p.73도 기본 출력은 합산 **CGR**이라고 명시한다. 모듈이 반환하는 것은 성장량이 아니라 성장률이다. HTML 자체의 후처리 문단은 이 점을 정확히 설명하므로 문서 내부 용어도 일관되지 않다. “반환한 성장률을 시간 적분해”로 수정하면 된다.

### W3. p41: “10초 이내”는 엄밀한 성능 요구와 다름 — WRONG(경계값)

HTML: “1000번 실행이 10초 이내여야 합니다.”

§5.2.1.7 p.108 원문:

> For a case with the existence of at least five cracks of arbitrary type, depth, and length—subject to at least two instances of overlapping cracks—the coalescence module shall be capable of execution 1000 times in less than 10 seconds.

정확한 요구는 **10초 미만**이다. 30 kB **이하**, 균열 **최소 5개**, 겹침 사례 **최소 2개**, **1000회**는 맞다. “겹치는 경우가 2회”는 시간에 따른 두 번의 사건으로 읽힐 수 있으므로 “최소 두 겹침 사례가 있는 구성”이 더 정확하다. 이것은 성능 요구사항이며 이 문장만으로 실측 성능을 주장할 수는 없다.

### W4. p30: 사용자 입력/비하드코딩 문단의 쪽수 — WRONG(인용 위치)

HTML은 “식의 매개변수 상당수는 소스 코드에 박혀 있지 않고 사용자 입력입니다(p.71)”라고 한다. 내용은 SUPPORTED이지만 정확한 원문 위치는 §3.1 **p.70**(PDF 71)이다. 원문: “Numerous parameters of these model forms are user inputs to the xLPR program (i.e., they are not hardwired into the source code).” 이 한 문장의 괄호 인용에서 PDF 페이지와 인쇄 쪽수가 섞였다.

## 2 원문에 직접 근거 없는 해석

### I1. p30 Table 3-1의 코드 6–9 PWSCC “모델 없음” — INFERENCE(모델 개발과 계산 경로의 구별 누락)

§2.2.4.2 p.38은 SS·페라이트강에 대해 “no SCC CGR model was developed to support xLPR Version 2.0”이라고 한다. **재료별 SCC 모델을 개발하지 않았다**는 뜻에서는 HTML의 축약은 근거가 있다. 그러나 제목이 “재료 코드와 쓰이는 식”이므로 해당 코드에 **계산 경로가 없다**고 읽으면 틀리다. §3.2.1.3 p.72는 사용자 정의 재료 외의 모든 재료에서 PWSCC 활성 시 식 3-1을 사용한다고 명시한다. 비감수성 재료는 mechanism flag 또는 α=0으로 비활성화할 수 있다. p.38에는 범용 식 2-8도 있다.

권장 표기: “정상 PWR용 재료별 권장 SCC 모델/값 미개발; PWSCC 활성 시 공통 식 3-1 경로, 비활성화 가능.” 코드 4–5의 “합의된 모델 없음, 값 미제공”은 p.38·81의 직접 근거가 있으나 역시 계산 경로가 없다는 뜻이 아님을 덧붙이는 것이 필요하다.

### I2. p35: “양의 거리 하나” — INFERENCE(0을 포함하는 정의의 축약)

양의 합체 거리가 간섭·붕괴를 대리한다는 p.94 문장 자체는 근거가 있다. 다만 이를 모든 쌍의 정의로 확장하면 0을 배제한다. 같은 페이지의 혼합 쌍 기본 거리는 0이고, p.98 삼각분포의 최솟값도 0이며, Table 5-1 p.109의 거리 입력 검증 범위는 ≥0이다. “0 이상인 합체 거리”로 설명하면 전체 규칙과 일치한다. **0~20 in를 모듈 입력의 강제 상한으로 볼 근거는 없으며**, HTML은 이를 가능한 범위/분포 예로 표현하므로 그 부분은 틀렸다고 판정하지 않았다.

### I3. p34: “재료와 상관없이” — INFERENCE(한정어 생략)

p.93 원문은 “generally applicable irrespective of material”이다. HTML의 단정적 표현은 원문의 “일반적으로”를 생략했다. “일반적으로 재료와 무관하게 적용”이 정확하다. 보고서 밖의 재료·환경에 대한 검증 완료 주장으로 확대해서는 안 된다.

### I4. p47: “2.0은 세 재료 그룹의 이종금속 용접” — INFERENCE(기본 형상만 요약)

p.120은 세 인접 환형 재료 그룹을 기본으로 설명하지만 바로 이어 “Weld overlay or onlay may be modeled with a fourth material group.”이라고 명시한다. 세 그룹 설명은 근거가 있으나 xLPR 2.0의 모든 표현 능력을 세 그룹으로 제한하는 해석은 근거가 없다. “기본 이종금속 용접은 세 인접 환형 그룹; overlay/onlay는 네 번째 그룹 가능”으로 보완할 필요가 있다.

### I5. p2: “이 정리 자료는 … 2장부터 6장까지의 식을 다룹니다” — INFERENCE(자체 편집 설명)

PDF가 뒷받침할 수 있는 문장은 아니라 HTML의 편집 범위 설명이다. 새 자료는 1장 요약과 다수의 무수식 페이지도 포함하므로 “보고서 1–6장의 요약과 2–6장 관련 식을 다룬다”가 실제 구성에 더 맞는다. 물리적 모델 오류는 아니다.

## 3 빠진 중요한 내용

아래는 문장을 틀렸다고 판정하는 항목과 구별한 누락이다. 수식 상세를 다시 감사하지 않고 신규 개요가 독자에게 알려야 할 조건·한계·운영 정보를 우선했다.

| HTML 위치 | 중요한 누락 | 보고서 근거(인쇄 쪽수) |
|---|---|---|
| p30 코드 3 | Alloy 82 IF=2.6은 모델링한 PWSCC가 **오직 Alloy 82에 존재한다고 확인된 특수 경우**에만 적용. 보통 용접부 전체 Ni계 용접금속에는 더 높은 Alloy 182 CGR을 가정한다. 숫자 2.6 자체는 맞지만 적용 조건이 빠졌다. | §2.2.2.2 p.28 각주 7; Table 3-4 p.82 |
| p30 코드 2·3 | 수소 효과를 켜면 단순히 수소항만 곱하는 것이 아니라 활성화에너지·스케일·불확실성 입력도 해당 권장 세트로 바뀐다. Alloy 82에도 수소 포함/미포함 선택이 적용된다. | §2.2.3.2 p.34–35; Table 3-4 p.82 |
| p30 Ni계 피로 | 코드 1–5가 식 2-13/14를 사용하고 용접 f=2인 것은 맞지만 온도 함수는 600/82/182/132에 식 2-17, 690/52/152에 식 2-18을 적용한다. 표가 모든 Ni계의 매개변수까지 같다는 인상을 주지 않도록 구분 필요. | §2.3.2.2 p.43–44 |
| p30 SS 피로 | Table 3-1 코드 6에 316L이 있는 것은 원문 그대로. 그러나 §6.2.1의 후속 계수 개정은 316L을 304L·304LE와 함께 묶는다. 재료 식별 코드와 개정된 계수 그룹을 구별해야 한다. | Table 3-1 p.71; §6.2.1 p.118–119 |
| p30 코드 9 | EAC 여부와 균열 전진 정보는 위치별 영구 메모리에 저장하며 Framework가 crack-location index를 제공해야 한다. 현재 스텝 입력만으로 완결되는 무기억 함수가 아니다. ΔKb<ΔKth이면 비종료 300번대 오류를 기록한다. | §3.2.1.3 p.73; §3.2.2.1 p.75 |
| p30 개요 | 허용 입력 범위 이탈은 치명적 오류이고, 입력 검증 범위와 물리 모델 validation 범위는 다르다. 성능 요구는 ≤20 kB, 21,600회 호출 <30초, 여러 재료군·양쪽 메커니즘·최소 5개 천이 성분 조건이다. | §3.2.1.5 p.74; §3.3 p.76 |
| p35·p37 | 합체 거리의 체계적 변화 미반영은 **균열 길이뿐 아니라 부품 두께**와도 관련된다. 짧은 균열에는 대체로 조기 합체, 긴 균열에는 대체로 지연 합체 편향이 예상된다. 보수성은 거리 입력에 따라 달라진다. | §4.3 p.101 |
| p36·p37 | 표면+관통은 실제로 상당히 비대칭일 수 있으며 세 형상 제한 때문에 천이형으로 근사한다. 비대칭 사다리꼴의 네 번째 형상이 향후 완화책이다. 혼합 조합은 실험적 직접 검증이 아니라 형상 선택의 공학적 판단이 포함된다. | §4.2.1.2 p.94–95; p.99 각주 37; Table 5-2 p.116 |
| p37 coplanar | 겹침이 적으면 누설확률·누설률·파단 감수성이 증가하는 쪽, 겹침이 크면 누설률 약 절반 및 누설확률·파단 감수성 감소 가능. “항상 보수적이지 않다”의 근거와 지표별 차이가 빠졌다. | §4.3 p.100 |
| p37 axial | 직교 균열 교차가 crack blunting으로 한 균열을 정지시킬 수 있어 이를 무시하는 가정은 누설·안정성에 대해 보수적이라고 설명한다. 원주 소구간당 공학적 크기의 축균열은 최대 하나로 모델링한다. | §4.3 p.101 |
| p37 곡률 | 작은 반경의 pressurizer nozzle 또는 큰 균열에서 ID 곡률 영향이 중요할 수 있고, 그 불확실성을 합체 거리 분포로 고려할 수 있다. | §4.3 p.101 |
| p38–p39 절차 | 입력 검증 뒤 원주 위치 순으로 재정렬, 미발생·흡수·축균열 제외, 활성 원주균열 2개 미만이면 인수를 그대로 반환. 인접 균열끼리만 쌍별 합체하도록 요구한다. | §5.2.1.1–5.2.1.2 p.105 |
| p39 구현 | 방향 2는 형상을 미러링·재인덱싱한 뒤 기본 시계 순회를 실행하고 종료 후 되돌린다. B의 각도를 A보다 크게 재정의하여 원주 경계를 처리한다(350°/20°→350°/380°). | §5.4 p.112–113 |
| p40 입력·단위 | Table 5-1의 균열 수 **0–200**; crack type **−3≤x<100**; 중심 **0≤x<2π rad**; ID/OD 입력은 **반길이(m)**; 거리 규칙 1 modifier와 관통 거리는 **m**, 규칙 2 modifier는 무차원. 따라서 in 예시를 실제 모듈 입력에 그대로 넣으면 안 된다. | Table 5-1 p.109(렌더 확인) |
| p40·p41 코드 | 미발생 0, 표면 −1, 천이 −2, 이상화 관통 −3, 흡수 양의 정수. 방향 배열은 원주 1/축 2이다. 흡수 표시는 HTML에 있지만 나머지 값은 없다. | §5.3.1 p.110 |
| p41 오류 | **0** 정상, **101–115** 입력 범위 이탈(종료), **201·210** 계산 출력 범위 이탈(종료), **301** 한 호출 쌍별 합체 >1(비종료). 301의 빈도를 Framework가 추적하고 자주 발생하면 반대 방향으로 재실행하여 편향을 확인해야 한다. “기록만 남김”만으로 운영 지침은 완전하지 않다. | §5.3.3 p.111–112 |
| p41 출력 | 갱신된 배열 외에 쌍별 합체 횟수 자체도 반환한다. 모든 입력 벡터는 같은 길이이며 입력·출력 순서는 발생 시간 순이다. Index Transformation은 원주 위치 순서와 매핑한다. | §5.2.2 p.108; §5.3.3 p.111 |
| chapter 5 전체 | 실제 구현은 DLL/Coalesce2, 소스 Coalesce_v1.6.f90. V&V는 **정적 51개·동적 72개**, 동적 45개 합체 구성(MATLAB 대조)+26개 입력 오류+1개 성능; 이상 14건 모두 해결·종결. 51개 요구사항(45 module-level+6 interface)과 정적 시험 51개를 혼동하지 말아야 한다. | §5.2 p.104; §5.4 p.112–113; §5.5 p.115 |
| chapter 5 검증 | Table 5-2의 validation 권장 범위: surface distance rule=2, modifier 0–0.75, TW 거리 0–20 in, depth rule=1. Table 5-1의 허용 입력 범위(거리≥0, rule 1/2, depth 1/2/3)와 다르다. 모든 조합의 동일 수준 직접 검증을 주장할 수 없다. | Table 5-1 p.109; Table 5-2 p.116 |
| p42 hybrid/cold work | hybrid 모델 도입 시 PWSCC 매개변수·불확실성을 재적합해야 한다. 냉간가공 의존성 추가 또는 가공 범위별 모델 개발이 제안된다. | §6.1.1 p.117 |
| p42 경계·상관 | 계면/희석 별도 모델은 없지만 butt-weld 현장 경험은 저Cr 재료 계면 부근 Alloy 82/182의 뚜렷한 선호 균열을 보이지 않았다. 발생–성장 상관의 정량화에는 계획된 실험을 제안한다. | §6.1.1 p.118 |
| p47 복잡 형상 | overlay/onlay의 네 번째 재료 그룹; 비대칭 원인인 off-axis bending·용접내 감수성 변동; subsurface flaw의 예인 overlay lack of fusion과 위험 영향; 비동일평면/내부결함 처리를 위한 Framework–Models 공동 개발 필요가 빠졌다. | §6.3.1 p.120 |

Section 1의 8개 업무는 모두 들어 있다. 공동 작업 그룹 이름(K-Calculation Models Subgroup, Inputs Group, Framework Group)과 Alloy 132의 일본 PWR 용도 각주 생략은 이 수준의 요약에서 중요한 왜곡으로 보지 않았다. p43과 p46은 주요 논지를 충실히 요약한다.

## 4 쪽수·절 번호 점검

### 장과 절의 매핑 — 모두 SUPPORTED

| HTML 장 | 원문 절 | 원문 시작 인쇄 쪽수 | 판정 |
|---|---|---:|---|
| INTRODUCTION | §1 | 17 | SUPPORTED |
| CRACK GROWTH MODELS | §2 | 20 | SUPPORTED |
| CRACK GROWTH RATE MOUDLE | §3 | 68 | SUPPORTED |
| CRACK COALESCENCE MODEL | §4 | 92 | SUPPORTED |
| CRACK COALESCENCE MODUEL | §5 | 103 | SUPPORTED |
| RECOMMENATIONS FOR FUTURE WORK | §6 | 117 | SUPPORTED |

영문 장 제목의 MOUDLE/MODUEL/RECOMMENATIONS 오타는 사용자 지정이므로 오류로 처리하지 않았다. 실제 HTML 장별 페이지는 1장 p1–2, 2장 p3–29, 3장 p30–33, 4장 p34–37, 5장 p38–41, 6장 p42–47이다. 번호 1–47의 누락·중복은 없다.

### 신규 페이지 헤더

| HTML | 현재 헤더 | 판정·필요한 보완 |
|---|---|---|
| p1 | p.17–19 / §1.1 | §1.1은 p.17–18. p.19는 이 페이지의 8개 업무와 기준의 근거가 아님. **WRONG(정밀 범위)**: p.17–18로 좁히기. |
| p2 | p.18–19 / §1.2–1.4 | SUPPORTED. |
| p30 | p.68–73 / §3.1–3.2.1.4 | 기본 module flow와 routing은 SUPPORTED. MRP 등의 출처 문장은 p.68의 §3 도입부. 표의 코드 1 P=1은 p.81, IF 권장값은 p.28·82, Ni계 식·f 값은 p.42–44, SS 식은 p.48, 페라이트 식은 p.52, 합의 모델 없음은 p.38·81. **헤더만으로 표 전체 근거가 완결되지 않음**: 관련 §2.2–2.3, §3.3.2 및 쪽수 추가. |
| p34 | p.92–93 / §4.1, §4.2.1 | 핵심은 SUPPORTED. 세 형상·재료 일반 적용은 §4.2 도입부 p.93이므로 §4.2도 표시하면 정확함. |
| p35 | p.93–94,98 / §4.2.1.1,§4.2.2 | SUPPORTED. |
| p36 | p.94–95 / §4.2.1.2 | SUPPORTED. |
| p37 | p.98–101 / §4.2.2–4.3 | 자체 모델 내용 SUPPORTED. 순회 방향은 §5.2.1.3 p.106 및 §5.3.2 p.110–111: 관련 근거 추가. |
| p38 | p.103–104 / §5.1 | module overview SUPPORTED. 1개월 기본값과 다중 합체 희소성은 p.111/§5.3.2: 헤더 관련 근거 추가. |
| p39 | p.105–106 / §5.2.1.3 | A/B 절차 SUPPORTED. 시계1/반시계2 및 동시 2개 이하 방향 무관은 §5.3.2 p.110–111: 관련 근거 추가. |
| p40 | p.106,110–111 / §5.2.1.4,§5.3.2 | SUPPORTED. 단위·허용 범위를 추가하면 Table 5-1 p.109도 표시. |
| p41 | p.107–108 / §5.2.1.5–5.2.1.7 | SUPPORTED. 구체 오류코드를 보완하면 §5.3.3 p.111–112도 추가. |
| p42 | p.117–118 / §6.1.1 | SUPPORTED. |
| p43 | p.118 / §6.1.2 | SUPPORTED. |
| p46 | p.119 / §6.2.3–6.2.4 | SUPPORTED. |
| p47 | p.120–121 / §6.3.1–6.3.2 | SUPPORTED. |

기존 수식 페이지는 헤더의 식 위치만 확인했다. p3–p13: 식 2-1(21), 2-2(27), 2-3~2-5(33), 2-6(34), 2-8(38), 2-9~2-10(39), 2-11~2-12(40); p14–p19: 2-13~2-14(42), 2-15~2-17(43), 2-18(44); p20–p28: 2-19(48), 2-20~2-22(49), 2-23(52), 2-24(54), 2-25(55), 2-26~2-27(56); p29 §2.4.1–2.4.2(61–63); p31–p33: 3-1~3-2(72),3-3(73); p44–p45: 6-1~6-2(119). 모두 해당 헤더의 쪽수·절과 일치한다. 기존 본문에 대한 이전 검토 결론을 재심사했다는 뜻은 아니다.

## 5 확인된 점(짧게)

§1.1의 8개 업무, Table 3-1의 10개 코드·재료명, 재료별 피로 주식, 합체 후 유형·깊이·중심·ID/OD 길이, Crack A/B 절차는 원문과 일치한다. 방향 1/2, 표면 거리 규칙 1/2, 깊이 규칙 1/2/3, 삼각분포 0/0.5/0.75, TW 거리 0–20 in 균일분포 예, 301 비종료 경고, 30 kB 상한도 맞다. 향후 과제의 주요 논지는 원문에 근거한다. 각 문장·표 행의 판정은 아래에 기록했다.

### 부록: 신규 페이지 문장·표 행별 판정

행의 주장 표현은 HTML 문장/표 행을 짧게 식별하기 위한 축약이다. 한 행 안에서 나열한 주장들은 표시된 쪽수에서 각각 확인했다. WRONG와 INFERENCE는 위 항목으로 연결했다. 문장 안의 괄호 설명·수치도 판정에 포함했다.

| 위치 | 문장·표 행의 주장 | 판정 / 인쇄 쪽수 |
|---|---|---|
| p1 업무1 | 1.0 시범 PWSCC 모델·불확실성 검토 / 대체로 수용 가능 | SUPPORTED p.17 |
| p1 업무2 | PWSCC 개선 / 매개변수 유연화·용접간 변동 포함 | SUPPORTED p.17 |
| p1 업무3 | 피로 구현 여부·방법 / 천이 정의·K 천이 변환·CGR 구조 공동 개발 | SUPPORTED p.17 |
| p1 업무4 | 피로 CGR 구현 / 재료별 3종 | SUPPORTED p.17 |
| p1 업무5 | BWR SS IGSCC 조사 / PWR 한정이라 2.0 미개발 | SUPPORTED p.17 |
| p1 업무6 | 52/152 PWSCC 조사·구현 업무 / 유연 모듈·IF, 입력 개발은 프로젝트 외부 | SUPPORTED p.17–18; **52/152의 완성된 권장 모델을 구현했다는 뜻 아님** |
| p1 업무7 | module V&V / 구현 정확성·실험/현장 CGR 일치 확인 | SUPPORTED p.18 |
| p1 업무8 | 합체 모듈 구현 / 보고서에 모델·모듈 설명 | SUPPORTED p.18 |
| p1 요약 | xLPR 풀네임·2.0, 정상 PWR 일정/반복 하중, 성장·합체 모델 선택·모듈화 보고 | SUPPORTED p.17 |
| p1 기준 | 독립변수, 불확실성, 현장/실험 일치, 구현 용이성, 기술/산업 선례 5개 | SUPPORTED p.17 |
| p1 개발 | Framework 통합용 모듈 및 요구·설계·소스·V&V 문서 | SUPPORTED p.17 |
| p2 PWSCC-1 | 환경·하중 함수와 불확실성 포함 모듈 | SUPPORTED p.18 |
| p2 PWSCC-2 | 정상 PWR 600 및 82/182/132 권장 입력 | SUPPORTED p.18 |
| p2 PWSCC-3 | 기타 재료 입력 미제시, PWSCC 없음/600 대비 훨씬 낮음의 증거 | SUPPORTED p.18 |
| p2 피로-1 | 피로도 같은 방식의 모듈 | SUPPORTED p.18 |
| p2 피로-2 | Ni계/오스테나이트SS/페라이트 3 하위 모델 | SUPPORTED p.18 |
| p2 피로-3 | PWSCC+피로 CGR 합산하여 Framework 사용 | SUPPORTED p.18 |
| p2 합체-1 | 규칙 기반, coplanar circumferential, engineering scale 약1–3mm+, 종류·형상·위치 기반 | SUPPORTED p.19·각주2 |
| p2 합체-2 | K 증폭/ligament 소성붕괴, 단독 아임계 성장보다 빠른 현상 대리 | SUPPORTED p.19 |
| p2 합체-3 | 매개변수 실험·파괴역학 검증 | SUPPORTED p.19; 개별 조합의 근거 수준은 별도 |
| p2 범위-1 | primary piping·DMW/SMW·정상 PWR SCC/피로 CGR 목표 | SUPPORTED p.19 |
| p2 범위-2 | Framework의 이상화 균열 조합 예측 | SUPPORTED p.19 |
| p2 구성-1 | 1~7장 순서와 내용 | SUPPORTED p.19 |
| p2 구성-2 | 정리 자료의 2~6장 식 범위 | INFERENCE 자체 설명/I5 |
| p30 표제 | Table3-1+§3.2.1.3+§2의 식 연결 표 | SUPPORTED p.71–73; Table3-1 자체는 코드·재료 두 열만 있음 |
| p30 코드1 | 600=1, PWSCC3-1/2-1·P=1, 피로2-13/14 | SUPPORTED p.71–72,21,42,81–82 |
| p30 코드2 | 182/132=2, 수소 미포함2-2/포함2-3, Ni계 피로·f=2 | SUPPORTED p.71–72,27,33,42–44 |
| p30 코드3 | 82=3, PWSCC3-1·IF2.6, Ni계 용접 f2 | SUPPORTED p.71–72,28,44,82; IF 적용 조건 누락 |
| p30 코드4 | 690=4, 합의 PWSCC 모델·값 없음, Ni 피로 f1 | SUPPORTED p.38,43,71–72,81 |
| p30 코드5 | 52/152=5, 합의 PWSCC 모델·값 없음, Ni 피로 f2 | SUPPORTED p.38,44,71–72,81 |
| p30 코드6 | 304/316L SS 및 용접=6, 피로2-19 | SUPPORTED p.71,73,48 |
| p30 코드7 | 316 SS 및 용접=7, 피로2-19 | SUPPORTED p.71,73,48 |
| p30 코드8 | 304L/304LE SS 및 용접=8, 피로2-19 | SUPPORTED p.71,73,48 |
| p30 코드9 | CS/LAS·용접·모재 HAZ=9, 피로2-23 TCF/EAC | SUPPORTED p.71,73,52–53 |
| p30 코드6–9 | PWSCC “모델 없음” | INFERENCE p.38의 개발 부재를 축약/I1; 계산 경로는3-1 |
| p30 코드10 | custom=10, PWSCC3-2, 피로3-3 | SUPPORTED p.71–73 |
| p30 기호 | CGR 명칭, Material Group 코드, 피로 transient component | SUPPORTED p.68–71 |
| p30 필요-1 | 주어진 재료·환경·하중 조건의 CGR 계산 | SUPPORTED p.68 |
| p30 필요-2a | Framework가 균열별·위치별 입력, 표면 최심점·끝점 | SUPPORTED p.68 |
| p30 필요-2b | “반환한 성장량” 적분 | WRONG W2; p.69 반환은 CGR |
| p30 호출① | 범위 검증, 오류 반환 | SUPPORTED p.68,70 |
| p30 호출② | 재료·메커니즘 입력 선택·함수 routing | SUPPORTED p.69,71 |
| p30 호출③a | ΔK·R·T·ΔKth 전처리 | SUPPORTED p.71 |
| p30 호출③b | 위 모두 “식2-9~2-12”로 처리 | WRONG W1; p.39–42 |
| p30 호출④ | PWSCC 한 번·피로 활성 천이별 호출·합산 | SUPPORTED p.69 Figure3-1; 선택한 활성 메커니즘에 한함 |
| p30 재료 | 현재 균열 위치 코드·mechanism flag로 PWSCC/피로/양쪽 선택 | SUPPORTED p.71 |
| p30 후처리-1 | da/dN×현재 사이클 수/스텝시간으로 시간율 변환 | SUPPORTED p.73 |
| p30 후처리-2 | PWSCC+모든 천이 피로 CGR 반환 | SUPPORTED p.73 |
| p30 후처리-3 | PWSCC 또는 피로 음수/NaN이면200번대 | SUPPORTED p.73 |
| p30 범위-1 | 모듈은 CGR만 계산 | SUPPORTED p.69 |
| p30 범위-2 | 시간·균열 전선 위치 적분 bookkeeping은 Framework | SUPPORTED p.69 |
| p30 범위-3 | TIFFANY/K-solution, 합체/천이/안정성 모듈 담당 구분 | SUPPORTED p.69–70 |
| p30 범위-4 | 많은 입력값이 소스 hardwire가 아님 | SUPPORTED p.70; HTML의 본문 괄호 p.71은 WRONG(인용 쪽수), 정확히 p.70 |
| p30 근거 | PWSCC MRP55/115/263, fatigue N643-2/N809/CR6721 | SUPPORTED p.68 |
| p34 기호 | ID/OD, ligament 뜻 | SUPPORTED p.93 Figure4-1, p.92 |
| p34 이유-1 | 정밀 파괴역학 대신 규칙으로 빠른 조합 모사 | SUPPORTED p.92 |
| p34 이유-2 | 간섭 K 증폭/성장 가속과 TW ligament 완전소성 실패 | SUPPORTED p.92 |
| p34 범위-1 | 성장 중 macro1–3mm+, micro-fissure 초기 합체 제외 | SUPPORTED p.92 |
| p34 범위-2a | coplanar·반타원SC/천이TW/이상화TW | SUPPORTED p.93 |
| p34 범위-2b | 무조건 “재료와 상관없이” | INFERENCE I3; 원문 generally/p.93 |
| p34 적용-1 | pairwise | SUPPORTED p.93 |
| p34 적용-2 | 드문3개 이상 동일 시점/위치 합체는 쌍별 순차 | SUPPORTED p.93 |
| p34 적용-3 | Monte Carlo에서 개별 예측 중요도 작아 단순 규칙 정당화 | SUPPORTED p.93 |
| p34 판정 | 최소ID ligament<거리이면 임박, 두 균열을 하나로 대체 | SUPPORTED p.93 |
| p34 안내 | 다음2페이지가 거리·형상 설명 | SUPPORTED HTML p35–36 자체 구성 |
| p35 SC행 | 사용자 절대거리/최대깊이×계수, 후자 권장 | SUPPORTED p.94 |
| p35 SC행 수치 | best0.5·0~약0.75·triangular min0/mode0.5/max0.75 | SUPPORTED p.94,98 |
| p35 SC행 근거 | 깊이·간섭 의존, ASME IWA3000 half-depth미만 안정성 전 합침 | SUPPORTED p.94 |
| p35 TW행 | 사용자 거리0–20in 가능·ligament collapse | SUPPORTED p.94; 강제 입력 상한 아님 |
| p35 혼합행 | 기본0·알려진ASME 고려없음·실제ligament없음 | SUPPORTED p.94 |
| p35 기호 | ligament<합체거리이면 합체 | SUPPORTED p.93 |
| p35 이유-1 | “양의 거리 하나”로 모사 | INFERENCE I2; p.94 양의 거리 설명을 전체로 일반화 |
| p35 이유-2 | 유형 쌍마다 근거 달라3종 구별 | SUPPORTED p.94 |
| p35 사용-1 | 쌍에 따라 거리 결정 | SUPPORTED p.94 |
| p35 사용-2 | 분포로 불확실성·정밀모델로 줄이므로epistemic 권장 | SUPPORTED p.98 |
| p35 길이-1 | TW 길이 의존2.0 미구현 | SUPPORTED p.94 |
| p35 길이-2 | 개발 후 분석 거리:길이≈1:1 | SUPPORTED p.98 |
| p36 종류행 | SC+SC→SC/천이+천이→천이/이상화+이상화→이상화/상이종→천이 | SUPPORTED p.94 |
| p36 깊이행 | TW포함시두께, SC+SC min/max/avg·max권장 | SUPPORTED p.95 |
| p36 중심행 | ID를 감싸는 arc의 중심 | SUPPORTED p.95 |
| p36 OD행 | OD 감싸는arc길이, SC+SC0, SC+TW원TW OD | SUPPORTED p.95 |
| p36 ID행 | 동류SC/TW쌍 arc길이, 혼합쌍 면적합 보존 | SUPPORTED p.95 |
| p36 기호 | 세 균열 유형·합친 깊이 | SUPPORTED p.94–95 |
| p36 이유-1 | 계속 계산하려면 인식가능 세 형상으로 재정의 | SUPPORTED p.94 |
| p36 이유-2 | 물리적 기대·논리적 고려로 규칙 설정 | SUPPORTED p.94 |
| p36 사용-1 | 표 규칙으로 속성 결정 | SUPPORTED p.94–95 |
| p36 사용-2 | ID arc중심=새중심 | SUPPORTED p.95 |
| p36 사용-3 | 혼합 면적합 보존으로 안정성 예측 연속성 도모 | SUPPORTED p.95 |
| p36 사용-4 | OD 규칙으로 누설 연속성 도모 | SUPPORTED p.95; 보장/증명이 아니라 도모 |
| p36 max근거 | re-entrant K 증폭이 대략 대칭회복 때까지 지속하리란 기대 | SUPPORTED p.95 |
| p37 검증-1 | 실험·higher-order해석으로 대체로validation | SUPPORTED p.99 |
| p37 검증-2 | SC K증폭 개시를 depth분율0–0.75거리로 예측 | SUPPORTED p.99 |
| p37 검증-3 | ligament<crack length 전 rapid tearing 가능성 낮음 | SUPPORTED p.99 |
| p37 검증-4 | SC+TW 직접 실험없음 | SUPPORTED p.99 각주37 |
| p37 전제-1 | 규칙이 역학 계산 대리 | SUPPORTED p.100 |
| p37 전제-2 | 원주coplanar·axial합체제외 | SUPPORTED p.100–101 |
| p37 전제-3 | coplanar항상보수적아님·많이겹치면누설률감소가능 | SUPPORTED p.100 |
| p37 한계-1 | 평판validation·큰곡률영향불확실 | SUPPORTED p.101 |
| p37 한계-2 | TW거리길이의존미구현 | SUPPORTED p.94,101 |
| p37 한계-3 | 쌍별반복·순회방향 민감도 | SUPPORTED p.106,110–111; 헤더범위밖 |
| p37 불확실성-1 | 거리외 종류·중심·깊이·ID/OD 규칙 deterministic | SUPPORTED p.98 |
| p37 불확실성-2 | max깊이규칙 run별변경 민감도 | SUPPORTED p.98–99 |
| p38 기호 | A/B 기준/상대, absorbed 이후사실상무시 | SUPPORTED p.103,105–106 |
| p38 필요-1 | Framework가 매 timestep호출가능, 활성구성갱신 | SUPPORTED p.103 |
| p38 필요-2 | §4규칙구현 | SUPPORTED p.103 |
| p38 동작-1 | 활성 쌍 검사 반복 | SUPPORTED p.103 |
| p38 동작-2 | 합체/흡수 속성갱신, 만족쌍없을때반환 | SUPPORTED p.103 |
| p38 입력 | crack configuration/component geometry/model params | SUPPORTED p.103 |
| p38 범위-1 | coplanar원주한정 | SUPPORTED p.104 |
| p38 범위-2 | axial제외·세유형가정 | SUPPORTED p.104 |
| p38 범위-3 | 기본1개월·동일스텝3개이상드물것으로봄 | SUPPORTED p.111; 헤더범위밖 |
| p39 기호 | direction시계1/반시계2 | SUPPORTED p.110 |
| p39 판정-1 | 관찰자원점, B왼끝A두끝사이 또는A오른끝부터시계방향거리기준 | SUPPORTED p.105–106 |
| p39 판정-2 | 거리는쌍유형·형상에의존 | SUPPORTED p.106 |
| p39 순서-1 | subunit1기원균열을첫A | SUPPORTED p.106; 실제활성처리는전처리와함께해석 |
| p39 순서-2 | A시계바로옆부터 다른균열을순차B | SUPPORTED p.106 |
| p39 순서-3 | 만족상대없으면 시계바로옆새A | SUPPORTED p.106 |
| p39 순서-4 | A합체/B흡수, 만족쌍없을때까지반복 | SUPPORTED p.106 |
| p39 방향-1 | 다중쌍합체에서방향별상이우려·반전가능 | SUPPORTED p.106 |
| p39 방향-2 | 동시2개이하방향무관,3개이상은의존가능 | SUPPORTED p.111 |
| p40 direction행 | 시계1/반시계2 | SUPPORTED p.110 |
| p40 distance-rule행 | 절대1/최대깊이비율2권장 | SUPPORTED p.111 |
| p40 SCmodifier행 | rule1거리/rule2거리÷maxdepth·triangle0/0.5/0.75 | SUPPORTED p.111 |
| p40 TWmodifier행 | TW거리·당시길이와대략맞는분포·uniform0–20in예 | SUPPORTED p.111 |
| p40 depth행 | max1권장/min2/avg3 | SUPPORTED p.111 |
| p40 이유 | 입력매개변수·플래그로동작정의 | SUPPORTED p.110 |
| p40 사용-1 | 표입력설정 | SUPPORTED p.110–111 |
| p40 사용-2 | rule2계수삼각샘플/TW당시길이에맞는분포샘플 | SUPPORTED p.111; 샘플은Framework담당/p.108 |
| p40 사용-3 | 0–20in균일분포는예 | SUPPORTED p.111 |
| p40 쌍규칙 | SC거리or깊이비/TW사용자거리/혼합0 | SUPPORTED p.106 |
| p41 속성-1 | 흡수crack-type양의정수 | SUPPORTED p.107 |
| p41 속성-2 | 값은Ainitiation-time index·진단용 | SUPPORTED p.107 각주39 |
| p41 속성-3 | 합체속성은§4규칙 | SUPPORTED p.107 |
| p41 출력-1 | 무관균열속성불변 | SUPPORTED p.107 |
| p41 출력-2 | 반환전허용범위검증·문제출력오류flag | SUPPORTED p.108 |
| p41 출력-3 | 한호출pairwise>1이면301,300번대비종료·log | SUPPORTED p.108 |
| p41 출력-4 | 벡터출력발생시간순재정렬 | SUPPORTED p.108 |
| p41 성능-a | ≤30kB,≥5cracks,≥2overlap사례,1000회 | SUPPORTED p.108 |
| p41 성능-b | ≤10초 | WRONG W3; 원문<10초/p.108 |
| p42 필요-1 | 기존모델보완영역열거 | SUPPORTED p.117 |
| p42 필요-2 | 상당수EPRI전문가패널조사 | SUPPORTED p.117 |
| p42 K-1 | 낮은K<15–20/높은K>80MPa√m데이터미대표 | SUPPORTED p.117 |
| p42 K-2 | 새자료로plateau등형상변경/600threshold재검토가능 | SUPPORTED p.117 |
| p42 H-1 | 82수소입력은대부분182자료 | SUPPORTED p.117 |
| p42 H-2 | 600수소의존·타입력/불확실성조정추가분석 | SUPPORTED p.117 |
| p42 기계 | hybridyield명시/실부품yield충분정확하면불확실성감소가능 | SUPPORTED p.117 |
| p42 가공 | PWSCC냉간가공의존,thick-wallwrought600유의가속에높은수준필요 | SUPPORTED p.117 |
| p42 열처리 | 인접CS/LASPWHT효과·프랑스182IF2.0추천 | SUPPORTED p.117; 해당PWHT노출조건에한함 |
| p42 경계-1 | 2.0HAZ/희석영역복잡물성미모델 | SUPPORTED p.117–118 |
| p42 경계-2 | tip용접안은용접모델,모재진입즉시모재모델 | SUPPORTED p.118 |
| p42 상관-1 | 발생/성장상관기능·정확값미권장 | SUPPORTED p.118 |
| p42 상관-2 | 최초발생균열높은CGR로위험평가중요가능 | SUPPORTED p.118; 원문tends to라는경향 |
| p43 내용-1 | 600/82/182/132개선및타재료/환경CGR개발유용 | SUPPORTED p.118 |
| p43 내용-2 | 3-1수용희망·다른식형태필요가능 | SUPPORTED p.118 |
| p43 Ni690 | 600및용접다음690/52/152등모델필요·패널개발중 | SUPPORTED p.118; 보고서작성당시상태 |
| p43 BWR-1 | 다양부품확장시BWR필요가능 | SUPPORTED p.118 |
| p43 BWR-2 | 실험기반SSIGSCC기존모델구현가능 | SUPPORTED p.118 |
| p46 threshold-1 | 재료무관동일fatigueΔKth모델 | SUPPORTED p.119 |
| p46 threshold-2 | 재료별수용가능validation/ASME재료별시험모델진행/향후참고 | SUPPORTED p.119 |
| p46 validation-1 | 주로대안식·software예측,일부개발독립아님 | SUPPORTED p.119 |
| p46 validation-2 | 독립실험피로CGR더필요 | SUPPORTED p.119 |
| p46 validation-3 | 피로진전확인·1회이상운전cycle잔류ISI사례로현장율추정 | SUPPORTED p.119 |
| p47 복합-1 | 단순균열·부품형상에의존 | SUPPORTED p.120 |
| p47 복합-2a | 기본DMW3그룹·향후두께구배/J-groove | SUPPORTED p.120; “3그룹만”해석은INFERENCE/I4 |
| p47 복합-2b | 3균열형상모두대칭·비대칭개선 | SUPPORTED p.120 |
| p47 복합-2c | 원주coplanar·noncoplanar개선 | SUPPORTED p.120 |
| p47 복합-2d | subsurface발생/성장/합체/안정성예측없음 | SUPPORTED p.120 |
| p47 합체-1 | K-solutions인접응력장무시/안정성ligamentcollapse무시 | SUPPORTED p.120–121 |
| p47 합체-2 | 합체규칙으로대리 | SUPPORTED p.120–121 |
| p47 합체-3 | 파괴역학해를K/stability/coalescence에구현또는길이의존규칙개선 | SUPPORTED p.120–121 |
| p47 합체-4 | interaction2차결정요인길이/collapse시비슷한균열의ligament:길이≈1:1 | SUPPORTED p.120–121; 1차결정요인은ligament길이 |
| p47 axial-1 | 현재axial/circumferentialinteraction무시 | SUPPORTED p.121 |
| p47 axial-2 | 직교교차효과개선가능·mixedorientation타모듈과제 | SUPPORTED p.121 |
| p47 micro | micro-fissure합체는발생과정일부·InitiationSubgroup향후과제 | SUPPORTED p.121 |

검토 중 HTML은 수정하지 않았다. Git 명령 및 orchestration script는 실행하지 않았다.


