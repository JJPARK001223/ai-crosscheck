# DECISION — Round 4 (최종: Claude 판정)

주제: `FE재현계획_HCP_3PB균열.html` (FE 재현 작업 계획서) + 현행 스크립트
`01_cement_paste_3PB_model.py` · `02_read_K.py` 의 정확성.

입력: `round4/claude.md` (Claude 자체분석), `round4/codex.md` (Codex blind),
`round4/codex_review.md` (Codex의 claude.md 검토). 원문 §4.2–4.3, Abaqus 공개 문서.

---

## 1. 확정 오류 — 반드시 고칠 것

### 1.1 ★ 곡선맞춤 응력 성분 : $\sigma_{yy}$ → $\sigma_{xx}$ (S11)
- 좌표계: $X$=길이, $Y$=깊이, $Z$=폭. 균열면 = $X=L/2$ 평면. 개구방향 = $X$.
  균열 성장·거리 $s$ = $+Y$. 균열전선 = $Z$축.
- **모드 I 개구 정상응력 = $\sigma_{xx}$ = S11.** 계획서가 쓴 $\sigma_{yy}$(S22)는 성장방향 응력 → 틀림.
- 표준: $\sigma_{xx} = K_I/\sqrt{2\pi s}$. 논문 $\sigma_e = K/\sqrt s$ → **$K_{paper} = K_I/\sqrt{2\pi}$.**
- 단, 논문의 $\sigma_e$ 가 전역 S11 인지 **최대 주응력** 인지는 원문 §2·그림으로 추가 확인
  (등방 취성재 → 통상 최대 정규응력). 확인 전 S11 ≡ $\sigma_e$ 로 단정 금지.

### 1.2 ★ 무차원 형상계수 : $K/(P H^{-3/2})$ → $K_I\,W\sqrt{H}/P$
- 표준 SENB: $K_I = \dfrac{P\,S}{W\,H^{3/2}}F(a/H)$ &nbsp;($W$=두께=우리 폭, $S$=스팬=$4H$).
- $H$=50·100 을 같은 축에서 비교할 무차원량:
  $$\boxed{\;\dfrac{K_I\,W\sqrt{H}}{P} = \dfrac{S}{H}\,F(a/H) = 4\,F(a/H)\;}$$
- 계획서 $K H^{3/2}/P$ 는 여기에 $H/W$ 가 더 곱해져 $H$=100 을 $H$=50 대비 2배 이동시킴 → 틀림.
- claude.md 대안 $K H^{-1/2}/P$ 도 차원이 $1/\text{길이}$ → 오답. **$W$ 를 곱해야 무차원.**
- (동일 $W$=100 데이터의 collapse 여부만 보면 $K_I\sqrt H/P$ 로도 판단 가능 — 공통상수 $1/W$ 생략.
  단 보고·검증용 형상계수는 $K_I W\sqrt H/P$ 로.)

### 1.3 ★ 2D / 3D 역할 뒤바뀜
- 논문 §4.2: 3D 반모델로 "K 폭방향 균일" **1회 확인** → **2D 4절점으로 6케이스 예측**.
- 계획서·현행 `01`(3D C3D10, 3케이스)은 논문 본체(2D 곡선맞춤)와 요소·차원·추출법이
  전부 달라 재현이 아님.
- **주 워크플로우 = 2D 6케이스. 3D = 대표 1케이스 $K(z)$ 검증.**

### 1.4 ★ 코드 버그 — `centerVerts` (01, 103–108행)
- 압출 육면체 $X{=}0,Y{=}0$ edge 는 $Z{=}0,W$ 끝에만 vertex. $Z{=}W/2$ 에 vertex 없음.
- `getByBoundingBox(...z=W/2...)` → 빈 배열 → `if len(centerVerts)>0:` 가 **경고 없이
  `Support-AntiRigid`(U3=0) 생략** → 폭방향 강체병진 $t_3$ 잔존 → **singular matrix.**
- 수정: (a) 지지 edge 를 $Z=W/2$ 에서 partition → vertex 생성 → 정확히 1개 assert, 또는
  (b) **폭 절반 모델 ($0..W/2$) + $Z=W/2$ 에 ZSYMM.**

