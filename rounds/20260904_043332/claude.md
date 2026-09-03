# Claude 독립 조사 결과 — LEFM 초보자용 설명 단일 HTML 문서

> 조사 방식: `PROBLEM.md`만 보고 독립 수행. `round1/codex.md`는 보지 않음.
> 사용 자료: **오직** `J:\Desktop\선행연구 관련\` 의 아래 2개 PDF 본문만.
> - **[선행연구 1]** Y. W. Kwon, "Revisiting Failure of Brittle Materials,"
>   *J. Pressure Vessel Technol.* **143**(6), 064503, Dec 2021. DOI: 10.1115/1.4050989
> - **[선행연구 3]** Y. W. Kwon, E. K. Markoff, S. DeFisher, "Unified Failure Criterion
>   Based on Stress and Stress Gradient Conditions," *Materials* **17**(3), 569, Jan 2024.
>   DOI: 10.3390/ma17030569

## 산출물

- **`round1/lefm_초보자_설명.html`** — 단일 HTML 문서(외부 파일·CDN·라이브러리 0개).
  - 본문: LEFM 초보자용 설명 (정의 → 강도기준의 한계 → 균열선단 응력집중과 K →
    K 대 K_Ic 파손판정 → 적용범위 → 수식 요약표 → 결론).
  - 시각화 3개를 문서 내부 `<canvas>` + 순수 JS로 그림 (이미지 파일 없음 → "단일 HTML" 유지):
    - **그림 1** 균열선단 응력집중: σ_x = K/√(2πr) vs r, σ_f 파선 겹침, r→0 발산.
    - **그림 2** 같은 곡선 log–log (기울기 −1/2 = "1/√r 특이성").
    - **그림 3** K 대 K_Ic 파손판정: (좌) K∝P 직선이 K_Ic 파선과 만나는 P_f = 파손,
      (우) 하중단계별 K/K_Ic 막대 + 에너지 관점 주석.
  - MathJax 미사용(단일 파일 유지 목적) → 수식은 HTML/유니코드로 표기.
  - `<script>` 끝에 `console.assert` self-check 3개(식 왕복·특이성 방향).

## 두 PDF 본문에서 직접 확인한 근거 (인용)

### [선행연구 1] — 전문(3쪽) 정독

| 위치 | 원문 | 문서 반영 |
|---|---|---|
| Introduction | "isotropic brittle materials … can be considered as linear elastic until failure" | §1 '선형탄성'의 의미 |
| Introduction | "If there is a line crack, the linear fracture mechanics approach has been applied to determine the failure load." | §1 LEFM 정의 근거 |
| Eq. (1) | σ_l ≥ σ_f | §2 강도조건 |
| Case 2 | "The stress at the crack tip is infinite" | §2 특이성 |
| Eq. (4) | σ_x = K/√(2πr) — "r is the radial distance from the crack tip [1]" (Irwin 1957) | §3 + 그림 1·2 |
| Eq. (5) | \|dσ_x/dy\| = K/(2√(2π) y^{3/2}) — "crack will propagate along … y-axis" | §3 응력구배 |
| Eq. (6) | w_f = K²/(2πE) | §4 + 그림 3 |
| Eq. (7) | K_IC = √(2πE w_f) — "fracture toughness K_Ic for the first mode (opening mode)" | §4 + 그림 3 |
| Eq. (2)~(3) 본문 | "units of w_f are Pa·m = N/m = J/m² … force per unit length or energy per unit area" | §4 에너지 차원 |
| References | [1] Irwin 1957, [2] Kirsch 1898, [3] Sapora 2018 — Griffith/에너지평형 유도는 **본문에 없음** | 자료의 한계 note |

### [선행연구 3] — Abstract·§1·§2·§4 정독 (전체 19쪽 중)

| 위치 | 원문 | 문서 반영 |
|---|---|---|
| §1 | "A structural member with a crack has stress singularity at the crack tip if the material behaves linearly elastically. Thus, fracture mechanics was also developed for structural members with cracks." | §1 정의 근거 |
| §1 | "an entirely different set of failure criteria was used because fracture mechanics is suitable for holes. The critical distance failure criteria … The cohesive zone model …" | §5 한계 (구멍엔 별도 기준) |
| §2 Eq. (1) | σ_e ≥ σ_f | §6 표 |
| §2 Eq. (2) | σ_e ≥ (2EY \|dσ_e/ds\|)^{1/3} | §6 표 |
| §2 Eq. (3) | σ_e = K/√s — "s is along the crack orientation … perpendicular to the loading direction" | §3 (간략형) |
| §2 Eq. (4) | Y = K²/E — "the material failure value Y is equivalent to the critical energy release rate in fracture mechanics" | §4 에너지 관점 + 그림 3 |
| §4.1 | "hardened cement paste behaved in a brittle manner with an elastic modulus of 20.8 GPa" | §2 선형탄성 예시 |
| §4.3 | "Because the crack with stress singularity, the stress gradient condition is used … K was obtained from 2D finite element analyses … a curve fit was conducted using Equation (3) to determine K … failure loads are determined using Equation (4)." | §3·그림3 주석 (K는 FEA로, K∝P) |
| §3.2 (연성재) | 알루미늄 합금은 "failure … was also governed by the stress condition rather than the stress-gradient condition" | §5 한계 (연성재 제외) |

## 판단·근거

1. **"단일 HTML"** = 외부 의존 0. → 그림을 PNG로 굽지 않고 문서 내부 canvas/JS로 그린다.
   matplotlib 스크립트(이전 `lefm_viz.py`)는 별도 파일·실행이 필요해 "단일 문서" 요건에 안 맞음.
   MathJax도 CDN 의존이라 배제, 수식은 유니코드.
2. **곡선의 형태는 전부 위 2개 논문의 수식에서 직접 나온다.** 수치(K=1 MPa√m, E=3 GPa,
   σ_f=70 MPa, K_Ic=1 MPa√m)는 "개념 설명용 예시"로 명시. 두 논문은 무한판 K 닫힌형
   (K=σ√(πa))을 본문에 안 주므로 그 식은 쓰지 않음.
3. **2π 불일치**를 문서에 경고로 넣음: [선1] w_f=K²/(2πE) vs [선3] Y=K²/E → 6.28배.
   (원인: [선1]은 σ=K/√(2πr), [선3]은 σ_e=K/√s 로 √(2π) 처리가 다름.)
4. **자료의 한계**를 상단 note로 분리: 두 논문은 LEFM 해설 논문이 아니라 통합기준 논문이고,
   Griffith 에너지평형·SSY·K-지배영역은 본문에 없고 참고문헌에만 있음 → 문서에서 다루지 않음.
5. **[선행연구 3] §1의 "fracture mechanics is suitable for holes"** 문구는 앞뒤 논리
   (구멍엔 critical distance·cohesive zone 등 *다른* 기준을 쓴다)와 모순 → "not"의
   누락/오타로 보임. 문서에는 논문의 논리(구멍엔 별도 기준)만 반영하고 그 문구는 인용하지 않음.

## 시각화 사양 (그림별)

- **그림 1** σ_x=K/√(2πr): x=0~5 mm, y=0~350 MPa(상한 클리핑). σ_f=70 MPa 파선.
  캡션에 "강도기준은 선단 근처에서 언제나 만족 ⇒ K 필요". 근거 [선1] Eq.4 / Case 2.
- **그림 2** 동일식 log–log: log10 r = −5~−2.3, log10 σ = 6~9. 직선 기울기 −1/2.
- **그림 3** (좌) 축 K/K_Ic vs P/P_f, 직선 y=x, K_Ic·P_f 파선, (1,1) 빨간 점 "파손".
  (우) 막대 0.4/0.7/1.0×K_Ic("낮음/중간/파손") + K_Ic 파선. 주석에 [선1] Eq.7,
  [선3] Eq.4. K∝P는 "선형탄성 가정의 결과, 비례상수는 형상 의존([선3] §4.3 FEA)"로 명시.

## 검증

- 두 PDF를 직접 열어 위 표의 원문을 대조함 (근거: "Codex가 말했다"가 아니라 원문).
- HTML self-check(console.assert): ① 선단 근처 σ>σ_f, 멀리서 σ<σ_f  ② Eq.(6)↔(7) 왕복 = K_Ic.
- 브라우저 실행 확인은 이 세션 범위 밖(파일만 저장). 사용자/후속 단계에서 열어 확인 필요.

## 미해결 / 후속 확인 필요

- 그림 3 좌측의 "K ∝ P"는 두 논문이 명시 식으로 주지 않고 선형탄성에서 따라오는 것 →
  캡션에 그렇게 적었으나 초보자 오해 소지 있는지 교차검증에서 볼 것.
- 한글 폰트: `Malgun Gothic` 우선 지정(Windows 기본). 타 OS에서 canvas 텍스트 폰트 대체됨 —
  기능엔 영향 없음.
- [선행연구 3] 10~19쪽(PLA·복합재 사례)은 LEFM 초보 설명과 무관해 미반영.
