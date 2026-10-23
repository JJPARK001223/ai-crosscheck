# round60 Codex 독립 전사

## 범위와 확인 방법

- 원문: `round60/input/c202.pdf`(318 PDF쪽). `round60/PROBLEM.md`와 원문 PDF만 사용했다. 다른 AI 결과 및 지정된 XLPR HTML은 읽지 않았다.
- 요청된 수식 27개 PDF쪽과 표가 있는 PDF 32~36쪽을 Poppler `pdftoppm -r 200 -png`로 렌더링하여 각 페이지 이미지를 직접 확인했다. PDF 100쪽도 추가 렌더링하여 본문 식 참조임을 확인했다.
- 전체 318쪽을 `pdftotext -layout`으로 추출하여 대괄호 식 번호를 검색하고, 본문 참조와 실제 독립 표시식을 구분했다.
- **추가 번호식 없음. 번호식 총 59개**: 1장 20개, 4장 1개, 5장 4개, 6장 22개, 7장 1개, 8장 4개, 부록 C 7개. 하나의 번호에 여러 줄이 있는 경우 하나로 센다. PDF 100쪽의 [6-7], [6-8]은 본문 참조이며 실제 식은 PDF 101쪽에 있다.
- 아래 위치 표기는 `[인쇄쪽/PDF쪽, 식 번호]`이다. 괄호·첨자·분포 표기를 교정하지 않았다. 수학적 타당성에 대한 판단은 전사와 구분한다. 판독 불명확 항목은 별도로 `확인 불가`라고 표시한다.

## 번호식 전사

### 1장

[1-5/22, 식 1-1]
$$t=\Lambda(\boldsymbol{\theta})\cdot g(T,\sigma,\ldots;Q,n,\ldots)$$

[1-6/23, 식 1-2]
$$t=\Lambda_{cc}(\boldsymbol{\theta}_{cc})\Lambda_{wc}(\boldsymbol{\theta}_{wc})\cdot g(T,\sigma,\ldots;Q,n,\ldots)$$

[1-8/25, 식 1-3]
$$\begin{aligned}
t&=\Lambda_{cc}\cdot\Lambda_{wc}\cdot g(T,\sigma;Q,n)\\
g&=e^{Q/(R_{gas}T)}\sigma^{-n}
\end{aligned}$$

[1-9/26, 식 1-4]
$$\begin{aligned}\Lambda_{cc}&=\frac{1}{A_{cc}}\\A_{cc}&\sim\text{log-N}(0,\sigma_{A,cc})\end{aligned}$$

[1-9/26, 식 1-5]
$$\begin{aligned}\Lambda_{wc}&=\frac{1}{A_{wc}}\\A_{wc}&\sim\text{log-N}(\mu_{A,wc},\sigma_{A,wc})\end{aligned}$$

[1-9/26, 식 1-6]
$$\begin{aligned}
t&=\Lambda_{cc}\cdot\Lambda_{wc}\cdot g(T,\sigma,\sigma_{ys},\sigma_{ult},E;Q,z_1,z_2,v,w,q,a_{dm2},b_{dm2},c_{dm2},k_{dm2})\\
g&=Ge^{Q/R_{gas}T}\ln\left[\frac{D-z}{\dfrac{\sigma}{\sigma_{ys}}-z}\right]
\end{aligned}$$
원문 그대로: 지수는 [1-3]의 `Q/(R_gas T)`와 달리 슬래시 뒤 분모 괄호 없이 `Q/R_gas T`로 인쇄되어 있다.

[1-9/26, 식 1-7]
$$G=m^{-q}\frac{\ln(D)}{\ln\left(\dfrac{D-z}{1-z}\right)}$$

[1-9/26, 식 1-8]
$$z=z_1+z_2\ln(\zeta)$$

[1-9/26, 식 1-9]
$$D=v\cdot e^{w\cdot\zeta}$$

