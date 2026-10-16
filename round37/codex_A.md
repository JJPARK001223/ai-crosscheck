# round37 독립 감사 A — HTML 슬라이드 1~17

## 범위와 근거

- 대상: `round37/audit_deck.txt`의 `===== HTML SLIDE 1 =====`부터 `===== HTML SLIDE 17 =====`까지. 제목, 표, 설명, 적용 조건, `[EQUATION TeX]`, 인용 페이지·절을 대조했다. HTML 및 보고서는 수정하지 않았다.
- 원전: Kyle Schmitt, EPRI, *xLPR Models Subgroup Report—Crack Growth and Coalescence*, xLPR-MSGR-CGR Version 1.0, 2016-06-29. 이하 모든 원문 근거는 이 보고서다. 원문 p.xx는 인쇄 페이지이며, `cgr_text.txt`의 `=====PAGE xx+1=====`에 해당한다.
- 수식은 텍스트 추출뿐 아니라 `pages/p022.png`, `p028.png`, `p034.png`, `p035.png`, `p039.png`, `p040.png`, `p041.png`, `p043.png`, `p044.png`, `p073.png`로 확인했다. 파일 숫자는 PAGE 마커 숫자이며 인쇄 페이지보다 1 크다.
- Claude 조사·결론은 읽지 않았다. 아래는 원문과 대상 텍스트만으로 수행한 대조다.
- 단순 요약·직접적인 수학적 귀결·교육용 제목이라는 이유만으로 ADDED-CLAIM 또는 COINED-TITLE로 판정하지 않았다. PLAUSIBLE은 확정 오류 수에 포함하지 않는다.

## 확인 항목

### [슬라이드 2] 합체 상호작용이 응력확대계수를 높일 수 있다는 가능성 표현 삭제
- 문제 문구(HTML 인용): “균열 끝 상호작용(crack tip interaction)으로 응력확대계수가 커지는 것과 두 균열을 가르는 ligament의 소성 붕괴(plastic collapse)”
- 원문 근거(원문 인용 + 실제 쪽 + 절): “including crack tip interaction that **can lead to** intensified stress intensity factors and plastic collapse of a ligament separating two cracks.” — p.19, §1.2, PAGE 20.
- 판정: **OMISSION-OF-HEDGE / CONFIRMED**. 원문은 상호작용이 응력확대계수 증가를 일으킬 수 있다고 설명한다. HTML은 증가를 단정하는 명사구로 바꿨다. coalescence를 “합체”로 번역한 것이 문제는 아니다.
- 수정 제안: “균열 끝 상호작용으로 응력확대계수가 커질 수 있는 효과와 두 균열 사이 ligament의 소성 붕괴”로 수정.

### [슬라이드 5] 제한적인 Alloy 82 자료가 시사한 피크 이동을 확정된 현상으로 서술
- 문제 문구(HTML 인용): “파라미터는 Alloy 182/132 데이터 기반이고, Alloy 82는 피크 위치가 어긋나 추가 시험이 필요합니다.”
- 원문 근거(원문 인용 + 실제 쪽 + 절): “**Very limited data** for Alloy 82 analyzed in MRP-263 **suggested** a roughly Gaussian dependency relative to ECP, but exhibited a shift in the peak CGR from the **estimated location** of the Ni/NiO transition. Additional testing is required to resolve this **apparent discrepancy**.” — p.34, §2.2.3.2, PAGE 35.
- 판정: **OMISSION-OF-HEDGE / CONFIRMED**. 원문은 매우 제한적인 자료, 전이 위치의 추정, 겉보기 불일치라는 한계를 함께 제시한다. HTML의 “추가 시험이 필요”는 유지되어 있지만, 그 앞의 “Alloy 82는 피크 위치가 어긋나”는 관측 자료의 한계를 재료 자체의 확정된 성질로 확대한다.
- 수정 제안: “매개변수는 Alloy 182/132 자료에 기반합니다. Alloy 82의 매우 제한적인 자료에서는 추정된 Ni/NiO 전이 위치와 피크 CGR 위치의 차이가 나타났으며, 이 겉보기 불일치를 확인할 추가 시험이 필요합니다.”

