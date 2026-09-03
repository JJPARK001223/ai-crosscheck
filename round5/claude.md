# Round 5 — Claude 자체 검증 (보고서)

`round5/보고서.html` 를 내가 직접 재검토한 결과. Codex 는 이 파일을 보지 말고 독립 판정할 것.

## 1장 LEFM — 자체 판정: 정확

- $\sigma_x = K_I/\sqrt{2\pi r}$ 는 모드 I 균열 전방($\theta=0$) 개구응력의 표준 선단 전개 주항. 정확.
- $K_I \propto P$ (선형탄성) — 정확.
- SSY: 소성역 $r_p \ll$ (a, H−a, K-지배영역) → $K_I$ 유일 파라미터. 표준 서술.
- 취성재 $\sigma_e$ = 최대 수직응력, 파괴 경로 $s \perp \sigma_1$ — Kwon 2024 §2 및 DISCUSSION §2.3 과 정합.
- 우려: 그림 1-1 의 소성역·K-지배영역 경계는 개념 도식이며 축 눈금 없음 → 정성적으로만 읽어야 함. 본문에 그렇게 명시함.

## 2장 에너지 접근법 — 자체 판정: 정확 (단 개념 도식 주의)

- Griffith: $-d\Pi/dA \geq 2\gamma_s$, 계수 2 = 두 새 표면. 정확.
- Irwin $G = K_I^2/E'$, $E'$ 구분 정확 (DECISION_round1 §2.4 와 동일).
- $Y = G/(2\pi)$ (평면응력), $\neq G_c$ — DECISION_round1 §4.2, DISCUSSION §2.1 과 정합.
  6.28배(=2π) 차이, 문헌 $G_c$ 대입 금지 경고 포함.
- 그림 2-1: 표면에너지 $\propto +a$, 방출 변형에너지 $\propto -a^2$, 전체 극대 $a_c$ 에서 $dΠ/da=0$.
  중앙균열 무한판 기준 표준 도식. 단 3점굽힘 유한시편에 정량적으로 그대로 적용되진 않음 —
  "개념도"로만 제시함.
- 참고문헌: [9][10][11][12] 서지정보는 원문 References(선행연구3_원문번역 673–676행)에서 직접 확인.
  [9–16] 이 "균열 있는 부재의 파괴역학" 배경 인용 묶음이라는 것도 원문 126행에서 확인.

## 3장 식 유도 — 자체 판정: 정확 (round1 양측 blind 재유도 일치)

핵심 검산 ($w_f$ 관례, 표준 $K_I$):
- $\sigma_x^3 = K_I^3/[(2\pi)^{3/2} r^{3/2}]$
- $|d\sigma_x/dr| = K_I/[2(2\pi)^{1/2} r^{3/2}]$, 따라서 $|dr/d\sigma_x| = 2(2\pi)^{1/2} r^{3/2}/K_I$
- $\frac{\sigma_x^3}{2E}|dr/d\sigma_x|
   = \frac{K_I^3}{(2\pi)^{3/2} r^{3/2} \cdot 2E} \cdot \frac{2(2\pi)^{1/2} r^{3/2}}{K_I}
   = \frac{K_I^2 (2\pi)^{1/2}}{(2\pi)^{3/2} E}
   = \frac{K_I^2}{2\pi E}$   → $r$ 소거. ✔
- $w_f = K_I^2/(2\pi E)$, $K_{IC} = \sqrt{2\pi E w_f}$ — 선1 식(6)(7). ✔
- 선3: $\sigma_e = K/\sqrt s$ (2π 없음) → $Y = K^2/E$ → $K=K_I/\sqrt{2\pi}$ → $Y = K_I^2/(2\pi E) = w_f$. ✔
- DECISION_round1 §1 표: Claude·Codex 양측 이 유도를 각자 재현해 일치.

## 4장 6케이스 역산 — 자체 판정: 정확 (round2·4 반영)