[1-9/26, 식 1-10]
$$m=k_{dm2}\left(\frac{\sigma_{ys}}{E}\right)^{a_{dm2}}(\zeta-1)^{b_{dm2}}(\zeta)^{c_{dm2}}$$

[1-9/26, 식 1-11]
$$\zeta=\frac{\sigma_{ult}}{\sigma_{ys}}$$

[1-10/27, 식 1-12]
$$\begin{aligned}\Lambda_{cc}&=B_{cc}\\B_{cc}&\sim\text{log-N}(0,\sigma_{B,cc})\end{aligned}$$

[1-10/27, 식 1-13]
$$\begin{aligned}\Lambda_{wc}&=B_{wc}\\B_{wc}&\sim\text{log-N}(\mu_{B,wc},\sigma_{B,wc})\end{aligned}$$

[1-10/27, 식 1-14]
$$\sigma_{th}=z\sigma_{ys}$$

[1-11/28, 식 1-15]
$$\sigma_{max}=D\sigma_{ys}$$

[1-11/28, 식 1-16]
$$\begin{aligned}
t&=\Lambda\cdot g(T,\sigma;Q,n,T_{ref},\sigma_{ref})\\
g&=\exp\left[\frac{Q}{R_{gas}}\left(\frac{1}{T}-\frac{1}{T_{ref}}\right)\right]\left(\frac{\sigma}{\sigma_{ref}}\right)^{-n}
\end{aligned}$$

[1-11/28, 식 1-17]
$$\begin{aligned}\Lambda&\sim W(\beta,c)\\F_{\Lambda}(t;\beta,c)&=1-\exp\left[-t^\beta\exp(c)\right]\end{aligned}$$

[1-12/29, 식 1-18]
$$\theta=\exp[-c/\beta]$$

[1-12/29, 식 1-19]
$$\begin{aligned}
t&=\Lambda_{cc}\cdot g(T,\sigma,N;Q,n,T_{ref},\sigma_{ref})\\
g&=\exp\left[\frac{Q}{R_{gas}}\left(\frac{1}{T}-\frac{1}{T_{ref}}\right)\right]\left(\frac{\sigma}{\sigma_{ref}}\right)^{-n}N^{1/\beta_{cc}}\\
\Lambda_{cc}&\sim W(\beta_{cc},c_{cc})\\
F_{\Lambda_{cc}}(t;\beta_{cc},c_{cc})&=1-\exp\left[-t^{\beta_{cc}}\exp(c_{cc})\right]
\end{aligned}$$

[1-12/29, 식 1-20]
$$g_{Zn}=\begin{cases}1&C_{Zn}\le C_{Zn,th}\\FOI&C_{Zn}>C_{Zn,th}\end{cases}$$

### 4장과 5장

[4-13/75, 식 4-1]
$$\sigma_{true}=102\exp\left[0.0035\cdot\sigma_{eng}\right]$$

[5-9/86, 식 5-1]
$$\sigma_{th}=z\sigma_{ys}$$

[5-10/87, 식 5-2]
$$z=z_1+z_2\ln(\zeta)$$

[5-10/87, 식 5-3]
$$\zeta=\frac{\sigma_{ult}}{\sigma_{ys}}$$

[5-11/88, 식 5-4]
$$\sigma_{th,i}=\left(\frac{60\ \mathrm{EFPY}}{t_i}\right)^{-\frac{1}{n}}\sigma_i$$

### 6장

[6-3/97, 식 6-1]
$$F_{\Lambda}(t)=P(\Lambda\le t)$$

[6-3/97, 식 6-2]
$$f_{\Lambda}(t)=\frac{d}{dt}F_{\Lambda}(t)$$

[6-3/97, 식 6-3]
$$\lambda_{\Lambda}(t)=\frac{f_{\Lambda}(t)}{1-F_{\Lambda}(t)}$$

