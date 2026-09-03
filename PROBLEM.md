# 이번에 풀 문제

## 배경
석사연구 선행연구 검증. 두 논문의 **수식 유도**가 수학적으로 옳은지 독립 검증한다.

- **선행연구 1**: Y. W. Kwon, "Revisiting Failure of Brittle Materials",
  *J. Pressure Vessel Technol.* 2021, 143, 064503. (3쪽)
  원문 PDF: `J:\Desktop\선행연구 관련\[선행연구 1] Revisintg Failure of Brittle Materials (2021-12).pdf`
- **선행연구 3**: Y. W. Kwon, E. K. Markoff, S. DeFisher, "Unified Failure Criterion
  Based on Stress and Stress Gradient Conditions", *Materials* 2024, 17, 569. (19쪽)
  원문 PDF: `J:\Desktop\선행연구 관련\[선행연구 3] Unified Failure Criterion Based on Stress ans Stress Gradient Conditions (2024-01).pdf`
  페이지 이미지: `J:\Desktop\공학\claude_code\2026_09_01_선행연구분석\images\paper3_page-01..19.png`

## 검증할 항목 (각각 "유도가 맞는가 / 어디가 느슨한가"를 답하라)

### 선행연구 1
1. 식(2)→식(3): 변형에너지밀도 ÷ (단위응력당 응력구배) 를 정리하면
   `wf = (σ_l³ / 2E) · |ds/dσ_l|` 이 되는가?
2. Case 2 (무한판 중앙균열):
   - 식(4) `σx = K/√(2πr)` 에서 식(5) `|dσx/dy| = K / (2√(2π) y^{3/2})` 유도.
   - 식(6) `wf = K² / (2πE)` 유도.
   - 식(7) `K_IC = √(2πE wf)` 유도.
3. Case 3 (무한판 원형홀, Kirsch 해):
   - 식(9)에서 `σθ(R, π/2) = 3σo` 확인.
   - 식(11) `|∂σθ/∂r (R,π/2)| = 7σo/R` 유도.
   - 식(12)(13) 파괴조건.

### 선행연구 3
4. 식(1)(2): 응력조건 `σe ≥ σf`, 응력구배조건 `σe ≥ (2EY·|dσe/ds|)^{1/3}`.
   선행연구 1의 `wf` 와 선행연구 3의 `Y` 는 같은 양인가?
5. 식(3) `σe = K/√s` → 식(4) `Y = K²/E` 유도.
6. 논문 주장 "Y 는 파괴역학의 임계 에너지방출률(G_c)과 동등하다" 는 맞는가?
   선행연구 1의 `wf = K²/(2πE)` 와 선행연구 3의 `Y = K²/E` 의 2π 차이는 무엇인가?
7. Figure 8·9 (경화 시멘트 페이스트 3점굽힘):
   - 반쪽 모델 형상(H, L/2, W, 균열깊이 a), 경계조건, 하중.
   - K 를 FEA + 식(3) 곡선맞춤으로 뽑는 절차가 타당한가?
   - 참고용: SENB 3점굽힘 표준 K 핸드북식(ASTM E399, S/W=4)과 개념 비교.

## 규칙
- Blind. 상대 답 보지 말 것. 각자 `round1/claude.md`, `round1/codex.md` 에 작성 후 commit/push.
- 손으로 미분·대입해서 확인. "맞다"가 아니라 유도 스텝을 보여라.
- 최종 종합·판정은 Claude 가 `DECISION.md` 에 작성.
