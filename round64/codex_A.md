# B046 수식 blind 전사 — 담당 A

범위: 인쇄 9~29쪽 / PDF 21~41쪽. 출처: `round64/input/b046.pdf`만 사용. 전 쪽을 Poppler로 210 dpi PNG로 렌더링하고 직접 확인했다. 텍스트 추출은 보조 대조용이다. 다른 AI의 결과와 XLPR 폴더의 HTML은 읽지 않았다.

전사 기준: 하나의 식 번호에 묶인 계수식은 같은 표시식 안에 전부 옮겼다. 공통 where 목록은 각 해당 식 아래 반복했다. where가 없는 식에는 그 사실만 표시했다. 원문 줄바꿈은 문장 단위로 이어 적었으며, 기호는 LaTeX로 표기했다. 본문에 삽입된 단순 비율·수치, 도형의 치수 표지, 그래프 범례 및 표의 열 제목은 독립 표시식으로 세지 않았다. 인쇄 10, 15~19쪽 / PDF 22, 27~31쪽에는 독립 표시식이 없다.

### [9/21, Eqn. 2-1]
$$2\le\frac{R_i}{t}\le20$$
where
- $a$ = crack depth, m
- $c$ = one-half of the crack length at the inside surface, m
- $R_i$ = inner radius of pipe, m
- $t$ = pipe wall thickness, m

### [9/21, Eqn. 2-2]
$$0\le\frac{a}{t}\le0.95$$
where
- $a$ = crack depth, m
- $c$ = one-half of the crack length at the inside surface, m
- $R_i$ = inner radius of pipe, m
- $t$ = pipe wall thickness, m

### [9/21, Eqn. 2-3]
$$0\le\frac{a}{c}\le1$$
where
- $a$ = crack depth, m
- $c$ = one-half of the crack length at the inside surface, m
- $R_i$ = inner radius of pipe, m
- $t$ = pipe wall thickness, m

### [11/23, Eqn. 2-4]
$$2\le\frac{R_i}{t}\le20$$
where
- $a$ = crack depth, m
- $c$ = one-half of the crack length at the mid-thickness of the wall, m
- $R_m$ = radius of pipe at the mid-thickness of the wall, m

원문 그대로: 공통 목록에는 $a$가 있고 $R_i$, $t$의 정의는 없다.

### [11/23, Eqn. 2-5]
$$0\le\frac{2c}{\pi R_m}\le1.7\quad\text{(circumferential crack)}$$
where
- $a$ = crack depth, m
- $c$ = one-half of the crack length at the mid-thickness of the wall, m
- $R_m$ = radius of pipe at the mid-thickness of the wall, m

### [11/23, Eqn. 2-6]
$$0\le\frac{2c}{t}\le20\quad\text{(axial crack)}$$
where
- $a$ = crack depth, m
- $c$ = one-half of the crack length at the mid-thickness of the wall, m
- $R_m$ = radius of pipe at the mid-thickness of the wall, m

### [12/24, Eqn. 2-7]
$$\sigma(x)_A=A_0+A_1\left(\frac{x}{a}\right)+A_2\left(\frac{x}{a}\right)^2+A_3\left(\frac{x}{a}\right)^3+A_4\left(\frac{x}{a}\right)^4$$
where
- $A_j$ = coefficients of polynomial representation of stress distribution over crack depth, MPa
- $x$ = distance from the surface and moving positive towards the tip of the crack, m
- $\sigma(x)_A$ = polynomial representation of stress distribution over crack depth, MPa

### [12/24, Eqn. 2-8]
$$K_I=\sum_{j=0}^{4}A_jG_j\left(\frac{\pi a}{Q}\right)^{1/2}$$
where
- $G_j$ = influence coefficients for the stress intensity factor
- $K_I$ = Mode I stress intensity factor, MPa√m
- $Q$ = flaw shape parameter, = $1+1.464(a/c)^{1.65}$

### [12/24, Eqn. 2-9]
$$\sigma(x)_B=B_0+B_1\left(\frac{x}{t}\right)+B_2\left(\frac{x}{t}\right)^2+B_3\left(\frac{x}{t}\right)^3+B_4\left(\frac{x}{t}\right)^4$$
where
- $B_j$ = coefficients of polynomial representation of stress distribution over thickness, MPa
- $\sigma(x)_B$ = polynomial representation of stress distribution over thickness, MPa