[6-3/97, 식 6-4]
$$S_{\Lambda}(t)=1-P(\Lambda\le t)=P(\Lambda>t)$$

[6-5/99, 식 6-5]
$$\begin{aligned}
\lambda_i&=\frac{t_i}{g(T_i,\sigma_i,\ldots;Q,n,\ldots)}\quad i\in R\\
\nu_i&=\frac{s_i}{g(T_i,\sigma_i,\ldots;Q,n,\ldots)}\quad i\in P
\end{aligned}$$

[6-5/99, 식 6-6]
$$\begin{aligned}
\lambda_i&=\int_{\tau=0}^{t_i}\frac{1}{g(T_i(\tau),\sigma_i(\tau),\ldots;Q,n,\ldots)}\,d\tau\\
\nu_i&=\int_{\tau=0}^{s_i}\frac{1}{g(T_i(\tau),\sigma_i(\tau),\ldots;Q,n,\ldots)}\,d\tau
\end{aligned}$$
원문 그대로: 이 쪽 본문은 위쪽의 정규화를 설명하면서 “Eq. [6-6]”이라고 참조한다. 식 번호 자체는 위가 [6-5], 아래가 [6-6]이다.

[6-7/101, 식 6-7]
$$\begin{aligned}
f_{\Lambda}(t;\boldsymbol{\theta})&=f_{\Lambda}(t;\mu_A,\sigma_A)=\frac{1}{t\sigma_A\sqrt{2\pi}}e^{-\frac{(\ln t+\mu_A)^2}{2\sigma_A^2}}\\
S_{\Lambda}(t;\boldsymbol{\theta})&=S_{\Lambda}(t;\mu_A,\sigma_A)=\frac12-\frac12\operatorname{erf}\left[\frac{\ln t+\mu_A}{\sqrt{2}\sigma_A}\right]
\end{aligned}$$

[6-7/101, 식 6-8]
$$\begin{aligned}
f_{\Lambda}(t;\boldsymbol{\theta})&=f_{\Lambda}(t;\mu_B,\sigma_B)=\frac{1}{t\sigma_B\sqrt{2\pi}}e^{-\frac{(\ln t-\mu_B)^2}{2\sigma_B^2}}\\
S_{\Lambda}(t;\boldsymbol{\theta})&=S_{\Lambda}(t;\mu_B,\sigma_B)=\frac12-\frac12\operatorname{erf}\left[\frac{\ln t-\mu_B}{\sqrt{2}\sigma_B}\right]
\end{aligned}$$

[6-7/101, 식 6-9]
$$\begin{aligned}
f_{\Lambda}(t;\boldsymbol{\theta})&=f_{\Lambda}(t;\beta,c)=\beta t^{\beta-1}e^{c-e^ct^\beta}\\
S_{\Lambda}(t;\boldsymbol{\theta})&=S_{\Lambda}(t;\beta,c)=\exp\left[-t^\beta\exp(c)\right]
\end{aligned}$$

[6-7/101, 식 6-10]
$$\mathrm{L}(\boldsymbol{\theta}\mid\lambda_i,\nu_i)=\prod_{i\in P}S_{\Lambda}(\nu_i;\boldsymbol{\theta})\cdot\prod_{i\in R}f_{\Lambda}(\lambda_i;\boldsymbol{\theta})$$

[6-7/101, 식 6-11]
$$\hat{\boldsymbol{\theta}}=\underset{\boldsymbol{\theta}}{\arg\max}\left(\mathrm{L}(\boldsymbol{\theta}\mid\lambda_i,\nu_i)\right)$$

[6-8/102, 식 6-12]
$$\begin{aligned}
\hat{\boldsymbol{\theta}}&=\underset{\boldsymbol{\theta}}{\arg\max}\left(\log\mathrm{L}(\boldsymbol{\theta}\mid\lambda_i,\nu_i)\right)\\
\log\mathrm{L}(\boldsymbol{\theta}\mid\lambda_i,\nu_i)&=\sum_{i\in P}\log\left(S_{\Lambda}(\nu_i;\boldsymbol{\theta})\right)+\sum_{i\in R}\log\left(f_{\Lambda}(\lambda_i;\boldsymbol{\theta})\right)
\end{aligned}$$

