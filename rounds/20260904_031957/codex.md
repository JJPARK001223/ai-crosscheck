# Round 1 Codex 독립 검증

## 검증 범위와 원문 확인

`PROBLEM.md`에 지정된 두 원문 PDF를 직접 읽고, 선행연구 1의 식 (1)--(13)과 선행연구 3의 식 (1)--(4), Figure 8--11 및 그 전후 설명을 확인하였다. 이 문서는 blind 검증 결과이며 `round1/claude.md`는 읽지 않았다.

사용한 문헌은 다음과 같다.

1. Y. W. Kwon, “Revisiting Failure of Brittle Materials,” *Journal of Pressure Vessel Technology*, 143, 064503 (2021), DOI: 10.1115/1.4050989.
2. Y. W. Kwon, E. K. Markoff, S. DeFisher, “Unified Failure Criterion Based on Stress and Stress Gradient Conditions,” *Materials*, 17, 569 (2024), DOI: 10.3390/ma17030569.
3. ASTM E399, *Standard Test Method for Linear-Elastic Plane-Strain Fracture Toughness of Metallic Materials*. 아래 SENB 식은 개념적 교차검산용이며 시멘트 페이스트 시험을 E399 적합성 시험이라고 간주한 것은 아니다.

기호 충돌을 피하려고 표준 LEFM 응력확대계수는 아래에서 (K_I^{\rm std}), 선행연구 3의 식 (3)에 쓰인 계수는 (K^{(3)})로 쓴다.

## 1. 선행연구 1 식 (2)에서 식 (3)

원문의 식 (2)는

\[
\frac{\sigma_l^2/(2E)}{(1/\sigma_l)|d\sigma_l/ds|}\ge w_f
\]

이다. 분모의 역수를 곱하면

\[
\frac{\sigma_l^2}{2E}
\frac{\sigma_l}{|d\sigma_l/ds|}
=\frac{\sigma_l^3}{2E}
\left|\frac{ds}{d\sigma_l}\right|.
\]

마지막 등호는 해당 경로에서 (d\sigma_l/ds\ne0)이고 국소적으로 역함수가 존재할 때

\[
\left|\frac{ds}{d\sigma_l}\right|
=\frac{1}{|d\sigma_l/ds|}
\]

이므로 성립한다. 임계 시점에 등호를 취하면

\[
w_f=\frac{\sigma_l^3}{2E}\left|\frac{ds}{d\sigma_l}\right|.
\]

**판정: 대수 유도는 맞다.** 다만 원래 조건은 부등식이고 식 (3)의 등식은 임계상태에서만 성립한다. 응력구배가 0이면 역미분 표기는 정의되지 않으므로 식 (3)을 균일응력장에 직접 적용할 수 없다. 차원은 ‎(w_f:[\mathrm{Pa\,m}]=[\mathrm{J/m^2}])이다.

## 2. 선행연구 1 Case 2: 무한판 중앙균열

균열선 전방에서 (r=y>0)로 두면 식 (4)는

\[
\sigma_x(y)=\frac{K_I^{\rm std}}{\sqrt{2\pi y}}
=\frac{K_I^{\rm std}}{\sqrt{2\pi}}y^{-1/2}.
\]

따라서

\[
\frac{d\sigma_x}{dy}
=-\frac{K_I^{\rm std}}{2\sqrt{2\pi}}y^{-3/2},
\qquad
\left|\frac{d\sigma_x}{dy}\right|
=\frac{K_I^{\rm std}}{2\sqrt{2\pi}\,y^{3/2}},
\]

로 식 (5)가 나온다. 이를 식 (2)의 좌변에 직접 대입하면

\[
\begin{aligned}
w_f
&=\frac{\sigma_x^3}{2E|d\sigma_x/dy|}\\
&=\frac{\left(K_I^{\rm std}/\sqrt{2\pi y}\right)^3}
{2E\left[K_I^{\rm std}/(2\sqrt{2\pi}y^{3/2})\right]}\\
&=\frac{(K_I^{\rm std})^3}{(2\pi)^{3/2}y^{3/2}}
\frac{\sqrt{2\pi}y^{3/2}}{E K_I^{\rm std}}\\
&=\frac{(K_I^{\rm std})^2}{2\pi E}.
\end{aligned}
\]