### [12/24, Eqn. 2-10]
$$K_I=\sum_{j=0}^{4}B_j\left(\frac{a}{t}\right)^jG_j\left(\frac{\pi a}{Q}\right)^{1/2}$$
별도 where 목록 없음.

### [13/25, Eqn. 2-11]
$$K_I=\int_0^a m(x,a)\sigma(x)\,dx$$
where
- $m(x,a)$ = Mode I weight function, 1/√m
- $\sigma(x)$ = stress distribution obtained in the absence of the crack, MPa

### [13/25, Eqn. 2-12]
$$m(x,a)=\frac{2}{(2\pi(a-x))^{1/2}}\left[1+M_1\left(1-\frac{x}{a}\right)^{1/2}+M_2\left(1-\frac{x}{a}\right)+M_3\left(1-\frac{x}{a}\right)^{3/2}\right]$$
where $M_j$ are universal weight function coefficients for the deepest point of a semi-elliptical part-through-wall crack that depend on the geometry of the cracked structure.

### [13/25, Eqn. 2-13]
$$m(x,a)=\frac{2}{(\pi x)^{1/2}}\left[1+N_1\left(\frac{x}{a}\right)^{1/2}+N_2\left(\frac{x}{a}\right)+N_3\left(\frac{x}{a}\right)^{3/2}\right]$$
where $N_j$ are universal weight function coefficients for the surface point of a semi-elliptical part-through-wall crack that depend on the geometry of the cracked structure.

### [14/26, Eqn. 2-14]
$$\sigma_i(x)=d_{0i}+d_{1i}x+d_{2i}x^2+d_{3i}x^3$$
where $d_{ji}$ are stress coefficients that describe the piece-wise cubic interpolation of the stress distribution between data points at $x_i$ and $x_{i+1}$, and $\sigma_i(x)$ are piece-wise cubic interpolations of the stress distribution between data points at $x_i$ and $x_{i+1}$.

### [20/32, Eqn. 2-15]
$$\sigma_i(x)=k_ix+b_i\qquad(i=1,\ldots,n)$$
where (원문에서는 Eqn. 2-16, 2-17이 이어지고 그 아래 and와 공통 정의 목록이 있다.)
- $b_i$ = constant of piece-wise linear representation of actual stress distribution over the interval $x_i$ and $x_{i+1}$, MPa
- $k_i$ = coefficient of piece-wise linear representation of actual stress distribution over the interval $x_i$ and $x_{i+1}$, MPa/m
- $n$ = number of intervals of piece-wise linear representation of actual stress distribution, dimensionless
- $x_i$ = positions of discrete data points of stress $\sigma(x_i)$, m
- $\sigma(x_i)$ = discrete data points of stress at positions $x_i$, MPa
- $\sigma_i(x)$ = piece-wise linear representation of actual stress distribution, MPa

### [20/32, Eqn. 2-16]
$$b_i=\sigma(x_i)-x_i\left(\frac{\sigma(x_{i+1})-\sigma(x_i)}{x_{i+1}-x_i}\right)$$
where (Eqn. 2-15~2-17 공통 목록, 원문 연결어: and)
- $b_i$ = constant of piece-wise linear representation of actual stress distribution over the interval $x_i$ and $x_{i+1}$, MPa
- $k_i$ = coefficient of piece-wise linear representation of actual stress distribution over the interval $x_i$ and $x_{i+1}$, MPa/m
- $n$ = number of intervals of piece-wise linear representation of actual stress distribution, dimensionless
- $x_i$ = positions of discrete data points of stress $\sigma(x_i)$, m
- $\sigma(x_i)$ = discrete data points of stress at positions $x_i$, MPa
- $\sigma_i(x)$ = piece-wise linear representation of actual stress distribution, MPa