### 1.5 코드 버그 — `02_read_K.py` K1 평탄화 (29–49행)
- 모든 history region 의 K1 을 한 리스트로 append → contour 번호 + **crack-front 위치**(3D
  다절점) 가 섞임 → "앞 N개 제외 평균" 무의미.
- 수정: region 이름 파싱 → `(front node / z, contour number)` 로 구조화 → 위치별 contour
  plateau 확인 → plateau 평균·범위·변동계수 저장.

## 2. 확정 — 맞았던 것 (유지)

| 항목 | 판정 |
|---|---|
| 반모델 형상·BC (대칭면 $U_1$=0 단 균열면 제외 / 롤러 / 상단 절반하중) | ✅ 물리적으로 일관 (원문 문구별 대조는 도면 확보 시) |
| 하중 규약 (식 11) | ✅ 반모델 $P_0/2$ 입력 → K는 **총하중 $P_0$ 상태**의 K → $(K/P)_{total}=K_{contour}/P_0$. 추가 2배·$\sqrt2$ 보정 **금지** |
| `symmetric=True` | ✅ 에너지 2배로 **올바른 K** 계산 (K를 절반으로 만들지 않음) |
| `crackNormal` 의미 | ✅ 균열면 **법선** ($q=t\times n$ 자동). $t$=+Z, $n$=+X → $q$=+Y (의도 부합). 단 edge 순서 반대면 부호 뒤집힘 → `.dat` q 방향·J 부호 확인 |
| round3 15식 매핑 (계획서 §3) | ✅ DECISION §7.2 와 정합 |
| 스펙문서(00) 폐기논리 정정 | ✅ round2 반영 정확 |

## 3. 확인 불가 (원문·설치본 확인 게이트)

| 항목 | 게이트 |
|---|---|
| `ContourIntegral(crackNormal=...)` Python 인자 형식 | 공개 2016 Reference = 두 점 sequence. **2020/2021 설치본**의 CAE replay 또는 로컬 Scripting Reference 로 최종 확인. 일단 `crackNormal=((0.,0.,0.),(1.,0.,0.))` 로 수정 |
| 2D 평면응력 vs 평면변형 | 논문 §4.2 요소명·두께 규약 확인. 명시 없으면 3D 중앙부 $K/P$ 와 두 가정 대조 + 민감도 보고. **$Y=K^2/E$ 만으로 평면응력 확정 금지** |
| 논문 $\sigma_e$ = S11 vs 최대주응력 | 원문 그림·데이터 |
| $S=L$ | Karihaloo 원 도면 (round2) |

## 4. claude.md 정정 (내가 틀렸던 것)

- "$K H^{3/2}/P$ 는 차원이 틀림 (지수 부호)" → **틀린 설명.** 그 양은 무차원. 문제는 $W$ 누락.
- 대안 "$K H^{-1/2}/P$" → 차원 $1/\text{길이}$, 오답. 정답 $K_I W\sqrt H/P$.
- "강체회전 구속 불완전" → **근거 부족.** 세 BC 가 실제 적용되면 6 강체모드 모두 제거
  (리거먼트면 $U_1$=0 → $t_1,\omega_2,\omega_3$ / 지지선 $U_2$=0 → $t_2,\omega_1$ / 1점 $U_3$=0 → $t_3$).
  진짜 문제는 §1.4 (BC 가 코드상 안 걸림).
- "$\sigma_{yy}$ 곡선맞춤" → §1.1, $\sigma_{xx}$ 로 정정.
- "평면응력으로 확정" → §3, 확인 불가.

## 5. 추가 필수 절차 (계획서·스크립트에 넣을 것)

1. **경로 A/B 정규화 분리**: CSV·변수명에서 $K_{paper}=K_I/\sqrt{2\pi}$ 와 $K_I$ 를 구분.
   Y 역산은 사용한 K 정의에 맞춰 $\sqrt{EY}$ (논문 K) 또는 $\sqrt{2\pi EY}$ ($K_I$).
