# Codex 작업 지시 (Round 6, blind)

[CROSSCHECK_WORKER] `round6/PROBLEM.md` 와 `round6/읽기자료_선행연구1_3.html` 를 읽고 독립 검증한다.

## 하지 말 것
- `round6/claude.md` 가 있으면 열지 말 것 (blind). 현재는 없음.

## 참조
- 원자료 번역 HTML (반드시 대조):
  `J:/Desktop/공학/claude_code/2026_09_01_선행연구분석/선행연구1_원문번역_영한대역_Revisiting_Failure_of_Brittle_Materials.html`
  `J:/Desktop/공학/claude_code/2026_09_01_선행연구분석/선행연구3_원문번역_영한대역_Unified_Failure_Criterion.html`
- 선행 DECISION: `DECISION_round1_수식검증.md`, `DECISION_round2_인용검증.md`, `DECISION.md`(round3),
  `DECISION_round4_FE재현계획.md`, `DECISION_round5_보고서검증.md`, `DISCUSSION.md`

## 할 일
`round6/PROBLEM.md` 의 검증 항목 1~7 을 각각 판정: **정확 / 부분 정정 필요 / 틀림 / 확인 불가** + 근거(조회 문서·범위 명시).

특히:
- 항목 2 (수식): 읽기자료에 옮긴 선1 식(4)~(7)·(11)~(13), 선3 식(2)~(4)·(8) 을 원자료와 한 자 한 자 대조.
- 항목 3 (2π 정정): 읽기자료의 경고 박스가 정확한지 — Y=G_c/(2π) 평면응력 / G_c/[2π(1-ν²)] 평면변형,
  "선1 식(6)은 문제없음" 서술이 맞는지, 과장·오류 없는지.
- 항목 4 (시각화): 그림 A-1~A-3, B-1~B-7, C-2 의 물리적 정확성. 특히 A-2(r 소거), A-3(θ=90°에서 3σ_o),
  B-5(6케이스), B-6(홀 크기별 파괴위치 전이).
- 항목 5 (케이스 사실): 수치·치수·재료·참고문헌 번호가 원문과 일치하는지.

## 결과물
`round6/codex.md` 에 한국어로: 항목별 판정표 + 근거 + 보고서에서 고칠 구체 지점(장·문단·문장) + 빠진 필수 내용.

완료 후:
rm -f .git/index.lock; git add round6/codex.md; git commit -m "round6: Codex blind 검증 (선행연구1·3 읽기자료)"; git push origin main

근거 없는 주장 금지. 모르면 "확인 불가".