### [20/32, Eqn. 2-17]
$$k_i=\frac{\sigma(x_{i+1})-\sigma(x_i)}{x_{i+1}-x_i}$$
where (Eqn. 2-15~2-17 공통 목록, 원문 연결어: and)
- $b_i$ = constant of piece-wise linear representation of actual stress distribution over the interval $x_i$ and $x_{i+1}$, MPa
- $k_i$ = coefficient of piece-wise linear representation of actual stress distribution over the interval $x_i$ and $x_{i+1}$, MPa/m
- $n$ = number of intervals of piece-wise linear representation of actual stress distribution, dimensionless
- $x_i$ = positions of discrete data points of stress $\sigma(x_i)$, m
- $\sigma(x_i)$ = discrete data points of stress at positions $x_i$, MPa
- $\sigma_i(x)$ = piece-wise linear representation of actual stress distribution, MPa

### [20/32, Eqn. 2-18]
$$K_I=\int_0^a\frac{2\sigma(x)}{(2\pi(a-x))^{1/2}}\left[1+M_1\left(1-\frac{x}{a}\right)^{1/2}+M_2\left(1-\frac{x}{a}\right)+M_3\left(1-\frac{x}{a}\right)^{3/2}\right]dx$$
별도 where 목록 없음.

### [20/32, Eqn. 2-19]
$$K_I=\sqrt{\frac{2}{\pi}}\int_0^a\sigma(x)\left[\frac{1}{\sqrt{a-x}}+\frac{1}{\sqrt a}M_1+\frac{\sqrt{a-x}}{a}M_2+\frac{a-x}{a\sqrt a}M_3\right]dx$$
별도 where 목록 없음.

### [21/33, Eqn. 2-20]
$$K_I(k_i,b_i)=\sqrt{\frac{2}{\pi}}\sum_{i=1}^n\int_{x_i}^{x_{i+1}}(k_ix+b_i)\left[\frac{1}{\sqrt{a-x}}+\frac{1}{\sqrt a}M_1+\frac{\sqrt{a-x}}{a}M_2+\frac{a-x}{a\sqrt a}M_3\right]dx$$
where
- $K_I(k_i,b_i)$ = stress intensity factor based on piece-wise linear representation of the actual astress distribution, MPa√m

원문 그대로: “astress”.

### [21/33, Eqn. 2-21]
$$K_I(k_i,b_i)=K_{IM0}+K_{IM1}M_1+K_{IM2}M_2+K_{IM3}M_3$$
where
- $K_{IMj}$ = stress intensity factors based on piece-wise linear representation of the actual stress distribution and for a value of $M_j$ of unity, MPa√m

### [21/33, Eqn. 2-22]
$$K_{IM0}=\frac{2\sqrt2}{3\sqrt\pi}\sum_{i=1}^n\left[(k_ix_i+2k_ia+3b_i)\sqrt{a-x_i}-(k_ix_{i+1}+2k_ia+3b_i)\sqrt{a-x_{i+1}}\right]$$
별도 where 목록 없음.

### [21/33, Eqn. 2-23]
$$K_{IM1}=\sqrt{\frac2\pi}\frac1{\sqrt a}\sum_{i=1}^n\left[\frac{k_i}{2}(x_{i+1}^2-x_i^2)+b_i(x_{i+1}-x_i)\right]$$
별도 where 목록 없음.

### [21/33, Eqn. 2-24]
$$K_{IM2}=\frac2{15}\sqrt{\frac2\pi}\frac1a\sum_{i=1}^n\left[(3k_ix_i+2k_ia+5b_i)(a-x_i)^{3/2}-(3k_ix_{i+1}+2k_ia+5b_i)(a-x_{i+1})^{3/2}\right]$$
별도 where 목록 없음. 원문 그대로: 식 번호가 “(Eqn. 2-”와 “24)”로 줄바꿈되어 있다.

### [21/33, Eqn. 2-25]
$$K_{IM3}=\sqrt{\frac2\pi}\frac1{a\sqrt a}\sum_{i=1}^n\left[\frac{k_i}{3}(x_i^3-x_{i+1}^3)+\frac12(k_ia-b_i)x_{i+1}^2-\frac12(k_ia-b_i)x_i^2+b_ia(x_{i+1}-x_i)\right]$$
별도 where 목록 없음. 원문 그대로: 식 번호가 “(Eqn. 2-”와 “25)”로 줄바꿈되어 있다.

