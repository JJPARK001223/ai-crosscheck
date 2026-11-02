# round86 — 15편 평가에 "글쓰기 교훈(writing lesson)" 레이어 추가

## 배경
round85에서 가솔린 엔진 SCI(E) 논문 15편의 Abstract/Introduction/Methodology/Results 평가(상/중/하, 근거 포함)를
`round85/input/evaluation_data.md`에 고정하고, HTML 보고서(`SCI논문15편_교차검증_종합보고서.html`)의 PART 1에
논문별 등급·근거 카드로 제시했다.

사용자 피드백: "중간고사 대체 평가인데 이거 너무 정성이 없는거 아님??" → 원인 파악 결과, "과학논문작성법" 수업 과제인데
보고서가 '등급이 왜 매겨졌는가(사실 설명)'에서 멈췄고, '그 등급이 글쓰기 관점에서 어떤 교훈을 주는가'가 없었다.

## 과제
`round85/input/evaluation_data.md`에 있는 기존 확정 등급·근거(새 등급·새 사실 추가 금지)를 바탕으로,
각 논문의 섹션별 평가에 **과학논문 글쓰기 교훈**을 한 단락씩 덧붙인다.

### 반드시 지킬 것
1. evaluation_data.md에 없는 논문 내용(새로운 수치, 새로운 인용, 등급 변경)을 추가하지 않는다.
2. "글쓰기 교훈"은 (a) 이미 확정된 근거 문장을 다시 인용하고, (b) 그 근거가 과학적 글쓰기의 어떤 원칙과 연결되는지
   설명하는 방식으로만 작성한다 — 즉 "사실(evaluation_data.md 근거) + 원칙(글쓰기 이론) + 교훈(이 논문에서 배울 점)" 3단 구조.
3. 사용하는 글쓰기 원칙은 출처를 밝힐 수 있는 것만 사용한다. 예:
   - Swales의 CARS 모델(Create a Research Space: 선행연구 정리→연구공백 제시→연구목적 진술) — Introduction 분석에 적용
     (Swales, J. M. (1990). *Genre Analysis: English in Academic and Research Settings*. Cambridge University Press.)
   - IMRaD 구조에서 Abstract의 정량적 요약 원칙(독자가 초록만으로 기여도를 판단할 수 있어야 한다) — 여러 과학적 글쓰기
     교본(예: Day, R. A., & Gastel, B. (2011). *How to Write and Publish a Scientific Paper*. Cambridge University Press.)에서
     공통적으로 강조하는 원칙 — Abstract 분석에 적용
   - Methodology의 재현가능성(reproducibility) 원칙 — 동일 교본의 Materials and Methods 장(섹션 재현을 위한 구체적 수치·장비 명시 요구) — Methodology 분석에 적용
   - Results에서 정성적 서술어(increased/decreased 등 헤징 표현)와 정량적 수치 제시의 설득력 차이 — 동일 계열 원칙 — Results 분석에 적용
   - 이 네 가지 외의 새로운 이론을 임의로 끌어오지 않는다. 확인 불가능한 주장은 "확인 불가"로 표시.
4. 논문 개별 교훈 외에, 15편 전체를 관통하는 "섹션별 공통 교훈" 요약(Abstract/Introduction/Methodology/Results 각 1개씩,
   총 4개)도 작성한다 — 어떤 논문이 그 원칙을 잘 지켰고 어떤 논문이 어겼는지 구체적으로 논문 번호를 인용해서 설명.

## 절차
1. Claude가 `round86/claude_lessons.md`에 15편 개별 교훈 + 섹션별 공통 교훈 4개를 작성(단독, 아래 2단계 전에 작성 완료).
2. Codex가 `round86/claude_lessons.md`를 `round85/input/evaluation_data.md`와 대조해 검증 → `round86/codex_review.md`에 작성:
   - evaluation_data.md에 없는 사실을 추가했는지(사실 왜곡 점검)
   - 글쓰기 원칙 4가지(CARS, 정량적 요약, 재현가능성, 정성/정량 서술) 외의 근거 없는 원칙을 끌어왔는지
   - 특정 논문에 대한 교훈이 근거 문장과 논리적으로 연결되지 않는 경우가 있는지
   - 보완하면 좋을 점(놓친 논문, 더 명확히 설명할 수 있는 연결)
3. Claude가 codex_review.md의 지적사항을 evaluation_data.md로 재대조해 수용 여부를 결정하고 HTML 보고서에 반영.

## 범위
- 이미 확정된 등급(상/중/하)·근거 문장은 수정하지 않는다. 이번 라운드는 "교훈 레이어"만 추가한다.
- 최종 산출물은 round85의 HTML 보고서(`SCI논문15편_교차검증_종합보고서.html`)에 각 논문 카드 아래 "글쓰기 교훈" 박스로 삽입된다.
