# round34 원문 한정 감사

대상: `round34/audit_html.txt`의 HTML 40–49페이지 전체. 대조 자료: Kyle Schmitt, *xLPR Models Subgroup Report—Crack Growth and Coalescence*, xLPR-MSGR-CGR Version 1.0, 2016, 인쇄 p.103–121 및 HTML이 추가 인용한 p.45, p.48, p.71. 저자·버전·연도는 보고서 서명면에서 확인했다. 아래 쪽수는 모두 인쇄 쪽수이며, `=====PAGE n=====` 뒤 블록을 p.n−1로 대응했다.

아래에는 요청한 유형의 문제만 기록한다. 내용 오류와 별도로, 사용자의 ‘원문에 없는 소제목 금지’ 규칙에 걸리는 편집 소제목도 표시한다. 단순한 번역어 자체를 신조어로 판정하지 않았다. 제공된 감사 텍스트에 식의 수식 본문이 없는 경우, 식 번호와 주변 설명만 대조했으며 HTML 원본의 수식 표시까지 확인했다는 의미는 아니다.

## 1. HTML 44 — WRONG: K 범위 누락·수치 의미 변경

- 대상 문구 그대로: “현재 K 의존성은 대체로 낮은 K(80 MPa√m)를 대표하지 않는 데이터로 개발되었습니다.”
- 원문 근거: p.117, §6.1.1: “The currently implemented stress intensity factor dependency has been developed from data that do not generally represent low (<15 to 20 MPa√m) or high (>80 MPa√m) values.”
- 문제: 낮은 K의 범위가 빠졌고, 높은 K의 경계인 80을 낮은 K에 연결했다. 낮은 범위와 높은 범위 양쪽이 원문에 있다.
- 최소 교체안: “현재 구현된 응력확대계수 의존성은 낮은 값(<15~20 MPa√m)이나 높은 값(>80 MPa√m)을 대체로 대표하지 않는 데이터로 개발되었습니다(p.117).”

## 2. HTML 43 — OMISSION-OF-HEDGE: 진단상 유용성 단정

- 대상 문구 그대로: “그 값은 coalescence 상대인 “Crack A”의 발생 시점 번호이며 실행 후 진단에 도움이 됩니다.”
- 원문 근거: p.107, 각주 39: “Specifically, absorbed cracks are given a crack type equal to the initiation time index of the crack with which it coalesces (i.e., “Crack A”). This information can be diagnostically helpful at the end of program execution.”
- 문제: “can be”가 빠져 유용성을 단정한다.
- 최소 교체안: “그 값은 coalescence 상대인 “Crack A”의 initiation time index이며, 이 정보는 프로그램 실행이 끝났을 때 진단에 도움이 될 수 있습니다.”

## 3. HTML 43 — INFERENCE/DERIVED/JUDGMENT: 기록으로만 한정

- 대상 문구 그대로: “xLPR에서 300번대 오류는 프로그램을 끝내지 않고 실행 기록에만 남깁니다.”
- 원문 근거: p.108, §5.2.1.6: “By definition within xLPR, a 300-level error does not result in termination of the program instance, but is logged to a run file for the benefit of the user or reviewers.” p.111, §5.3.3: “Second, an error flag is returned to communicate any errors or anomalies encountered during the call of the coalescence module.”
- 문제: 원문은 실행을 종료하지 않고 run file에 기록한다고 설명한다. ‘기록에만’이라는 배타적 한정은 없다. error flag도 반환한다.
- 최소 교체안: “xLPR에서 300번대 오류는 프로그램 실행을 종료하지 않으며 run file에 기록됩니다.”

## 4. HTML 49 — WRONG: Complex를 ‘복합’으로 번역

- 대상 문구 그대로: “6.3 복합 성장 예측과 coalescence 개선” / “복합 성장 예측(§6.3.1)”
- 원문 근거: p.120의 절 제목은 “6.3 Crack Growth and Coalescence”, “6.3.1 Complex Growth Prediction”이다. 본문은 “More complex geometries constitute extensive development efforts, but could improve the overall fidelity of xLPR.”라고 설명하고 component geometry, asymmetric crack growth, non-coplanar cracks, subsurface flaws를 열거한다.
- 문제: 해당 문맥의 complex는 형상·성장 예측의 복잡성을 뜻한다. ‘복합’은 원문 절 제목과 뜻이 다르며, 6.3 제목도 자체 재구성했다.
- 최소 교체안: 각각 “6.3 Crack Growth and Coalescence”, “6.3.1 Complex Growth Prediction”.

## 5. HTML 40 — INFERENCE/DERIVED/JUDGMENT: 자체 질문형 소제목

- 대상 문구 그대로: “coalescence module은 어떻게 불리고 동작하나”
- 원문 근거: p.103–104의 해당 절 제목은 “5.1 Module Scope and Limitations”. p.103 본문은 “At each time discretization, the Framework may call the coalescence module to update the crack configuration” 및 “the coalescence module implements an iterative procedure”라고 서술한다.
- 문제: 내용의 근거는 있지만 질문형 제목 자체는 원문의 소제목이 아니다. 자체 소제목 금지 규칙에 따른 편집 문제다.
- 최소 교체안: “5.1 Module Scope and Limitations”.

## 6. HTML 41 — INFERENCE/DERIVED/JUDGMENT: 자체 소제목