### [21/33, Eqn. 2-26]
$$K_I=\int_0^a\frac{2\sigma(x)}{(\pi x)^{1/2}}\left[1+N_1\left(\frac xa\right)^{1/2}+N_2\left(\frac xa\right)+N_3\left(\frac xa\right)^{3/2}\right]dx$$
별도 where 목록 없음.

### [22/34, Eqn. 2-27]
$$K_I=\frac2{\sqrt\pi}\int_0^a\sigma(x)\left[\frac1{\sqrt x}+\frac1{\sqrt a}N_1+\frac{\sqrt x}{a}N_2+\frac{x}{a\sqrt a}N_3\right]dx$$
별도 where 목록 없음.

### [22/34, Eqn. 2-28]
$$K_I(k_i,b_i)=\frac2{\sqrt\pi}\sum_{i=1}^n\int_{x_i}^{x_{i+1}}(k_ix+b_i)\left[\frac1{\sqrt x}+\frac1{\sqrt a}N_1+\frac{\sqrt x}{a}N_2+\frac{x}{a\sqrt a}N_3\right]dx$$
별도 where 목록 없음.

### [22/34, Eqn. 2-29]
$$K_I(k_i,b_i)=K_{IN0}+K_{IN1}N_1+K_{IN2}N_2+K_{IN3}N_3$$
where
- $K_{INj}$ = stress intensity factors based on piece-wise linear representation of the actual stress distribution and for a value of $N_j$ of unity, MPa√m

### [22/34, Eqn. 2-30]
$$K_{IN0}=\frac4{3\sqrt\pi}\sum_{i=1}^n\left[\sqrt{x_{i+1}}(k_ix_{i+1}+3b_i)-\sqrt{x_i}(k_ix_i+3b_i)\right]$$
별도 where 목록 없음.

### [22/34, Eqn. 2-31]
$$K_{IN1}=\frac1{\sqrt{\pi a}}\sum_{i=1}^n\left[x_{i+1}(k_ix_{i+1}+2b_i)-x_i(k_ix_i+2b_i)\right]$$
별도 where 목록 없음.

### [22/34, Eqn. 2-32]
$$K_{IN2}=\frac4{15a\sqrt\pi}\sum_{i=1}^n\left[x_{i+1}^{3/2}(3k_ix_{i+1}+5b_i)-x_i^{3/2}(3k_ix_i+5b_i)\right]$$
별도 where 목록 없음.

### [22/34, Eqn. 2-33]
$$K_{IN3}=\frac1{3a\sqrt{\pi a}}\sum_{i=1}^n\left[x_{i+1}^2(2k_ix_{i+1}+3b_i)-x_i^2(2k_ix_i+3b_i)\right]$$
별도 where 목록 없음.

### [22/34, Eqn. 2-34]
$$M_1=\frac{2\pi}{\sqrt{2Q}}(3G_1-G_0)-\frac{24}{5}$$
별도 where 목록 없음.

### [23/35, Eqn. 2-35]
$$M_2=3$$
별도 where 목록 없음.

### [23/35, Eqn. 2-36]
$$M_3=\frac{6\pi}{\sqrt{2Q}}(G_0-2G_1)+\frac85$$
별도 where 목록 없음.

### [23/35, Eqn. 2-37]
$$N_1=\frac{3\pi}{\sqrt Q}(2G_0-5G_1)-8$$
별도 where 목록 없음.

### [23/35, Eqn. 2-38]
$$N_2=\frac{15\pi}{\sqrt Q}(3G_1-G_0)+15$$
별도 where 목록 없음.

### [23/35, Eqn. 2-39]
$$N_3=\frac{3\pi}{\sqrt Q}(3G_0-10G_1)-8$$
별도 where 목록 없음.

### [24/36, Eqn. 2-40]
$$\begin{aligned}
G_0&=a_0+a_1\left(\frac at\right)+a_2\left(\frac at\right)^{2.5}\\
a_0&=1.145-0.6875\left(\frac ac\right)+2.859\left(\frac ac\right)^2-4.794\left(\frac ac\right)^3+2.521\left(\frac ac\right)^4\\
a_1&=0.1432+0.6729\left(\frac ac\right)-18.27\left(\frac ac\right)^2+41.95\left(\frac ac\right)^3-24.72\left(\frac ac\right)^4\\
a_2&=1.125+2.445\left(\frac ac\right)+0.8622\left(\frac ac\right)^2-17.96\left(\frac ac\right)^3+14.09\left(\frac ac\right)^4
\end{aligned}$$
별도 where 목록 없음. 위치 문구: “Fitted relations for $R_i/t=1$”, “Deepest point:”.

