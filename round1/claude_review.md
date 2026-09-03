# Round 1 교차검증 — Claude가 codex.md 검토

> 대상: `round1/codex.md` (Codex 산출물: 단일 HTML) vs `round1/claude.md` + `round1/lefm_초보자_설명.html` (Claude 산출물).
> 근거: 두 PDF를 직접 열어 대조함.
> - `[선행연구 1]` Kwon, *J. Pressure Vessel Technol.* **143**(6), 064503 (2021) — 전문 3쪽.
> - `[선행연구 3]` Kwon, Markoff, DeFisher, *Materials* **17**(3), 569 (2024) — pp. 1–9 확인.
>
> 참고: 두 산출물의 형식이 다르다. Claude는 "보고서(claude.md) + HTML" 을, Codex는 "HTML 한 파일(codex.md)" 만 냈다.
> 아래 검토는 **두 HTML 문서의 내용**을 비교한 것.

---

## 1. 공통점 (양쪽 모두 맞음 — PDF로 확인)

| 항목 | 확인 근거 |
|---|---|
| **출처 제한 준수** — 두 PDF만 사용, K=σ√(πa)·Griffith 유도 등 교과서 내용 배제 | 양쪽 문서 모두 상단에 명시. [선1] References는 Irwin·Kirsch·Sapora 3건뿐, Griffith 없음 — 확인 |
| **단일 HTML, 외부 의존 0** | Claude: `<canvas>`+JS / Codex: 인라인 `<svg>`. 둘 다 CDN·이미지 파일 없음 |
| σ_x = K/√(2πr) 를 [선1] Eq.(4)로 인용, Irwin 근접장 | [선1] p.2 Eq.(4) 원문 일치. "r is the radial distance from the crack tip [1]" |
| 균열선단 응력 → 무한대(특이성) | [선1] Case 2 "The stress at the crack tip is infinite" / [선3] §1 "stress singularity at the crack tip" |
| **선단에서는 응력조건이 자동 만족 → 응력구배(또는 K)가 파손 지배** | [선1] Case 2 "Then, the stress gradient is the dominating factor" / [선3] §4.3 "the stress condition is already satisfied at the crack tip" — 양쪽 문서 모두 정확히 반영 |
| K_Ic = √(2πE·w_f), w_f 단위 J/m²(에너지/면적) | [선1] Eq.(7) + 본문 "units of w_f are Pa·m = N/m = J/m²" |
| 파손 판정 = K 대 K_Ic, 에너지방출률 관점과 등가 | [선3] Eq.(4) "the material failure value Y is equivalent to the critical energy release rate" |
| **구멍·둔한 노치엔 K 대 K_Ic를 그대로 쓰지 않음** (critical distance, cohesive zone 등 별도 기준) | [선3] §1 원문. 양쪽 문서 모두 "혼동 주의" 박스로 처리 |
| [선3] §4.3: K는 2D FEA + Eq.(3) 곡선맞춤으로 구함, 파손하중은 Eq.(4)로 | [선3] p.7 원문 일치. Codex의 "Figs. 8–11" 인용도 정확(Fig 8 모델, 9 메쉬, 10 곡선맞춤, 11 비교) |
| 그림은 원문 복제가 아니라 새로 그림 | 양쪽 명시 |
| 실제 재료는 선단 소성·손상으로 무한응력이 그대로 나오진 않음 | 양쪽 캡션에 명시 |

**→ 두 문서 사이에 사실관계 정면충돌은 없다.** 인용한 식·문장은 양쪽 다 PDF와 일치.

---

## 2. 충돌 / 접근 차이 (사실 오류 아님, 완성도·깊이 차이)

### (a) 시각화 방식 — **가장 큰 차이**
- **Claude**: `σ_x=K/√(2πr)` 를 실제로 계산해 그린 정량 그래프 3개
  (선형축 발산 곡선 / log–log 기울기 −1/2 / K–K_Ic 판정 + 하중단계 막대) + `console.assert` self-check 2개.
- **Codex**: 계산 없는 **개념 도식** 2개. §tip의 "σ ∝ 1/√r" 곡선은 실제 식이 아니라 손으로 그린 베지어 path
  (`d="M48 44C73 72 ..."`). §judge는 K vs K_Ic **게이지**(초보자에겐 직관적).
- 평가: PROBLEM의 "균열선단 응력집중 시각화" 요건은 **정량 표현이 Claude 쪽이 충실**. 발산·−1/2 기울기를
  Codex 문서에서는 볼 수 없음. 반면 K–K_Ic 비교의 **직관적 전달은 Codex 게이지가 더 나음**.

