# B050 식 독립 전사 (blind)

출처: `input/b050.pdf`. PDF 1~101쪽을 150 dpi PNG로 렌더링하여 육안 확인. 인쇄쪽은 본문에서 PDF쪽 − 16. 상대 결과 및 HTML 카드는 열지 않았다. Context와 식 안의 설명은 영어 원문을 보존했다. `/`로 인쇄된 식은 분수로 재구성하지 않고 slash와 괄호 구조를 보존했다. 번호 없는 항목은 출현 위치별로 세며, 동일 식의 반복 출현도 별도 항목이다. 한 기호 설명 bullet 또는 한 연속 조건 묶음은 한 항목으로 센다.

## 번호식

### Eq. 1 — PDF 20 / 인쇄 4
Context: The collapse moment can be calculated for cracks located in the tension zone as
$$
M=2\sigma_f R_m^2t\left[2\sin\beta_N-\sum_{j=1}^{N}\frac{a_{0j}}{t}\cos\gamma_j\sin\theta_j\right]
$$

### Eq. 2 — PDF 20 / 인쇄 4
Context: where
$$
\beta_N=\pi-\frac{\pi R_i^2p_{eff}}{2\sigma_f R_mt}-\sum_{j=1}^{N}\frac{a_{0j}}{t}\theta_j
$$

### Eq. 3 — PDF 21 / 인쇄 5
Context: The pressure sent to subroutines, including the effect of applied axial loads other than pressure, is derived from the axial stress equation.
$$
\sigma_{ax}=\frac{\pi R_i^2p+F_{ax}}{2\pi R_mt}=\frac{\pi R_i^2p_{eff}}{2\pi R_mt}
$$

### Eq. 4 — PDF 21 / 인쇄 5
Context: Thus,
$$
p_{eff}=\frac{\pi R_i^2P+F_{ax}}{\pi R_i^2}
$$

### Eq. 5 — PDF 23 / 인쇄 7
Context: The collapse moment can be calculated for cracks located in the tension zone.
$$
M_{NSC}=2\sigma_f R_m^2t\left[2\sin\beta-\frac{a_0}{t}\sin\theta\right],\theta\leq\pi-\beta
$$

### Eq. 6 — PDF 23 / 인쇄 7
Context: where
$$
\beta=\frac{\pi-\frac{a_0}{t}\theta}{2}-\frac{\pi R_i^2p_{eff}}{4\sigma_f R_mt}
$$

### Eq. 7 — PDF 23 / 인쇄 7
Context: The term a0/t is unity for a through-wall crack, so the equations above simplify to:
$$
M_{NSC}=2\sigma_f R_m^2t[2\sin\beta-\sin\theta],\theta\leq\pi-\beta
$$

### Eq. 8 — PDF 23 / 인쇄 7
Context: where
$$
\beta=\frac{\pi-\theta}{2}-\frac{\pi R_i^2p_{eff}}{4\sigma_f R_mt}
$$

### Eq. 9 — PDF 24 / 인쇄 8
Context: It is assumed that the J-integral is obtained by the sum of an elastic part and the plastic part.
$$
J=J_e+J_p
$$

### Eq. 10 — PDF 24 / 인쇄 8
Context: Similarly, the total rotation and axial displacement due to the crack are written as
$$
\phi^c=\phi_e^c+\phi_p^c
$$

### Eq. 11 — PDF 24 / 인쇄 8
Context: Total axial displacement due to the crack.
$$
\delta^c=\delta_e^c+\delta_p^c
$$

### Eq. 12 — PDF 24 / 인쇄 8
Context: The stress-strain constitutive relation is represented by the Ramberg-Osgood equation,
$$
\frac{\varepsilon}{\varepsilon_o}=\frac{\sigma}{\sigma_o}+\alpha\left(\frac{\sigma}{\sigma_o}\right)^n
$$

### Eq. 13 — PDF 25 / 인쇄 9
Context: The elastic component of the J-integral can be obtained as
$$
J_e=\frac{K_I^2}{E}
$$

### Eq. 14 — PDF 25 / 인쇄 9
Context: The K_I solution is given as
$$
K_I=(F_t\sigma_t+F_b\sigma_b)\sqrt{\pi R_m\theta}
$$

### Eq. 15 — PDF 25 / 인쇄 9
Context: The elastic components of the rotation and axial displacement are given as,
$$
\phi_e^c=\frac{M}{\pi R_m^2tE}I_b(\theta)
$$

### Eq. 16 — PDF 25 / 인쇄 9
Context: The elastic components of the rotation and axial displacement are given as,
$$
\delta_e^c=\frac{T}{4\pi tE}I_t(\theta)
$$

### Eq. 17 — PDF 25 / 인쇄 9
Context: where I_b and I_t are defined as,
$$
I_b(\theta)=4\int_0^\theta\xi F_b^2(\xi)d\xi
$$

### Eq. 18 — PDF 25 / 인쇄 9
Context: where I_b and I_t are defined as,
$$
I_t(\theta)=4\int_0^\theta\xi F_t^2(\xi)d\xi
$$

### Eq. 19 — PDF 25 / 인쇄 9
Context: The plastic part of the J-integral is defined below, again, separated into bending and tension components as,
$$
J_p^b=-\int_0^{\phi_p^c}\left.\frac{\partial M}{\partial A}\right|_{\phi_p^c}d\phi_p^c
$$

### Eq. 20 — PDF 25 / 인쇄 9
Context: The plastic part of the J-integral, tension component; A is the exposed crack area.
$$
J_p^t=-\int_0^{\delta_p^c}\left.\frac{\partial T}{\partial A}\right|_{\delta_p^c}d\delta_p^c
$$

### Eq. 21 — PDF 26 / 인쇄 10
Context: When the plastic part of (Eqn. 12) applies, it is assumed that,
$$
\phi_p^c=L_b'\alpha\left(\frac{\sigma_b}{\sigma_o}\right)^{n-1}\phi_e^c
$$

### Eq. 22 — PDF 26 / 인쇄 10
Context: When the plastic part of (Eqn. 12) applies; utilizing (Eqn. 15) and (Eqn. 16).
$$
\delta_p^c=L_t'\alpha\left(\frac{\sigma_t}{\sigma_o}\right)^{n-1}\delta_e^c
$$

### Eq. 23 — PDF 26 / 인쇄 10
Context: For a circumferential TWC in a single-material pipe subjected to bending load.
$$
L_b'=\left(\frac{t}{t_e}\right)^{n-1}\left(\frac{\pi}{4\widehat K}\right)^n
$$

### Eq. 24 — PDF 26 / 인쇄 10
Context: L_b' and L_t' can be shown to be, after some manipulation,
$$
L_t'=\left(\frac{t}{t_e}\right)^{n-1}
$$

### Eq. 25 — PDF 26 / 인쇄 10
Context: where; Γ(x) is the gamma function.
$$
\widehat K\approx\frac{\sqrt{\pi}}{2}\frac{\Gamma\left(1+\frac{1}{2n}\right)}{\Gamma\left(\frac{3}{2}+\frac{1}{2n}\right)}
$$

### Eq. 26 — PDF 26 / 인쇄 10
Context: (Eqn. 19) and (Eqn. 20) can be integrated to evaluate J_p in closed-form as
$$
J_p^b=\frac{\pi R_m}{2}\left(\frac{\alpha}{E\sigma_o^{n-1}}\right)\left(\frac{1}{n+1}\right)H_bL_b'I_b\left(\frac{M}{\pi R_m^2t}\right)^{n+1}
$$

### Eq. 27 — PDF 27 / 인쇄 11
Context: Closed-form plastic J-integral, tension component.
$$
J_p^t=\frac{\pi R_m}{2}\left(\frac{\alpha}{E\sigma_o^{n-1}}\right)\left(\frac{1}{n+1}\right)H_tL_t'I_t\left(\frac{T}{2\pi R_mt}\right)^{n+1}
$$

### Eq. 28 — PDF 27 / 인쇄 11
Context: where
$$
H_b=\frac{1}{I_b}\frac{\partial I_b}{\partial\theta}+\frac{1}{L_b'}\frac{\partial L_b'}{\partial\theta}
$$

### Eq. 29 — PDF 27 / 인쇄 11
Context: and
$$
H_t=\frac{1}{I_t}\frac{\partial I_t}{\partial\theta}+\frac{1}{L_t'}\frac{\partial L_t'}{\partial\theta}
$$

### Eq. 30 — PDF 27 / 인쇄 11
Context: For combined tension and bending moment conditions, J_p is estimated as
$$
J_p=J_p^b+J_p^t
$$

### Eq. 31 — PDF 27 / 인쇄 11
Context: The moment M in Eq. (17) must be replaced with an effective moment M_eff.
$$
M_{eff}=M+Te
$$

### Eq. 32 — PDF 27 / 인쇄 11
Context: where
$$
e=R_m\sin\left(\frac{\theta}{2}\right)
$$

### Eq. 33 — PDF 27 / 인쇄 11
Context: The angular specification of the crack size in radians is replaced by the arc length of the crack at the mean radius in length units as
$$
a=R_m\theta
$$

### Eq. 34 — PDF 27 / 인쇄 11
Context: Two conditions must be satisfied at crack instability.
$$
J(a_0,a^*)_{applied}=J(a_0,a^*)_{material}
$$

### Eq. 35 — PDF 27 / 인쇄 11
Context: Two conditions must be satisfied at crack instability.
$$
\frac{dJ(a_0,a^*)}{da}_{applied}=\frac{dJ(a_0,a^*)}{da}_{material}
$$

### Eq. 36 — PDF 28 / 인쇄 12
Context: Given a model for the pipe material’s J-resistance, given by
$$
J_{material}=J_i+C(\Delta a)^m
$$

### Eq. 37 — PDF 28 / 인쇄 12
Context: The contribution of axial loads, inclusive of pressure, is accounted for by use of an effective pressure term.
$$
\sigma_{ax}=\frac{\pi R_i^2p+F_{ax}}{2\pi R_mt}=\frac{\pi R_i^2p_{eff}}{2\pi R_mt}
$$

### Eq. 38 — PDF 29 / 인쇄 13
Context: Thus,
$$
p_{eff}=\frac{\pi R_i^2P+F_{ax}}{\pi R_i^2}
$$

### Eq. 39 — PDF 29 / 인쇄 13
Context: Used within this subroutine to calculate the critical pressure, pSESC for the axial half-crack length.
$$
p_{SESC}=p_o\,[(1-d/t)/(1-d/t/(tM_2))]
$$
원문 그대로: 분모의 중첩 slash 및 `(tM₂)`를 보존했다.

### Eq. 40 — PDF 30 / 인쇄 14
Context: Calculate the axial critical half-crack length for the through-wall crack for limit load conditions as,
$$
p=(t\ \sigma_f)/(R_m\ M_1)
$$

### Eq. 41 — PDF 30 / 인쇄 14
Context: where
$$
M_1=[1+1.2987\lambda^2-0.026905\lambda^4+5.3549\mathrm{x}10^{-4}\lambda^6]^{0.5}
$$

### Eq. 42 — PDF 30 / 인쇄 14
Context: Non-dimensional crack length in the Folias/bulging factor.
$$
\lambda=c/(R_m\,t)^{0.5}
$$

