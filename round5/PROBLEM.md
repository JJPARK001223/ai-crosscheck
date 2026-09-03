# PROBLEM — Round 5: 보고서 검증

대상: `round5/보고서.html`
(제목 "선형탄성파괴역학과 에너지 접근법에 기반한 경화 시멘트 페이스트 3점굽힘 균열시편 — FE 재현을 위한 모델 수치 역산")

이 보고서는 round1~4 교차검증 결과 + 선행연구 3 §4 원문을 근거로 Claude가 작성했다.
아래 항목이 **정확 / 부분 정정 필요 / 틀림 / 확인 불가** 인지 각각 독립 판정한다.

## 검증 항목

1. **1장 LEFM 개념** — 균열 선단 특이응력장 $\sigma_x = K_I/\sqrt{2\pi r}$, $K_I \propto P$,
   소규모 항복(SSY)·K-지배영역 설명이 교과서적으로 정확한가. 과장·오류 있는가.

2. **2장 에너지 접근법**
   - Griffith 에너지 균형: $-d\Pi/dA \geq dW_s/dA = 2\gamma_s$ → $G \geq 2\gamma_s$ (계수 2 = 두 표면)
   - Irwin: $G = K_I^2/E'$, $E' = E$(평면응력) / $E/(1-\nu^2)$(평면변형)
   - 본 기준 관계: $Y = w_f = K_I^2/(2\pi E) = G/(2\pi)$ (평면응력), $\neq G_c$
   - 그림 2-1 (표면에너지 선형↑ + 방출에너지 $-a^2$ + 전체 극대 $a_c$) 개념도가 맞는가
   - 참고문헌 인용 ([11][12] Griffith, [9][10] Irwin)이 배경/대비 인용이라는 서술이 맞는가

3. **3장 식 유도 박스체인** — 대수 검산:
   - $\sigma_x = \frac{K_I}{\sqrt{2\pi}} r^{-1/2}$ → $\frac{d\sigma_x}{dr} = -\frac{K_I}{2\sqrt{2\pi}\, r^{3/2}}$
   - 응력구배조건 $\frac{\sigma_x^3}{2E}\left|\frac{dr}{d\sigma_x}\right| \geq w_f$ 에 대입
   - $r$ 완전 소거 → $w_f = K_I^2/(2\pi E)$, $K_{IC} = \sqrt{2\pi E w_f}$
   - 선3 평행 유도 $Y = K^2/E$, $K = K_I/\sqrt{2\pi}$ → $Y = w_f$
   각 스텝의 지수·계수가 맞는가. $(2\pi)$ 처리가 정확한가.

4. **4장 6케이스 역산 표**
   - 고정값: $W=100$, $L/H=4$, $E=20.8$ GPa (§4.1 원문 대조)
   - 판독값: $H \in \{50, 100\}$ mm, $a/H \in \{0.1, 0.3, 0.5\}$ (Fig 11)
   - 6케이스 = 2×3, $a$ = 5/15/25 (H50), 10/30/50 (H100) mm — 산술 확인
   - Case 4 (H=100, a/H=0.1) = Y 보정, Case 5 (H=100, a/H=0.3) = 이상치
   - 가정값 표기 ($S=L$, $\nu=0.2$, $P_0$, 평면가정)가 적절히 "가정"으로 분류됐는가

5. **4장 Fig 11 파괴하중 판독표** — Exp/Theory (kN) 근사값.
   Codex가 원문 스캔 접근 불가하면 "확인 불가" 명시. 접근 가능하면 값 대조.
   보고서가 "±0.1~0.2 kN 근사, 원 데이터(Karihaloo 2003) 확보 필요"라고 단서를 단 것이 적절한가.

6. **5장 워크플로우**
   - $K_{I,\text{fit}} = \sqrt{2\pi}\,\hat K$
   - $Y = K_{f,4}^2/(2\pi E)$, $K_{f,4} = (K_I/P)_4 \cdot P_{f,4}$
   - $P_{\text{pred},i} = \sqrt{2\pi E Y}/(K_I/P)_i$
   - SENB 폐형식 $K_I/P = \frac{S}{W H^{3/2}} F(a/H)$, $F(\alpha)$ 형상함수 (Srawley/Tada)
   - 무차원 $K_I W \sqrt{H}/P = (S/H) F(a/H)$
   식·계수가 맞는가. round4 DECISION과 정합하는가.

7. **6장 확정/정정/열림 요약** — round1~4 DECISION 파일들
   (`DECISION_round1_수식검증.md`, `DECISION_round2_인용검증.md`, `DECISION.md`(round3),
   `DECISION_round4_FE재현계획.md`, `DISCUSSION.md`)의 결론과 정확히 정합하는가.
   빠지거나 왜곡된 항목 있는가.

## 결과물
`round5/codex.md` 에 한국어로: 항목별 판정표 + 근거 + 보고서에서 고칠 곳(장·문단 단위).
근거 없는 주장 금지. 모르면 "확인 불가".
