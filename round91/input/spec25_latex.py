# -*- coding: utf-8 -*-
# Eqn. 1~25 슬라이드 내용. 수식·제목은 HTML(XLPR_누설률_B047.html) 카드에서, 기호 정의 영문은 원문 where 목록/본문에서.
# $...$ = 인라인 수식. 단위 [..] 는 쓰지 않음(사용자 요청).
S = []
def add(id, title, bullets, tex, rows, pm, eqsz=1600, tsz=1200):
    S.append(dict(id=id, title=title, bullets=bullets, tex=tex, rows=rows, pm=pm, eqsz=eqsz, tsz=tsz))

add('1', r'질량 유속 식 $\psi(G_c^{2},p_c)=0$',
    ['1차원 운동량 보존 법칙과 질량 보존 법칙에 근거하여 균열 출구 (throat)의 질량 유속을 계산하는 식임',
     '균열 출구에서의 질량 유속과 압력은 연립 비선형 방정식의 미지수임'],
    r'\psi\left(G_c^{2},p_c\right)=G_c^{2}-\frac{1}{\left[\left(\dfrac{x_c v_{g(c)}}{\gamma_0 p_c}\right)-\left(v_{fg(c)}N\dfrac{dx_E}{dp_c}\right)\right]_c}=0',
    [('G_c', 'Mass flux at crack exit plane (aka throat or choking plane)'),
     ('p_c', 'Absolute pressure at the throat'),
     ('x_c', 'Non-equilibrium vapor quality at throat'),
     ('v_{g(c)}', 'Specific volume of saturated vapor at throat'),
     (r'\gamma_0', 'Isentropic expansion coefficient for wet or superheated vapor'),
     ('N', 'Empirical parameter'),
     ('v_{fg(c)}', 'Specific volume change due to vaporization evaluated at the throat'),
     ('x_E', 'Equilibrium vapor quality at the throat'),
     (r'\dfrac{dx_E}{dp_c}', 'First derivative of equilibrium vapor quality with respect to pressure at the throat')], 'p.17')

add('2', r'질량 유량으로부터 체적 유량 $Q$',
    ['질량 유량과 체적 유량을 모두 출력하도록 한 요구사항 SR-LRM-006에 따라, 체적 유량을 질량 유량으로부터 계산하는 식임'],
    r'Q=\dot{m}\,v_{std}',
    [('Q', 'Volumetric flow rate'), (r'\dot{m}', 'Mass flow rate'),
     ('v_{std}', 'The specific volume that satisfies the definition of the Leakage Rate')], 'p.17')

add('3', r'압력 강하 구속 식 $\Omega(G_c^{2},p_c)=0$',
    ['Eqn. 1의 해를 구속하는 힘 평형 (force balance) 식임',
     '유로를 따른 전체 압력 강하를 다섯 가지 기여 메커니즘으로 나눔'],
    r'\Omega\left(G_c^{2},p_c\right)=\left(p_0-p_c\right)-\Delta p_e-\Delta p_a-\Delta p_f-\Delta p_k-\Delta p_{aa}=0',
    [('p_0', 'Absolute stagnation pressure of the subcooled liquid at the crack entrance of the pipe'),
     ('p_c', 'Absolute pressure at the crack exit'),
     (r'\Delta p_e', 'Pressure loss due to entrance effects'),
     (r'\Delta p_a', 'Pressure loss due to acceleration by vaporization'),
     (r'\Delta p_f', 'Pressure loss due to frictional effects'),
     (r'\Delta p_k', 'Pressure loss due to tortuosity of flow path'),
     (r'\Delta p_{aa}', 'Pressure loss due to acceleration by changing flow area')], 'p.18')

add('4', r'입구 압력 손실 $\Delta p_e$',
    [r'입구 효과로 인한 압력 손실 $\Delta p_e$를 계산하는 식임'],
    r'\Delta p_e=\frac{G_c^{2}v_{l(0)}}{2C_D^{2}}\left(\frac{A_c^{2}}{A_0^{2}}\right)',
    [('G_c', 'Mass flux at the crack exit plane (aka choking or throat plane)'),
     ('v_{l(0)}', 'Specific volume of subcooled liquid at crack entrance plane'),
     ('C_D', r'Discharge coefficient $0.60\le C_D\le 0.95$'),
     ('A_0', 'Flow area at crack entrance plane'),
     ('A_c', 'Flow area at the throat')], 'p.18')

