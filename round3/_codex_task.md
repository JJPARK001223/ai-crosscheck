# Codex 작업 지시 (Round 3, blind)

[CROSSCHECK_WORKER] 이 파일과 `PROBLEM.md` 만 근거로 독립 유도·검증한다.

## 하지 말 것
- `round3/claude.md` 를 열거나 읽지 말 것 (blind).
- `round1/`, `round2/` 결과도 이번 판단 근거로 쓰지 말 것 (독립성 유지).

## 할 일
`PROBLEM.md` "검증 대상 — 완전한 유도 경로"의 Part A / B / C 각 스텝을
**직접 손으로 재유도**해서 다음을 판정한다.

1. 각 스텝: **정확 / 오류(수정안 제시) / 불완전(보완 필요)**.
2. 특히 아래 두 대수를 독립적으로 재유도:
   - B3: w_f = σ_x³ / (2E|dσ_x/dr|) 에서 r 이 소거되고 결과가 K_I²/(2πE) 가 되는가.
     (2π)^{1/2} / (2π)^{3/2} = 1/(2π) 확인.
   - C4: P_pred = √(EY)/(K/P)  와  P_pred = √(2πEY)/(K_I/P)  가 동일 값인가
     (K_I = √(2π)·K 라는 선3 정의 하에서).
3. B5: Y = K²/E = K_I²/(2πE) = G/(2π) 가 맞는가. 논문의
   "Y ≡ critical energy release rate" 서술이 수치적으로 정확한지/부정확한지.
4. **누락된 필수 식**: 이 과업(HCP 3PB 균열 FE 재현 + 파괴하중 역산)을 실제로
   수행하는 데 반드시 필요한데 Part A/B/C 에 빠진 식·관계가 있는가.
5. **과잉 식**: Part A/B/C 중 이 과업엔 불필요한 것.
6. C2(FE 응력 곡선맞춤으로 K 추출), C3(케이스4에서 Y 1회 보정), C4(나머지 예측)
   워크플로우가 논문 §4.2~4.3 서술과 일치하는지 (PMC10856633 §4 접근 가능하면 확인,
   안 되면 "확인 불가").

## 참고 (서지)
- 선행연구 1: Kwon, Y.W. "Revisiting Failure of Brittle Materials," J. Press. Vessel
  Technol. 2021, 143(6), 064503.
- 선행연구 3: Kwon, Y.W.; Markoff, E.K.; DeFisher, S. "Unified Failure Criterion
  Based on Stress and Stress Gradient Conditions," Materials 2024, 17(3), 569
  (PMC10856633, open access).

## 결과물
`round3/codex.md` 에 **한국어로**:
- Part A/B/C 스텝별 판정표
- B3·C4·B5 재유도 전 과정(계산 보이기)
- 누락 식 / 과잉 식 목록
- §4 워크플로우 일치 여부 (근거·접근 범위 명시, 추측 금지)

완료 후: `git add round3/codex.md && git commit -m "round3: Codex blind 유도 검증" && git push origin main`.
`AGENTS.md` 규칙 준수. 근거 없는 주장 금지. 모르면 "확인 불가".