[6-8/102, 식 6-13]
$$\begin{aligned}
\mathbf{cov}_{\boldsymbol{\theta}}&=I^{-1}(\hat{\boldsymbol{\theta}})\\
I(\boldsymbol{\theta})&=\left(\frac{-\delta^2\log\mathrm{L}(\boldsymbol{\theta}\mid\lambda_i,\nu_i)}{\delta\theta_i\ \delta\theta_j}\right)
\end{aligned}$$
원문 그대로: 미분 표시는 `\partial`로 교정하지 않고 인쇄된 `\delta`를 옮겼다.

[6-8/102, 식 6-14]
$$\boldsymbol{\theta}\sim\mathrm{N}\left(\hat{\boldsymbol{\theta}},\mathbf{cov}_{\boldsymbol{\theta}}\right)$$

[6-9/103, 식 6-15]
$$\mathrm{L}(\boldsymbol{\theta}\mid\lambda_i,\nu_i)=\prod_{i\in P}S_{\Lambda}(\nu_i;\boldsymbol{\theta})\cdot\prod_{i\in R}\left(S_{\Lambda}(\lambda_{i(-1)};\boldsymbol{\theta})-S_{\Lambda}(\lambda_i;\boldsymbol{\theta})\right)$$

[6-9/103, 식 6-16]
$$\mathrm{L}(\boldsymbol{\theta}\mid\lambda_i,\nu_i)=\prod_{i\in P}\left(S(\nu_i;\boldsymbol{\theta})+p\left(1-S(\nu_i;\boldsymbol{\theta})\right)\right)\cdot\prod_{i\in R}(1-p)\left(S(\lambda_{i(-1)};\boldsymbol{\theta})-S(\lambda_i;\boldsymbol{\theta})\right)$$
원문 그대로: [6-15]의 `S_\Lambda`와 달리 이 식에서는 `S`에 Λ 첨자가 없다.

[6-10/104, 식 6-17]
$$\begin{aligned}
&\mathrm{L}(\boldsymbol{\theta}_N,N\mid\lambda_{i,j},\nu_{i,j})=\\
&\prod_{i,j\in P(N)}\left(S_{\Lambda}(\nu_{i,j};\boldsymbol{\theta}_N)+p\left(1-S_{\Lambda}(\nu_{i,j};\boldsymbol{\theta}_N)\right)\right)\cdot\prod_{i,j\in R(N)}(1-p)\left(S_{\Lambda}(\lambda_{i(-1),j};\boldsymbol{\theta}_N)-S_{\Lambda}(\lambda_{i,j};\boldsymbol{\theta}_N)\right)
\end{aligned}$$
원문 그대로: 바로 앞 본문의 참조는 “Eq. [6-17]”이다.

[6-11/105, 식 6-18]
$$\begin{aligned}
t&=\Lambda\cdot g(T,\sigma,\ldots;Q,n,\ldots)\\
\Lambda&=\Lambda_{cc}\cdot\Lambda_{wc}\\
\Lambda_{cc}&\sim\text{log-N}(0,\sigma_{cc})\\
\Lambda_{wc}&\sim\text{log-N}(\mu_{wc},\sigma_{wc})
\end{aligned}$$

[6-12/106, 식 6-19]
$$\begin{aligned}\Lambda&\sim\text{log-N}(\mu_{total},\sigma_{total})\\\mu_{total}&=\mu_{wc}\\\sigma_{total}&=\sqrt{\sigma_{cc}^2+\sigma_{wc}^2}\end{aligned}$$