add('5', r'증발에 의한 가속 압력 손실 $\Delta p_a$',
    [r'증발에 의한 가속 (phasic acceleration)으로 인한 압력 손실 $\Delta p_a$를 계산하는 식임'],
    r'\Delta p_a=G_c^{2}\left(\frac{A_c}{A_i}\right)\left(\frac{A_c}{A_0}\right)\left[\left(1-x_{c(h)}\right)v_{f(c)}+x_{c(h)}v_{g(c)}-v_{l(0)}\right]',
    [('A_c', 'Flow area at the crack exit plane (at z = L)'),
     ('A_0', 'Flow area at the crack entrance plane (at z = 0)'),
     ('A_i', r'Flow area where vapor generation begins (at $12D_h$)'),
     ('v_{l(0)}', 'Specific volume of subcooled liquid at crack entrance plane'),
     ('v_{f(c)}', 'Specific volume of saturated liquid at throat'),
     ('v_{g(c)}', 'Specific volume of saturated vapor at throat'),
     ('x_{c(h)}', 'Isenthalpic equilibrium vapor quality at the crack exit plane')], 'p.19')

add('6', r'유로 단면적의 선형 변화 $A(z)$',
    ['유로를 따른 단면 유로 면적이 선형으로 변한다고 가정한 식임'],
    r'A(z)=A_0+\left(\frac{z}{L}\right)\left(A_c-A_0\right)',
    [('z', 'Distance along flow path from the crack entrance'),
     ('L', 'Total length of the flow path'),
     ('A_0', 'Flow area at crack entrance plane (at z = 0)'),
     ('A_c', 'Flow area at the crack exit plane (at z = L)')], 'p.19')

add('7', r'$z=12D_h$에서의 유로 면적 $A_i$',
    [r'Eqn. 6에서 $z=12D_h$로 두어 $A_i$를 구하는 식임'],
    r'A_i=A_0+\left(\frac{12D_h}{L}\right)\left(A_c-A_0\right)',
    [('A_i', r'Flow area where vapor generation begins (at $12D_h$)'),
     ('D_h', 'Hydraulic diameter of the crack entrance flow area (Equation 8)'),
     ('L', 'Total length of the flow path'),
     ('A_0', 'Flow area at crack entrance plane (at z = 0)'),
     ('A_c', 'Flow area at the crack exit plane (at z = L)')], 'p.19')

add('8', r'수력직경 $D_h$',
    [r'균열 입구 유로 면적의 수력직경 (hydraulic diameter) $D_h$를 정의하는 식임'],
    r'D_h=\frac{4A_0}{P_w}',
    [('D_h', 'Hydraulic diameter of the crack entrance flow area'),
     ('A_0', 'Flow area at crack entrance plane'),
     ('P_w', 'Wetted perimeter of the flow area')], 'p.19')

add('9', r'마찰 압력 손실 $\Delta p_f$ ($L/D_h\ge 12$)',
    [r'마찰 효과로 인한 압력 손실 $\Delta p_f$를 계산하는 식임 ($D_h$는 출구면에서 구한 수력직경)'],
    r'\Delta p_f=\frac{G_c^{2}}{2}\left\{12f\left(\frac{A_c^{2}}{A_iA_0}\right)v_{l(0)}+f\left(\frac{L}{D_h}-12\right)\left(\frac{A_c}{A_i}\right)\left[\bar v_f+\bar x_{(h)}\bar v_{fg}\right]\right\}',
    [('G_c^{2}', 'Mass flux at the crack exit plane'),
     ('f', 'Darcy friction factor (see Equation 11)'),
     ('A_c', 'Flow area at the crack exit plane'),
     ('A_i', 'Flow area where vapor generation begins'),
     ('A_o', 'Flow area at the crack entrance plane'),
     ('v_{l(0)}', 'Specific volume of subcooled liquid at the crack entrance plane'),
     ('L', 'Total flow path length'),
     ('D_h', 'Hydraulic diameter (see Equation 8)'),
     (r'\bar v_f', 'Saturated liquid specific volume at average pressure'),
     (r'\bar x_{(h)}', 'Isenthalpic vapor quality at average pressure'),
     (r'\bar v_{fg}', 'Change in specific volume by vaporization at average pressure')], 'p.20', eqsz=1400, tsz=1100)