- 고정값 $W=100$, $L/H=4$, $E=20.8$ GPa: 선행연구3_원문번역 312–313행에서 직접 인용 확인.
- $H = 50, 100$ mm: Fig 11 범례 "Exp/Theory for H = 0.05 m / 0.1 m" (page-08 스캔 + 362행 번역).
- $a/H = 0.1, 0.3, 0.5$: Fig 11 데이터 점 3곳 (page-08 스캔 직접 확인). 356행 본문이
  "a/H=0.1, H=100" (보정), "a/H=0.3, H=100" (이상치) 명시.
- 6케이스 산술: 5/15/25, 10/30/50 mm — 단순 곱, 확인.
- Karihaloo ref [39] = "Size effect in concrete beams," EFM 2003, 70, 979–993 (714행에서 확인).
  노치비 0.05/0.10/0.30/0.50 은 round2 Codex 가 확인 (0.50 포함).
- $S=L$, $\nu=0.2$, $P_0$, 평면가정 = 모두 "가정"/"FE" 태그로 분류. DECISION_round4 §3 열림 항목과 정합.

## 5장 Fig 11 판독표 — 자체 판정: 근사값, 단서 명시함

- 값은 page-08 Fig 11 산점도 육안 판독. ±0.1~0.2 kN 불확실.
- a/H=0.1: H50 Exp≈2.2 Theory≈2.35 / H100 Exp≈Theory≈3.5 (보정점, 겹침)
- a/H=0.3: H50 Exp≈1.65 Theory≈1.45 / H100 Exp≈2.9 Theory≈2.35 (이상치, 실험>이론)
- a/H=0.5: H50 ≈0.8~0.9 / H100 Exp≈1.35 Theory≈0.95
- Karihaloo 2003 원 데이터 표 미확보 → 정량 재현 판정 불가라고 명시 (round4 §7).

## 6장 워크플로우 — 자체 판정: 정확 (round3·4)

- $K_{I,\text{fit}} = \sqrt{2\pi}\hat K$ (곡선맞춤 상수 → 표준 K).
- $Y = K_{f,4}^2/(2\pi E)$, $P_{\text{pred}} = \sqrt{2\pi EY}/(K_I/P)$ — DECISION_round4 §5.
- SENB $F(\alpha)$ = Srawley 1976 형상함수 (S/W=4). DECISION_round1 §4.3 에 동일 식.
- 무차원 $K_I W\sqrt H/P = (S/H)F(a/H)$ — DECISION_round4 §1.2.
- 정규화 거리 역변환·반모델 하중 환산 언급 — DISCUSSION §2.2.

## 7장 확정/정정/열림 — 자체 판정: DISCUSSION·DECISION 과 정합하도록 작성

- 확정: DISCUSSION §1 + DECISION_round1 §1.
- 정정: Y≡Gc (round1), σ_xx (round4 §1.1), 무차원 (round4 §1.2), 2D/3D (round4 §1.3),
  2식 추가 (round3, DISCUSSION §2.2), 인용 (round2, DISCUSSION §2.4·2.5), 스크립트 버그 (round4 §1.4·1.5).
- 열림: DISCUSSION §3 + DECISION_round4 §7.

## 내가 의심하는 부분 (Codex 가 집중 검토해줄 것)

1. 그림 2-1 (Griffith 에너지 곡선) 을 3점굽힘 유한시편 맥락에 넣는 게 오해를 유발하나?
   (무한판 중앙균열 도식인데)
2. Fig 11 판독값 중 a/H=0.5 H100 Theory≈0.95 가 특히 불확실. 산점도에서 4점이 뭉쳐 있음.
3. 1장에서 $\sigma_x$ 로 개구응력을 쓴 것 — 선1 원문은 Case 2 에서 $\sigma_x$, 좌표축은
   $y$ 방향으로 $s$ 를 잡음. 보고서 4장에서는 모델 좌표계로 개구=X, 성장 s=+Y.
   1장(일반 LEFM)과 4장(모델 좌표계) 의 축 표기가 혼동되지 않나?
4. "$G \geq 2\gamma_s$" 에서 비가역 파괴는 $G \geq G_c$ 로 써야 하는데, 2장에서 두 표기가
   섞여 나오는 것이 문제인가?