따라서 식 (6)은 맞다. 이를 (K_I^{\rm std})에 관해 풀면

\[
(K_{Ic}^{\rm std})^2=2\pi E w_f,
\qquad K_{Ic}^{\rm std}=\sqrt{2\pi E w_f},
\]

이므로 식 (7)도 맞다.

**판정: 식 (4)→(5)→(6)→(7)의 대수는 모두 맞다.** 다만 이것이 고전적 Irwin 관계 (G=K_I^2/E')의 재유도는 아니다. 여기서는 제안된 응력구배 기준의 정의 때문에 (w_f=K_I^2/(2\pi E))가 나온다. 또한 평면변형률에서는 고전 관계의 유효탄성계수 (E'=E/(1-\nu^2))를 구분해야 한다.

## 3. 선행연구 1 Case 3: 무한판 원형홀

원문의 Kirsch 원주응력 식 (9)은

\[
\sigma_\theta(r,\theta)=\frac{\sigma_o}{2}
\left[1+\frac{R^2}{r^2}
-\left(1+\frac{3R^4}{r^4}\right)\cos2\theta\right].
\]

‎(r=R,\theta=\pi/2)에서 ‎(\cos\pi=-1)이므로

\[
\sigma_\theta(R,\pi/2)
=\frac{\sigma_o}{2}[1+1-(1+3)(-1)]
=3\sigma_o.
\]

반경 미분은

\[
\frac{\partial\sigma_\theta}{\partial r}
=\frac{\sigma_o}{2}
\left[-\frac{2R^2}{r^3}
+\frac{12R^4}{r^5}\cos2\theta\right].
\]

따라서

\[
\frac{\partial\sigma_\theta}{\partial r}(R,\pi/2)
=\frac{\sigma_o}{2}\left[-\frac2R-\frac{12}{R}\right]
=-\frac{7\sigma_o}{R},
\]

즉

\[
\left|\frac{\partial\sigma_\theta}{\partial r}(R,\pi/2)\right|
=\frac{7\sigma_o}{R}
\]

로 식 (11)이 맞다.

두 파괴조건은 각각

\[
3\sigma_o\ge\sigma_f
\quad\Longleftrightarrow\quad
\sigma_o\ge\frac{\sigma_f}{3},
\]

그리고

\[
\frac{(3\sigma_o)^3}{2E(7\sigma_o/R)}
=\frac{27R\sigma_o^2}{14E}\ge w_f
\quad\Longleftrightarrow\quad
\sigma_o\ge\sqrt{\frac{14Ew_f}{27R}}
\]

이다. 따라서 제안 기준에 따른 최초 파괴 공칭응력은 두 조건을 동시에 만족시키는

\[
\sigma_{o,c}=\max\left(
\frac{\sigma_f}{3},
\sqrt{\frac{14Ew_f}{27R}}
\right)
\]

이다.

**판정: 식 (9)→(11)과 식 (12)(13)의 대입은 맞다.** 다만 논문이 식 (13)을 “dominant”라고 부르는 것은 (\sigma_o\ge\sigma_f/3)이라는 사실만으로 자동 보장되지 않는다. 실제 지배조건은 위 두 임계 공칭응력의 크기를 비교해야 정해진다.

## 4. 선행연구 3 식 (1)(2) 및 (w_f)와 (Y)

원문 식 (1)은 (\sigma_e\ge\sigma_f)이다. 식 (2)은 인쇄상 절댓값 표시가 없으며

\[
\sigma_e\ge\left(2EY\frac{d\sigma_e}{ds}\right)^{1/3}
\]

로 적혀 있다. 그러나 균열 전방처럼 응력이 진행방향으로 감소하면 (d\sigma_e/ds<0)이어서 우변이 음수가 되고 조건이 무의미하게 항상 만족된다. 선행연구 1의 식 (2), 그리고 선행연구 3의 이후 사용 의도에 맞는 형태는