### (b) 두 논문의 2π 불일치 처리
- **Claude**: 명시 경고 박스 — [선1] w_f=K²/(2πE) vs [선3] Y=K²/E → **2π(≈6.28)배 차이, 섞어 쓰지 말 것**.
  직접 검산함: 동일한 응력구배 판정식에 [선1]은 σ=K/√(2πr), [선3]은 σ_e=K/√s 를 대입 →
  각각 K²/(2πE), K²/E 가 나옴. **실재하는 불일치가 맞다** (관례상 G=K²/E' 이므로 [선3] 쪽이 표준).
- **Codex**: "두 원문은 상수 표기가 다르다. 여기선 [1] 표기를 일관 사용" 한 줄. **정량화 안 함, [선3] Eq.(4)(Y=K²/E) 자체를 문서에 아예 안 실음.**
- 평가: Claude가 더 정확·완전. 초보자용이라도 이 6.28배 함정은 짚어줄 가치가 있음.

### (c) 다루는 범위
- Claude만 있음: log–log 특이성 뷰, 핵심 수식 요약표(§6), 개념설명용 예시 수치(K=1 MPa√m 등),
  **연성재 한계** ([선3] §3.2 알루미늄 — "failure ... governed by the stress condition rather than the
  stress-gradient condition, even though they contain a circular hole", PDF p.5·p.4 확인).
- Codex만 있음: sticky 목차·헤더 등 문서 완성도, K–K_Ic 게이지 메타포.

---

## 3. Codex의 오류 / 약점

| 구분 | 내용 |
|---|---|
| **약점(사실오류 아님)** | §tip SVG 곡선이 식 그래프가 아니라 장식용 path — 초보자가 "발산"을 못 봄 |
| **약점** | 2π 불일치 미정량 + [선3] Eq.(4) Y=K²/E 누락 (2절 b) |
| **약점** | [선3] §3.2 연성재 한계(응력조건 지배) 미반영 — §limits는 "큰 비선형 영역" 일반론만 |
| **약점** | Irwin(1957)을 식(4) 출처로 이름 명시 안 함 ([선1]이 명시적으로 [1]=Irwin 인용) |
| **약점** | self-check/검산 장치 없음 (JS 없음) |
| **경미(문구)** | §tip `<desc>` alt-text: "응력이 1 제곱근 r에 비례해 증가" — "1/√r에 반비례"의 잘못된 표현. 정작 그림 라벨·캡션엔 "σ ∝ 1/√r" 로 맞게 적힘 |
| **경미** | 출처 목록 "[1] 식 (1)–(7)" — [선1]엔 Eq.(13)까지 있음(구멍 사례). "문서에 쓴 식" 범위 표기로는 무방 |

**하드 팩트 오류는 발견 못 함.** Codex가 인용한 식·문장은 전부 PDF와 일치.

---

## 4. Claude가 놓친 점 / Claude 문서의 약점

| 구분 | 내용 |
|---|---|
| **내부 모순** | HTML 요약줄 "두 논문 모두 K²/E (∝ 에너지방출률)" 및 §7 결론 "K²/E ∝ G_c" — 바로 위 2π 경고 박스와 어긋남. [선1]은 K²/**(2π**E**)**. → "[선1]: K²/(2πE), [선3]: K²/E" 로 구분해 써야 함 |
| **개념 뭉갬** | [선1] σ_l("local stress")과 [선3] σ_e("effective stress")를 §2·§6 표에서 "σ_l ≥ σ_f" 로 통합. [선3]의 σ_e는 재료거동별로 다르게 정의됨(취성=최대주응력, 연성=최대전단/8면체전단, 이방성=복수). **[선3]이 연성·이방성·복합재까지 확장되는 근거가 이 effective stress 개념인데** 초보 설명에서 이를 "국부응력"으로만 부르면 그 확장성이 사라짐 |
| 표현 | [선3] Eq.(3)을 "[선1]의 간략형(√(2π) 생략)" 으로 규정 — 두 논문은 그런 관계를 명시하지 않음(같은 저자의 다른 표기일 뿐). 다만 Irwin 관례가 √(2π) 포함이므로 방향은 맞음 |
| 자기지적 | 그림3 좌측 "K ∝ P" 축이 초보자에게 순환적(P_f가 곧 파손하중). Claude 스스로 미해결로 남김 — Codex는 P축을 안 그려 회피 |
| 검증 공백 | 양쪽 다 브라우저 렌더링 미확인. Claude canvas 텍스트 위치(`fillText` 하드코딩 좌표) 겹침 가능성 미검증 — Codex도 동일 수준 |

---

## 5. 종합

- **정확성**: 양쪽 모두 두 PDF에 충실. 인용 식·문장에 하드 오류 없음. 사실 충돌 없음.
- **Claude 우위**: 정량 시각화, 2π 불일치 정량화, 연성재 한계, 수식 요약표, self-check.
- **Codex 우위**: 문서 완성도(목차·레이아웃), K–K_Ic 게이지의 직관성.
- **Claude가 고쳐야 할 것**: HTML의 "K²/E" 일반화(→ [선1]은 K²/(2πE)), σ_l/σ_e 개념 구분.
- **Codex가 보완해야 할 것**: 시각화를 실제 식 그래프로, 2π 불일치·[선3] Eq.(4)·연성재 한계 반영.
