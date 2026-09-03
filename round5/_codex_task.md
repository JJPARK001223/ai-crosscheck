# Codex 작업 지시 (Round 5, blind)

[CROSSCHECK_WORKER] `round5/PROBLEM.md` 와 `round5/보고서.html` 를 읽고 독립 분석한다.

## 하지 말 것
- `round5/claude.md` 를 열지 말 것 (blind).

## 참조 가능
- `round5/보고서.html` (검증 대상)
- 선행 DECISION 들: `DECISION_round1_수식검증.md`, `DECISION_round2_인용검증.md`,
  `DECISION.md` (round3), `DECISION_round4_FE재현계획.md`, `DISCUSSION.md`
- 원문 번역(있으면): `J:/Desktop/공학/claude_code/2026_09_01_선행연구분석/선행연구3_원문번역_영한대역_Unified_Failure_Criterion.html`
  및 `선행연구1_원문번역_영한대역_Revisiting_Failure_of_Brittle_Materials.html`
  (원문 PDF·figure 스캔은 접근 불가할 수 있음 → 그 경우 "확인 불가")

## 할 일
`round5/PROBLEM.md` 의 검증 항목 1~7 을 각각 독립 판정: **정확 / 부분 정정 필요 / 틀림 / 확인 불가** + 근거.

특히:
- **항목 3 (식 유도 대수)**: $\sigma_x^3/2E \cdot |dr/d\sigma_x|$ 대입 후 $(2\pi)$ 지수 계산을
  손으로 재검산. $r$ 이 정확히 소거되는지, 최종 $w_f = K_I^2/(2\pi E)$ 계수가 맞는지.
- **항목 2 (에너지)**: $Y = G/(2\pi)$ 관계, 그림 2-1 개념도가 유한 3점굽힘 시편 맥락에서
  오해를 유발하는지. $G \geq 2\gamma_s$ vs $G \geq G_c$ 표기 혼용 문제.
- **항목 4 (6케이스)**: 고정/판독/가정 분류가 타당한지. $S=L$ 을 "가정"으로 둔 것이 맞는지.
- **항목 7 (요약)**: 6장 확정/정정/열림이 선행 DECISION 들과 정합하는지 — 왜곡·누락 지적.

## 결과물
`round5/codex.md` 에 한국어로:
- 항목별 판정표 + 근거(조회한 문서·범위 명시)
- 보고서에서 구체적으로 고칠 것 (장·문단 단위)
- 빠진 필수 내용

완료 후:
`rm -f .git/index.lock; git add round5/codex.md; git commit -m "round5: Codex blind 분석 (보고서 검증)"; git push origin main`

근거 없는 주장 금지. 모르면 "확인 불가".