### [슬라이드 12] 세 재료군에 같은 문턱 모델을 채택한 조건부 성격 누락
- 문제 문구(HTML 인용): “Ni계, 오스테나이트, 페라이트 모두 이 한 식을 씁니다(Ni계는 데이터가 적어 같은 식을 선택).”
- 원문 근거(원문 인용 + 실제 쪽 + 절): “The limited low ΔK data presented by Mills [24] are at high load ratios and are similar to the values reported in Figure 2-10. Therefore, it was selected that the same ΔKth model be used for all three material classes **unless additional data that refute this approach are produced or identified**.” — p.42, §2.3.1, PAGE 43.
- 판정: **OMISSION-OF-HEDGE / CONFIRMED**. xLPR 2.0이 같은 식을 사용하는 구현 설명 자체는 맞다. 다만 원문은 Ni계의 낮은 ΔK 자료가 고하중비에 한정된다는 점과 반증 자료가 나오면 재검토한다는 조건을 명시한다. HTML은 자료 부족만 남기고 공통 모델 선택의 잠정성을 생략했다. 공통 문턱식이 세 재료에 독립적으로 충분히 확립되었다는 뜻으로 읽히지 않게 해야 한다.
- 수정 제안: “xLPR 2.0은 세 재료군에 같은 식을 채택했습니다. Ni계의 낮은 ΔK 자료는 적고 고하중비에 한정되어 있으며, 이 접근을 반박하는 추가 자료가 나오면 재검토하는 조건의 선택입니다.”

## 추가 확인 후보 — 확정 오류 아님

### [슬라이드 12] 공칭 온도 선택 방식의 실험적 미확정성이 설명에서 빠짐
- 문제 문구(HTML 인용): “공칭 온도를 사이클의 평균(플래그 1), 최소(2), 최대(3) 중 사용자가 선택합니다(p.39, 87).”
- 원문 근거(원문 인용 + 실제 쪽 + 절): “no specification is given in source documentation as to how to calculate nominal temperature”; “Most laboratory data available did not include temperature cycling so the appropriate convention cannot be determined from how model development from these data was performed.” — p.39, §2.3.1, PAGE 40. p.87, §3.3.4는 일반적으로 평균인 1을 쓰고 2·3은 근사에 대한 민감도 연구에 사용할 수 있다고 설명한다.
- 판정: **OMISSION-OF-HEDGE / PLAUSIBLE — 추가 확인**. 플래그 값과 사용자 선택 가능성은 정확하다. 다만 원문이 강조하는 ‘적절한 선택을 개발 자료로 결정할 수 없음’과 평균의 일반 권고가 빠졌다. 이 슬라이드를 단순 입력 안내로 쓰는지, 모델의 근거까지 설명하는지에 따라 보완 필요성이 달라지므로 확정 오류로 세지 않는다.
- 수정 제안: “통상 평균(1)을 쓰고, 최소(2)·최대(3)는 민감도 검토에 사용할 수 있습니다. 개발 자료 대부분에 온도 사이클링이 없어 최적 선택을 자료로 확정하지는 못했습니다.”

### [슬라이드 16] 용접금속 전체의 2.0 계수가 자료 외삽이라는 근거 누락
- 문제 문구(HTML 인용): “원문은 모든 용접금속에서 f_{alloy}를 2.0으로 둔다고 합니다(p.44).”
- 원문 근거(원문 인용 + 실제 쪽 + 절): “Fatigue crack growth data for Alloys 82, 52, and 152 in air were not available. Given this information, it is considered most appropriate to apply the Alloy 600 model to Alloys 82/182/132 and the Alloy 690 model to Alloys 52/152 with the only exception that the alloy factor, f_alloy, is set to 2.0 for all of the weld metals.” — p.44, §2.3.2.2, PAGE 45. 앞 문단의 약 2배 관측은 Alloy 182의 35개 시험에 관한 것이다.
- 판정: **OMISSION-OF-HEDGE / PLAUSIBLE — 추가 확인**. 모든 해당 용접금속에 2.0을 쓰는 보고서의 선택은 정확하게 옮겼다. 따라서 숫자 오류나 ADDED-CLAIM은 아니다. 다만 앞의 Alloy 182 관측과 이어져 Alloy 82/52/152에도 독립적인 시험 근거가 있는 듯 읽힐 여지가 있다. 설명 범위에 따른 보완 후보로 남긴다.
- 수정 제안: “Alloy 182의 시험 결과를 바탕으로 해당 용접금속 모두에 2.0을 적용하도록 권고했습니다. Alloy 82/52/152의 공기 중 피로 자료는 없었으므로 이 재료들에 대한 적용은 모델 선택에 따른 확장입니다.”

## 슬라이드별 대조 결과