### [24/36, Eqn. 2-41]
$$\begin{aligned}
G_1&=b_0+b_1\left(\frac at\right)^{0.5}+b_2\left(\frac at\right)^3\\
b_0&=0.699-0.4763\left(\frac ac\right)+4.81\left(\frac ac\right)^2-8.261\left(\frac ac\right)^{2.5}+3.969\left(\frac ac\right)^3\\
b_1&=0.03786+0.2835\left(\frac ac\right)-10.99\left(\frac ac\right)^2+22.1\left(\frac ac\right)^{2.5}-11.49\left(\frac ac\right)^3\\
b_2&=0.5703+1.966\left(\frac ac\right)-15.11\left(\frac ac\right)^2+21.16\left(\frac ac\right)^{2.5}-8.362\left(\frac ac\right)^3
\end{aligned}$$
별도 where 목록 없음. $R_i/t=1$, Deepest point.

### [25/37, Eqn. 2-42]
$$\begin{aligned}
G_0&=c_0+c_1\left(\frac at\right)+c_2\left(\frac at\right)^{1.5}\\
c_0&=0.112+2.907\left(\frac ac\right)-0.8041\left(\frac ac\right)^{1.5}-3.061\left(\frac ac\right)^2+2.045\left(\frac ac\right)^{2.5}\\
c_1&=-0.1387+9.454\left(\frac ac\right)-36.13\left(\frac ac\right)^{1.5}+38.8\left(\frac ac\right)^2-12.8\left(\frac ac\right)^{2.5}\\
c_2&=0.2363-17.42\left(\frac ac\right)+78.99\left(\frac ac\right)^{1.5}-102.1\left(\frac ac\right)^2+41.39\left(\frac ac\right)^{2.5}
\end{aligned}$$
별도 where 목록 없음. $R_i/t=1$, “Surface point:”.

### [25/37, Eqn. 2-43]
$$\begin{aligned}
G_1&=d_0+d_1\left(\frac at\right)+d_2\left(\frac at\right)^{1.5}+d_3\left(\frac at\right)^2\\
d_0&=0.1385\left(\frac ac\right)+1.523\left(\frac ac\right)^2-5.48\left(\frac ac\right)^3+7.611\left(\frac ac\right)^4-3.605\left(\frac ac\right)^5\\
d_1&=1.607\left(\frac ac\right)-11.98\left(\frac ac\right)^2+7.291\left(\frac ac\right)^3+36.24\left(\frac ac\right)^4-33.02\left(\frac ac\right)^5\\
d_2&=-4.648\left(\frac ac\right)+63.83\left(\frac ac\right)^2-199.23\left(\frac ac\right)^3+224.2\left(\frac ac\right)^4-84.62\left(\frac ac\right)^5\\
d_3&=3.033\left(\frac ac\right)-49.28\left(\frac ac\right)^2+191.75\left(\frac ac\right)^3-271.95\left(\frac ac\right)^4+126.9\left(\frac ac\right)^5
\end{aligned}$$
별도 where 목록 없음. $R_i/t=1$, Surface point.

### [26/38, Eqn. 2-44]
$$\begin{aligned}
G_0&=a_0+a_1\left(\frac at\right)^{0.5}+a_2\left(\frac at\right)+a_3\left(\frac at\right)^3\\
a_0&=1.172-0.253\left(\frac ac\right)^{0.5}+0.3206\left(\frac ac\right)-0.2573\left(\frac ac\right)^{1.5}+0.06087\left(\frac ac\right)^2\\
a_1&=-0.9925-3.059\left(\frac ac\right)^{0.5}+18.63\left(\frac ac\right)-26.19\left(\frac ac\right)^{1.5}+11.54\left(\frac ac\right)^2\\
a_2&=3.251+3.817\left(\frac ac\right)^{0.5}-41.47\left(\frac ac\right)+62.81\left(\frac ac\right)^{1.5}-28.31\left(\frac ac\right)^2\\
a_3&=-0.5334+14.96\left(\frac ac\right)^{0.5}-42.55\left(\frac ac\right)+44.27\left(\frac ac\right)^{1.5}-16\left(\frac ac\right)^2
\end{aligned}$$
별도 where 목록 없음. 위치 문구: “Fitted relations for $R_i/t=3$”, “Deepest point:”.