[6-12/106, 식 6-20]
$$\begin{aligned}\ln(\lambda)&=\Lambda'\\\Lambda'&=\Lambda'_{cc}+\Lambda'_{wc}\\\Lambda'_{cc}&\sim\mathrm{N}(0,\sigma_{cc})\\\Lambda'_{wc}&\sim\mathrm{N}(\mu_{wc},\sigma_{wc})\end{aligned}$$

[6-12/106, 식 6-21]
$$\begin{aligned}\Lambda'&\sim\mathrm{N}(\mu_{total},\sigma_{total})\\\mu_{total}&=\mu_{wc}\\\sigma_{total}&=\sqrt{\sigma_{cc}^2+\sigma_{wc}^2}\end{aligned}$$

[6-13/107, 식 6-22]
$$\sigma_{wc}=\sqrt{\sigma_{total}^2-\sigma_{cc}^2}=\sqrt{\sigma_{N=n}^2-\sigma_{cc}^2}$$

### 7장과 8장

[7-10/120, 식 7-1]
$$\frac{da}{dt}=\alpha_g\exp\left[-\frac{Q_g}{R_{gas}}\left(\frac{1}{T}-\frac{1}{T_{ref,g}}\right)\right]K^{\beta_g}$$

[8-25/169, 식 8-1]
$$\hat{S}_{\Lambda}(t)=\prod_{t_i<t}\frac{l_i-d_i}{l_i}$$

[8-30/174, 식 8-2]
$$D_{KS}=\sqrt{n_{data}}\left(\sup\left|\hat{S}_{\Lambda}(t)-S_{\Lambda}(t)\right|\right)$$

[8-32/176, 식 8-3]
$$y_{\Lambda}(t)=\ln\left(-\ln\left(1-F_{\Lambda}(t)\right)\right)$$

[8-35/179, 식 8-4]
$$y(t)=\Phi^{-1}\left(F_{\Lambda}(t)\right)$$
같은 쪽 where: $\Phi^{-1}=\text{inverse standard normal cumulative distribution function}$.

### 부록 C

[C-1/317, 식 C-1]
$$\mathrm{L}(\boldsymbol{\theta}\mid\lambda_i,\nu_i)=\prod_{i\in P}S_{\Lambda}(\nu_i;\boldsymbol{\theta})\cdot\prod_{i\in R}\left(S_{\Lambda}(\lambda_{i(-1)};\boldsymbol{\theta})-S_{\Lambda}(\lambda_i;\boldsymbol{\theta})\right)$$

[C-1/317, 식 C-2]
$$f(x_i\mid\boldsymbol{\theta})=S_{\Lambda}(\nu_i;\boldsymbol{\theta})^{1-x_i}\left(S_{\Lambda}(\lambda_{i(-1)};\boldsymbol{\theta})-S_{\Lambda}(\lambda_i;\boldsymbol{\theta})\right)^{x_i}$$

[C-1/317, 식 C-3]
$$f(y_i\mid\boldsymbol{\theta})=\int p(y_i\mid x_i)f(x_i\mid\boldsymbol{\theta})\,dx$$
원문 그대로: 적분 미분항은 `dx`이며 `dx_i`로 고치지 않았다.

[C-1/317, 식 C-4]
$$f(y_i\mid\boldsymbol{\theta})=\sum_{j=0,1}p(y_i\mid x_i=j)\,f(x_i=j\mid\boldsymbol{\theta})$$

[C-2/318, 식 C-5]
$$\begin{aligned}
p(y_i=1\mid x_i=1)&=1-p\\
p(y_i=0\mid x_i=1)&=p\\
p(y_i=1\mid x_i=0)&=0\\
p(y_i=0\mid x_i=0)&=1
\end{aligned}$$

