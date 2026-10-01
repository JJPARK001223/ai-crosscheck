# Round 13 — Codex blind 독립 조사

## 조사 범위와 표기

이 문서는 Kwon (2021)과 Kwon, Markoff 및 DeFisher (2024)의 본문, 그리고 고전 선형탄성 파괴역학(LEFM)의 정의를 서로 대조해 A–D를 정리한 것이다. 요청에 따라 Kwon and Park (2013) 및 Kwon and Darcy (2018)의 단위셀 닫힌형 수식은 조사하거나 유도하지 않았다. 아래에서 논문 1의 재료 파괴값은 $w_f$, 논문 3의 재료 파괴값은 $\Upsilon$, 표준 LEFM 응력확대계수는 필요할 때 $K_I^{\mathrm{std}}$로 구별한다.

먼저 반드시 짚어야 할 정규화 문제가 있다. 논문 3은 식 (4) 뒤에서 $\Upsilon$이 임계 에너지 해방률과 “equivalent”하다고 서술하지만, 논문에 인쇄된 식을 표준 LEFM 정의와 대조하면 **같은 차원이고 일정한 비례관계에 있는 양**이지, 통상적인 $G_c$와 항상 수치적으로 동일한 양은 아니다. 이 점은 B와 D에서 엄밀히 구분한다.

---

## A. 식 유도 과정

### A.1. Kwon (2021) 식 (6): $w_f=K^2/(2\pi E)$

파괴 개시의 응력구배 조건은

$$
\frac{\sigma_l^3}{2E\left|d\sigma_l/ds\right|}\geq w_f. \tag{2}
$$

균열 끝단 앞의 고려 경로에서 $r=y$로 두면 식 (4), (5)는

$$
\sigma_l=\frac{K}{\sqrt{2\pi y}}
=\frac{K}{\sqrt{2\pi}}y^{-1/2}, \tag{4}
$$

$$
\left|\frac{d\sigma_l}{dy}\right|
=\left|-\frac{K}{2\sqrt{2\pi}}y^{-3/2}\right|
=\frac{K}{2\sqrt{2\pi}}y^{-3/2}. \tag{5}
$$

이를 식 (2)의 좌변에 한 줄씩 대입하면

$$
\begin{aligned}
\frac{\sigma_l^3}{2E|d\sigma_l/dy|}
&=
\frac{\left(\dfrac{K}{\sqrt{2\pi}}y^{-1/2}\right)^3}
{2E\left(\dfrac{K}{2\sqrt{2\pi}}y^{-3/2}\right)}\\[3pt]
&=
\frac{\dfrac{K^3}{(2\pi)^{3/2}}y^{-3/2}}
{\dfrac{EK}{\sqrt{2\pi}}y^{-3/2}}\\[3pt]
&=\frac{K^2}{2\pi E}
\underbrace{\frac{y^{-3/2}}{y^{-3/2}}}_{=1}\\[3pt]
&=\frac{K^2}{2\pi E}.
\end{aligned}
$$

파괴 개시의 등호 상태에서 따라서

$$
\boxed{w_f=\frac{K^2}{2\pi E}}. \tag{6}
$$

중요한 결과는 $y$가 완전히 소거된다는 것이다.

$$
\frac{\partial}{\partial y}\left(\frac{K^2}{2\pi E}\right)=0.
$$

즉, LEFM의 $y^{-1/2}$ 특이장 안에서는 어느 $y$를 택하더라도 이 조합은 같은 균열구동력 척도를 준다(단, 고차항을 무시할 수 있는 $K$-지배 영역 안이어야 한다).

### A.2. Kwon et al. (2024) 식 (4): $\Upsilon=K^2/E$

논문 3은 근접장을 다음처럼 정의한다.

$$
\sigma_e=\frac{K}{\sqrt{s}}=Ks^{-1/2}. \tag{3}
$$

따라서

$$
\left|\frac{d\sigma_e}{ds}\right|
=\left|-\frac{K}{2}s^{-3/2}\right|
=\frac{K}{2}s^{-3/2}.
$$

식 (2)의 개시 등호를 세제곱하면

$$
\sigma_e^3=2E\Upsilon\left|\frac{d\sigma_e}{ds}\right|.
$$

대입하여 정리하면

$$
\begin{aligned}
(Ks^{-1/2})^3
&=2E\Upsilon\left(\frac{K}{2}s^{-3/2}\right),\\
K^3s^{-3/2}&=E\Upsilon Ks^{-3/2},\\
K^2&=E\Upsilon,\\
\boxed{\Upsilon&=\frac{K^2}{E}}. \tag{4}
\end{aligned}
$$