add('10', r'마찰 압력 손실 $\Delta p_f$ ($L/D_h<12$)',
    [r'$L/D_h<12$일 때의 마찰 압력 손실 $\Delta p_f$를 계산하는 식임'],
    r'\Delta p_f=\frac{G_c^{2}}{2}\left\{12f\left(\frac{A_c^{2}}{A_iA_0}\right)v_{l(0)}\right\}',
    [('G_c^{2}', 'Mass flux at the crack exit plane'),
     ('f', 'Darcy friction factor (see Equation 11)'),
     ('A_c', 'Flow area at the crack exit plane'),
     ('A_i', 'Flow area where vapor generation begins'),
     ('A_0', 'Flow area at the crack entrance plane'),
     ('v_{l(0)}', 'Specific volume of subcooled liquid at the crack entrance plane')], 'p.20')

add('11', r'Darcy 마찰 계수 $f$',
    [r'Darcy 마찰 계수 (friction factor) $f$를 계산하는 식임'],
    r'f=\left[C_1\log_{10}\left(\frac{D_h}{\mu}\right)+C_2\right]^{-2}',
    [('f', 'Darcy friction factor (see also Figure 2)'),
     (r'C_1,\ C_2', 'C coefficients (defined below Equation 12)'),
     ('D_h', 'The hydraulic diameter ratio by Equation 19'),
     (r'\mu', 'The effective surface roughness defined by Equation 15')], 'p.20')

add('12', r'$D_h/\mu$의 하한',
    ['수력직경 대 유효 표면 거칠기의 비를 제한하는 식임'],
    r'\frac{D_h}{\mu}=MAX\left(\frac{D_h}{\mu},\,3.65\right)',
    [(r'D_h/\mu', 'The hydraulic diameter to effective surface roughness'),
     (r'\mu', 'The effective surface roughness defined by Equation 15')], 'p.20')

add('13', r'유로 tortuosity 압력 손실 $\Delta p_k$',
    [r'균열면 표면 morphology의 영향을 받는 유로 tortuosity 압력 손실 $\Delta p_k$를 계산하는 식임'],
    r'\Delta p_k=e_{vloss}\frac{G_c^{2}}{2}\left(\frac{A_c}{A_i}\right)\left[\left(1-\bar{x}_{(h)}\right)\bar{v}_f+\bar{x}_{(h)}\bar{v}_g\right]',
    [('e_{vloss}', 'Velocity head loss (expression defined by Equation 14)'),
     ('G_c', 'Mass flux at the crack exit plane'),
     ('A_c', 'Flow area at the crack exit plane'),
     ('A_i', 'Flow area where vapor generation begins'),
     (r'\bar x_{(h)}', 'Isenthalpic vapor quality at average pressure'),
     (r'\bar v_f', 'Saturated liquid specific volume at average pressure'),
     (r'\bar v_g', r'Specific volume of saturated vapor by vaporization at the average pressure, $p_{avg}$')], 'p.21')

add('14', r'속도수두 손실 $e_{vloss}$',
    [r'Eqn. 13의 $e_{vloss}$에 대한 식을 정의함'],
    r'e_{vloss}=\eta_t\left(\frac{L_{eff}}{L}\right)L=\eta_t\,L_{eff}',
    [('e_{vloss}', 'Velocity head loss'),
     (r'\eta_t', 'Effective number of turns per unit length'),
     ('L_{eff}', 'Adjusted flow path length'),
     ('L', 'Total length of the flow path')], 'p.21')

add('15', r'유효 표면 거칠기 $\mu$',
    [r'Darcy 마찰 계수 $f$에 필요한 유효 표면 거칠기 $\mu$를 균열 열림 변위 $\delta_{COD}$의 함수로 정의하는 식임'],
    r'\mu=\begin{cases}\mu_L & \text{for } 0<\dfrac{\delta_{COD}}{\mu_G}\le 0.1\\ \mu_L+\dfrac{\left(\mu_G-\mu_L\right)}{9.9}\left[\dfrac{\delta_{COD}}{\mu_G}-0.1\right] & \text{for } 0.1\le\dfrac{\delta_{COD}}{\mu_G}<10\\ \mu_G & \text{for } \dfrac{\delta_{COD}}{\mu_G}\ge 10\end{cases}',
    [(r'\mu', 'Effective surface roughness'), (r'\mu_L', 'Local surface roughness'),
     (r'\mu_G', 'Global surface roughness'), (r'\delta_{COD}', 'Crack-opening displacement')], 'p.22')