\[
\sigma_e\ge\left(2EY\left|\frac{d\sigma_e}{ds}\right|\right)^{1/3}
\]

이다. 양변이 비음수라고 놓고 세제곱하면

\[
\sigma_e^3\ge2EY|d\sigma_e/ds|
\quad\Longleftrightarrow\quad
\frac{\sigma_e^3}{2E|d\sigma_e/ds|}\ge Y.
\]

이는 선행연구 1 식 (2)의 좌변과 동일하다. 따라서 **동일한 응력, 경로, 탄성계수 및 절댓값 관례를 쓰면 (Y=w_f)** 이다. 둘 다 차원은 ‎(\mathrm{Pa\,m}=\mathrm{J/m^2})이다.

**판정: 식 (2)에 절댓값을 보충하면 두 논문의 물질값은 같은 정의이다. 원문 그대로라면 부호상 결함이 있다.** 같은 차원을 가진다는 사실만으로 같은 물리량이 되는 것은 아니지만, 여기서는 부등식을 재배열하면 정의 자체가 일치한다.

## 5. 선행연구 3 식 (3)에서 식 (4)

논문의 비표준 표기 그대로

\[
\sigma_e=\frac{K^{(3)}}{\sqrt{s}}=K^{(3)}s^{-1/2}
\]

이면

\[
\frac{d\sigma_e}{ds}=-\frac{K^{(3)}}{2}s^{-3/2},
\qquad
\left|\frac{d\sigma_e}{ds}\right|=\frac{K^{(3)}}{2s^{3/2}}.
\]

파괴 개시의 등호조건에 대입하면

\[
\begin{aligned}
\left(\frac{K^{(3)}}{\sqrt{s}}\right)^3
&=2EY\left(\frac{K^{(3)}}{2s^{3/2}}\right),\\
\frac{(K^{(3)})^3}{s^{3/2}}
&=\frac{EY K^{(3)}}{s^{3/2}},\\
Y&=\frac{(K^{(3)})^2}{E}.
\end{aligned}
\]

**판정: 식 (3)을 정의로 받아들이면 식 (4)의 대수 유도는 맞다.** 단, 식 (3)은 표준 Mode-I 균열선 전방장

\[
\sigma_{yy}(r,0)=\frac{K_I^{\rm std}}{\sqrt{2\pi r}}
\]

에서 (1/\sqrt{2\pi})를 생략했다. (s=r)라면 두 계수의 관계는

\[
K^{(3)}=\frac{K_I^{\rm std}}{\sqrt{2\pi}}
\]

이며, 둘을 같은 (K)라고 부르면 안 된다.

## 6. (Y)가 임계 에너지방출률 (G_c)와 동등하다는 주장 및 (2\pi) 차이

표준 LEFM의 Irwin 관계는