- 대상 문구 그대로: “반복 적용 규칙: Crack A와 Crack B” / “방향 플래그가 있는 이유”
- 원문 근거: p.105–106의 절 제목은 “5.2.1.3 Iterative Application of Coalescence Rules”. p.106은 “This capability was built-in to investigate the concern that—for configurations requiring more than one instance of pairwise coalescence—the iterative coalescence rules may give different updated crack configurations depending on directionality of the iterative procedure.”라고 직접 서술한다.
- 문제: 본문 내용 오류와 구분되는 자체 소제목 문제다. 두 소제목은 원문 제목에 없다.
- 최소 교체안: 첫 제목은 “5.2.1.3 Iterative Application of Coalescence Rules”, 두 번째 소제목은 DELETE(뒤의 근거 있는 본문은 유지).

## 7. HTML 43 — INFERENCE/DERIVED/JUDGMENT: 자체 통합 소제목

- 대상 문구 그대로: “속성 갱신과 출력, 오류”
- 원문 근거: p.107 “5.2.1.5 Updating Crack Attributes”, “5.2.1.6 Output Requirements”; p.111 “5.3.3 Other Output Arguments”.
- 문제: 여러 절을 자체 제목 하나로 합쳤다. 자체 소제목 금지 규칙에 해당한다.
- 최소 교체안: DELETE. 필요하면 해당 본문 앞에 위 원문 절 제목을 각각 사용한다.

## 8. HTML 44 — INFERENCE/DERIVED/JUDGMENT: 자체 질문형 소제목

- 대상 문구 그대로: “왜 보완이 필요한가”
- 원문 근거: p.117의 절 제목은 “6.1.1 Refinements to Alloy 600/82/182 PWSCC Models”. 도입은 “Refinements and extensions of the existing Alloy 600/82/182 PWSCC CGR models are desired for several areas.”이다.
- 문제: 원문은 개선·확장이 바람직한 영역을 소개한다. 질문형 소제목은 원문에 없다.
- 최소 교체안: DELETE(이미 제시된 §6.1.1 제목과 뒤의 본문 유지).

## 9. HTML 46 — INFERENCE/DERIVED/JUDGMENT: 자체 식 제목·질문형 소제목

- 대상 문구 그대로: “식 6-1 · 오스테나이트 합금 계수 개정” / “왜 이 식을 쓰나” / “어떤 조건에 쓰나” / “적용 방법”
- 원문 근거: p.118의 절 제목은 “6.2.1 Updated Fatigue Crack Growth Relations for Austenitic SS”. p.119는 “The material groupings for the SS alloy effect were changed to:” 뒤에 식 6-1을 제시하고 “Also, the upper limit of 2000 seconds for loading rise time in [Eqn. 2-22] was eliminated.”라고 서술한다.
- 문제: 식 6-1은 실제로 있지만 제시된 식 제목과 설명용 소제목은 원문 제목이 아니다. 자체 소제목 금지 규칙에 따른 문제이며, 이것만으로 뒤의 설명 내용이 틀렸다는 뜻은 아니다.
- 최소 교체안: 첫 제목은 “6.2.1 Updated Fatigue Crack Growth Relations for Austenitic SS”; 나머지 세 소제목은 DELETE(본문 유지).

## 10. HTML 47 — INFERENCE/DERIVED/JUDGMENT: 자체 식 제목·질문형 소제목

- 대상 문구 그대로: “식 6-2 · Ni계 환경계수 산포 개선안” / “왜 이 식을 쓰나” / “어떤 조건에 쓰나” / “적용 방법”
- 원문 근거: p.119의 절 제목은 “6.2.2 Enhancements to Probabilistic Model for Nickel-Based Alloys”. 본문은 “This model could be improved in a later version of xLPR by implementing an environmental factor whose dispersion could vary with the fatigue CGR prediction in air.”라고 서술하고 식 6-2를 제시한다.
- 문제: 자체 식 제목과 설명용 소제목이다. p.45에는 선형 변화가 직접 서술되어 있으므로, 해당 본문을 자체 계산이나 유도라고 판정하는 것은 타당하지 않다.
- 최소 교체안: 첫 제목은 “6.2.2 Enhancements to Probabilistic Model for Nickel-Based Alloys”; 나머지 세 소제목은 DELETE(본문 유지).

## 11. HTML 48 — INFERENCE/DERIVED/JUDGMENT: 자체 통합 소제목

- 대상 문구 그대로: “6.2.3–6.2.4 ΔK 문턱값과 향후 검증”
- 원문 근거: p.119에는 “6.2.3 Material-Specific Stress Intensity Factor Range Threshold”와 “6.2.4 Future Validation Efforts”가 별도 절로 있다.
- 문제: 원문에 없는 통합 소제목이다. 절 번호 자체는 맞다.
- 최소 교체안: DELETE. 두 본문 앞에 각각 위 원문 절 제목을 사용한다.

## 12. HTML 49 — INFERENCE/DERIVED/JUDGMENT: 자체 통합 소제목

- 대상 문구 그대로: “균열 간섭과 ligament 붕괴(§6.3.2)”
- 원문 근거: p.120의 절 제목은 “6.3.2 Crack Coalescence”. 그 아래 p.120에 “Crack interaction”, p.121에 “Ligament collapse”가 별도 항목으로 있다.
- 문제: 두 항목을 묶은 자체 제목이다. §6.3.2 자체의 제목은 Crack Coalescence이다.
- 최소 교체안: “6.3.2 Crack Coalescence”.

ROUND34 DONE