[C-2/318, 식 C-6]
$$f(y_i\mid\boldsymbol{\theta})=\left(S_{\Lambda}(\nu_i;\boldsymbol{\theta})+p\left(1-S_{\Lambda}(\nu_i;\boldsymbol{\theta})\right)\right)^{1-y_i}\left((1-p)\left(S_{\Lambda}(\lambda_{i(-1)};\boldsymbol{\theta})-S_{\Lambda}(\lambda_i;\boldsymbol{\theta})\right)\right)^{y_i}$$

[C-2/318, 식 C-7]
$$\mathrm{L}(\boldsymbol{\theta}\mid\lambda_i,\nu_i)=\prod_{i\in P}\left(S(\nu_i;\boldsymbol{\theta})+p\left(1-S(\nu_i;\boldsymbol{\theta})\right)\right)\cdot\prod_{i\in R}(1-p)\left(S(\lambda_{i(-1)};\boldsymbol{\theta})-S(\lambda_i;\boldsymbol{\theta})\right)$$
원문 그대로: [C-6]의 `S_\Lambda`와 달리 [C-7]에는 Λ 첨자가 없다. [C-7] 직전 문장은 “Then, by definition, the new likelihood Equation_ is as follows:”로, `Equation` 다음 번호 없이 밑줄 하나가 인쇄되어 있다. 번호를 보충하지 않았다.

## 표 전사

마크다운 표는 병합 셀을 지원하지 않으므로, 세로 병합은 첫 행에만 내용을 적고 이어지는 칸은 비웠다. 아래에 병합 범위를 명시한다. 이 빈칸을 수치 0 또는 누락값으로 해석하지 않는다. 원래 비어 있는 Heat 등은 그대로 비웠다. 페이지에 걸쳐 나뉜 표는 행 순서대로 연결했다.

### [1-10/27, Table 1-1] Direct Model 2 Cold Work Parameters

병합 상단 행(9열 전체): **Direct Model 2 Inputs for Ni-Based Alloys**

| $z_1$ | $z_2$ | $v$ | $w$ | $q$ | $a_{dm2}$ | $b_{dm2}$ | $c_{dm2}$ | $k_{dm2}$ |
|---|---|---|---|---|---|---|---|---|
| 0.350 | 0.333 | 0.66 | 0.5 | 0.375 | 0.25 | -0.75 | -0.25 | 8.2 |

원문 각주: For Alloy 82/182, the value of the coefficient k was modified from 10.0 in EPRI 1019032 13 to 8.2 in EPRI 1025121 14.

### [2-2~2-3/32~33, Table 2-1] Direct Model 1 Parameter Recommendations

| Description | Units | Characterization of Uncertainty | Distribution Parameters | Model Parameters |
|---|---|---|---|---|
| Number of subunits | - | deterministic | best-estimate | 19 |
| Thermal activation energy | kJ/mol | deterministic | best-estimate | 185.0 |
| Inverse proportionality constant, $A_{cc}$ (component-to-component) | - | distributed (epistemic) | type | Log-Normal |
| | | | log-norm μ | 0.00 |
| | | | log-norm σ | 2.89 |
| Inverse proportionality constant, $A_{wc}$ (within-component) | (1/EFPY)(1/MPa⁵) | distributed (aleatory) | type | Log-Normal |
| | | | log-norm μ | -4.40 |
| | | | log-norm σ | 3.66 |
| Stress threshold | MPa | deterministic | best-estimate | 0.0 ¹ |
| Stress exponent | - | deterministic | best-estimate | 5.0 |

병합: $A_{cc}$ 및 $A_{wc}$ 각각의 Description/Units/Characterization 세 칸은 type·μ·σ의 3행에 걸친다. 원문은 $A_{wc}$ Description을 PDF 32쪽 “Inverse proportionality”, PDF 33쪽 “constant, $A_{wc}$ (within-component)”로 나누어 인쇄한다. σ=3.66 행은 PDF 33쪽이다.

(1) The PWSCC initiation module of xLPR Version 2.0 does not allow the stress threshold input to be less than or equal to zero. Therefore, the Direct Model 1 stress threshold input to xLPR should be set to an arbitrarily small positive value to emulate this report’s recommendation of 0 MPa.