\[
G=\frac{(K_I^{\rm std})^2}{E'},
\qquad
E'=\begin{cases}
E & \text{평면응력},\\
E/(1-\nu^2) & \text{평면변형률}
\end{cases}
\]

이다. 반면 선행연구 3의 계수 정규화 관계를 정확히 넣으면

\[
Y=\frac{(K^{(3)})^2}{E}
=\frac{(K_I^{\rm std})^2}{2\pi E}.
\]

이는 선행연구 1의

\[
w_f=\frac{(K_I^{\rm std})^2}{2\pi E}
\]

와 정확히 같다. 즉 질문의 (2\pi) 차이는 두 물질값의 차이가 아니라 **응력장 계수의 정규화 차이를 같은 기호 (K)로 표시한 데서 생긴다.**

평면응력에서는

\[
Y=w_f=\frac{G}{2\pi},
\]

평면변형률에서는

\[
Y=w_f=\frac{(K_I^{\rm std})^2}{2\pi E}
=\frac{G}{2\pi(1-\nu^2)}.
\]

따라서 (Y)와 (G_c)는 차원이 같고 서로 비례하지만, 표준 (K_I) 및 표준 Irwin 관계를 기준으로 **수치적으로 동등하지 않다.** 선행연구 3의 “(Y) is equivalent to the critical energy release rate”라는 문장은 “동일 차원의 파괴에너지형 물질상수”라는 느슨한 의미라면 가능하지만, 등값이라는 의미라면 틀리다. 더구나 평면응력/평면변형률의 (E') 구분도 빠져 있다.

## 7. Figure 8·9의 3점굽힘 모델과 (K) 추출

### 7.1 형상, 경계조건, 하중의 원문 확인

원문 설명과 Figure 8에서 확인되는 사항은 다음과 같다.

- 전체 시편은 (L\times H\times W) 직육면체이고 (W=100\ \mathrm{mm}), (L/H=4)이다. (H)와 (a/H)를 변화시켰다.
- 길이 중앙의 바닥에서 깊이 (a)인 관통균열이 폭 (W) 전체를 지난다.
- 대칭 때문에 길이방향 반쪽만 모델링하여 길이가 (L/2)이다. 중앙 단면의 균열면을 제외한 부분에 대칭조건을 주었다.
- 바깥 지점에는 지지조건, 중앙 상면에는 폭 방향으로 분포된 하향하중을 가했다. 전체 형상으로 보면 단순지지 3점굽힘이다.
- 3D 모델은 약 (0.3\ \mathrm{mm}) 균일 솔리드 요소를 사용했다. 폭에 따른 균열선 응력분포가 유사하다는 관찰 뒤 4절점 사각형 요소의 2D 모델(약 10,000 요소)로 파괴하중을 계산했다.

Figure 8의 치수선은 지점에서 중앙까지 (L/2)이므로 전체 지점간 거리 (S=L)로 읽히며, 따라서 (S/H=4)이다. 다만 논문은 지지 접촉, 하중 분포 폭, 2D 평면응력/평면변형률 선택, 요소 적분법 및 정확한 구속 자유도를 충분히 명시하지 않았다. 반쪽 모델에서는 중앙 하중과 반력의 계수가 전체 모델의 총하중 (P)인지 반쪽 모델의 등가하중 (P/2)인지도 명확히 정의해야 한다.

### 7.2 FEA 응력곡선 맞춤의 타당성

선형탄성 균열해석에서 FEA로 얻은 균열 전방 응력을 (s^{-1/2})에 맞춰 선도계수를 구하는 발상 자체는 타당하다. 선형 해석이면 (K\propto P)이므로 단위하중당 (K)를 구한 뒤 임계값에 도달하는 하중을 스케일링할 수도 있다.

그러나 논문의 실행에는 다음 검증 공백이 있다.

1. 맞춤식은 표준장이 아니라 (\sigma=K^{(3)}/\sqrt{s})이다. 따라서 산출 계수는 (K_I^{\rm std}/\sqrt{2\pi})이고 표준 SIF와 이름만 같을 뿐 수치가 다르다.
2. Figure 10의 횡축은 “Normalized Distance from Crack Tip”인데 식 (3)의 (s)는 길이 차원을 가져야 한다. (\bar s=s/\ell_0)에 맞췄다면
   \[
   \sigma=\frac{K^{(3)}}{\sqrt{s}}
   =\frac{K^{(3)}/\sqrt{\ell_0}}{\sqrt{\bar s}}
   \]
   이므로 맞춤계수에 반드시 ‎(\sqrt{\ell_0})를 다시 곱해야 한다. 정규화 길이와 역변환이 보고되지 않아 Figure 10만으로는 (K)의 차원과 값 재현이 불가능하다.
3. 균열첨단 바로 옆의 일반 유한요소 응력은 메시 의존적이므로 첫 절점들을 제외해야 하고, 너무 먼 점에서는 비특이 (T)-stress와 고차항이 개입한다. 즉 (K)-지배영역의 맞춤 구간, 절점/적분점 값, 가중치, 적합도 및 구간 변화 민감도를 제시해야 한다. 논문에는 이 정보가 없다.
4. quarter-point 특이요소, (J)-적분 또는 interaction integral과의 교차검산이 없다. “약 10,000 요소”라는 총수와 정성적 mesh sensitivity 언급만으로 (K) 수렴을 입증할 수 없다.
5. 한 시험 ‎(H=100\ \mathrm{mm},a/H=0.1)에서 (Y)를 역식별하고 그 점에서 이론과 실험이 정확히 일치한다고 한 것은 검증이 아니라 보정이다. 나머지 형상에 대한 예측만 독립 검증 자료가 된다.

따라서 **절차의 원리는 타당하지만, 현재 보고만으로 추출된 (K)의 표준값·차원·수렴성과 불확도를 재현 검증할 수 없어 정량적 타당성 입증은 불충분하다.**

### 7.3 ASTM E399형 SENB 식과 개념 비교

폭(여기서는 시편 높이) (H), 두께 (B=W), 지점간 거리 (S), 중앙 총하중 (P), (x=a/H)인 단일모서리균열 3점굽힘(SENB)의 통상 핸드북형은

\[
K_I^{\rm std}=\frac{PS}{B H^{3/2}}f(x),
\]

\[
f(x)=\frac{3\sqrt{x}}{2(1+2x)(1-x)^{3/2}}
\left[1.99-x(1-x)(2.15-3.93x+2.7x^2)\right]
\]

형태이다. 이 식은 논문 형상의 (S/H=4), (B=W), (x=a/H)를 넣어 FEA의 **표준** (K_I^{\rm std}/P)를 독립 교차검산하는 데 적합하다. 논문 식 (3)으로 맞춘 값과 비교하려면

\[
\frac{K^{(3)}}{P}
=\frac{1}{\sqrt{2\pi}}
\frac{S}{BH^{3/2}}f(a/H)
\]

로 변환해야 한다. 이 비교를 하지 않으면 (2\pi), 총하중/반모델 하중, 길이 정규화 오류를 탐지하기 어렵다.

단, ASTM E399는 금속재료의 유효한 평면변형률 파괴인성 (K_{Ic}) 측정을 위한 시편·균열·크기·하중 유효성 요건까지 포함한다. 여기서는 경화 시멘트 페이스트와 논문 모델에 그 유효성 요건이 충족되었다고 확인할 자료가 없으므로, 위 식은 **기하 및 SIF 계산의 개념적 교차검산**에만 사용해야 한다.

## 종합 판정표

| 항목 | 판정 | 핵심 이유 |
|---|---|---|
| 1 | 맞음(조건부) | 역미분과 임계 등호가 성립하는 비영 구배 구간에서 식 (3)이 정확히 나옴 |
| 2 | 맞음 | 직접 미분·대입하면 식 (5)--(7)이 정확히 나옴 |
| 3 | 맞음, 지배조건 설명은 느슨함 | Kirsch 대입과 미분은 정확하나 실제 지배조건은 두 임계응력 비교 필요 |
| 4 | 절댓값 보충 시 맞음 | 재배열하면 (Y=w_f); 선행연구 3 인쇄식은 구배 부호 문제 있음 |
| 5 | 자체 표기 안에서는 맞음 | 식 (4)는 나오지만 (K^{(3)}=K_I^{\rm std}/\sqrt{2\pi}) |
| 6 | 등값 주장 틀림 | 표준 LEFM 기준 (Y=G/(2\pi)) (평면응력), 평면변형률에는 추가 (1-\nu^2) 계수 |
| 7 | 원리는 가능, 보고·검증 불충분 | 거리 정규화, 맞춤창, SIF 정규화, 하중 정의, 수렴·독립 교차검산이 미보고 |

가장 중요한 결론은 선행연구 1과 3의 파괴값 사이에 실제 (2\pi) 불일치가 있는 것이 아니라, 선행연구 3이 비표준 균열장 계수를 표준 SIF와 구별하지 않은 데 문제가 있다는 것이다. 그 정규화를 일관되게 복원하면 (Y=w_f=K_I^2/(2\pi E))이고, 바로 그 때문에 (Y=G_c)라는 수치적 동일성 주장은 성립하지 않는다.