여기서도 $s^{-3/2}$가 정확히 소거된다.

두 논문의 $2\pi$ 차이는 장의 진폭을 정의한 방식 때문이다.

$$
\sigma=\frac{K_I^{\mathrm{std}}}{\sqrt{2\pi s}}
=\frac{K^{(2024)}}{\sqrt{s}}
\quad\Longrightarrow\quad
K^{(2024)}=\frac{K_I^{\mathrm{std}}}{\sqrt{2\pi}}.
$$

따라서

$$
\frac{(K^{(2024)})^2}{E}
=\frac{(K_I^{\mathrm{std}})^2}{2\pi E}.
$$

즉 $2\pi$가 물리에서 사라진 것이 아니라 논문 3의 $K$ 정의 안으로 흡수되었다.

### A.3. Kirsch 해에서 최대 원주응력과 식 (11)

원공을 가진 무한평판의 원주응력은

$$
\sigma_\theta(r,\theta)=\frac{\sigma_o}{2}
\left[\left(1+\frac{R^2}{r^2}\right)
-\left(1+\frac{3R^4}{r^4}\right)\cos 2\theta\right]. \tag{9}
$$

$\theta=\pi/2$이면 $\cos 2\theta=\cos\pi=-1$이므로

$$
\begin{aligned}
\sigma_\theta(r,\pi/2)
&=\frac{\sigma_o}{2}\left[left(1+\frac{R^2}{r^2}\right)
+\left(1+\frac{3R^4}{r^4}\right)\right]\\
&=\frac{\sigma_o}{2}\left(2+\frac{R^2}{r^2}+\frac{3R^4}{r^4}\right).
\end{aligned}
$$

구멍 경계 $r=R$에서

$$
\sigma_\theta(R,\pi/2)
=\frac{\sigma_o}{2}(2+1+3)
=\boxed{3\sigma_o}.
$$

이제 $\theta=\pi/2$를 고정하고 $r$로 미분한다.

$$
\begin{aligned}
\frac{\partial\sigma_\theta(r,\pi/2)}{\partial r}
&=\frac{\sigma_o}{2}
\left[-2R^2r^{-3}-12R^4r^{-5}\right]\\
&=-\sigma_o\left(\frac{R^2}{r^3}+\frac{6R^4}{r^5}\right).
\end{aligned}
$$

$r=R$를 대입하면

$$
\left.\frac{\partial\sigma_\theta}{\partial r}\right|_{(R,\pi/2)}
=-\sigma_o\left(\frac1R+\frac6R\right)
=-\frac{7\sigma_o}{R},
$$

따라서 절댓값은

$$
\boxed{\left|\frac{\partial\sigma_\theta(R,\pi/2)}{\partial r}\right|
=\frac{7\sigma_o}{R}}. \tag{11}
$$

### A.4. 식 (12)에서 공칭응력 조건

식 (12)에 위 결과를 대입하면

$$
\sigma_\theta(R,\pi/2)\geq\sigma_f
\quad\Longleftrightarrow\quad
3\sigma_o\geq\sigma_f
\quad\Longleftrightarrow\quad
\boxed{\sigma_o\geq\frac{\sigma_f}{3}}.
$$

이는 응력 조건의 필요조건일 뿐이다. 실제 파괴에는 식 (13)의 구배 조건도 동시에 만족되어야 한다.

### A.5. 논문 3 식 (5)–(9)의 구조: 논문이 말하는 범위와 말하지 않는 범위

식 (5)는 상향화(upscaling)를

$$
E^c_{ijkl}=f(E^f_{ijkl},E^m_{ijkl},\nu^f,\nu^m) \tag{5}
$$

로만 나타낸다. 섬유·기지의 물성텐서와 체적분율로 균질 복합재의 유효 강성텐서를 만드는 사상이다. 식 (6)은 하향화(downscaling)를

$$
\varepsilon^f_{ij}=g_1(\varepsilon^c_{ij}),\qquad
\varepsilon^m_{ij}=g_2(\varepsilon^c_{ij}) \tag{6}
$$

로 나타낸다. 거시 복합재 변형률을 구성재별 변형률로 국소화한다. 이후

$$
\sigma^{f\ \mathrm{or}\ m}_{ij}
=E^{f\ \mathrm{or}\ m}_{ijkl}\varepsilon^{f\ \mathrm{or}\ m}_{kl} \tag{7}
$$