- 슬라이드 1: 문제 없음(§1.1의 목적·선정 기준·8개 업무 및 모듈 개발 산출물에 관하여 확인 가능한 문제 없음; p.17–18).
- 슬라이드 2: 위 CONFIRMED 1건. 다른 개요·범위·구성 및 깊이 1~3 mm 예시는 p.18–19와 일치.
- 슬라이드 3: 문제 없음(식 2-1, 기호, 개발 범위, 낮은 K 한계, 수소·아연 설명; p.21–25). 검증 범위 10~80 MPa√m·280~350°C는 p.25에 실제로 있음. 열·시편 계수의 대수정규분포도 p.23–24에 근거함.
- 슬라이드 4: 문제 없음(식 2-2, 1.6·1.16, Kth=0, 19개 용접·77개 측정, Alloy 82 개선계수 제한, 덴드라이트 방향계수; p.27–30, p.82). 회귀에서 활성화 에너지를 고정했다는 서술은 개발 절차 설명이며, 실제 확률 입력의 불확실성이 없다는 주장으로 판정하지 않음.
- 슬라이드 5: 위 CONFIRMED 1건. 식 2-3과 104 kJ/mol 권장값 및 검증 범위는 p.33–37에 근거함. 식에 K≤Kth 분기가 없는 것은 원문 식 2-3도 동일하므로 전사 오류가 아님.
- 슬라이드 6: 문제 없음(식 2-4, Gaussian 의존성, P 독립 검증 부재, P−1의 분포 및 0.714; p.33–37, p.76, p.82). c에서 약 40% 감소한다는 설명은 p.81에 명시되어 있어 ADDED-CLAIM이 아님. P=1에서 fH2=1은 식의 직접 귀결이며 p.81에도 수소 효과 제거 방법으로 제시됨.
- 슬라이드 7: 문제 없음(식 2-5, 단위, log의 밑에 대한 보충; p.33, p.72). 식 3-1 이미지에서 log10과 T=TC+273.15를 확인.
- 슬라이드 8: 문제 없음(식 2-6의 계수·지수 및 섭씨 설명; p.34, p.72). 원문 식 2-6 자체에는 T 단위가 없고 모듈 식 3-1에 TC가 명시됨.
- 슬라이드 9: 문제 없음(식 2-8과 일반 모델의 목적; p.38, p.72). 정상 PWR 환경이라는 제한이 본문에 유지되어 있어 모든 조건의 SCC 저항성을 단정한 것으로 판정하지 않음.
- 슬라이드 10: 문제 없음(식 2-9, 압축-압축 및 인장 구간 설명; p.39). 후자는 원문에 직접 존재하는 설명으로 ADDED-CLAIM이 아님.
- 슬라이드 11: 문제 없음(식 2-10, Kmin≤0에서 R=0, ASME 근거; p.39).
- 슬라이드 12: 위 CONFIRMED 1건, PLAUSIBLE 추가 확인 1건. 식 2-11, 30%·2배, epistemic 분류, 표본추출 빈도와 플래그 숫자는 원문과 일치.
- 슬라이드 13: 문제 없음(식 2-12, R≥0.10·28개 점, log-σ=0.139, 1.27, 상한 1.517배; p.40). p.83의 중앙값 1과 p.86 표의 log-μ=0.239의 차이를 HTML이 원문 내 차이로 명시했으므로 HTML 오류로 돌리지 않음.
- 슬라이드 14: 문제 없음(식 2-13, 기호·단위·개발 데이터 범위·재료 코드·상승시간 정의; p.42–44, p.71–72, p.78, p.86). nenv=0.25~0.33은 표 3-5의 균일분포 범위와 일치. 1E-9 m/s는 원문 p.44의 시간당 피로 속도 표현을 옮긴 것이며 식의 사이클당 단위와 혼동한 전사 오류가 아님.
- 슬라이드 15: 문제 없음(식 2-14, Alloy 690 약 60개 시험과 온도 효과 재추정; p.42–44). 원문 F_T 정의에 별도 단위가 명시되어 있지 않다는 설명도 맞음.
- 슬라이드 16: 확정 문제 없음. 위 PLAUSIBLE 추가 확인 1건. 식 2-15와 모든 해당 용접금속에 2.0을 적용하는 모델 선택은 원문과 일치.
- 슬라이드 17: 문제 없음(식 2-16, b=0.82·p=2.2 및 R 개발 범위; p.43). 이 계수는 Alloy 600 공기 중 일정 온도 시험의 개별 자료 적합에서 얻었으며, HTML은 이 수치를 다른 재료의 독립 시험 결과라고 주장하지 않음.

## 판정 집계와 작업 상태

- CONFIRMED: 3건(모두 OMISSION-OF-HEDGE). PLAUSIBLE: 2건(추가 확인 후보).
- 확인한 범위에서 확정 WRONG, ADDED-CLAIM, COINED-TITLE, CITATION, EQUATION 오류는 찾지 못했다. 이는 보고서 이외의 독립 실험으로 물리적 타당성을 재검증했다는 뜻이 아니라, 지정 원전 대비 전사·요약 감사 결과다.
- 결과 파일 저장 후 `git add -- round37/codex_A.md`도 `.git/index.lock`: Permission denied로 실패했다. 이 파일을 스테이징할 수 없어 커밋·push는 수행하지 못했다.
- 시작 시 `git pull`을 실행했으나 `cannot open '.git/FETCH_HEAD': Permission denied`로 실패했다. 따라서 원격 최신 상태는 확인하지 못했다. 다른 작업자의 기존 변경은 건드리지 않았다.

__DONE__