### Eq. 43 — PDF 31 / 인쇄 15
Context: Derivatives of the J values at the current iteration crack length are found numerically using three values, J₁, J₂, and J₃ at small increments of crack growth.
$$
dJ/da=(J_3-J_1)/(c_3-c_1)
$$

### Eq. 44 — PDF 31 / 인쇄 15
Context: Derivatives of the J values at the current iteration crack length.
$$
d^2J/da^2=(J_3-2J_2+J_1)/(0.001c)^2
$$

### Eq. 45 — PDF 31 / 인쇄 15
Context: Jmaterial values and derivatives are computed using the user input fracture toughness parameter values, Ji, C, and m.
$$
J_{material}=J_i+C(\Delta a)^m
$$

### Eq. 46 — PDF 31 / 인쇄 15
Context: Derivative of Jmaterial with respect to the crack length.
$$
dJ_{material}/da=m\ C(\Delta a)(m-1)
$$
원문 그대로: `(m-1)`은 위첨자가 아니라 보통 높이의 곱 괄호로 인쇄되어 있다.

### Eq. 47 — PDF 31 / 인쇄 15
Context: Second derivative of Jmaterial with respect to the crack length.
$$
d^2J_{material}/da^2=m\,(m-1)\,C(\Delta a)^{(m-2)}
$$

### Eq. 48 — PDF 31 / 인쇄 15
Context: During the solution process, the half the hoop stress is used.
$$
\sigma^\infty=(p\ R_i)/(2t)
$$