### [2-3/33, Table 2-2] Direct Model 2 Parameter Recommendations

| Description | Units | Characterization of Uncertainty | Distribution Parameters | Model Parameters |
|---|---|---|---|---|
| Number of subunits | - | deterministic | best-estimate | 19 |
| Thermal activation energy | kJ/mol | deterministic | best-estimate | 185.0 |
| Proportionality constant, $B_{cc}$ (component-to-component) | - | distributed (epistemic) | type | Log-Normal |
| | | | log-norm μ | 0.00 |
| | | | log-norm σ | 1.49 |
| Proportionality constant, $B_{wc}$ (within-component) | EFPY | distributed (aleatory) | type | Log-Normal |
| | | | log-norm μ | -28.43 |
| | | | log-norm σ | 1.91 |
| Cold work parameters | - | deterministic | best-estimate | see Table 1-1 |

병합: $B_{cc}$, $B_{wc}$ 각각의 앞 3열이 type·μ·σ의 3행에 걸친다.

### [2-4/34, Table 2-3] Weibull Model Parameter Recommendations

| Description | Units | Characterization of Uncertainty | Distribution Parameters | Model Parameters |
|---|---|---|---|---|
| Number of subunits | - | deterministic | best-estimate | 19 |
| Thermal activation energy | kJ/mol | deterministic | best-estimate | 185.0 |
| Pivot time¹˒² | EFPY | deterministic | best-estimate | 10.4 |
| Percent of components with crack at pivot time¹˒² | % | deterministic | best-estimate | 10.0 |
| Vertical intercept error | - | distributed (epistemic) | type | Normal |
| | | | mean | 0.00 |
| | | | st dev | 0.38 |
| Weibull slope | - | distributed (epistemic) | type | Normal |
| | | | mean | 0.45 |
| | | | st dev | 0.08 |
| Correlation between vertical intercept error and Weibull slope³ | - | deterministic | best-estimate | -0.800 |
| Stress exponent | - | deterministic | best-estimate | 5.0 |
| Reference temperature | K | deterministic | best-estimate | 588.7 |
| Reference stress | MPa | deterministic | best-estimate | 325.0 |

병합: Vertical intercept error, Weibull slope 각각의 앞 3열이 type·mean·st dev의 3행에 걸친다.

각주 [2-5/35]:

(1) The adjustment in Eq. [1-19] requires that $N$ is the number of independent samples taken (i.e., two times the number of subunits when both orientations are simulated). However, the implementation in xLPR uses the number of subunits, resulting in a factor of $2^{1/\beta}$ bias in the initiation time prediction. This bias has been corrected for in this table by subtracting ln(2) from the component-to-component vertical intercept estimated in Section 7.5 of this report.

(2) The pivot time and the percent of components with a crack at the pivot time are inputs to xLPR Version 2.0. These parameters may be interpreted as follows: given a best-estimate slope of 0.45 and a best-estimate vertical intercept of -3.30 (see Section 7.5.1 and footnote 1), the percent of components (10.0%) is expected to experience PWSCC by the pivot time (10.4 EFPY). They are directly related to the best-estimate vertical intercept (c) and slope (β) used throughout this report with a simple algebraic equation (e.g., Eq. [1-17]).

(3) Correlation expressed here and elsewhere in this report refers to Pearson’s correlation coefficient for two normal distributions.

### [2-5/35, Table 2-4] Zinc Effect Parameter Recommendations

| Description | Units | Characterization of Uncertainty | Distribution Parameters | Model Parameters |
|---|---|---|---|---|
| Zinc concentration threshold | ppb | deterministic | best-estimate | 3.0 |
| Zinc factor of improvement | - | distributed (epistemic) | type | Shifted Log-normal |
| | | | shift parameter | 1.0 |
| | | | log-norm μ | -0.29 |
| | | | log-norm σ | 0.93 |