로 구성재 응력을 얻는다. 문제에 적힌 식 (7)의 마지막 첨자를 $ij$로 반복하면 아인슈타인 합 규약상 부정확하므로, 후크 법칙의 표준 텐서 축약인 $kl$로 썼다. 논문 3은 $f,g_1,g_2$의 명시적 닫힌형을 싣지 않고 유도도 생략한다. 따라서 여기서 더 전개하는 것은 논문 3 본문만으로는 불가능하다.

식 (8)은 섬유 축방향 정상응력과 축방향 전단응력을 하나의 응력차원 스칼라로 묶는다.

$$
\sigma_e^f=\sqrt{(\sigma^f_{11})^2+
\left(\frac{E_1^f}{G_{12}^f}\right)^2
\left[(\sigma^f_{12})^2+(\sigma^f_{13})^2\right]}. \tag{8}
$$

$E_1^f/G_{12}^f$는 무차원 가중치이므로 $\sigma_e^f$의 단위는 응력이다. 즉 섬유가 주로 지지하는 1방향 응력과 관련 전단성분을 동일한 파괴 판정 스칼라로 환산한다. 이것을 식 (1), (2)의 $\sigma_e$로 사용한다.

식 (9)는 계면 접선·법선 모드를 결합한다.

$$
\sigma_e^{int}=\sqrt{
\left(\frac{\sigma^m_{12}+\sqrt{\nu^f}(\sigma^m_{22}-\sigma^m_{11})}
{\tau^{int}_{fail}}\right)^2
+\left(\frac{\langle\sigma^m_{22}\rangle}{\sigma^{int}_{fail}}\right)^2}. \tag{9}
$$

첫 항은 계면 접선 파괴강도로 정규화한 전단형 구동량이고, 둘째 항은 계면 법선강도로 정규화한 인장 개구 구동량이다. Macaulay 괄호 $\langle x\rangle=\max(x,0)$는 압축 법선응력이 계면 개구파괴에 기여하지 않게 한다. 식 (9)는 인쇄된 형태상 **무차원 파괴지수**이다. 논문이 이를 “effective stress”라고 부르더라도 식 (1), (2)에 직접 넣으려면 임계값과 구배를 같은 정규화 체계로 정의해야 한다. 그 세부 연결식은 해당 본문에 명시되어 있지 않으므로 더 단정할 수 없다.

---

## B. 물리적 의미 — 왜 이런 형태인가

### B.1. 에너지 밀도와 특성 감쇠 길이의 곱

식 (2)의 좌변은 다음처럼 정확히 분해된다.

$$
\frac{\sigma^3}{2E|d\sigma/ds|}
=\underbrace{\frac{\sigma^2}{2E}}_{u}
\underbrace{\frac{\sigma}{|d\sigma/ds|}}_{\ell_\sigma}.
$$

- $u=\sigma^2/(2E)=\tfrac12\sigma\varepsilon$는 단축 선형탄성 상태의 변형률에너지 밀도이다. “한 점에 얼마나 많은 탄성에너지가 저장되어 있는가”를 뜻한다.
- $\ell_\sigma=\sigma/|d\sigma/ds|$는 현재 기울기가 유지된다고 보았을 때 응력이 자기 크기만큼 변하는 데 필요한 길이, 즉 국소 특성 감쇠 길이이다. 로그 기울기로 쓰면 $\ell_\sigma=|d\ln\sigma/ds|^{-1}$이다.
- 따라서 $u\ell_\sigma$는 에너지/체적에 유효 길이를 곱한 양, 곧 새 파면 단위면적당 동원 가능한 국소 탄성에너지의 척도로 읽을 수 있다. 다만 이는 실제 체적 적분으로 엄밀히 유도한 $J$-적분이 아니라 저자들이 제안한 국소 척도이다.

차원은

$$
[u]=\frac{\mathrm J}{\mathrm m^3}=\mathrm{Pa},\qquad
[\ell_\sigma]=\mathrm m,
$$

$$
\left[\frac{\sigma^3}{2E|d\sigma/ds|}\right]
=\frac{\mathrm{Pa}^3}{\mathrm{Pa}(\mathrm{Pa}/\mathrm m)}
=\mathrm{Pa\,m}
=\frac{\mathrm N}{\mathrm m}
=\frac{\mathrm J}{\mathrm m^2}.
$$

따라서 $w_f$와 $\Upsilon$은 에너지 해방률과 같은 차원을 갖는다.