### [26/38, Eqn. 2-45]
$$\begin{aligned}
G_1&=b_0+b_1\left(\frac at\right)^{0.5}+b_2\left(\frac at\right)^{1.5}\\
b_0&=0.7012-0.3249\left(\frac ac\right)+3.082\left(\frac ac\right)^2-5.182\left(\frac ac\right)^{2.5}+2.463\left(\frac ac\right)^3\\
b_1&=-0.1263-1.823\left(\frac ac\right)+18.02\left(\frac ac\right)^2-31.05\left(\frac ac\right)^{2.5}+14.93\left(\frac ac\right)^3\\
b_2&=1.296-1.638\left(\frac ac\right)-22.4\left(\frac ac\right)^2+50.92\left(\frac ac\right)^{2.5}-28.07\left(\frac ac\right)^3
\end{aligned}$$
별도 where 목록 없음. $R_i/t=3$, Deepest point.

### [27/39, Eqn. 2-46]
$$\begin{aligned}
G_0&=c_0+c_1\left(\frac at\right)^{0.5}+c_2\left(\frac at\right)^{2.5}\\
c_0&=0.1153+2.684\left(\frac ac\right)-4.102\left(\frac ac\right)^2+2.497\left(\frac ac\right)^{2.5}\\
c_1&=0.0424+0.02856\left(\frac ac\right)-0.4422\left(\frac ac\right)^2+0.3575\left(\frac ac\right)^{2.5}\\
c_2&=-0.2892+10.23\left(\frac ac\right)-32.83\left(\frac ac\right)^2+23.29\left(\frac ac\right)^{2.5}
\end{aligned}$$
별도 where 목록 없음. $R_i/t=3$, “Surface point:”.

### [27/39, Eqn. 2-47]
$$\begin{aligned}
G_1&=d_0+d_1\left(\frac at\right)^{1.5}+d_2\left(\frac at\right)^2+d_3\left(\frac at\right)^3\\
d_0&=0.1251\left(\frac ac\right)+1.876\left(\frac ac\right)^2-7.633\left(\frac ac\right)^3+11.81\left(\frac ac\right)^4-5.988\left(\frac ac\right)^5\\
d_1&=-0.9053\left(\frac ac\right)+52.68\left(\frac ac\right)^2-266.9\left(\frac ac\right)^3+447.76\left(\frac ac\right)^4-232.33\left(\frac ac\right)^5\\
d_2&=3.787\left(\frac ac\right)-101.73\left(\frac ac\right)^2+498.9\left(\frac ac\right)^3-835.08\left(\frac ac\right)^4+433.86\left(\frac ac\right)^5\\
d_3&=-3.859\left(\frac ac\right)+89.62\left(\frac ac\right)^2-435.3\left(\frac ac\right)^3+733.65\left(\frac ac\right)^4-384.1\left(\frac ac\right)^5
\end{aligned}$$
별도 where 목록 없음. $R_i/t=3$, Surface point.

### [28/40, Eqn. 2-48]
$$\begin{aligned}
G_0&=a_0+a_1\left(\frac at\right)^{0.5}+a_2\left(\frac at\right)+a_3\left(\frac at\right)^3\\
a_0&=1.153-0.8897\left(\frac ac\right)+2.387\left(\frac ac\right)^{1.5}-2.599\left(\frac ac\right)^2+0.9924\left(\frac ac\right)^{2.5}\\
a_1&=-1.145+2.549\left(\frac ac\right)+8.51\left(\frac ac\right)^{1.5}-22.05\left(\frac ac\right)^2+12.11\left(\frac ac\right)^{2.5}\\
a_2&=3.402-20.3\left(\frac ac\right)+20.23\left(\frac ac\right)^{1.5}+8.67\left(\frac ac\right)^2-11.96\left(\frac ac\right)^{2.5}\\
a_3&=3.229-42.71\left(\frac ac\right)+106.7\left(\frac ac\right)^{1.5}-102.7\left(\frac ac\right)^2+35.59\left(\frac ac\right)^{2.5}
\end{aligned}$$
별도 where 목록 없음. 위치 문구: “Fitted relations for $R_i/t=5$”, “Deepest point:”.