병합: Zinc factor of improvement의 앞 3열은 type·shift parameter·μ·σ의 4행에 걸친다. 원문의 “Shifted”와 “Log-normal” 사이 줄바꿈을 한 셀 안 공백으로 표시했다.

### [2-6/36, Table 2-5] Initial Flaw Size Parameter Recommendations

| Description | Units | Characterization of Uncertainty | Distribution Parameters | Model Parameters |
|---|---|---|---|---|
| Initial crack depth¹ | mm | distributed (aleatory) | type | Log-normal |
| | | | lower truncation | 0.5 |
| | | | log-norm μ | -6.50 |
| | | | log-norm σ | 0.35 |
| Initial crack length¹ | mm | distributed (aleatory) | type | Log-normal |
| | | | log-norm μ | -5.34 |
| | | | log-norm σ | 0.80 |

병합: Initial crack depth의 앞 3열은 4행, Initial crack length의 앞 3열은 3행에 걸친다.

(1) Technical basis in xLPR-SRD-CI-SCC [19]

### [5-10~5-11/87~88, Table 5-2] Stress Threshold Estimates Based on Direct Model 2

| Reference | Alloy | Heat | $\sigma_{ys}$, MPa | $\sigma_{ult}$, MPa | $\sigma_{th}$, MPa |
|---|---|---|---|---|---|
| Jang, 2008 [112] | 82/182 | | 397 | 639 | 202 |
| Itoh, 1997 [77] | 132 | | 355 | 612 | 189 |
| | 82 | | 379 | 655 | 202 |
| Itatani, 2009 [99] | 182 | | 418 | 696 | 217 |
| | 82 | | 396 | 655 | 205 |
| Scott, 2005 [72] | 182 | SOUDENEL CG5 | 363 | 637 | 195 |
| Vaillant, 2005 [113] | 182 | D545 | 395 | 657 | 205 |
| Vaillant, 2006 [76] | 182 | D481 | 372 | 641 | 198 |
| | 82 | D347 | 396 | 610 | 196 |
| Couvant, 2013 [92] | 182 | D1054 | 386 | 627 | 198 |
| Calonne, 2010 [87] | 182 | Block A | 483 | 689 | 226 |
| | 182 | Block B | 461 | 677 | 220 |
| | 182 | Block C | 445 | 644 | 211 |
| | 182 | Block D | 435 | 638 | 208 |
| | | | | **AVG** | 205 |

병합: Reference 열의 Itoh 2행, Itatani 2행, Vaillant 2006 2행, Calonne 4행. Calonne의 Block D 및 AVG는 PDF 88쪽에 이어진다. AVG 행에는 원문에 표시된 AVG와 205만 옮겼다.

## 이상 표기·확인 범위 기록

- 위 식의 `S`/`S_\Lambda`, `\lambda`/`\Lambda`, $\theta$와 $\boldsymbol{\theta}$, `log-N`/`N` 및 표의 `Log-Normal`/`Log-normal` 대소문자는 원문 그대로다.
- [C-2/318]의 “Equation_” 번호 빈칸과 [6-5/99]의 본문 식 참조는 위에 원문 그대로 표시했다. 이를 추가 번호식으로 세지 않았다.
- [C-1/317] 본문은 “P and R are the set of failed and suspended items, respectively.”라고 인쇄되어 있다(원문 그대로). 전사식의 곱 인덱스를 이 문장에 맞추어 바꾸지 않았다.
- 본문에서 다른 식을 인용한 페이지는 추가 식으로 세지 않았다. 전체 검색에서 실제 번호식은 위 59개이며, 별도의 새 번호·번호식 페이지는 발견되지 않았다.
- 수식·표에서 판독 불명확하여 `확인 불가`로 남긴 셀이나 항은 없다. 이 진술은 수식의 물리·통계적 정확성 검증을 뜻하지 않는다.