### B.2. 왜 세제곱을 기울기로 나누는가: $r$-불변성

일반적으로 $\sigma=C r^{-1/2}$이면

$$
\sigma^3=C^3r^{-3/2},\qquad
\left|\frac{d\sigma}{dr}\right|=\frac C2r^{-3/2}.
$$

따라서

$$
\frac{\sigma^3}{2E|d\sigma/dr|}=\frac{C^2}{E},
$$

로 거리 의존성이 사라진다. 즉 “세제곱/1차 기울기” 조합은 LEFM의 $r^{-1/2}$ 특이장에 대해 균열끝 거리나 FE 표본점 선택에 의존하지 않는 $K^2/E$형 상수를 만든다. 이것이 이 형태의 핵심 설계 원리이다. 날카로운 균열에서는 응력 조건이 $r\to0$에서 자동으로 만족되고, 남는 구배 조건은 임계 $K$ 또는 그에 비례하는 임계 에너지 조건이 된다.

다만 “정확히 $G_c$와 같다”는 표현에는 정규화 주의가 필요하다. 표준 LEFM에서는

$$
G=\frac{(K_I^{\mathrm{std}})^2}{E'},\qquad
E'=\begin{cases}
E & \text{평면응력},\\
E/(1-\nu^2) & \text{등방성 평면변형률}.
\end{cases}
$$

논문 1의 정의를 그대로 쓰면

$$
w_f=\frac{(K_I^{\mathrm{std}})^2}{2\pi E}.
$$

따라서 평면응력에서는 $G=2\pi w_f$이지 $G=w_f$가 아니다. 논문 3에서도 $K^{(2024)}=K_I^{\mathrm{std}}/\sqrt{2\pi}$로 해석하면

$$
\Upsilon=\frac{(K^{(2024)})^2}{E}
=\frac{(K_I^{\mathrm{std}})^2}{2\pi E}
=\frac{G}{2\pi}\qquad(\text{평면응력}).
$$

평면변형률에서는 논문식의 $E$를 그대로 둘 경우 $E'$ 차이도 추가된다. 그러므로 정확한 결론은 다음과 같다.

1. 이 기준은 날카로운 균열 극한에서 **$K^2/E$형 임계조건**, 즉 Griffith–Irwin 에너지 기준과 상수배로 일대일 대응하는 조건으로 환원된다.
2. 표준 $G_c$와 수치적으로 동일하게 쓰려면 $2\pi$ 정규화 및 $E'$를 일관되게 반영해야 한다. 예컨대 평면응력에서 $\widetilde\Upsilon=2\pi\Upsilon$로 정의하면 $\widetilde\Upsilon=G_c$이다.
3. 논문 3의 “equivalent to the critical energy release rate”는 이 물리적 등가성을 뜻한다고 읽을 수 있지만, 인쇄된 정의에서 $\Upsilon=G_c$라는 수치 등식은 성립하지 않는다.

원공처럼 응력이 유한한 경우에도 같은 국소량은 계산 가능하다. 특이성이 없어도 $\sigma$, $d\sigma/ds$, $E$가 있으면 $u\ell_\sigma$를 얻을 수 있고, 응력 집중이 매우 좁으면 $\ell_\sigma$가 작아 구배 조건이 엄격해지며, 응력 고원이 넓으면 $\ell_\sigma$가 커져 완화된다. 그래서 균열 전용의 기하학적 $K$ 해가 없어도 구멍·노치·무노치 형상을 같은 두 조건으로 평가한다는 것이 저자들의 통합 취지이다.

### B.3. 왜 두 조건이 모두 필요한가

응력 조건과 구배 조건은 각각 다른 실패 모드를 막는다.

- **응력 조건만 사용:** 이상적인 날카로운 균열에서는 $\sigma\sim r^{-1/2}\to\infty$이므로 아무리 작은 외력에도 충분히 작은 $r$에서 $\sigma\geq\sigma_f$가 된다. 그러면 유한한 임계 하중을 결정하지 못하고 “항상 파괴”라는 잘못된 결론에 이른다.
- **구배 조건만 사용:** 균일 단축응력에서는 $d\sigma/ds=0$이다. 재배열형 식 (2) 우변은 0이므로 구배 조건은 모든 양의 응력에서 만족한다(원래 분수형은 분모 0이므로 극한적으로 무한대). 그러나 실제 개뼈다귀 시편은 $\sigma=\sigma_f$에 도달해야 파괴한다. 따라서 강도 문턱이 별도로 필요하다.

결국 파괴 개시는 후보점 $x$에서

$$
\sigma_e(x)\geq\sigma_f,qquad
\frac{\sigma_e(x)^3}{2E|d\sigma_e/ds|(x)}\geq\Upsilon
$$

를 동시에 만족하는 최초 하중으로 정의된다. 논리적으로는 두 요구 문턱 중 더 늦게 충족되는 쪽이 하중을 지배한다.

### B.4. 연성 알루미늄에서 구배 조건이 이미 만족되는 이유

Kwon et al. (2024)의 §3은 개뼈다귀 시험에서 얻은 응력–변형률 곡선을 넣어 탄소성 FE를 수행했다. 소성영역에서 접선계수 $E_t=d\sigma/d\varepsilon$는 탄성계수보다 훨씬 작다. 구멍 가장자리에서 추가 변형이 크게 늘어도 응력 증가는 작으므로 응력 꼭대기가 재분배되고 공간 분포가 평탄해진다. 즉 $|d\sigma_e/ds|$가 탄성 취성 해석보다 적어도 한 자릿수 작아졌다고 논문은 보고한다.

식 (2)의 구배 문턱을

$$
\sigma_{\mathrm{grad}}(x)
=\left(2E\Upsilon|d\sigma_e/ds|(x)\right)^{1/3}
$$

라 쓰면, 구배가 작아질수록 이 요구 응력도 작아진다. 동등하게 여유함수를

$$
M_g(x)=\frac{\sigma_e^3}{2E|d\sigma_e/ds|}
$$

라 쓰면 구배가 작아질수록 $M_g$가 커져 $\Upsilon$을 쉽게 넘는다. 따라서 이 사례에서는 구배 조건이 먼저 충족되고, 최종 파괴하중은 $\sigma_e\geq\sigma_f$가 결정한다. “연성이므로 언제나 그렇다”는 일반법칙이 아니라, 해당 낮은 접선계수와 형상에서 FE로 확인된 결과이다.

### B.5. PLA의 구멍에서 떨어진 파괴: 두 조건의 공간 교차

최소단면을 따라 구멍 가장자리에서의 거리를 $s$라 하자. PLA 해석에는 세 곡선이 있다.

1. 재료 강도 $\sigma_f$: 위치에 무관한 수평선,
2. 구배 요구응력 $\sigma_{\mathrm{grad}}(s)=[2E\Upsilon|d\sigma_e/ds|]^{1/3}$: 위치별 구배 때문에 변하는 곡선,
3. 주어진 하중의 실제 등가응력 $\sigma_e(s)$: 구멍 부근에서 크고 멀어질수록 변하는 곡선.

작은 3 mm 구멍의 가장자리에서는 $\sigma_e$가 크더라도 구배가 너무 가파르므로 $\sigma_e<\sigma_{\mathrm{grad}}$여서 구배 조건이 실패한다. 더 멀리 가면 구배 조건은 쉬워지지만 실제 응력도 감소하여, 어느 지점 이후에는 $\sigma_e<\sigma_f$가 된다. 따라서 그 사이에서 두 조건을 동시에 막 충족하는 교차점이 최초 파괴위치가 된다. 이것이 가장자리가 아닌 떨어진 곳에서 파괴가 시작되는 이유다.

4 mm 구멍에서는 가장자리와 떨어진 지점이 거의 같은 하중에 후보가 되어 두 잠재 위치가 나타났고, 6 mm 구멍에서는 가장자리가 최초 위치가 되었다. 즉 “최대응력점 찾기”가 아니라 하중을 증가시키며 $\sigma_e(s)$가 $\max[\sigma_f,\sigma_{\mathrm{grad}}(s)]$에 최초로 닿는 위치와 하중을 찾는 문제다.

---

## C. 모델링을 해서 무엇을 구해야 하는가

### C.1. 일반적인 FE 출력과 판정 알고리즘

FE 모델이 최종적으로 제공해야 할 핵심은 후보 파괴 경로 $s$를 따른

$$
\boxed{\sigma_e(s;P)}
\qquad\text{및}\qquad
\boxed{\frac{d\sigma_e(s;P)}{ds}}
$$

이다. 여기서 $P$는 하중 또는 변위 하중계수이다. 취성 등방재라면 보통 최대주응력과 그 최대주축에 수직인 경로를 쓰고, 연성재나 비등방재·복합재에는 그 재료의 파괴모드에 맞는 등가응력을 써야 한다.

실무 판정은 다음과 같이 쓸 수 있다.

$$
F_1(s,P)=\frac{\sigma_e(s;P)}{\sigma_f},
\qquad
F_2(s,P)=\frac{\sigma_e(s;P)^3}
{2E\Upsilon|d\sigma_e(s;P)/ds|}.
$$

찾아야 할 파괴하중과 위치는

$$
P_c=\inf\left\{P:\exists s\ \text{such that}\ F_1(s,P)\geq1
\ \text{and}\ F_2(s,P)\geq1\right\},
$$

$$
s_c=\operatorname*{arg\,first}_{s}
\left[F_1(s,P_c)\geq1\ \land\ F_2(s,P_c)\geq1\right].
$$

즉 목표는 (i) 응력장, (ii) 그 공간구배, (iii) 두 조건을 동시에 만족시키는 최소 하중, (iv) 그 최초 위치다. 수치미분은 메시와 응력 외삽에 민감하므로 경로 방향, 절점/적분점 값의 처리, 메시수렴성을 함께 확인해야 한다.

### C.2. 시멘트 페이스트 균열 시험편: 캘리브레이션–예측 절차

논문 3 §4.2–4.3의 절차는 다음과 같다.

1. 폭 방향 관통균열을 가진 3점굽힘 시험편 절반을 3D 솔리드 요소로 먼저 모델링한다. 논문은 약 0.3 mm 균일 요소, 지지·대칭 경계조건 및 폭 방향 하중을 사용했다.
2. 선형탄성 해석 뒤 폭을 따라 균열선 응력분포가 거의 같음을 확인해 2D 4절점 사각요소 모델로 단순화했다. 최종 2D 메시는 메시 민감도 검토 후 약 10,000개 요소였다.
3. 통상 FE의 균열끝 바로 근처 응력은 특이성과 메시 의존성 때문에 점값 자체를 신뢰하지 않는다. 대신 $K$-지배 구간의 여러 FE 응력값을

   $$
   \sigma_e(s)=\frac{K}{\sqrt{s}}
   $$

   에 곡선맞춤하여 주어진 기준 하중 $P_0$에 대한 진폭 $K_0$를 역산한다. **이 사례에서 모델링으로 직접 구해야 하는 핵심량은 이 $K$다.** 맞춤 구간은 균열끝 요소의 오염영역은 피하면서 고차항·경계영향이 작아야 한다. 논문은 곡선맞춤을 사용했다고 명시하지만 구간선정 오차나 회귀 통계는 제시하지 않는다.
4. 기준 시편($a/H=0.1$, $H=100\,\mathrm{mm}$)의 실험 파괴하중 $P_f^{\mathrm{ref}}$를 사용한다. 선형탄성 범위에서 $K\propto P$이므로

   $$
   K_f^{\mathrm{ref}}=K_0^{\mathrm{ref}}
   \frac{P_f^{\mathrm{ref}}}{P_0}.
   $$

5. 그 재료의 미지 파괴값을

   $$
   \boxed{\Upsilon=\frac{(K_f^{\mathrm{ref}})^2}{E}}
   $$

   로 한 번 역산한다. 이 기준 시편은 보정에 사용되었으므로 예측값과 실험값이 일치하는 것은 독립 검증이 아니라 캘리브레이션의 당연한 결과다.
6. 다른 $a/H$와 높이 $H$의 시편 각각에 대해 같은 방식으로 기준 하중의 $K_{0,j}$를 구하되, $\Upsilon$은 다시 맞추지 않는다. 임계 진폭은

   $$
   K_c=\sqrt{E\Upsilon}
   $$

   이므로 선형 비례를 이용해

   $$
   \boxed{P_{c,j}=P_{0,j}\frac{\sqrt{E\Upsilon}}{K_{0,j}}}
   $$

   로 파괴하중을 예측한다.
7. 예측하중을 나머지 실험과 비교한다. 논문은 $a/H=0.3$, $H=100\,\mathrm{mm}$ 한 경우를 제외하고 근접한 일치를 보고했으며, 그 예외의 원인은 추가 정보가 없어 확인하지 못했다고 명시한다.

균열끝에서는 $\sigma\to\infty$이므로 응력 조건은 이미 만족한다고 보고 구배/$K$ 조건이 지배한다. 이는 “FE 특이응력의 최댓값”을 구하는 작업이 아니라, 해상 가능한 근접장 전체에서 특이장 **진폭**을 식별하는 작업이다. 단위셀 식 (5)–(9)의 닫힌형 유도와는 별개의 절차다.

### C.3. PLA와 복합재에 같은 일반론을 적용하는 방법

PLA에서는 1/4 2D 모델에 변위를 증분 적용하고, 최소단면의 각 위치에서 최대법선 등가응력, 그 경로방향 구배, $\sigma_f$, $\sigma_{\mathrm{grad}}(s)$를 비교한다. 하중을 올려 두 조건을 최초로 동시에 만족하는 위치가 3, 4, 6 mm 구멍에 따라 가장자리 밖·복수 후보·가장자리로 바뀐다.

적층 유리섬유 복합재에서는 거시 FE 변형률/응력을 식 (5)–(7)의 상·하향화로 섬유와 기지 수준에 내린 뒤, 섬유 식 (8), 기지 최대법선응력, 계면 식 (9) 등 모드별 등가량과 각각의 구배를 검사한다. 하중 증분 중 최초로 두 조건을 만족하는 구성재·층·위치·모드를 찾는다. 논문 사례에서는 0°층 구멍 가장자리의 섬유파단이 주 파괴 개시였고, 6 mm 시편에서 보정한 섬유 $\Upsilon$을 3 mm와 9 mm에 재사용했다. 이 역시 “한 시편 보정, 다른 형상 예측” 구조다.

---

## D. $K$가 의미하는 것

### D.1. 고전 파괴역학의 $K$

등방 선형탄성체의 균열끝 근접장은 일반적으로

$$
\sigma_{ij}(r,\theta)=
\frac{K_I}{\sqrt{2\pi r}}f_{ij}^{(I)}(\theta)
+\frac{K_{II}}{\sqrt{2\pi r}}f_{ij}^{(II)}(\theta)
+\frac{K_{III}}{\sqrt{2\pi r}}f_{ij}^{(III)}(\theta)
+O(r^0)
$$

로 쓴다. $K$는 $1/\sqrt r$ 특이장의 **진폭**이다. 재료점의 응력 자체가 아니라 하중, 균열 길이, 시험편 형상 및 하중모드를 한 값에 압축한 장 매개변수이다. 차원은

$$
[K]=[\sigma]\sqrt{[r]}=\mathrm{Pa}\sqrt{\mathrm m},
$$

공학 단위로 $\mathrm{MPa}\sqrt{\mathrm m}$이다. 모드 I의 임계값 $K_{IC}$는 유효한 평면변형률 시험 조건에서의 파괴인성이다.

Irwin 관계는

$$
G=\frac{K_I^2}{E'}
$$

이며, 혼합모드에서는 각 모드의 기여와 재료/평면상태에 맞는 관계를 써야 한다. $K$는 국소 응력장의 세기를, $G$는 균열면적 증가당 방출되는 잠재에너지를 나타내지만 LEFM 안에서는 서로 일대일 대응한다.

### D.2. 두 논문에서 확장된 $K$

논문 1의 식 (4)는 표준적인 $1/\sqrt{2\pi r}$ 형태다. 논문 3은

$$
\sigma_e=\frac{K}{\sqrt s}
$$

로 $2\pi$를 계수 $K$에 흡수한 형태를 쓴다. 그러므로 두 논문의 기호가 같다고 수치까지 같은 $K$로 취급하면 안 된다.

시멘트 페이스트 사례에서 논문 3은 FE 응력분포를 위 함수에 맞춰 $K$를 회귀한다. 그 시험편에는 실제 날카로운 균열이 있으므로 이는 근접장 진폭을 수치적으로 식별하는 절차다. 보다 일반적으로 같은 형태를 노치의 국소장에 맞춘다면 그 값은 표준 균열해의 엄밀한 SIF라기보다 **그 선택 구간에서의 등가 근접장 진폭**이다. 이때 $K$는

- 응력이 얼마나 큰지(진폭),
- 거리와 함께 얼마나 감소하는지($1/\sqrt s$ 형상과 결합)

를 하나의 계수로 요약한다. 그러나 원공의 실제 Kirsch 장은 일반적으로 정확한 $s^{-1/2}$ 특이장이 아니므로, 임의의 유한 노치에 맞춘 등가 $K$는 맞춤 구간 의존성을 가질 수 있다. 논문 3의 PLA·원공 분석은 실제로는 위치별 $\sigma_e$와 구배를 직접 비교하며, 모든 비균열 문제를 반드시 $K$ 하나로 환원한 것은 아니다.

### D.3. 왜 균열 근접장에서는 $K$로 두 조건을 평가할 수 있는가

$\sigma_e=K/\sqrt s$이면

$$
\sigma_e(s)=Ks^{-1/2},\qquad
\left|\frac{d\sigma_e}{ds}\right|=\frac K2s^{-3/2}.
$$

따라서 응력 조건은

$$
\frac{K}{\sqrt s}\geq\sigma_f
\quad\Longleftrightarrow\quad
s\leq\left(\frac K{\sigma_f}\right)^2,
$$

구배 조건은

$$
\Upsilon\leq\frac{\sigma_e^3}{2E|d\sigma_e/ds|}
=\frac{K^2}{E}
\quad\Longleftrightarrow\quad
K\geq\sqrt{E\Upsilon}.
$$

즉 $K$와 좌표 $s$, 그리고 재료상수 $E,\sigma_f,\Upsilon$가 주어지면 두 조건을 모두 계산할 수 있다. 특히 $s\to0$인 이상 균열끝에서는 첫 조건이 자동 충족되고 $K\geq K_c$라는 둘째 조건만이 유한한 임계하중을 정한다. “$K$ 하나만 알면 된다”는 말은 이 근접장 형상과 재료상수가 이미 정해졌다는 전제에서 맞으며, 임의의 비특이 응력장이나 파괴위치까지 $K$만으로 항상 결정된다는 뜻은 아니다.

---

## 결론 요약

이 통합기준의 핵심은 강도 문턱과 응력분포의 공간적 폭을 동시에 요구하는 데 있다. $\sigma^3/(2E|d\sigma/ds|)$는 탄성에너지 밀도와 특성 감쇠 길이의 곱이고, $r^{-1/2}$ 균열장에서는 거리 의존성이 정확히 소거되어 $K^2/E$형 균열구동력으로 환원된다. 비특이 구멍 문제에서는 같은 국소량을 직접 계산해 두 조건의 최초 공간 교차를 찾는다. FE의 최종 목적은 단순 최대응력이 아니라 $\sigma_e(s)$, $d\sigma_e/ds$, 최초 동시충족 하중과 위치이며, 균열 시험편에서는 특이 점응력 대신 곡선맞춤한 $K$를 구해 한 기준 시편의 $\Upsilon$을 보정한 뒤 다른 형상에 재사용하는 것이다.

단, 논문식의 $w_f,\Upsilon$을 표준 $G_c$와 숫자까지 동일시해서는 안 된다. 표준 $K_I/\sqrt{2\pi r}$ 및 $E'$ 정의를 적용하면 논문식과 $G$ 사이에 $2\pi$ 및 평면상태 정규화가 남는다. 물리적으로는 일대일 대응하지만, 수치 등식은 정의를 맞춘 뒤에만 성립한다.

## 확인한 출처

1. Kwon, Y. W., “Revisiting Failure of Brittle Materials,” *Journal of Pressure Vessel Technology*, 143(6), 064503 (2021), DOI: [10.1115/1.4050989](https://doi.org/10.1115/1.4050989).
2. Kwon, Y. W., Markoff, E. K., and DeFisher, S., “Unified Failure Criterion Based on Stress and Stress Gradient Conditions,” *Materials*, 17(3), 569 (2024), DOI: [10.3390/ma17030569](https://doi.org/10.3390/ma17030569). 식 (1)–(9), 알루미늄 §3, 시멘트 페이스트 §4, PLA §5, 복합재 §6의 절차와 결과를 본문에서 직접 확인했다.
3. Irwin, G. R., “Analysis of Stresses and Strains Near the End of a Crack Traversing a Plate,” *Journal of Applied Mechanics*, 24, 361–364 (1957). 균열끝 특이장과 에너지 해방률–응력확대계수 대응의 원전.
4. Griffith, A. A., “The Phenomena of Rupture and Flow in Solids,” *Philosophical Transactions of the Royal Society A*, 221, 163–198 (1921). 균열성장의 에너지 균형 원전.
5. Anderson, T. L., *Fracture Mechanics: Fundamentals and Applications*, 4th ed., CRC Press (2017). 표준 LEFM의 $K$, $G$, $E'$ 관계 및 평면응력/평면변형률 구분을 대조하는 데 사용했다.
6. ASTM International, *ASTM E399, Standard Test Method for Linear-Elastic Plane-Strain Fracture Toughness of Metallic Materials*. $K_{Ic}$의 평면변형률 파괴인성 의미와 단위 확인에 사용했다.