### [28/40, Eqn. 2-49]
$$\begin{aligned}
G_1&=b_0+b_1\left(\frac at\right)^{0.5}+b_2\left(\frac at\right)+b_3\left(\frac at\right)^{2.5}\\
b_0&=0.7026-0.4167\left(\frac ac\right)+4.042\left(\frac ac\right)^2-6.903\left(\frac ac\right)^{2.5}+3.315\left(\frac ac\right)^3\\
b_1&=-0.449+4.929\left(\frac ac\right)-44.82\left(\frac ac\right)^2+78.85\left(\frac ac\right)^{2.5}-38.55\left(\frac ac\right)^3\\
b_2&=1.197-13.08\left(\frac ac\right)+105.2\left(\frac ac\right)^2-178.9\left(\frac ac\right)^{2.5}+85.61\left(\frac ac\right)^3\\
b_2&=1.082-3.018\left(\frac ac\right)-13.75\left(\frac ac\right)^2+41.33\left(\frac ac\right)^{2.5}-25.56\left(\frac ac\right)^3
\end{aligned}$$
별도 where 목록 없음. $R_i/t=5$, Deepest point. 원문 그대로: 마지막 계수식의 좌변도 $b_2$이며 $b_3$로 고치지 않았다.

### [29/41, Eqn. 2-50]
$$\begin{aligned}
G_0&=c_0+c_1\left(\frac at\right)+c_2\left(\frac at\right)^2+c_3\left(\frac at\right)^4\\
c_0&=0.113+2.758\left(\frac ac\right)-4.343\left(\frac ac\right)^2+2.669\left(\frac ac\right)^{2.5}\\
c_1&=0.2589-3.776\left(\frac ac\right)+11.54\left(\frac ac\right)^2-8.145\left(\frac ac\right)^{2.5}\\
c_2&=-0.6153+14.31\left(\frac ac\right)-43.05\left(\frac ac\right)^2+30\left(\frac ac\right)^{2.5}\\
c_3&=0.4854-3.034\left(\frac ac\right)+4.725\left(\frac ac\right)^2-2.382\left(\frac ac\right)^{2.5}
\end{aligned}$$
별도 where 목록 없음. $R_i/t=5$, “Surface point:”.

### [29/41, Eqn. 2-51]
$$\begin{aligned}
G_1&=d_0+d_1\left(\frac at\right)+d_2\left(\frac at\right)^{2.5}+d_3\left(\frac at\right)^3\\
d_0&=-0.001068+0.1597\left(\frac ac\right)+1.92\left(\frac ac\right)^2-3.752\left(\frac ac\right)^{2.5}+1.86\left(\frac ac\right)^3\\
d_1&=-0.06841+3.065\left(\frac ac\right)-30.05\left(\frac ac\right)^2+52.49\left(\frac ac\right)^{2.5}-25.32\left(\frac ac\right)^3\\
d_2&=0.4945-16.94\left(\frac ac\right)+208.96\left(\frac ac\right)^2-386.16\left(\frac ac\right)^{2.5}+193.45\left(\frac ac\right)^3\\
d_3&=-0.5577+19.47\left(\frac ac\right)-216.42\left(\frac ac\right)^2+390.25\left(\frac ac\right)^{2.5}-192.53\left(\frac ac\right)^3
\end{aligned}$$
별도 where 목록 없음. $R_i/t=5$, Surface point.

## 범위 집계

- 번호식: **51개** — Eqn. 2-1~2-51, 누락·중복 번호 없음. 같은 번호에 묶인 계수식은 해당 번호식에 포함했다.
- 번호 없는 독립 표시식: **0개** — 위 전사 기준에 따른 집계.
- 판독 확인 불가: 없음.