add('16', r'단위 길이당 유효 굽이 수 $\eta_t$',
    [r'단위 길이당 유효 굽이 수 $\eta_t$도 균열 열림 변위 $\delta_{COD}$의 함수임'],
    r'\eta_t=\begin{cases}\eta_{tL} & \text{for } 0<\dfrac{\delta_{COD}}{\mu_G}\le 0.1\\ \eta_{tL}-\dfrac{\left(\eta_{tL}\right)}{11}\left[\dfrac{\delta_{COD}}{\mu_G}-0.1\right] & \text{for } 0.1\le\dfrac{\delta_{COD}}{\mu_G}<10\\ 0.1\,\eta_{tL} & \text{for } \dfrac{\delta_{COD}}{\mu_G}\ge 10\end{cases}',
    [(r'\eta_t', 'Effective number of turns per unit length'), (r'\eta_{tL}', 'Local number of turns in the flow path'),
     (r'\delta_{COD}', 'Crack-opening displacement'), (r'\mu_G', 'Global surface roughness')], 'p.22')

add('17', r'조정 유로 길이 대 벽 두께 비 $L_{eff}/L$',
    [r'조정된 유로 길이 $L_{eff}$ 대 배관 벽 두께 $L$의 비를 $\delta_{COD}/\mu_G$의 함수로 정의하는 식임'],
    r'\frac{L_{eff}}{L}=\begin{cases}K_{G+L} & \text{for } 0<\dfrac{\delta_{COD}}{\mu_G}\le 0.1\\ K_{G+L}-\dfrac{\left(K_{G+L}-K_G\right)}{9.9}\left[\dfrac{\delta_{COD}}{\mu_G}-0.1\right] & \text{for } 0.1\le\dfrac{\delta_{COD}}{\mu_G}<10\\ K_G & \text{for } \dfrac{\delta_{COD}}{\mu_G}\ge 10\end{cases}',
    [('L_{eff}', 'Adjusted flow path length'), ('L', 'Pipe wall thickness'),
     ('K_G', 'Global factor for flow path deviation from straight'),
     ('K_{G+L}', 'Local factor for flow path deviation from straight'),
     (r'\delta_{COD}', 'Crack-opening displacement'), (r'\mu_G', 'Global surface roughness')], 'p.22', eqsz=1400)

add('18', r'유로 면적 변화에 의한 가속 압력 손실 $\Delta p_{aa}$',
    [r'유로 면적 변화에 의한 가속으로 인한 압력 손실 $\Delta p_{aa}$를 계산하는 식임'],
    r'\Delta p_{aa}=\frac{G_c^{2}v_{l(0)}}{2}\left[\left(\frac{A_c}{A_i}\right)^{2}-\left(\frac{A_c}{A_0}\right)^{2}\right]+\frac{G_c^{2}}{2}\left[\left(1-\bar{x}_{(h)}\right)\bar{v}_f+\bar{x}_{(h)}\bar{v}_g\right]\left[1-\left(\frac{A_c}{A_i}\right)^{2}\right]',
    [('A_0', 'Flow area at crack entrance plane (at z = 0)'),
     ('A_c', 'Flow area at the crack exit plane (at z = L)'),
     ('A_i', r'Flow area at $z=12D_h$'),
     (r'\bar v_f', r'Specific volume of saturated liquid at average pressure, $p_{avg}$'),
     (r'\bar v_g', r'Specific volume of saturated vapor by vaporization at the average pressure, $p_{avg}$'),
     ('p_{avg}', r'$(p_0-\Delta p_e+p_c)/2$')], 'p.23', eqsz=1300)

add('19', r'수력직경 $D_h$ (단면 평균 유로 면적 기준)',
    [r'각 단면 형상에 대해 균열 채널의 수력직경 $D_h$를 계산하는 식임'],
    r'D_h=\frac{4A_{xmf}}{P_w}',
    [('D_h', 'Hydraulic diameter of the crack channel'),
     ('A_{xmf}', 'Cross-sectional mean flow area'),
     ('P_w', 'Wetted perimeter')], 'p.23')