2. **검증 게이트 순서**:
   ① 무균열/얕은균열 모델 반력·대칭 검산
   ② 2D 케이스 1개 → 표준 SENB 폐형식과 대조 (하중·폭·두께·K 정규화 검증)
   ③ 같은 케이스 메시 3수준 + 맞춤창 이동 → $K_{fit}$·contour K 수렴
   ④ 3D 대표 케이스 → $K(z)$ (자유표면 vs 중앙면)
   ⑤ 검증된 2D 절차를 6케이스에 → 케이스4 1회 보정 → 나머지 5개 예측
3. **반력 검산**: 선택면적 × 압력 = $P_0/2$ assert, 해석 후 $\sum RF2$ 검산, 압력 부호 확인.
4. **모든 `getByBoundingBox` 선택**: 예상 개수·좌표·길이 assert (조용한 과/무선택 방지).
5. **contour**: "앞 N개 제외 평균" 금지 → 위치별 contour plateau·경로독립 구간 선택.
6. **J 출력 병행**: $J = K_I^2/E'$ 로 kFactor 검산.
7. **Fig 11 값**: 눈대중 ±0.15 kN 삭제 → **Karihaloo, Abdalla, Xiao 2003 원 데이터 표**
   (케이스 조합·폭·스팬·파괴하중) 확정. 이 입력 없으면 정량 재현 판정 불가.
8. **±5% 임의 기준 삭제** → 메시·데이터 불확도 예산으로 대체.

## 6. 스크립트 재작성 방침

### 신규 `01_2d_sixcases.py` (본체) — 2D 6케이스
- $H\in\{50,100\}$ × $a/H\in\{0.1,0.3,0.5\}$ 이중 루프.
- 평면 요소 CPE4/CPS4 (평면변형/응력 선택 파라미터). 두께 = $W$ = 100.
- 균열: seam (X=L/2, Y=0..a). 팁 메시 0.3 mm, focused rosette 권장 (없으면 조밀 free).
- 경로 A: 균열선 $s$ 따라 S11 (또는 최대주응력) path 출력.
- 경로 B: 2D ContourIntegral (`crackNormal=((0.,0.,0.),(1.,0.,0.))`, 두 점).
- 반력·assert·수렴 게이트 포함.

### `02_read_K.py` 재작성
- 6 tag, `(z/front, contour)` 파싱, plateau 통계, `K1`·`J`·`K1/sqrt(2π)`·`K1/P0` 컬럼.
- Abaqus 2020 = Python 2.7 → `open(...,'wb')` 유지 (Codex의 Python3 지적은 2024+ 버전 한정).

### 신규 `03_curvefit_K.py` — 경로 A
- path CSV → $\ln\sigma$ vs $\ln s$ 최소자승. 자유기울기 → $-\tfrac12$ 근접 확인 →
  $-\tfrac12$ 고정 재적합. 맞춤창 $[s_{min},s_{max}]$ 스윕. $\hat K$ → $K_{I,fit}=\sqrt{2\pi}\hat K$.

### 신규 `04_backcalc.py`
- 케이스4: $K_{f,4}=(K_I/P)_4 \cdot P_{f,4}$ → $Y = K_{f,4}^2/(2\pi E)$ (표준 $K_I$ 기준).
- 나머지 5개: $P_{pred,i} = \sqrt{2\pi E Y}/(K_I/P)_i$.
- Fig 11 비교표 + 무차원 $K_I W\sqrt H/P$ vs $a/H$ 플롯.

### 기존 `01_cement_paste_3PB_model.py` → `01b_3d_validation.py` 로 격리
- 대표 1케이스 (예: 케이스4) 3D 반모델, $K(z)$ 출력. `centerVerts` → 반폭+ZSYMM 로 수정.

---

## 7. 남은 것
- Abaqus 2020 설치본에서 `ContourIntegral` API·`crackNormal` 형식 최종 확인
- 논문 $\sigma_e$ 정의 (S11 vs 최대주응력), 2D 평면가정 원문 확인
- Karihaloo 2003 원 데이터 표 확보
- $S=L$ 확정 (Karihaloo 도면)