### Eq. 49 — PDF 31 / 인쇄 15
Context: The elastic part of the crack-driving force, Je.
$$
J_e=(1/E)\{(\sigma^\infty(\pi c)^{0.5}F\}^2
$$
원문 그대로: `{(`로 시작하지만 닫는 부분은 `}` 하나로 인쇄되어 있다. KaTeX에서 인쇄 문자로 표시하기 위해 중괄호를 escape했다.

### Eq. 50 — PDF 31 / 인쇄 15
Context: The plastic limit pressure pL.
$$
p_L=(2/3^{0.5})\,\sigma_y\,(t/R_m)(1/\{1+0.34\lambda+1.34\lambda^2\}^{0.5})
$$

### Eq. 51 — PDF 32 / 인쇄 16
Context: The plastic part of the crack-driving force, Jp.
$$
J_p=\alpha\ \sigma_y\,\varepsilon_0\,c\ h_1(n)\,(p/p_L)^{n+1}
$$

### Eq. 52 — PDF 32 / 인쇄 16
Context: Plastic zone correction terms.
$$
\phi=1/\{(1+(p/p_L)^2\}\ ,\ r_y=\{1/(2\pi)\}\{(n-1)/(n+1)\}\{(K/\sigma_y)^2\}
$$
원문 그대로: 첫 식은 `{(`로 시작하고 `}` 앞에 이에 대응하는 닫는 소괄호가 없다.

### Eq. 53 — PDF 32 / 인쇄 16
Context: and
$$
K=(J_e\ E)^{0.5}
$$

### Eq. 54 — PDF 82 / 인쇄 66
Context: Estimation of the Ramberg-Osgood parameters from the literature [57,58].
$$
\frac{\frac{\sigma_u}{\sigma_y}\exp\left(\frac{1}{n}\right)}{\left(1.002+\frac{\sigma_y}{E}\right)}=\left(\frac{\frac{1}{n}}{\ln\left(1.002+\frac{\sigma_y}{E}\right)}\right)^{\frac{1}{n}}
$$

### Eq. 55 — PDF 82 / 인쇄 66
Context: Estimation of the Ramberg-Osgood parameters.
$$
\frac{\sigma_o}{\sigma_u}(1.002+\varepsilon_o)=\left(2.718\,n\,\ln(1.002+\varepsilon_o)\right)^{\frac{1}{n}}
$$

### Eq. 56 — PDF 82 / 인쇄 66
Context: The parameter was also estimated using the EPRI and Framatome equations, respectively.
$$
\alpha=\frac{\left[\frac{\ln(1.002+\varepsilon_o)^{\frac{1}{n}}}{(1.002+\varepsilon_o)}\right]^n}{\varepsilon_o}
$$

### Eq. 57 — PDF 82 / 인쇄 66
Context: Framatome equation for the parameter α.
$$
\alpha=\frac{\left[(1/\varepsilon_o)ln(1.002+\varepsilon_o)-1.002-\varepsilon_o\right]}{(1.002+\varepsilon_o)^n}
$$

### Eq. 58 — PDF 82 / 인쇄 66
Context: The Charpy V-notch impact test upper shelf energy (USE) values were used to arrive at the JIC values.
$$
J_i=9.6\times10^{-5}\ CVN\ \sigma_f
$$

### Eq. 59 — PDF 83 / 인쇄 67
Context: The expression for the tearing modulus (Tmat) was used to obtain the constants C and m.
$$
T_{mat}=\frac{125\ CVN}{\sigma_f}
$$

### Eq. 60 — PDF 83 / 인쇄 67
Context: Assuming an average value of the tearing modulus [60].
$$
T_{mat}=\frac{E}{\sigma_f^2}\frac{dJ}{da}
$$

### Eq. 61 — PDF 83 / 인쇄 67
Context: Estimation of the J-R curve constant, C, by assuming m=1.
$$
\frac{dJ}{da}=C\ m\ (\Delta a)^{m-1}=C
$$

### Eq. 62 — PDF 83 / 인쇄 67
Context: Estimation of the J-R curve constant, C.
$$
\frac{T_{mat}\ \sigma_f^2}{E}=C,\qquad m=1
$$

### Eq. 63 — PDF 85 / 인쇄 69
Context: Dimensionless plastic zone parameter (DPZP) analysis [61].
$$
DPZP=\frac{2EJ_i}{\pi^2D_m\sigma_f^2}
$$

## 번호 없는 식·정의식·조건식

### Eq. U001 — PDF 6 / 인쇄 v
Context: The ratio of the input pressure to the critical pressure for the rupture of the pipe.
$$
p/p_{crit}
$$

### Eq. U002 — PDF 6 / 인쇄 v
Context: Pressure margin by computing the ratio of the input pressure to critical pressure.
$$
p/p_{crit}
$$

### Eq. U003 — PDF 7 / 인쇄 vi
Context: Overall, the average value for these 17 experiments.
$$
p_{Expt}/p_{Crit}
$$

### Eq. U004 — PDF 8 / 인쇄 vii
Context: Overall the average value for these 26 experiments.
$$
c_{Expt}/c_{Crit}
$$

### Eq. U005 — PDF 8 / 인쇄 vii
Context: For these 12 experiments, the average ratio.
$$
c_{Expt}/c_{Crit}
$$

### Eq. U006 — PDF 11 / 인쇄 x
Context: Figure 12. Distribution of results from Table 17 using J-M fracture toughness data.
$$
\theta/\theta\mathrm{crit}
$$

### Eq. U007 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
a\qquad\text{Half the circumferential crack length or surface crack depth}
$$

### Eq. U008 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
a_0\qquad\text{Crack depth of constant depth surface crack}
$$

### Eq. U009 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
a_{0j}\qquad\text{Crack depth of constant depth surface crack from an ensemble of surface cracks}
$$

### Eq. U010 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\mathrm{BM}\qquad\text{Bending moment}
$$

### Eq. U011 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\mathrm{BM_{max}}\qquad\text{Critical bending moment}
$$

### Eq. U012 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
C\qquad\text{Coefficient in extrapolated J-R curve expression}
$$

### Eq. U013 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\mathrm{C(T)}\qquad\text{Compact tension specimen}
$$

### Eq. U014 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
c\qquad\text{Half the axial crack length}
$$

### Eq. U015 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
c_{eff}\qquad\text{Effective half the axial crack length}
$$

### Eq. U016 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
c_{Crit}\qquad\text{Half the axial critical crack length}
$$

### Eq. U017 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
c_{Expt}\qquad\text{Effective half axial crack length}
$$

### Eq. U018 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
c_1,c_2,c_3\qquad\text{Various different crack lengths}
$$

### Eq. U019 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
d\qquad\text{Crack depth of an axial surface crack}
$$

### Eq. U020 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
e\qquad\text{Through-wall crack axial force eccentricity}
$$

### Eq. U021 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
D_m\qquad\text{Mean pipe diameter}
$$

### Eq. U022 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
E\qquad\text{Elastic modulus}
$$

### Eq. U023 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
F\qquad\text{Shape factor for axial TWC solution stress intensity factor}
$$

### Eq. U024 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
F_{ax}\qquad\text{Applied axial force, exclusive of pressure effects}
$$

### Eq. U025 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
F_b\qquad\text{Stress intensity shape factor for bending}
$$

### Eq. U026 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
F_t\qquad\text{Stress intensity shape factor for tension}
$$

### Eq. U027 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
H_b\qquad\text{Plastic J bending influence function}
$$

### Eq. U028 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
H_t\qquad\text{Plastic J tension influence function}
$$

### Eq. U029 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
h_1\qquad\text{Fully plastic influence function for the GE/EPRI method}
$$

### Eq. U030 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
I_b\qquad\text{Bending compliance function}
$$

### Eq. U031 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
I_t\qquad\text{Tension compliance function}
$$

### Eq. U032 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
J\qquad\text{Elastic plastic fracture toughness}
$$

### Eq. U033 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
J_{applied}\qquad\text{Applied J}
$$

### Eq. U034 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\mathrm{J-D}\qquad\text{Deformation theory J}
$$

### Eq. U035 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
J_e\qquad\text{Elastic component of J}
$$

### Eq. U036 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
J_i\qquad\text{J at crack initiation}
$$

### Eq. U037 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
J_{material}\qquad\text{Material J}
$$

### Eq. U038 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\mathrm{J-M}\qquad\text{Modified J}
$$

### Eq. U039 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
J_p\qquad\text{Plastic component of J}
$$

### Eq. U040 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\mathrm{J-R}\qquad\text{J-Resistance of the material}
$$

### Eq. U041 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
J_R\qquad\text{J-Resistance}
$$

### Eq. U042 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
J_1,J_2,J_3\qquad\text{J at various different crack sizes}
$$

### Eq. U043 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
K\qquad\text{Stress intensity factor}
$$

### Eq. U044 — PDF 13 / 인쇄 xii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
K_I\qquad\text{Mode I (crack opening) stress intensity factor}
$$

### Eq. U045 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\widehat K\qquad\text{Bending integration function for bending equivalent thickness}
$$

### Eq. U046 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
L_b'\qquad\text{Elastic-to-plastic influence function for bending}
$$

### Eq. U047 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
L_t'\qquad\text{Elastic-to-plastic influence function for tension}
$$

### Eq. U048 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
m\qquad\text{Extrapolated J-R curve exponent}
$$

### Eq. U049 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
M\qquad\text{Bending moment}
$$

### Eq. U050 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
M_1\qquad\text{Folias bulging factor for axial through-wall crack}
$$

### Eq. U051 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
M_2\qquad\text{Folias bulging factor for axial surface crack}
$$

### Eq. U052 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
M_{eff}\qquad\text{Effective moment}
$$

### Eq. U053 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
M_{NSC}\qquad\text{Net-Section Collapse moment}
$$

### Eq. U054 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
n\qquad\text{Strain hardening exponent}
$$

### Eq. U055 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
p\qquad\text{Pipe pressure}
$$

### Eq. U056 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
p_{eff}\qquad\text{Effective pressure}
$$

### Eq. U057 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
p_L\qquad\text{Limit pressure}
$$

### Eq. U058 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
P_{crit}\qquad\text{Critical pressure from axially cracked pipe experiment}
$$

### Eq. U059 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
P_{expt}\qquad\text{Pressure from axially cracked pipe experiment}
$$

### Eq. U060 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
P_{pred}\qquad\text{Predicted pressure from axially cracked analysis}
$$

### Eq. U061 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
p_{SESC}\qquad\text{Critical pressure for axial surface crack solution}
$$

### Eq. U062 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
p_0\qquad\text{Axial surface crack normalized pressure}
$$

### Eq. U063 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
r_y\qquad\text{Plastic zone correction radius}
$$

### Eq. U064 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
R_i\qquad\text{Inside pipe radius}
$$

### Eq. U065 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
R_m\qquad\text{Mean pipe radius}
$$

### Eq. U066 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
R_o\qquad\text{Outside pipe radius}
$$

### Eq. U067 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
t\qquad\text{Pipe wall thickness}
$$

### Eq. U068 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
t_e\qquad\text{Equivalent pipe wall thickness}
$$

### Eq. U069 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
T\qquad\text{Tension force}
$$

### Eq. U070 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
T_{mat}\qquad\text{Tearing modulus}
$$

### Eq. U071 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\alpha\qquad\text{Coefficient in Ramberg-Osgood relationship}
$$

### Eq. U072 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\alpha\qquad\text{Half crack angle between the tips of two adjacent circumferential surface cracks}
$$

### Eq. U073 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\beta\qquad\text{Complement of the angle from crack centerline to the neutral axis}
$$

### Eq. U074 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\beta_N\qquad\text{Complement of the angle from crack centerline to the neutral axis for an ensemble of surface cracks}
$$

### Eq. U075 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\Gamma\qquad\text{Mathematical gamma function}
$$

### Eq. U076 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\gamma_j\qquad\text{Angular location from top of crack to the center of a surface crack in an ensemble of surface cracks}
$$

### Eq. U077 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\Delta a\qquad\text{Crack growth}
$$

### Eq. U078 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\delta^c\qquad\text{Axial displacement due to a crack}
$$

### Eq. U079 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\delta_e^c\qquad\text{Elastic axial displacement due to a crack}
$$

### Eq. U080 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\delta_p^c\qquad\text{Plastic axial displacement due to a crack}
$$

### Eq. U081 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\varepsilon\qquad\text{Strain}
$$

### Eq. U082 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\varepsilon_0\qquad\text{Ramberg-Osgood reference strain}
$$

### Eq. U083 — PDF 14 / 인쇄 xiii
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\eta\qquad\text{Geometric factor used in calculation of J-R curve from pipe experiment}
$$

### Eq. U084 — PDF 15 / 인쇄 xiv
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\theta_j\qquad\text{Half angular size of a surface crack in an ensemble of surface cracks}
$$

### Eq. U085 — PDF 15 / 인쇄 xiv
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\theta\qquad\text{Half the current crack angle}
$$

### Eq. U086 — PDF 15 / 인쇄 xiv
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\theta_{crit}\qquad\text{Half the critical crack angle}
$$

### Eq. U087 — PDF 15 / 인쇄 xiv
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\lambda\qquad\text{Axial surface crack normalized crack length}
$$

### Eq. U088 — PDF 15 / 인쇄 xiv
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\xi\qquad\text{Angular integration variable}
$$

### Eq. U089 — PDF 15 / 인쇄 xiv
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\sigma\qquad\text{Stress}
$$

### Eq. U090 — PDF 15 / 인쇄 xiv
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\sigma_b\qquad\text{Bending stress}
$$

### Eq. U091 — PDF 15 / 인쇄 xiv
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\sigma_f\qquad\text{Flow stress}
$$

### Eq. U092 — PDF 15 / 인쇄 xiv
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\sigma_u\qquad\text{Ultimate strength}
$$

### Eq. U093 — PDF 15 / 인쇄 xiv
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\sigma_t\qquad\text{Tension stress}
$$

### Eq. U094 — PDF 15 / 인쇄 xiv
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\sigma_y\qquad\text{Yield strength}
$$

### Eq. U095 — PDF 15 / 인쇄 xiv
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\sigma_0\qquad\text{Ramberg-Osgood reference stress}
$$

### Eq. U096 — PDF 15 / 인쇄 xiv
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\sigma_\infty\qquad\text{Remote stress}
$$

### Eq. U097 — PDF 15 / 인쇄 xiv
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\phi\qquad\text{Plastic zone correction factor}
$$

### Eq. U098 — PDF 15 / 인쇄 xiv
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\phi^c\qquad\text{Rotation due to a crack}
$$

### Eq. U099 — PDF 15 / 인쇄 xiv
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\phi_e^c\qquad\text{Elastic rotation due to a crack}
$$

### Eq. U100 — PDF 15 / 인쇄 xiv
Context: NOMENCLATURE/LIST OF SYMBOLS (원문은 등호 없는 두 열 정의).
$$
\phi_p^c\qquad\text{Plastic rotation due to a crack}
$$

### Eq. U101 — PDF 19 / 인쇄 3
Context: For some collection of constant depth cracks.
$$
a_i(\xi)=a_i
$$

### Eq. U102 — PDF 19 / 인쇄 3
Context: Figure 1. Crack-tip angular coordinates.
$$
\gamma_j-\theta_j
$$

### Eq. U103 — PDF 19 / 인쇄 3
Context: Figure 1. Crack-tip angular coordinates.
$$
\gamma_j+\theta_j
$$

### Eq. U104 — PDF 19 / 인쇄 3
Context: Figure 1. Neutral-axis coordinate.
$$
\pi-\beta_N
$$

### Eq. U105 — PDF 19 / 인쇄 3
Context: Figure 1. Remaining ligament.
$$
t-a_{0j}
$$

### Eq. U106 — PDF 21 / 인쇄 5
Context: where
$$
\sigma_{ax}=\text{total axial stress}
$$

### Eq. U107 — PDF 21 / 인쇄 5
Context: where
$$
R_i=\text{pipe inner radius}
$$

### Eq. U108 — PDF 21 / 인쇄 5
Context: where
$$
p=\text{pipe internal pressure}
$$

### Eq. U109 — PDF 21 / 인쇄 5
Context: where
$$
F_{ax}=\text{applied axial force (excluding pressure contribution)}
$$

### Eq. U110 — PDF 21 / 인쇄 5
Context: where
$$
R_m=\text{pipe mean radius}
$$

### Eq. U111 — PDF 21 / 인쇄 5
Context: where
$$
t=\text{pipe wall thickness}
$$

### Eq. U112 — PDF 21 / 인쇄 5
Context: where
$$
p_{eff}=\text{effective pipe internal pressure.}
$$

### Eq. U113 — PDF 22 / 인쇄 6
Context: For a given constant crack depth.
$$
a(\xi)=a_0
$$

### Eq. U114 — PDF 22 / 인쇄 6
Context: For an ideal through-wall crack, the crack depth is equal to the pipe wall thickness.
$$
a_0\ \text{is equal to the pipe wall thickness}
$$

### Eq. U115 — PDF 23 / 인쇄 7
Context: For cracks located in the tension zone.
$$
\theta\leq\pi-\beta
$$

### Eq. U116 — PDF 23 / 인쇄 7
Context: and
$$
M_{\mathrm{NSC}}=\text{collapse moment}
$$

### Eq. U117 — PDF 23 / 인쇄 7
Context: and
$$
\sigma_f=\text{flow stress}=\tfrac12(\sigma_y+\sigma_u)
$$

### Eq. U118 — PDF 23 / 인쇄 7
Context: and
$$
\sigma_y=\text{yield strength}
$$

### Eq. U119 — PDF 23 / 인쇄 7
Context: and
$$
\sigma_u=\text{ultimate strength}
$$

### Eq. U120 — PDF 23 / 인쇄 7
Context: and
$$
R_m=\text{pipe mean radius}
$$

### Eq. U121 — PDF 23 / 인쇄 7
Context: and
$$
t=\text{pipe wall thickness}
$$

### Eq. U122 — PDF 23 / 인쇄 7
Context: and
$$
a_0=\text{crack depth}=t\ \text{for a through-wall crack}
$$

### Eq. U123 — PDF 23 / 인쇄 7
Context: and
$$
R_i=\text{pipe inner radius}
$$

### Eq. U124 — PDF 23 / 인쇄 7
Context: and
$$
p_{eff}=\text{pipe effective internal pressure, as defined above}
$$

### Eq. U125 — PDF 23 / 인쇄 7
Context: and
$$
\theta=\text{half of the included crack angle}
$$

### Eq. U126 — PDF 23 / 인쇄 7
Context: and
$$
\beta=\text{complement of the angle from crack centerline to the neutral axis.}
$$

### Eq. U127 — PDF 23 / 인쇄 7
Context: The term a0/t is unity for a through-wall crack.
$$
\text{a0/t}\ \text{is unity}
$$

### Eq. U128 — PDF 24 / 인쇄 8
Context: Associated strain with elastic modulus E.
$$
\varepsilon_o=\sigma_o/E
$$

### Eq. U129 — PDF 24 / 인쇄 8
Context: σo is a reference stress that is usually assumed to be yield stress.
$$
\sigma_o\ \text{is a reference stress that is usually assumed to be yield stress}
$$

### Eq. U130 — PDF 25 / 인쇄 9
Context: Shape factors are a function of pipe geometry and crack size.
$$
\theta/\pi
$$

### Eq. U131 — PDF 25 / 인쇄 9
Context: where KI is the mode I stress intensity factor.
$$
K_I\ \text{is the mode }I\text{ stress intensity factor}
$$

### Eq. U132 — PDF 25 / 인쇄 9
Context: Applied stresses due to axial tension (T) and global bending (M), respectively.
$$
\sigma_t\ \text{and}\ \sigma_b\ \text{are applied stresses due to axial tension }(T)\text{ and global bending }(M)\text{, respectively}
$$

### Eq. U133 — PDF 25 / 인쇄 9
Context: Corresponding shape factors.
$$
F_t\ \text{and}\ F_b\ \text{are the corresponding shape factors}
$$

### Eq. U134 — PDF 25 / 인쇄 9
Context: where A is the exposed crack area.
$$
A\ \text{is the exposed crack area}
$$

### Eq. U135 — PDF 26 / 인쇄 10
Context: The equivalent reduced thickness.
$$
t_e\ \text{is the equivalent reduced thickness}
$$

### Eq. U136 — PDF 26 / 인쇄 10
Context: Gamma function.
$$
\Gamma(x)\ \text{is the gamma function}
$$

### Eq. U137 — PDF 27 / 인쇄 11
Context: At crack instability.
$$
\text{current crack size}=\text{critical crack size}
$$

### Eq. U138 — PDF 28 / 인쇄 12
Context: where
$$
J_i=\text{fracture initiation toughness}
$$

### Eq. U139 — PDF 28 / 인쇄 12
Context: where
$$
C=\text{fitting coefficient for extrapolated J-R curve}
$$

### Eq. U140 — PDF 28 / 인쇄 12
Context: where
$$
\Delta a=\text{crack growth}
$$

### Eq. U141 — PDF 28 / 인쇄 12
Context: where
$$
m=\text{J-R curve hardening exponent,}
$$

### Eq. U142 — PDF 28 / 인쇄 12
Context: where
$$
\sigma_{ax}=\text{total axial stress}
$$

### Eq. U143 — PDF 28 / 인쇄 12
Context: where
$$
R_i=\text{pipe inner radius}
$$

### Eq. U144 — PDF 28 / 인쇄 12
Context: where
$$
p=\text{pipe internal pressure}
$$

### Eq. U145 — PDF 28 / 인쇄 12
Context: where
$$
F_{ax}=\text{applied axial force due to deadweight, thermal expansion, and dynamic excitation}\\ \text{(excluding pressure contribution)}
$$

### Eq. U146 — PDF 28 / 인쇄 12
Context: where
$$
R_m=\text{pipe mean radius}
$$

### Eq. U147 — PDF 28 / 인쇄 12
Context: where
$$
t=\text{pipe wall thickness}
$$

### Eq. U148 — PDF 28 / 인쇄 12
Context: where
$$
p_{eff}=\text{effective pipe internal pressure.}
$$

### Eq. U149 — PDF 28 / 인쇄 12
Context: Initial crack length.
$$
a_0\ \text{is an unknown initial crack length}
$$

### Eq. U150 — PDF 28 / 인쇄 12
Context: Critical crack length.
$$
a^*\ \text{is the critical crack length at instability}
$$

### Eq. U151 — PDF 28 / 인쇄 12
Context: The critical crack length at instability is always larger than the initial crack size.
$$
a^*\ \text{is always larger than the initial crack size,}\ a_0
$$

### Eq. U152 — PDF 29 / 인쇄 13
Context: where
$$
\mathrm{p_o}=(\mathrm{t}\ \sigma_f)/\mathrm{R_o}
$$

### Eq. U153 — PDF 29 / 인쇄 13
Context: A so called bulging factor for an axial crack that accounts for the fact axially cracked pipes “bulge” when pressurized.
$$
\mathrm{M_2}=[1+1.61\ \lambda^2]^{0.5}
$$

### Eq. U154 — PDF 29 / 인쇄 13
Context: where
$$
\lambda=\mathrm{c}/(\mathrm{R_m}\,\mathrm{t})^{0.5}
$$

### Eq. U155 — PDF 29 / 인쇄 13
Context: where
$$
\sigma_y=\text{yield stress}
$$

### Eq. U156 — PDF 29 / 인쇄 13
Context: where
$$
\sigma_u=\text{ultimate stress}
$$

### Eq. U157 — PDF 29 / 인쇄 13
Context: σf is the flow stress calculated as,
$$
\sigma_f=0.5(\sigma_y+\sigma_u)
$$

### Eq. U158 — PDF 29 / 인쇄 13
Context: where
$$
\mathrm{R_o}=\text{outer radius of the pipe,}
$$

### Eq. U159 — PDF 29 / 인쇄 13
Context: where
$$
\mathrm{R_m}=\text{mean radius of the pipe,}
$$

### Eq. U160 — PDF 29 / 인쇄 13
Context: where
$$
\mathrm d=\text{crack depth,}
$$

### Eq. U161 — PDF 29 / 인쇄 13
Context: where
$$
\mathrm t=\text{pipe wall thickness, and}
$$

### Eq. U162 — PDF 29 / 인쇄 13
Context: where
$$
\mathrm c=\text{axial half-crack length of the constant depth surface crack.}
$$

### Eq. U163 — PDF 29 / 인쇄 13
Context: Effective half-crack length (original prose definition).
$$
c_{eff}\ \text{where the area is divided by the maximum depth of the semi-elliptical crack}
$$

### Eq. U164 — PDF 30 / 인쇄 14
Context: and,
$$
\mathrm p=\text{applied pressure,}
$$

### Eq. U165 — PDF 30 / 인쇄 14
Context: and,
$$
\mathrm{R_m}=\text{mean radius of pipe,}
$$

### Eq. U166 — PDF 30 / 인쇄 14
Context: and,
$$
\mathrm t=\text{pipe wall thickness,}
$$

### Eq. U167 — PDF 30 / 인쇄 14
Context: and,
$$
\mathrm c=\text{the current axial half-crack length,}
$$

### Eq. U168 — PDF 30 / 인쇄 14
Context: and,
$$
\sigma_f=\text{flow stress, and}
$$

### Eq. U169 — PDF 30 / 인쇄 14
Context: and,
$$
\mathrm{M_1}=\text{the Folias/bulging factor for an axial through-wall crack.}
$$

### Eq. U170 — PDF 30 / 인쇄 14
Context: The solution is applicable within the range of
$$
0<\lambda\leq5
$$

### Eq. U171 — PDF 31 / 인쇄 15
Context: where
$$
J_i=\text{the initiation fracture toughness,}
$$

### Eq. U172 — PDF 31 / 인쇄 15
Context: where
$$
C=\text{the coefficient for the J-R curve,}
$$

### Eq. U173 — PDF 31 / 인쇄 15
Context: where
$$
m=\text{the exponent for the J-R curve, and}
$$

### Eq. U174 — PDF 31 / 인쇄 15
Context: where
$$
\Delta\mathrm a=\text{crack growth, i.e. difference in the crack length between the initial and current crack length.}
$$

### Eq. U175 — PDF 31 / 인쇄 15
Context: The axial TWC EPFM model uses the non-dimensional crack length parameter.
$$
\lambda\square\ (=\mathrm{c/(Rm\ t)0.5})
$$
원문 그대로: λ 뒤의 빈 사각형과 baseline의 `0.5`를 보존했다.

### Eq. U176 — PDF 31 / 인쇄 15
Context: Total crack-driving force.
$$
\mathrm J=\mathrm{Je}+\mathrm{Jp}
$$

### Eq. U177 — PDF 31 / 인쇄 15
Context: Effective half-crack length in the estimation of Je.
$$
(\mathrm{ce=c+}\square\square\mathrm{ry})
$$
원문 그대로: PDF에서 c+와 ry 사이에는 빈 사각형 두 개가 보인다.

### Eq. U178 — PDF 31 / 인쇄 15
Context: Plastic zone correction (unrendered boxes in the original PDF).
$$
(\square\square\mathrm{ry})
$$
원문 그대로: □는 PDF에서 실제로 빈 사각형으로 보이는 글리프다. 의미를 추정하여 φ로 대체하지 않았다.

### Eq. U179 — PDF 32 / 인쇄 16
Context: where
$$
\mathrm p=\text{applied pressure}
$$

### Eq. U180 — PDF 32 / 인쇄 16
Context: where
$$
\mathrm{R_i}=\text{pipe inner radius}
$$

### Eq. U181 — PDF 32 / 인쇄 16
Context: where
$$
\mathrm{R_m}=\text{mean pipe radius}
$$

### Eq. U182 — PDF 32 / 인쇄 16
Context: where
$$
\mathrm t=\text{pipe wall thickness}
$$

### Eq. U183 — PDF 32 / 인쇄 16
Context: where
$$
\mathrm E=\text{elastic modulus of the material}
$$

### Eq. U184 — PDF 32 / 인쇄 16
Context: where
$$
\mathrm c=\text{current axial half crack length}
$$

### Eq. U185 — PDF 32 / 인쇄 16
Context: where
$$
\rho=\text{non-dimensional crack length}\ \rho=\mathrm c/(\mathrm{R_m}\,\mathrm t)^{0.5}
$$

### Eq. U186 — PDF 32 / 인쇄 16
Context: where
$$
\mathrm F=\text{a shape factor}
$$

### Eq. U187 — PDF 32 / 인쇄 16
Context: where
$$
\alpha=\text{coefficient of Ramberg-Osgood model}
$$

### Eq. U188 — PDF 32 / 인쇄 16
Context: where
$$
\sigma_y=\text{yield strength}
$$

### Eq. U189 — PDF 32 / 인쇄 16
Context: where
$$
\sigma^\infty=\text{half the value of the hoop stress}
$$

### Eq. U190 — PDF 32 / 인쇄 16
Context: where
$$
\varepsilon_0=\text{reference strain, e.g., strain at yielding}
$$

### Eq. U191 — PDF 32 / 인쇄 16
Context: where
$$
\mathrm{h_1}=\text{fully plastic influence function for the GE/EPRI method}
$$

### Eq. U192 — PDF 32 / 인쇄 16
Context: where
$$
\mathrm n=\text{hardening exponent in the Ramberg-Osgood model}
$$

### Eq. U193 — PDF 32 / 인쇄 16
Context: where
$$
\mathrm{p_L}=\text{plastic limit pressure, assuming a yield strength of }\sigma_y
$$

### Eq. U194 — PDF 32 / 인쇄 16
Context: where
$$
\mathrm{J_e}=\text{calculated value of the elastic part of the J-integral}
$$

### Eq. U195 — PDF 32 / 인쇄 16
Context: where
$$
\mathrm{J_p}=\text{calculated value of the plastic part of the J-integral}
$$

### Eq. U196 — PDF 32 / 인쇄 16
Context: where
$$
\mathrm K=\text{stress intensity factor.}
$$

### Eq. U197 — PDF 32 / 인쇄 16
Context: The parameter values are limited to the ranges of:
$$
5.0<R_m/t<20,\quad1.0<n<7.0,\quad0.5<\rho<3.0
$$

### Eq. U198 — PDF 34 / 인쇄 18
Context: Table 2. Limits / Comments.
$$
\text{Ro > thick}
$$

### Eq. U199 — PDF 34 / 인쇄 18
Context: Table 2. Limits / Comments.
$$
\text{Thick > 0}
$$

### Eq. U200 — PDF 34 / 인쇄 18
Context: Table 2. Limits / Comments.
$$
\text{Step\_size>0}
$$

### Eq. U201 — PDF 34 / 인쇄 18
Context: Table 2. Limits / Comments.
$$
\text{N>=0}
$$

### Eq. U202 — PDF 34 / 인쇄 18
Context: Table 2. Limits / Comments.
$$
\text{depth < thick}
$$

### Eq. U203 — PDF 34 / 인쇄 18
Context: Table 2. Limits / Comments.
$$
\text{0 < Theta < π}
$$

### Eq. U204 — PDF 34 / 인쇄 18
Context: Table 2. Limits / Comments.
$$
\text{- π < Gamma < π}
$$

### Eq. U205 — PDF 34 / 인쇄 18
Context: Table 2. Limits / Comments.
$$
\text{sigy > 0}
$$

### Eq. U206 — PDF 34 / 인쇄 18
Context: Table 2. Limits / Comments.
$$
\text{sigu >= sigy}
$$

### Eq. U207 — PDF 34 / 인쇄 18
Context: Table 2. Limits / Comments.
$$
\text{RO\_alpha > 0}
$$

### Eq. U208 — PDF 34 / 인쇄 18
Context: Table 2. Limits / Comments.
$$
\text{RO\_sigo > 0}
$$

### Eq. U209 — PDF 34 / 인쇄 18
Context: Table 2. Limits / Comments.
$$
\text{RO\_epso > 0}
$$

### Eq. U210 — PDF 35 / 인쇄 19
Context: Table 2 (continued). Limits / Comments; Step_phi description includes interval.
$$
\text{RO\_n > 0}
$$

### Eq. U211 — PDF 35 / 인쇄 19
Context: Table 2 (continued). Limits / Comments; Step_phi description includes interval.
$$
\text{Resist\_Jic > 0}
$$

### Eq. U212 — PDF 35 / 인쇄 19
Context: Table 2 (continued). Limits / Comments; Step_phi description includes interval.
$$
\text{Resist\_C > 0}
$$

### Eq. U213 — PDF 35 / 인쇄 19
Context: Table 2 (continued). Limits / Comments; Step_phi description includes interval.
$$
\text{Resist\_m > 0}
$$

### Eq. U214 — PDF 35 / 인쇄 19
Context: Table 2 (continued). Limits / Comments; Step_phi description includes interval.
$$
\text{[-π,π]}
$$

### Eq. U215 — PDF 35 / 인쇄 19
Context: Table 2 (continued). Limits / Comments; Step_phi description includes interval.
$$
\text{Step\_phi>=0}
$$

### Eq. U216 — PDF 35 / 인쇄 19
Context: Table 2 (continued). Limits / Comments; Step_phi description includes interval.
$$
\text{Uncert\_Flag>=0}
$$

### Eq. U217 — PDF 35 / 인쇄 19
Context: Table 2 (continued). Limits / Comments; Step_phi description includes interval.
$$
\text{Usample>=0}
$$

### Eq. U218 — PDF 35 / 인쇄 19
Context: Table 2 (continued). Limits / Comments; Step_phi description includes interval.
$$
\text{Uampli>=0}
$$

### Eq. U219 — PDF 35 / 인쇄 19
Context: Table 2 (continued). Limits / Comments; Step_phi description includes interval.
$$
\text{Rseed>=0}
$$

### Eq. U220 — PDF 35 / 인쇄 19
Context: Table 2 (continued). Limits / Comments; Step_phi description includes interval.
$$
\text{BM>=0}
$$

### Eq. U221 — PDF 35 / 인쇄 19
Context: Table 2 (continued). Limits / Comments; Step_phi description includes interval.
$$
\text{Pressure>=0}
$$

### Eq. U222 — PDF 35 / 인쇄 19
Context: Table 2 (continued). Limits / Comments; Step_phi description includes interval.
$$
\text{F\_ax >=0}
$$

### Eq. U223 — PDF 35 / 인쇄 19
Context: Table 2 (continued). Limits / Comments; Step_phi description includes interval.
$$
\text{0<=DMW\_ratio<=1}
$$

### Eq. U224 — PDF 35 / 인쇄 19
Context: Table 2. DMW_flag.
$$
\text{=0, not DMW analysis}
$$

### Eq. U225 — PDF 35 / 인쇄 19
Context: Table 2. DMW_flag.
$$
\text{=1,DMW analysis}
$$

### Eq. U226 — PDF 35 / 인쇄 19
Context: Table 2. crack_morph.
$$
\text{= 1, constant depth surface crack NSC}
$$

### Eq. U227 — PDF 35 / 인쇄 19
Context: Table 2. crack_morph.
$$
\text{= 2, parabolic surface crack NSC}
$$

### Eq. U228 — PDF 35 / 인쇄 19
Context: Table 2. crack_morph.
$$
\text{= 3, semi-elliptical surface crack NSC}
$$

### Eq. U229 — PDF 35 / 인쇄 19
Context: Table 2. crack_morph.
$$
\text{crack\_morph = 1}
$$

### Eq. U230 — PDF 35 / 인쇄 19
Context: Table 2. crack_morph.
$$
\text{crack\_morph = 2}
$$

### Eq. U231 — PDF 35 / 인쇄 19
Context: Table 2. crack_morph.
$$
\text{crack\_morph = 3}
$$

### Eq. U232 — PDF 35 / 인쇄 19
Context: Table 2. i_write.
$$
\text{= 0, do not write}
$$

### Eq. U233 — PDF 35 / 인쇄 19
Context: Table 2. i_write.
$$
\text{= 1, write solution values to file “SC\_Fail.out”}
$$

### Eq. U234 — PDF 35 / 인쇄 19
Context: Table 2. i_write.
$$
\text{i\_write = 0}
$$

### Eq. U235 — PDF 35 / 인쇄 19
Context: Table 2. i_write.
$$
\text{i\_write = 1}
$$

### Eq. U236 — PDF 36 / 인쇄 20
Context: Table 3. if_flag, solution return code.
$$
\text{= 0, the SC does not fail}
$$

### Eq. U237 — PDF 36 / 인쇄 20
Context: Table 3. if_flag, solution return code.
$$
\text{= 1, the SC will fail under the applied loads}
$$

### Eq. U238 — PDF 36 / 인쇄 20
Context: Table 3. if_flag, solution return code.
$$
\text{= -1, no solution due to an error}
$$

### Eq. U239 — PDF 36 / 인쇄 20
Context: Table 3. i_error.
$$
\text{= 101, Crack depth greater than or equal to thickness for any crack}
$$

### Eq. U240 — PDF 36 / 인쇄 20
Context: Table 3. i_error.
$$
\text{= 102, Outer radius less than or equal to 2*thick}
$$

### Eq. U241 — PDF 36 / 인쇄 20
Context: Table 3. i_error.
$$
\text{= 103, Crack half-length less than or equal to 0 or greater than or equal to π for any crack}
$$

### Eq. U242 — PDF 36 / 인쇄 20
Context: Table 3. i_error.
$$
\text{= 104, Crack location less than –π or greater than π}
$$

### Eq. U243 — PDF 36 / 인쇄 20
Context: Table 3. i_error.
$$
\text{= 105, Overlapping cracks}
$$

### Eq. U244 — PDF 36 / 인쇄 20
Context: Table 3. i_error.
$$
\text{= 106, Yield stress less than or equal to 0 or ultimate stress less than or equal to zero or yield stress greater than ultimate stress}
$$

### Eq. U245 — PDF 36 / 인쇄 20
Context: Table 3. i_error.
$$
\text{= 107, Any of the four Ramberg-Osgood parameters (RO\_alpha, RO\_sigo, RO\_epso, RO\_n) less than 0}
$$

### Eq. U246 — PDF 36 / 인쇄 20
Context: Table 3. i_error.
$$
\text{= 108, And of three J-R curve constants (resist\_Jic, resist\_C, resist\_m) less than zero}
$$

### Eq. U247 — PDF 36 / 인쇄 20
Context: Table 3. i_error.
$$
\text{= 109, Applied internal pressure less than 0 or applied bending moment less than 0}
$$

### Eq. U248 — PDF 36 / 인쇄 20
Context: Table 3. i_error.
$$
\text{= 110, Loading and/or crack size put neutral axis out of range}
$$

### Eq. U249 — PDF 36 / 인쇄 20
Context: Table 3. ratio_BM.
$$
\text{≥ 0.0, BM/BM\_max}
$$

### Eq. U250 — PDF 36 / 인쇄 20
Context: Table 3. ratio_BM.
$$
\text{= -1.0, if\_flag <0}
$$

### Eq. U251 — PDF 37 / 인쇄 21
Context: Table 4. Error 102, literal product within the condition.
$$
\text{Outer radius less than or equal to 2*thick}
$$

### Eq. U252 — PDF 38 / 인쇄 22
Context: Derived consistent units.
$$
\text{Stress: N/mm² = MPa}
$$

### Eq. U253 — PDF 38 / 인쇄 22
Context: Derived consistent units.
$$
\text{Pressure: N/mm² = MPa}
$$

### Eq. U254 — PDF 38 / 인쇄 22
Context: Derived consistent units.
$$
\text{Initiation toughness (Jic): N/mm = kJ/m²}
$$

### Eq. U255 — PDF 38 / 인쇄 22
Context: Derived consistent units.
$$
\text{Fracture resistance constant }(C)\text{: }\mathrm{N/mm}^{(m+1)}
$$

### Eq. U256 — PDF 38 / 인쇄 22
Context: Predicted failure, yes or no.
$$
\text{if\_flag = 1}
$$

### Eq. U257 — PDF 38 / 인쇄 22
Context: Predicted failure, yes or no.
$$
\text{if\_flag = 0}
$$

### Eq. U258 — PDF 41 / 인쇄 25
Context: Table 6. Limits/Comments.
$$
\text{Ro > thick}
$$

### Eq. U259 — PDF 41 / 인쇄 25
Context: Table 6. Limits/Comments.
$$
\text{Thick > 0}
$$

### Eq. U260 — PDF 41 / 인쇄 25
Context: Table 6. Limits/Comments.
$$
\text{0 < Theta < pi}
$$

### Eq. U261 — PDF 41 / 인쇄 25
Context: Table 6. Limits/Comments.
$$
\text{sigy > 0}
$$

### Eq. U262 — PDF 41 / 인쇄 25
Context: Table 6. Limits/Comments.
$$
\text{sigu >= sigy}
$$

### Eq. U263 — PDF 41 / 인쇄 25
Context: Table 6. Limits/Comments.
$$
\text{RO\_alpha > 0}
$$

### Eq. U264 — PDF 41 / 인쇄 25
Context: Table 6. Limits/Comments.
$$
\text{RO\_sigo > 0}
$$

### Eq. U265 — PDF 41 / 인쇄 25
Context: Table 6. Limits/Comments.
$$
\text{RO\_epso > 0}
$$

### Eq. U266 — PDF 41 / 인쇄 25
Context: Table 6. Limits/Comments.
$$
\text{RO\_n > 0}
$$

### Eq. U267 — PDF 41 / 인쇄 25
Context: Table 6. Limits/Comments.
$$
\text{Resist\_Jic > 0}
$$

### Eq. U268 — PDF 41 / 인쇄 25
Context: Table 6. Limits/Comments.
$$
\text{Resist\_C > 0}
$$

### Eq. U269 — PDF 41 / 인쇄 25
Context: Table 6. Limits/Comments.
$$
\text{Resist\_m > 0}
$$

### Eq. U270 — PDF 41 / 인쇄 25
Context: Table 6. Limits/Comments.
$$
\text{pressure >= 0}
$$

### Eq. U271 — PDF 41 / 인쇄 25
Context: Table 6. Limits/Comments.
$$
\text{BM >= 0}
$$

### Eq. U272 — PDF 41 / 인쇄 25
Context: Table 6. Limits/Comments.
$$
\text{F\_ax >=0}
$$

### Eq. U273 — PDF 41 / 인쇄 25
Context: Table 6. i_write.
$$
\text{=0, do not save}
$$

### Eq. U274 — PDF 41 / 인쇄 25
Context: Table 6. i_write.
$$
\text{=1, save analysis results for NSC and ENG2 calculations to file TWC\_fail.out}
$$

### Eq. U275 — PDF 41 / 인쇄 25
Context: Table 6. i_write.
$$
\text{i\_write = 0}
$$

### Eq. U276 — PDF 41 / 인쇄 25
Context: Table 6. i_write.
$$
\text{i\_write = 1}
$$

### Eq. U277 — PDF 42 / 인쇄 26
Context: Table 7. if_flag.
$$
\text{=-1, no solution has been found}
$$

### Eq. U278 — PDF 42 / 인쇄 26
Context: Table 7. if_flag.
$$
\text{= 0, the TWC does not fail}
$$

### Eq. U279 — PDF 42 / 인쇄 26
Context: Table 7. if_flag.
$$
\text{= 1, the TWC will fail under the applied loads}
$$

### Eq. U280 — PDF 42 / 인쇄 26
Context: Table 7. ratio_theta.
$$
\text{normally≥0.0, theta/theta\_max}
$$

### Eq. U281 — PDF 42 / 인쇄 26
Context: Table 7. ratio_theta.
$$
\text{=-1.0, no valid solution, see if\_flag and i\_err\_code values<300}
$$

### Eq. U282 — PDF 42 / 인쇄 26
Context: Table 8. i_err_code 100.
$$
\text{R\_o <= 2*thick}
$$

### Eq. U283 — PDF 42 / 인쇄 26
Context: Table 8. i_err_code 101.
$$
\text{theta<=0 OR theta>=π}
$$

### Eq. U284 — PDF 42 / 인쇄 26
Context: Table 8. i_err_code 102.
$$
\text{sigy<=0 OR sigu<=0 OR sigy>sigu}
$$

### Eq. U285 — PDF 42 / 인쇄 26
Context: Table 8. i_err_code 103.
$$
\text{RO\_alpha<0 OR RO\_sigo<0 OR RO\_epso<0 OR RO\_n<0}
$$

### Eq. U286 — PDF 42 / 인쇄 26
Context: Table 8. i_err_code 104.
$$
\text{RO\_alpha=0 AND RO\_sigo=0 AND RO\_epso=0 AND RO\_n=0}
$$

### Eq. U287 — PDF 42 / 인쇄 26
Context: Table 8. i_err_code 105.
$$
\text{Resist\_Jic<0 OR Resist\_C<0 OR Resist\_m<0}
$$

### Eq. U288 — PDF 42 / 인쇄 26
Context: Table 8. i_err_code 106.
$$
\text{Resist\_Jic=0 AND Resist\_C=0 AND Resist\_m=0}
$$

### Eq. U289 — PDF 42 / 인쇄 26
Context: Table 8. i_err_code 107.
$$
\text{pressure<0 OR BM<0}
$$

### Eq. U290 — PDF 42 / 인쇄 26
Context: Table 8. i_err_code 210.
$$
\text{NSC solution not in range of 0.0<theta\_max<π}
$$

### Eq. U291 — PDF 42 / 인쇄 26
Context: Table 8. i_err_code 212.
$$
\text{ENG2 solution not in range of 0.0<theta\_max<π}
$$

### Eq. U292 — PDF 43 / 인쇄 27
Context: Table 8 (continued). i_err_code 300, ratio_theta.
$$
\text{0<=value<1}
$$

### Eq. U293 — PDF 43 / 인쇄 27
Context: Table 8 (continued). i_err_code 301, ratio_theta.
$$
\text{0<=value<1}
$$

### Eq. U294 — PDF 43 / 인쇄 27
Context: Table 8 (continued). i_err_code 302, ratio_theta.
$$
\text{value>=1}
$$

### Eq. U295 — PDF 43 / 인쇄 27
Context: Table 8 (continued). i_err_code 303, ratio_theta.
$$
\text{value>=1}
$$

### Eq. U296 — PDF 43 / 인쇄 27
Context: Table 8 (continued). i_err_code 304, ratio_theta.
$$
\text{0<=value<1}
$$

### Eq. U297 — PDF 43 / 인쇄 27
Context: Table 8 (continued). i_err_code 304, Condition.
$$
\text{stress on remaining ligament>sigu}
$$

### Eq. U298 — PDF 43 / 인쇄 27
Context: Table 8 (continued). i_err_code 305, ratio_theta.
$$
\text{0<=value<1}
$$

### Eq. U299 — PDF 43 / 인쇄 27
Context: Table 8 (continued). i_err_code 305, Condition.
$$
\text{stress on remaining ligament>sigu}
$$

### Eq. U300 — PDF 43 / 인쇄 27
Context: Table 8 (continued). i_err_code 306, ratio_theta.
$$
\text{value>=1}
$$

### Eq. U301 — PDF 43 / 인쇄 27
Context: Table 8 (continued). i_err_code 306, Condition.
$$
\text{stress on remaining ligament>sigu}
$$

### Eq. U302 — PDF 43 / 인쇄 27
Context: Table 8 (continued). i_err_code 307, ratio_theta.
$$
\text{value>=1}
$$

### Eq. U303 — PDF 43 / 인쇄 27
Context: Table 8 (continued). i_err_code 307, Condition.
$$
\text{stress on remaining ligament>sigu}
$$

### Eq. U304 — PDF 43 / 인쇄 27
Context: Table 8 (continued). i_err_code 308, ratio_theta.
$$
\text{0<=value<1}
$$

### Eq. U305 — PDF 43 / 인쇄 27
Context: Table 8 (continued). i_err_code 309, ratio_theta.
$$
\text{0<=value<1}
$$

### Eq. U306 — PDF 43 / 인쇄 27
Context: Table 8 (continued). i_err_code 310, ratio_theta.
$$
\text{value>=1}
$$

### Eq. U307 — PDF 43 / 인쇄 27
Context: Table 8 (continued). i_err_code 311, ratio_theta.
$$
\text{value>=1}
$$

### Eq. U308 — PDF 43 / 인쇄 27
Context: Table 8 (continued). i_err_code 312, ratio_theta.
$$
\text{0<=value<1}
$$

### Eq. U309 — PDF 43 / 인쇄 27
Context: Table 8 (continued). i_err_code 312, Condition.
$$
\text{theta\_max=0.0}
$$

### Eq. U310 — PDF 43 / 인쇄 27
Context: Table 8 (continued). i_err_code 313, ratio_theta.
$$
\text{0<=value<1}
$$

### Eq. U311 — PDF 43 / 인쇄 27
Context: Table 8 (continued). i_err_code 313, Condition.
$$
\text{theta\_max=0.0}
$$

### Eq. U312 — PDF 43 / 인쇄 27
Context: Table 8 (continued). i_err_code 314, ratio_theta.
$$
\text{value>=1}
$$

### Eq. U313 — PDF 43 / 인쇄 27
Context: Table 8 (continued). i_err_code 314, Condition.
$$
\text{theta\_max=0.0}
$$

### Eq. U314 — PDF 43 / 인쇄 27
Context: Table 8 (continued). i_err_code 315, ratio_theta.
$$
\text{value>=1}
$$

### Eq. U315 — PDF 43 / 인쇄 27
Context: Table 8 (continued). i_err_code 315, Condition.
$$
\text{theta\_max=0.0}
$$

### Eq. U316 — PDF 43 / 인쇄 27
Context: Table 8 (continued). i_err_code 316, ratio_theta.
$$
\text{0<=value<1}
$$

### Eq. U317 — PDF 43 / 인쇄 27
Context: Table 8 (continued). i_err_code 316, Condition.
$$
\text{theta\_max=π}
$$

### Eq. U318 — PDF 43 / 인쇄 27
Context: Table 8 (continued). i_err_code 317, ratio_theta.
$$
\text{0<=value<1}
$$

### Eq. U319 — PDF 43 / 인쇄 27
Context: Table 8 (continued). i_err_code 317, Condition.
$$
\text{theta\_max=π}
$$

### Eq. U320 — PDF 43 / 인쇄 27
Context: Table 8 (continued). i_err_code 318, ratio_theta.
$$
\text{value>=1}
$$

### Eq. U321 — PDF 43 / 인쇄 27
Context: Table 8 (continued). i_err_code 318, Condition.
$$
\text{theta\_max=π}
$$

### Eq. U322 — PDF 43 / 인쇄 27
Context: Table 8 (continued). i_err_code 319, ratio_theta.
$$
\text{value>=1}
$$

### Eq. U323 — PDF 43 / 인쇄 27
Context: Table 8 (continued). i_err_code 319, Condition.
$$
\text{theta\_max=π}
$$

### Eq. U324 — PDF 44 / 인쇄 28
Context: Derived consistent units (plain baseline numerals in original).
$$
\text{Stress: N/mm2 = MPa}
$$

### Eq. U325 — PDF 44 / 인쇄 28
Context: Derived consistent units (plain baseline numerals in original).
$$
\text{Pressure: N/mm2 = MPa}
$$

### Eq. U326 — PDF 44 / 인쇄 28
Context: Derived consistent units (plain baseline numerals in original).
$$
\text{Initiation toughness (Jic): N/mm = kJ/m2}
$$

### Eq. U327 — PDF 44 / 인쇄 28
Context: Derived consistent units (plain baseline numerals in original).
$$
\text{Fracture resistance constant (C): N/mm(m+1)}
$$

### Eq. U328 — PDF 45 / 인쇄 29
Context: Table 9. RACS-1*.
$$
\text{c/ccrit > 0.9}
$$

### Eq. U329 — PDF 45 / 인쇄 29
Context: Table 9. RACS-9*.
$$
\text{[p/pcrit ≥ 1]}
$$

### Eq. U330 — PDF 45 / 인쇄 29
Context: Table 9. RACS-9*.
$$
\text{[Axial\_SC\_fail]=1}
$$

### Eq. U331 — PDF 45 / 인쇄 29
Context: Table 9. RACS-9*.
$$
\text{[i\_ctype]=1}
$$

### Eq. U332 — PDF 45 / 인쇄 29
Context: Table 9. RACS-9*.
$$
\text{[c\_over\_ccrit] set equal to its initial value of 1}
$$

### Eq. U333 — PDF 45 / 인쇄 29
Context: Table 9. RACS-10*.
$$
\text{c/ccrit}
$$

### Eq. U334 — PDF 45 / 인쇄 29
Context: Table 9. RACS-10*.
$$
\text{c/ccrit ≥ 0.9}
$$

### Eq. U335 — PDF 45 / 인쇄 29
Context: Table 9. RACS-10*.
$$
\text{[c\_over\_ccrit] ≥ 0.9}
$$

### Eq. U336 — PDF 46 / 인쇄 30
Context: Table 10. Limits / Comments.
$$
\text{R\_o > 0}
$$

### Eq. U337 — PDF 46 / 인쇄 30
Context: Table 10. Limits / Comments.
$$
\text{0 < thick < R\_o}
$$

### Eq. U338 — PDF 46 / 인쇄 30
Context: Table 10. Limits / Comments.
$$
\text{0 < depth < thick}
$$

### Eq. U339 — PDF 46 / 인쇄 30
Context: Table 10. Limits / Comments.
$$
\text{axial\_c > 0}
$$

### Eq. U340 — PDF 46 / 인쇄 30
Context: Table 10. Limits / Comments.
$$
\text{sigy > 0}
$$

### Eq. U341 — PDF 46 / 인쇄 30
Context: Table 10. Limits / Comments.
$$
\text{sigu > 0}
$$

### Eq. U342 — PDF 46 / 인쇄 30
Context: Table 10. Limits / Comments.
$$
\text{RO\_alpha > 0}
$$

### Eq. U343 — PDF 46 / 인쇄 30
Context: Table 10. Limits / Comments.
$$
\text{RO\_sigo > 0}
$$

### Eq. U344 — PDF 46 / 인쇄 30
Context: Table 10. Limits / Comments.
$$
\text{RO\_epso > 0}
$$

### Eq. U345 — PDF 46 / 인쇄 30
Context: Table 10. Limits / Comments.
$$
\text{RO\_n > 1}
$$

### Eq. U346 — PDF 46 / 인쇄 30
Context: Table 10. Limits / Comments.
$$
\text{Resist\_Jic > 0}
$$

### Eq. U347 — PDF 46 / 인쇄 30
Context: Table 10. Limits / Comments.
$$
\text{Resist\_C > 0}
$$

### Eq. U348 — PDF 46 / 인쇄 30
Context: Table 10. Limits / Comments.
$$
\text{Resist\_m > 0}
$$

### Eq. U349 — PDF 46 / 인쇄 30
Context: Table 10. Limits / Comments.
$$
\text{pressure >= 0}
$$

### Eq. U350 — PDF 47 / 인쇄 31
Context: Table 11. Axial_TWC_fail.
$$
\text{0 or 1; 0, TWC does not fail; 1, TWC will fail under the applied pressure}
$$

### Eq. U351 — PDF 47 / 인쇄 31
Context: Table 11. Axial_TWC_ratio.
$$
c/c_{crit}
$$

### Eq. U352 — PDF 47 / 인쇄 31
Context: Table 11. Axial_SC_fail.
$$
\text{0 or 1; 0, SC does not fail; 1, SC will fail under the applied pressure}
$$

### Eq. U353 — PDF 47 / 인쇄 31
Context: Table 11. Axial_SC_ratio.
$$
p/p_{crit}
$$

### Eq. U354 — PDF 47 / 인쇄 31
Context: Table 11. i_err_code.
$$
\text{101 to 109}
$$

### Eq. U355 — PDF 47 / 인쇄 31
Context: Table 11. i_err_code.
$$
\text{101, pipe outer radius, [Ro] is less than 0}
$$

### Eq. U356 — PDF 47 / 인쇄 31
Context: Table 11. i_err_code.
$$
\text{102, 2x[thick], wall thickness exceeds pipe diameter}
$$

### Eq. U357 — PDF 47 / 인쇄 31
Context: Table 11. i_err_code.
$$
\text{103, crack length, c is less than 0.0 or greater than 100×R\_mean}
$$

### Eq. U358 — PDF 47 / 인쇄 31
Context: Table 11. i_err_code.
$$
\text{104, yield strength, [sigy] is less than 0, or ultimate strength [sigu] is less than 0, or [sigy]>=[sigu]}
$$

### Eq. U359 — PDF 47 / 인쇄 31
Context: Table 11. i_err_code.
$$
\text{105, one or more of Ramberg-Osgood parameters is/are less than 0}
$$

### Eq. U360 — PDF 47 / 인쇄 31
Context: Table 11. i_err_code.
$$
\text{106, one or more of material fracture resistance, J-R curve parameters is/are less than 0}
$$

### Eq. U361 — PDF 47 / 인쇄 31
Context: Table 11. i_err_code.
$$
\text{107, applied internal pressure, [pressure] is less than 0.0}
$$

### Eq. U362 — PDF 47 / 인쇄 31
Context: Table 11. i_err_code.
$$
\text{108, pipe wall thickness [thick] is less than 0}
$$

### Eq. U363 — PDF 47 / 인쇄 31
Context: Table 11. i_err_code.
$$
\text{109, Depth of surface crack, [depth] is less than 0}
$$

### Eq. U364 — PDF 47 / 인쇄 31
Context: Table 11. if_flag_twc.
$$
\text{-2 to 2}
$$

### Eq. U365 — PDF 47 / 인쇄 31
Context: Table 11. if_flag_twc.
$$
\text{0, Axial TWC does not fail}
$$

### Eq. U366 — PDF 47 / 인쇄 31
Context: Table 11. if_flag_twc.
$$
\text{1, Axial TWC fails under applied loads by limit load}
$$

### Eq. U367 — PDF 47 / 인쇄 31
Context: Table 11. if_flag_twc.
$$
\text{2, Axial TWC fails under applied loads by EPFM}
$$

### Eq. U368 — PDF 47 / 인쇄 31
Context: Table 11. if_flag_twc.
$$
\text{-1, no solution from limit load or EPFM and [i\_err\_code] = 204 is returned to framework}
$$

### Eq. U369 — PDF 47 / 인쇄 31
Context: Table 11. if_flag_twc.
$$
\text{-2, Input error has occurred and corresponding [i\_err\_code] in the range from 101 – 109 is returned to the xLPR Framework}
$$

### Eq. U370 — PDF 48 / 인쇄 32
Context: Table 11 (Cont). if_flag_sc.
$$
\text{-3 to 1}
$$

### Eq. U371 — PDF 48 / 인쇄 32
Context: Table 11 (Cont). if_flag_sc.
$$
\text{0, Axial SC does not fail}
$$

### Eq. U372 — PDF 48 / 인쇄 32
Context: Table 11 (Cont). if_flag_sc.
$$
\text{1, Axial SC fails under the applied loads}
$$

### Eq. U373 — PDF 48 / 인쇄 32
Context: Table 11 (Cont). if_flag_sc.
$$
\text{-1, not a surface crack, since [depth] ≥ [thick], and [i\_err\_code]=201 is returned to the xLPR Framework to set [i\_ctype] = 1}
$$

### Eq. U374 — PDF 48 / 인쇄 32
Context: Table 11 (Cont). if_flag_sc.
$$
\text{-2, Input error has occurred and corresponding [i\_err\_code] in the range from 101 – 109 is returned to the xLPR Framework}
$$

### Eq. U375 — PDF 48 / 인쇄 32
Context: Table 11 (Cont). if_flag_sc.
$$
\text{-3, loading and/or crack such that no solution found for the pressure, and [i\_err\_code] = 202 is returned to the xLPR Framework}
$$

### Eq. U376 — PDF 48 / 인쇄 32
Context: Table 11 (Cont). i_twc_ll.
$$
\text{-3 to 0}
$$

### Eq. U377 — PDF 48 / 인쇄 32
Context: Table 11 (Cont). i_twc_ll.
$$
\text{0, unqualified good solution, and [i\_err\_code] = 302 is returned to the xLPR Framework}
$$

### Eq. U378 — PDF 48 / 인쇄 32
Context: Table 11 (Cont). i_twc_ll.
$$
\text{-1, solution not attempted because of bad input data, and the corresponding [i\_err\_code] = 101 – 109 is returned to the xLPR Framework}
$$

### Eq. U379 — PDF 48 / 인쇄 32
Context: Table 11 (Cont). i_twc_ll.
$$
\text{-2, iteration limit of 5000 is exceeded, and [i\_err\_code] = 205 is returned to the xLPR Framework}
$$

### Eq. U380 — PDF 48 / 인쇄 32
Context: Table 11 (Cont). i_twc_ll.
$$
\text{-3, solution for the maximum crack length outside the range. [c\_max] is less than 0.0 or greater than 100xmean radius, R\_mean, and the [i\_err\_code] = 303 is returned to the xLPR Framework}
$$

### Eq. U381 — PDF 49 / 인쇄 33
Context: Table 11 (continued). i_twc_epfm.
$$
\text{-4 to 4}
$$

### Eq. U382 — PDF 49 / 인쇄 33
Context: Table 11 (continued). i_twc_epfm.
$$
\text{0, unqualified good solution, and the [i\_err\_code] = 304 is returned to the xLPR Framework. [i\_err\_code] = 309 is returned when one or more of the Rm/t, rho, n, is beyond the range for which influence coefficients (h1,F) are available [21]}
$$

### Eq. U383 — PDF 49 / 인쇄 33
Context: Table 11 (continued). i_twc_epfm.
$$
\text{1, good solution, but stress in ligament at maximum crack length, [c\_max] exceeds ultimate strength, [sigu], and [i\_err\_code] = 305 is returned to xLPR Framework}
$$

### Eq. U384 — PDF 49 / 인쇄 33
Context: Table 11 (continued). i_twc_epfm.
$$
\text{2, solution found, but iteration limit exceeded and [c\_max] solution is minimum of error of J and dJ/da equations, and [i\_err\_code] = 306 is returned to xLPR Framework}
$$

### Eq. U385 — PDF 49 / 인쇄 33
Context: Table 11 (continued). i_twc_epfm.
$$
\text{3, Numerical solution method iteration limit exceeded and stress is high, then [c\_max] = 0.0 is assumed, and [i\_err\_code] = 307 is returned to xLPR Framework}
$$

### Eq. U386 — PDF 49 / 인쇄 33
Context: Table 11 (continued). i_twc_epfm.
$$
\text{4, Numerical solution method’s iteration limit exceeded and stress is low, [c\_max] = 100x R\_mean, mean radius is assumed, and [i\_err\_code] = 308 is returned to xLPR Framework}
$$

### Eq. U387 — PDF 49 / 인쇄 33
Context: Table 11 (continued). i_twc_epfm.
$$
\text{-1, solution not attempted due to faulty input data, and the corresponding [i\_err\_code] in the range from 101 – 108 is returned to xLPR Framework}
$$

### Eq. U388 — PDF 49 / 인쇄 33
Context: Table 11 (continued). i_twc_epfm.
$$
\text{-2, initial crack size starting guess could not be found in 5000 iterations, , and [i\_err\_code] = 206 is returned to xLPR Framework}
$$

### Eq. U389 — PDF 49 / 인쇄 33
Context: Table 11 (continued). i_twc_epfm.
$$
\text{-3, initial crack size starting estimate not within the bounds of 0.0 and 100xmean radius, R\_mean, and [i\_err\_code] = 207 is returned to xLPR Framework}
$$

### Eq. U390 — PDF 49 / 인쇄 33
Context: Table 11 (continued). i_twc_epfm.
$$
\text{-4, numerical solution iteration limit exceeded and could not find solution for minimum error of J and dJ/da equations, , and [i\_err\_code] = 310 is returned to xLPR Framework}
$$

### Eq. U391 — PDF 50 / 인쇄 34
Context: Table 11 (continued). i_sc_pc.
$$
\text{-2 to 0}
$$

### Eq. U392 — PDF 50 / 인쇄 34
Context: Table 11 (continued). i_sc_pc.
$$
\text{0, unqualified good solution, and the [i\_err\_code] = 301 is returned to xLPR Framework}
$$

### Eq. U393 — PDF 50 / 인쇄 34
Context: Table 11 (continued). i_sc_pc.
$$
\text{-1, solution not attempted because of bad input data, and the corresponding [i\_err\_code] = 101 – 109 is returned to xLPR Framework}
$$

### Eq. U394 — PDF 50 / 인쇄 34
Context: Table 11 (continued). i_sc_pc.
$$
\text{-2, solution for the maximum pressure, [p\_max] outside the range. [p\_max] is less than 0.0 or greater than 1000xapplied pressure, [pressure], and [i\_err\_code] = 203 is returned to xLPR Framework}
$$

### Eq. U395 — PDF 50 / 인쇄 34
Context: Table 12. Error 103.
$$
\text{Axial half-crack length is less than 0 or greater than 100×Rm}
$$

### Eq. U396 — PDF 51 / 인쇄 35
Context: Table 12 (continued). Error 203.
$$
\text{[0, 1000×applied pressure]}
$$

### Eq. U397 — PDF 51 / 인쇄 35
Context: Table 12 (continued). Error 207.
$$
\text{[0, 100×Rm]}
$$

### Eq. U398 — PDF 51 / 인쇄 35
Context: Table 12 (continued). Error 303.
$$
\text{[0,100×Rm]}
$$

### Eq. U399 — PDF 51 / 인쇄 35
Context: Table 12 (continued). Error 307.
$$
\text{c\_max = 0}
$$

### Eq. U400 — PDF 51 / 인쇄 35
Context: Table 12 (continued). Error 308.
$$
\text{c\_max = 100×Rm}
$$

### Eq. U401 — PDF 53 / 인쇄 37
Context: Derived consistent units (plain baseline numerals in original).
$$
\text{Stress: N/mm2 = MPa}
$$

### Eq. U402 — PDF 53 / 인쇄 37
Context: Derived consistent units (plain baseline numerals in original).
$$
\text{Pressure: N/mm2 = MPa}
$$

### Eq. U403 — PDF 53 / 인쇄 37
Context: Derived consistent units (plain baseline numerals in original).
$$
\text{Initiation toughness (Jic): N/mm = kJ/m2}
$$

### Eq. U404 — PDF 53 / 인쇄 37
Context: Derived consistent units (plain baseline numerals in original).
$$
\text{Fracture resistance constant (C): N/mm(m+1)}
$$

### Eq. U405 — PDF 53 / 인쇄 37
Context: Pressure margin to rupture.
$$
p/p_{crit}
$$

### Eq. U406 — PDF 53 / 인쇄 37
Context: Crack size margin.
$$
c/c_{crit}
$$

### Eq. U407 — PDF 56 / 인쇄 40
Context: Iteratively calculate the ratio.
$$
\theta/\theta_{max}
$$

### Eq. U408 — PDF 56 / 인쇄 40
Context: The Excel spreadsheet calculates the difference between the applied J and the material J.
$$
\text{J\_applied - J\_material}
$$

### Eq. U409 — PDF 56 / 인쇄 40
Context: The difference in the dJ/da values.
$$
\text{dJ/da\_applied - dJ/da\_material}
$$

### Eq. U410 — PDF 56 / 인쇄 40
Context: Test cases for which the TWC will fail under the applied loads.
$$
\text{if\_flag = 1}
$$

### Eq. U411 — PDF 56 / 인쇄 40
Context: The failure was predicted to be governed by the ENG2 method.
$$
\text{i\_err\_code = 303 or 307}
$$

### Eq. U412 — PDF 58 / 인쇄 42
Context: Predicted failure, yes or no.
$$
\text{if\_flag = 1}
$$

### Eq. U413 — PDF 58 / 인쇄 42
Context: Predicted failure, yes or no.
$$
\text{if\_flag = 0}
$$

### Eq. U414 — PDF 59 / 인쇄 43
Context: Crack discretization step size, mm (always set to).
$$
\text{π*OD/10000}
$$

### Eq. U415 — PDF 60 / 인쇄 44
Context: All of the single crack cases.
$$
\text{BM ratio > 1.523 or BM ratio < 0.451}
$$

### Eq. U416 — PDF 65 / 인쇄 49
Context: Surface crack depth to wall thickness ratio.
$$
\text{(a/t): 0.74}
$$

### Eq. U417 — PDF 65 / 인쇄 49
Context: Crack length.
$$
\text{π/6 radians}
$$

### Eq. U418 — PDF 66 / 인쇄 50
Context: Table 15. First column header.
$$
\text{α/π}
$$

### Eq. U419 — PDF 66 / 인쇄 50
Context: Table 15. Last column header.
$$
\text{BM Experiment / BM SC\_fail Critical (BM ratio)}
$$

### Eq. U420 — PDF 69 / 인쇄 53
Context: Figure 8. Horizontal axis.
$$
\text{Crack Length/Pipe Circumference}
$$

### Eq. U421 — PDF 69 / 인쇄 53
Context: Figure 8. Vertical axis.
$$
\text{Nominal Axial Tension Stress/Flow Stress}
$$

### Eq. U422 — PDF 72 / 인쇄 56
Context: A plot of all of the data from Table 17.
$$
\theta/\theta_{crit}
$$

### Eq. U423 — PDF 72 / 인쇄 56
Context: Variation from using different kinds of fracture toughness specimen geometries.
$$
\theta/\theta_{crit}
$$

### Eq. U424 — PDF 72 / 인쇄 56
Context: Severely non-conservative prediction (original prose condition).
$$
\theta/\theta_{crit}\ \text{much less than }1.0
$$

### Eq. U425 — PDF 72 / 인쇄 56
Context: Confidence interval testing.
$$
\theta/\theta_{crit}
$$

### Eq. U426 — PDF 75 / 인쇄 59
Context: Table 18. Last column header.
$$
\text{2c\_max moment / 2c\_initiation}
$$

### Eq. U427 — PDF 78 / 인쇄 62
Context: Figure 10. Horizontal axis.
$$
\text{2c\_Maximum Moment / 2c\_Initiation}
$$

### Eq. U428 — PDF 79 / 인쇄 63
Context: Figure 12. Axis and caption.
$$
\text{θ/θcrit}
$$

### Eq. U429 — PDF 80 / 인쇄 64
Context: Conservatively predict failure.
$$
P_{Expt}/P_{Crit}>1
$$

### Eq. U430 — PDF 80 / 인쇄 64
Context: The average value of ratio of the experimental pressure to the predicted critical pressure.
$$
P_{Expt}/P_{Crit}
$$

### Eq. U431 — PDF 80 / 인쇄 64
Context: Table 21. Last column header.
$$
P_{Expt}/P_{Crit}
$$

### Eq. U432 — PDF 81 / 인쇄 65
Context: Table 22. Last column header.
$$
c_{Expt}/c_{Crit}
$$

### Eq. U433 — PDF 81 / 인쇄 65
Context: For most of the cases shown in Table 22.
$$
c_{Expt}/c_{Crit}
$$

### Eq. U434 — PDF 82 / 인쇄 66
Context: Ratio of the experimental crack length to the predicted critical crack length.
$$
c_{expt}/c_{crit}
$$

### Eq. U435 — PDF 82 / 인쇄 66
Context: J-R curve equation (원문의 m은 baseline).
$$
\mathrm J=\mathrm{Ji}+\mathrm C(\square\mathrm a)\mathrm m
$$
원문 그대로: Δ에 해당할 것으로 추정되는 자리는 실제 PDF에서 빈 사각형(□) 하나로 보이며, 이를 추정 복원하지 않았다.

### Eq. U436 — PDF 83 / 인쇄 67
Context: By assuming.
$$
\text{m=1}
$$

### Eq. U437 — PDF 83 / 인쇄 67
Context: The larger of the two ratios.
$$
c_{Expt}/c_{Crit}
$$

### Eq. U438 — PDF 84 / 인쇄 68
Context: Table 24. Header.
$$
c_{Expt}/c_{Crit}
$$

### Eq. U439 — PDF 84 / 인쇄 68
Context: Table 24. Footnote (1).
$$
c/c_{crit}
$$

### Eq. U440 — PDF 84 / 인쇄 68
Context: There may be additional cases of larger diameter, lower toughness pipes.
$$
\mathrm{DPZP}\ \text{is less than }0.1
$$

### Eq. U441 — PDF 85 / 인쇄 69
Context: where,
$$
E=\text{elastic modulus}
$$

### Eq. U442 — PDF 85 / 인쇄 69
Context: where,
$$
J_i=\text{initiation toughness}
$$

### Eq. U443 — PDF 85 / 인쇄 69
Context: where,
$$
D_m=\text{mean pipe diameter}
$$

### Eq. U444 — PDF 85 / 인쇄 69
Context: where,
$$
\sigma_f=\text{flow stress.}
$$

### Eq. U445 — PDF 86 / 인쇄 70
Context: Figure 13. Best Fit for Surface Crack Data.
$$
C_1=34
$$

### Eq. U446 — PDF 86 / 인쇄 70
Context: Figure 13. Best Fit for TWC Data.
$$
C_1=18.3
$$

### Eq. U447 — PDF 92 / 인쇄 76
Context: Table 25. Normalized crack size.
$$
\lambda=\mathrm{c}/(\mathrm{R_m}\mathrm t)^{0.5}
$$

### Eq. U448 — PDF 92 / 인쇄 76
Context: Table 25. Design space for parametric parameters are:
$$
\text{0.05 ≤ λ ≤ 3}
$$

### Eq. U449 — PDF 92 / 인쇄 76
Context: Table 25. Design space for parametric parameters are:
$$
\text{5 ≤ Rm/t ≤ 20}
$$

### Eq. U450 — PDF 92 / 인쇄 76
Context: Table 25. Design space for parametric parameters are:
$$
\text{1 ≤ n ≤ 7}
$$

### Eq. U451 — PDF 92 / 인쇄 76
Context: Table 25. Some practical applications require.
$$
\text{n>7}
$$

### Eq. U452 — PDF 92 / 인쇄 76
Context: Table 25. Discrete values used in FEA for determining influence functions were:
$$
\text{Rm/t: 5 and 20}
$$

### Eq. U453 — PDF 92 / 인쇄 76
Context: Table 25. Discrete values used in FEA for determining influence functions were:
$$
\text{λ: 0.05, 1, 2, and 3}
$$

### Eq. U454 — PDF 92 / 인쇄 76
Context: Table 25. Discrete values used in FEA for determining influence functions were:
$$
\text{n: 1, 3, and 7}
$$

### Eq. U455 — PDF 97 / 인쇄 81
Context: Overall, the average value for these 17 experiments.
$$
P_{Expt}/P_{Pred}
$$

### Eq. U456 — PDF 97 / 인쇄 81
Context: The average value was greater than 1.0.
$$
P_{Expt}/P_{Pred}
$$

### Eq. U457 — PDF 97 / 인쇄 81
Context: The experimental crack size to the critical crack size.
$$
c_{Expt}/c_{Crit}
$$

## 전사 범위 및 계수

PDF 1~101쪽 전체 이미지 확인. 번호식은 1~63을 각 1회 전사했다. U001~U457은 번호가 없는 식, 기호의 원문 정의, 조건, 비율식의 출현 위치별 전사이다. 기호 목록의 등호 없는 두 열 정의 94개도 포함했으며 원문에 없는 등호를 보충하지 않았다. 코드 상태나 표의 한 행에 함께 인쇄된 조건은 해당 블록 하나로 센다. 동일 식의 다른 위치 반복은 각각 센다. 수치만 있는 데이터 셀, 단독 기호 인용, 참고문헌 서지사항은 식 개수에 포함하지 않았다.

번호식 63개, 번호 없는 식 457개 전사