add('20', r'타원 단면의 젖은 둘레 $P_w$',
    [r'타원 단면에 대한 젖은 둘레 (wetted perimeter) $P_w$를 정하는 식임',
     '원문은 직사각형과 마름모의 계산은 간단하지만 타원은 훨씬 복잡하다고 적음'],
    r'\begin{aligned}P_w&=4\,a\,E(e)\\ E(e)&=\text{complete elliptic integral of the second kind}\\ e&=\frac{\sqrt{a^{2}-b^{2}}}{a}=\text{eccentricity of the ellipse}\end{aligned}',
    [('P_w', 'Wetted perimeter'), ('a', 'Semi-major axis of the ellipse'), ('b', 'Semi-minor axis of the ellipse'),
     ('E(e)', 'Complete elliptic integral of the second kind'), ('e', 'Eccentricity of the ellipse')], 'p.23')

add('21', r'orifice 유동의 체적 유량 $Q$ (Regime 4)',
    ['Regime 4에서 넓은 균열을 얇은 square-edged orifice로 보고, 과냉각 액체를 비압축성으로 가정함',
     'LEAPOR에 구현된 orifice flow 유량 추정식임'],
    r'Q=\frac{C_D A_0\sqrt{2\,\Delta p\,v_{l(0)}}}{\sqrt{1-\beta^{4}}}',
    [('Q', 'Volumetric flow rate'), ('C_D', r'Discharge coefficient, using $C_D=0.6$'),
     ('A_0', 'Flow area at crack entrance plane'), (r'\Delta p', 'The required pressure loss (Equation 22)'),
     ('v_{l(0)}', 'Specific volume of subcooled liquid at crack entrance plane'),
     (r'\beta', r'Using $\beta=0.62$')], 'p.28')

add('22', r'Regime 4의 압력 손실 $\Delta p$',
    [r'$p_c/p_0$가 $L_{eff}/D_h=4.6$에서 0.552로 고정된다고 보고, $L_{eff}/D_h$에 선형 의존한다고 가정하여 필요한 압력 손실을 구하는 식임'],
    r'p_0-p_c=\Delta p=p_0\left[1-\left(\frac{0.552}{4.6}\right)\left(\frac{L_{eff}}{D_h}\right)\right];\ \text{for}\ \frac{L_{eff}}{D_h}\le 4.6',
    [('p_0', 'Absolute stagnation pressure of the subcooled liquid at the crack entrance of the pipe'),
     ('p_c', 'Absolute pressure at the crack exit'),
     (r'\Delta p', 'The required pressure loss'),
     ('p_c/p_0', r'Critical pressure ratio, fixed at 0.552 at $L_{eff}/D_h=4.6$'),
     ('L_{eff}', 'Adjusted flow path length'), ('D_h', 'Hydraulic diameter')], 'p.28')

add('23', r'균열 입구에서의 질량 유속 $G_0$ (orifice flow)',
    ['Eqn. 22를 Eqn. 21에 적용하여 균열 입구에서의 질량 유속을 구하는 식임'],
    r'G_0=\frac{Q}{v_{l(0)}A_0}=\frac{C_D\sqrt{2\Delta p\,v_{l(0)}}}{v_{l(0)}\sqrt{1-\beta^{4}}}',
    [('G_0', 'Mass flux at the entrance to the crack'), ('Q', 'Volumetric flow rate (Equation 21)'),
     ('v_{l(0)}', 'Specific volume of the subcooled liquid at the crack entrance'),
     ('A_0', 'Flow area at crack entrance plane'), ('C_D', r'Discharge coefficient, using $C_D=0.6$'),
     (r'\Delta p', 'The required pressure loss (Equation 22)'), (r'\beta', r'Using $\beta=0.62$')], 'p.28')

add('24', r'280°C에서 COV와 평균 누설률 $\lambda$',
    ['Figure 10의 결과에 근거하여, 평균 누설률 λ에 대한 선형 공간의 표준편차를 280°C 식(Eqn. 24)과 340°C 식(Eqn. 25) 사이에서 보간함'],
    r'COV=0.0175\,\lambda+0.0965',
    [('COV', 'Coefficient of variation, the ratio of the standard deviation of the leak rate to the mean leak rate'),
     (r'\lambda', 'Mean leak rate')], 'p.34')

add('25', r'340°C에서 COV와 평균 누설률 $\lambda$',
    ['340°C에서의 COV와 평균 누설률의 관계식이며, Eqn. 24와 함께 보간에 씀'],
    r'COV=0.0228\,\lambda+0.1186',
    [('COV', 'Coefficient of variation, the ratio of the standard deviation of the leak rate to the mean leak rate'),
     (r'\lambda', 'Mean leak rate')], 'p.34')
