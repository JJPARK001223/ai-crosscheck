# round57 Codex blind 전사 — B048

대상: (ML16341B048)Cyclic stress intensity factors.pdf, 37쪽. 본문 인쇄쪽 = PDF쪽 − 10. 기호표는 PDF 9쪽/인쇄 viii, 약어표는 PDF 10쪽/인쇄 ix.

전사 범위: 이 파일은 지정된 blind 단계의 원문 전사다. 다른 AI의 결과와 이전 라운드는 열람하지 않았다. 식과 Figure 1~3은 160dpi 렌더링으로 직접 판독했다. Eqn. 2는 320dpi 렌더링으로 추가 확인했다. 영어 인용은 원문의 철자와 표기를 유지한다. 줄바꿈과 수식의 공백은 조판상 정리했다. 원문 자체 이상은 마지막에 따로 기록한다.

## 1. 식 전사와 원문 정의

### Eqn. 1 — PDF 17쪽 / 인쇄 7쪽

$$
\rho c_{sp}\frac{\partial T}{\partial t}
=\frac{1}{r}\frac{\partial}{\partial r}\left(kr\frac{\partial T}{\partial r}\right)
$$

> “The following is the governing partial differential equation for the conduction of heat in the pipe wall under the idealized conditions mentioned above.” (p.7)

> “The temperature field is therefore a function of radial coordinate and time only, T(r, t).” (p.7)

> “In the general case, the material properties k, csp and ρ (thermal conductivity, specific heat and density) can be functions of temperature.” (p.7)

기호표(p.viii): r — “Radial coordinate”; t — “Time”; T — “Temperature”; csp — “Specific heat”; ρ — “Density”. k는 위 본문에서 직접 정의한다. ∂ 연산자 자체에 대한 원문 정의 없음.

### Eqn. 2 — PDF 18쪽 / 인쇄 8쪽

$$
\frac{\delta^{2}h^{2}\rho c_{sp}}{\Delta t}(T_j-T^{*}_{j})
=\frac{1}{r_j}\Bigl[
T_{j+1}(k_{j+1}r_{j+1}+k_jr_j)
-T_j(k_{j+1}r_{j+1}+2k_jr_j+k_{j-1}r_{j-1})
+T_{j-1}\bigl(k_jr_j+k_{j-1}r_{j-1}\Bigr]
$$

원문 마지막 항의 소괄호 닫힘은 보이지 않으며, 대괄호로 끝나는 모양을 그대로 전사했다.

> “This is accomplished by employing a finite difference procedure that utilizes second order correct differing of the diffusion term (i.e., spatial variation) and first order correct backward differing of the temporal term. This leads to equations such as” (p.8)

> “The ‘j’ subscript refers to conditions at the ‘j-th’ node. The ‘*’ superscript refers to conditions at the previous time-step. δ is the dimensionless nodal spacing, which equals [1/number of spatial increments in the material 1]=[1/number of spatial increments in material 2]. h is the total pipe wall thickness.” (p.8; 인용부호 모양만 본문과 구별해 표시)

T, r, k, ρ, csp: Eqn. 1의 원문 정의와 기호표. j±1을 별도로 풀어 쓴 원문 정의 없음. Δt에 대한 별도의 기호 정의 문장 없음(원문은 위에서 “temporal term”, “previous time-step”이라고 쓴다).

### Eqn. 3a–3c — PDF 19쪽 / 인쇄 9쪽

> “In region 1 (inner material)” (p.9)

$$
\sigma_r=\frac{E}{1-\mu}\frac{1}{r^2}
\left\{-\alpha_1\int_{r_i}^{r}r(T-T_0)\,dr
+\frac{r^2-r_i^2}{r_o^2-r_i^2}\Omega\right\}
\tag{3a}
$$

$$
\sigma_\theta=\frac{E}{1-\mu}\frac{1}{r^2}
\left\{\alpha_1\int_{r_i}^{r}r(T-T_0)\,dr
-\alpha_1r^2(T-T_0)
+\frac{r^2+r_i^2}{r_o^2-r_i^2}\Omega\right\}
\tag{3b}
$$

$$
\sigma_z=\frac{E}{1-\mu}
\left\{\frac{2}{r_o^2-r_i^2}\Omega-\alpha_1(T-T_0)\right\}
\tag{3c}
$$

원문 정의·문장:

> “The treatment here will be for the two materials to have the same elastic constants E and μ (E can be weighted to get an equivalent value, see Equation 6), but different coefficients of thermal expansion α.” (p.8)

> “The axial strain, εz, is taken to be constant (not zero) at any instant, and equal to a value that produces a zero net axial load.” (p.8)

> “This condition, along with the boundary condition of zero radial stress at the inner and outer pipe wall and continuity of displacements and radial stress at the bimaterial interface, allows the following end results to be obtained. (Refer to Figure 2 for the notation employed.)” (p.8)

> “In the above equations, μ is Poisson’s ratio.” (p.10)

> “Hence, the selection of a reference temperature (T₀) has an influence in the case of piping with 2 layers.” (p.10)

> “In xLPR-TIFFANY, T₀ is user specified.” (p.10)

E — “Elastic modulus”; α — “Coefficient of thermal expansion”; r, ri, ro, rc, T — 기호표의 원문 정의를 §2에 전사. 아래첨자 1, 2의 원문 정의는 Eqn. 6 아래 인용. Ω는 Eqn. 4로 제시된다. σr, σθ, σz 각각에 대한 명시적 기호-명칭 대응 정의 문장은 원문 정의 없음. 본문은 위 인용처럼 “radial stress”, “axial strain” 등을 사용한다. z의 별도 기호 정의 없음.

### Eqn. 4 — PDF 19쪽 / 인쇄 9쪽

> “where”

$$
\Omega=\alpha_1\int_{r_i}^{r_c}r(T-T_0)\,dr
+\alpha_2\int_{r_c}^{r_o}r(T-T_0)\,dr
$$

Ω: 위 식 이외의 명칭·정의 문장 원문 정의 없음. 나머지 기호는 Eqn. 3a–3c에 인용한 문장, 기호표 및 Figure 2의 표기. α1, α2의 아래첨자 1, 2는 Eqn. 6 아래 원문 문장 참조.

### Eqn. 5a — PDF 19쪽 / 인쇄 9쪽

> “In region 2 (outer material)” (p.9)

$$
\sigma_r=\frac{E}{1-\mu}\frac{1}{r^2}\left\{
-\alpha_2\int_{r_c}^{r}r(T-T_0)\,dr
-\frac{r_o^2-r^2}{r_o^2-r_i^2}\alpha_1\int_{r_i}^{r_c}r(T-T_0)\,dr
+\frac{r^2-r_i^2}{r_o^2-r_i^2}\alpha_2\int_{r_c}^{r_o}r(T-T_0)\,dr
\right\}
$$

기호의 원문 정의·문장: Eqn. 3a–3c와 동일한 본문(p.8,10), 기호표(p.viii), Figure 2(p.9). σr의 명시적 기호-명칭 대응은 원문 정의 없음.

### Eqn. 5b–5c — PDF 20쪽 / 인쇄 10쪽

$$
\sigma_\theta=\frac{E}{1-\mu}\frac{1}{r^2}\left\{
\alpha_2\int_{r_c}^{r}r(T-T_0)\,dr
-\alpha_2r^2(T-T_0)
+\frac{r^2+r_o^2}{r_o^2-r_i^2}\alpha_1\int_{r_i}^{r_c}r(T-T_0)\,dr
+\frac{r^2+r_i^2}{r_o^2-r_i^2}\alpha_2\int_{r_c}^{r_o}r(T-T_0)\,dr
\right\}
\tag{5b}
$$

$$
\sigma_z=\frac{E}{1-\mu}
\left\{\frac{2}{r_o^2-r_i^2}\Omega-\alpha_2(T-T_0)\right\}
\tag{5c}
$$

> “In the above equations, μ is Poisson’s ratio. It is easily shown that these results reduce to the corresponding ones in Timoshenko [7] for a uniform material when α1=α2.” (p.10)

기타 기호의 원문 정의·문장: Eqn. 3a–3c의 인용 및 §2 기호표. σθ, σz의 명시적 기호-명칭 대응 문장은 원문 정의 없음. Ω는 Eqn. 4.

### Eqn. 6 — PDF 20쪽 / 인쇄 10쪽

$$
E=\frac{E_1A_1+E_2A_2}{A_1+A_2}
$$

> “It should be noted that the effective elastic modulus, E, used in the program is calculated as a weighted average of the cross-sectional areas and elastic modulus values for the inner and outer material:” (p.10)

> “Where the variables denoted by the subscript 1 are for the inner material and denoted by the subscript 2 for the outer material.” (p.10)

E는 위 인용 및 기호표의 “Elastic modulus”. E1, E2, A1, A2를 개별적으로 등호 또는 기호 목록으로 정의한 문장은 원문 정의 없음. 원문 직접 설명은 위 두 문장이다.

### 본문·그림 중간 식과 수학 표기

Figure 1 — PDF 15쪽 / 인쇄 5쪽:

$$K_I=\int_0^a\sigma(x)m(x,a)\,dx$$

그림 상자: “Evaluation of Stress Intensity Factors vs. Time”. a, c — 기호표의 “Crack depth”, “Half crack length”. σ(x), m(x,a), x, 아래첨자 I에 대한 직접 정의 문장은 원문 정의 없음. 그림에는 별도 “Influence Functions” 상자가 있다. K — 기호표의 “Stress intensity factor”.

PDF 17쪽 / 인쇄 7쪽: $T(r,t)$ — “The temperature field is therefore a function of radial coordinate and time only, T(r, t).”

PDF 18쪽 / 인쇄 8쪽: $\delta=[1/\text{number of spatial increments in the material 1}]=[1/\text{number of spatial increments in material 2}]$ — Eqn. 2 아래의 직접 정의 문장을 수학 표기로 병기했다. $\varepsilon_z$ — “The axial strain, εz, is taken to be constant (not zero) at any instant, and equal to a value that produces a zero net axial load.”

PDF 20쪽 / 인쇄 10쪽:

> “As a sidelight if α1=α2 and T = constant, all of the stresses are zero. However if α₁ ≠ α₂, a uniform temperature produces stresses except at the single temperature T=T₀.”

수학 표기: $\alpha_1=\alpha_2$, $T=\mathrm{constant}$, $\alpha_1\ne\alpha_2$, $T=T_0$.

PDF 20~21쪽 / 인쇄 10~11쪽: $\sigma_T$, $\sigma_B$, $T_{sig}$, $T_0=70^{\circ}\mathrm{F}$, $\Delta p$.

> “A tension stress and a bending stress are input to TIFFANY (σ_T and σ_B) along with the temperature at which these values are applicable (Tsig, usually the normal operating temperature).” (p.10)

> “These are considered to be the non-pressure global stresses at the temperature T_sig. These stresses are zero at T₀ = 70ᵒF, and vary linearly with the average temperature in the pipe wall.” (pp.10–11)

> “The time variation of the pressure is a TIFFANY input (the deviation from the normal operating pressure is specified as Δp) and the effects on stress are computed by TIFFANY.” (p.11)

PDF 21쪽 / 인쇄 11쪽:

원문 표기: $\Delta K\ (K_{\max}-K_{\min})$. 원문에는 이 위치에 등호가 없다.

> “In the following discussion Kmax and Kmin refer to the maximum and minimum values of the stress intensity factor during the transient being analyzed, which as noted in the previous subsection for stresses are excursions from the stress intensity factor during normal operation.”

> “These values are needed for fatigue crack growth analyses that involve the transient change in cyclic stress intensity factors, ΔK (Kmax - Kmin).”

기호표(p.viii): ΔK — “Cyclic stress intensity factor”.

그 밖의 원문 수학 표기: Figure 1의 $h_1,h_2,r_i,r_o,t_0,t_1,t_2,a,2c,a_1,c_1,a_2,c_2,K_a,K_c$; Figure 2의 $r_o,r_c,r_i,h,h_1,h_2$; Figure 3의 $\mathrm{IAType}=1$, $\mathrm{IAType}=2\ \mathrm{or}\ 3$; 표의 $a/h,a/c,a/t,c,\theta,T(r,t),\sigma(r,t)$ 및 입력 제한 부등식. 표·그림의 해당 위치에서 모두 전사한다. 그림의 시간·균열 크기 곡선 아래첨자와 $K_a,K_c$의 직접 정의 문장은 원문 정의 없음. h는 Eqn. 2의 정의, h1/h2는 p.3의 “with thicknesses h1 and h2”와 기호표, 반경들은 기호표를 따른다. a/t의 t를 따로 벽두께라고 정의한 문장은 원문 정의 없음(기호표 t는 “Time”).

## 2. NOMENCLATURE/LIST OF SYMBOLS 및 ACRONYMS AND INITIALISMS

아래 고정폭 블록은 원문 인용이다. 기호표의 H1, h2, K의 대소문자를 유지했다.


### NOMENCLATURE/LIST OF SYMBOLS — PDF 9쪽 / 인쇄 viii

```text
NOMENCLATURE/LIST OF SYMBOLS
a              Crack depth
c              Half crack length
csp            Specific heat
E              Elastic modulus
H1             Inner pipe thickness (in case of overlay or clad piping)
h2             Outer pipe thickness (in case of overlay or clad piping)
K              Stress intensity factor
r              Radial coordinate
ri             Inside radius
ro             Outside radius
rc             Interface radius
t              Time
T              Temperature
α              Coefficient of thermal expansion
ΔK             Cyclic stress intensity factor
Δp             Deviation from the operating pressure
K              Thermal conductivity
ρ              Density
θ              Angular location
σT             Global membrane stress

σB             Global bending stress

μ              Poisson’s Ratio
```

### ACRONYMS AND INITIALISMS — PDF 10쪽 / 인쇄 ix

```text
ACRONYMS AND INITIALISMS
DLL            Dynamic Link Library
DMW            Dissimilar Metal Weld
FE             Finite Element
FEA            Finite Element Analysis
EPRI           Electric Power Research Institute
MVR            Module Validation Report
NRC            Nuclear Regulatory Commission
PWC            Part-Wall Crack
RTM            Requirements Traceability Matrix
SDD            Software Design Description
SI             Système International d’Unités
SRD            Software Requirements Document
STP            Software Test Plan
STRR           Software Test Results Report
TWC            Through-Wall Crack
V&V            Verification and Validation
xLPR           eXtremely Low Probability of Rupture
```

## 3. 표 전사

표의 열 배치와 행 안 줄바꿈은 고정폭 블록으로 보존했다. 병합 셀의 문구는 원문에 인쇄된 위치에 한 번 표기한다.

### §2.4.1 Assumptions — PDF 16쪽 / 인쇄 6쪽

```text
2.4.1 Assumptions

The usual assumptions of linear elasticity and classical heat conduction are made in the
TIFFANY analysis. The thermophysical properties are taken to be independent of
temperatuare, other than a linear variation with temperature of the thermal conductivity. The
thermal and elasticity analysis assumes a long circular cylinder with axisymmetric boundary
conditions. Plane cross-sections remain plane and there is no net axial force due to the radial
temperature gradient. The stress intensity factor solutions employed to obtain K from the
stresses are also for long circular cylinders. Hence, TIFFANY results are strictly applicable
only to long sections of pipe. They are assumed to be applicable to other piping components,
such as elbows, tees and nozzles.

                                                                            Expected Impact on
         Assumption                       Technical Basis                    Module Bias and
                                                                               Uncertainty
 assumptions of linear           The use of linear elastic behavior is     No bias or uncertainty
 elasticity and classical heat   conservative, as the effects of           expected.
 conduction                      through-wall thermal gradients and
                                 pressure driven stresses are
                                 impacted by the highly constrained
                                 material behavior, as all of the strain
                                 is elastic in nature. This prevents
                                 significant, and potentially
                                 advantageous stress redistribution,
                                 which would normally occur in an
                                 inelastic material environment, which
                                 could result in reduced stresses or
                                 limit the maximum stresses.
                                 The use of classical heat conduction
                                 assumes no phase transformation,
                                 which would invalidate the physical
                                 assumptions of classic heat
                                 conduction relationship. The
                                 exclusion of radiation and convection
                                 heat transfer behavior is reasonable,
                                 as the typical operating temperatures
                                 in nuclear piping components are
                                 insufficient to generate significant
                                 radiant heat transfer behavior, and
                                 convection heat transfer is only
                                 significant at material surfaces,
                                 which are already captured.
 thermophysical properties are   These properties vary minimally with      May result in some bias
 taken to be independent of      temperature                               with temperature but the
 temperatuare                                                              impact is expected to be
                                                                           minimal
 thermal and elasticity          Assumption simplifies the problem to      Minimal impact expected
 analysis assumes a long         one with a readily tractable & reliable
 circular cylinder with          solution
 axisymmetric boundary
 conditions
```

### §2.4.1 가정표 계속 — PDF 17쪽 / 인쇄 7쪽

```text
Expected Impact on
        Assumption                           Technical Basis                     Module Bias and
                                                                                   Uncertainty
 Plane cross-sections remain        Simplifying assumption that does not       Minimal impact expected
 plane and there is no net          take into account the effects of
 axial force due to the radial      variation in thermal expansion of the
 temperature gradient               different materials in DMWs. These
                                    differences may be small (?).
 the effective elastic modulus,     Simplifying assumption calculated          Minimal impact expected
 E, is calculated as a weighted     using a rule-of-mixtures type of
 average of the cross-              relationship but this does not account
 sectional areas and elastic        for the stresses arising due to the
 modulus values for the inner       dissimilar elastic modulii.
 and outer material                 The structural behavior of radial bi-
                                    metallic material is simulated by
                                    using a single constant value of E
                                    and µ. However, these values are
                                    ‘weighted,’ based on the cross-
                                    sectional areas of the two bimetallic
                                    materials. Therefore, bimetallic
                                    structures with a relatively small ratio
                                    of bimetallic material, will behave
                                    more strongly like the majority
                                    material. In addition, the variation of
                                    E and µ between typical steel
                                    materials is relatively small when
                                    compared to the variation of µ,
                                    thermal conductivity and diffusivity.
```

### Table 1. List of TIFFANY Module Requirements — PDF 23쪽 / 인쇄 13쪽

```text
Table 1.    List of TIFFANY Module Requirements

 Requirement              Short Description                         Acceptance Criteria
      RTIF-1     The subroutine shall be written in          The subroutine should be written in
                 Fortran such that it can be compiled to     Fortran.
                 a DLL
      RTIF-2     The subroutine must exhibit the             The subroutine should be readable
                 software design attributes of               and modular
                 maintainability and portability.
      RTIF-3     The subroutine shall be implemented in      The subroutine inputs and outputs
                 terms of SI units, with unit conversion     should be in SI units, with any
                 accomplished according to IEEE/ASTM         necessary unit conversion
                 SI 10 2010.                                 accomplished according to the
                                                             referenced standard.
      RTIF-4     If the module is called from the DLL        Static verification of framework SDD
                 wrapper, communication of inputs and        and wrapper DLL source code, if
                 outputs shall be conducted with explicit    applicable.
                 passing of variables.
      RTIF-5     The subroutine must follow the best         The subroutine should follow the
                 practices defined in [8]                    referenced best practices, where
                                                             possible.
      RTIF-6     The TIFFANY pre-processor shall call        Static verification of framework SDD
                 the Tiffany subroutine with a set of        and wrapper DLL source code, if
                 inputs that are in conformance with the     applicable.
                 required units, range of validity and
                 data types, specified in Table 1
      RTIF-7     The TIFFANY pre-processor shall also        Static verification of framework SDD
                 accept the outputs in conformance with      and wrapper DLL source code, if
                 the required units, range of validity and   applicable.
                 data types, specified in Table 2
      RTIF-8     Upon receiving an error message from        Static verification of framework SDD
                 this module, the framework shall            and wrapper DLL source code, if
                 terminate the analysis (individual          applicable.
                 realization or complete simulation, at
                 the discretion of the Computational
                 Group)
```

### Table 1 계속 — PDF 24쪽 / 인쇄 14쪽

```text
Requirement            Short Description                        Acceptance Criteria
    RTIF-9     Calculate T(r, t) with TIFFANY             Numerical procedure to independently
               subroutine                                 check computations of temperature
                                                          fields.
   RTIF-10     Calculate σ(r, t) with TIFFANY             Numerical procedure to independently
               subroutine                                 check computations of stress fields.
   RTIF-11     Calculate maximum K at the deepest         Numerical procedure to independently
               point for circumferential PW cracks, for   check the determination of maximum
               each combination of a/h, a/c and the       and minimum K values.
               angular location around the
               circumference and return as a 3-d
               array (a/c, a/h, θ)
   RTIF-12     Calculate minimum K at the deepest         Numerical procedure to independently
               point for circumferential PW cracks, for   check the determination of maximum
               each combination of a/h, a/c and the       and minimum K values.
               angular location around the
               circumference and return as a 3-d
               array (a/c, a/h, θ)
   RTIF-13     Calculate maximum K at the surface         Numerical procedure to independently
               point for circumferential PW cracks, for   check the determination of maximum
               each combination of a/h, a/c and the       and minimum K values.
               angular location around the
               circumference and return as a 3-d
               array (a/c, a/h, θ)
   RTIF-14     Calculate minimum K at the surface         Numerical procedure to independently
               point for circumferential PW cracks, for   check the determination of maximum
               each combination of a/h, a/c and the       and minimum K values.
               angular location around the
               circumference and return as a 3-d
               array (a/c, a/h, θ)
   RTIF-15     Calculate maximum K for                    Numerical procedure to independently
               circumferential TW cracks due to           check the determination of maximum
               membrane stress, for each                  and minimum K values.
               combination of c and the angular
               location around the circumference and
               return as a 2-d array (c, θ)
   RTIF-16     Calculate minimum K for                    Numerical procedure to independently
               circumferential TW cracks due to           check the determination of maximum
               membrane stress, for each                  and minimum K values.
               combination of c and the angular
               location around the circumference and
               return as a 2-d array (c, θ)
   RTIF-17     Calculate maximum K for                    Numerical procedure to independently
               circumferential TW cracks due to           check the determination of maximum
               bending stress, for each combination of    and minimum K values.
               c and the angular location around the
               circumference and return as a 2-d
               array (c, θ)
```

### Table 1 계속 — PDF 25쪽 / 인쇄 15쪽

```text
Requirement            Short Description                        Acceptance Criteria
   RTIF-18     Calculate minimum K for                    Numerical procedure to independently
               circumferential TW cracks due to           check the determination of maximum
               bending stress, for each combination of    and minimum K values.
               c and the angular location around the
               circumference and return as a 2-d
               array (c, θ)
   RTIF-19     Calculate maximum K at the deepest         Numerical procedure to independently
               point for axial PW cracks, for each        check the determination of maximum
               combination of a/h and a/c and return      and minimum K values.
               as a 2-d array (a/c, a/h)
   RTIF-20     Calculate minimum K at the deepest         Numerical procedure to independently
               point for axial PW cracks, for each        check the determination of maximum
               combination of a/h and a/c and return      and minimum K values.
               as a 2-d array (a/c, a/h)
   RTIF-21     Calculate maximum K at the surface         Numerical procedure to independently
               point for axial PW cracks, for each        check the determination of maximum
               combination of a/h and a/c and return      and minimum K values.
               as a 2-d array (a/c, a/h)
   RTIF-22     Calculate minimum K at the surface         Numerical procedure to independently
               point for axial PW cracks, for each        check the determination of maximum
               combination of a/h and a/c and return      and minimum K values.
               as a 2-d array (a/c, a/h)
   RTIF-23     Calculate maximum K for axial TW           Numerical procedure to independently
               cracks due to pressure stress, for each    check the determination of maximum
               crack size and return as a 1-d array (c)   and minimum K values.
   RTIF-24     Calculate minimum K for axial TW           Numerical procedure to independently
               cracks due to pressure stress, for each    check the determination of maximum
               crack size and return as a 1-d array (c)   and minimum K values.
   RTIF-25     Calculate maximum change in axial          Independent numerical procedures or
               stress due to pressure during the          by examining the intermediate output
               transient
   RTIF-26     Calculate maximum change in hoop           Independent numerical procedures or
               stress due to pressure during the          by examining the intermediate output
               transient
   RTIF-27     Calculate the maximum change of total      Independent numerical procedures or
               axial stress at the ID (includes radial    by examining the intermediate output
               gradient thermal stresses pressure,
               membrane and bending) for each
               segment and return as a 1-d array
   RTIF-28     Calculate the minimum change of total      Independent numerical procedures or
               axial stress at the ID (includes RGTS,     by examining the intermediate output
               pressure, membrane and bending) for
               each segment and return as a 1-d
               array (θ)
   RTIF-29     Calculate the time during the transient    Independent numerical procedures or
               at which the maximum change of total       by examining the intermediate output
               axial stress at the ID occurs for each
               segment and return as 1-d array (θ)
```

### Table 1 계속 — PDF 26쪽 / 인쇄 16쪽

```text
Requirement              Short Description                        Acceptance Criteria
      RTIF-30    Calculate the time during the transient    Independent numerical procedures or
                 at which the minimum change of total       by examining the intermediate output
                 axial stress at the ID occurs for each
                 segment and return as 1-d array (θ)
      RTIF-31    Calculate the maximum change of total      Independent numerical procedures or
                 hoop stress at the ID (includes RGTS       by examining the intermediate output
                 and pressure)
      RTIF-32    Calculate the minimum change of total      Independent numerical procedures or
                 hoop stress at the ID (includes RGTS       by examining the intermediate output
                 and pressure)
      RTIF-33    Calculate the time during the transient    Independent numerical procedures or
                 at which the maximum change of total       by examining the intermediate output
                 hoop stress at the ID occurs
      RTIF-34    Calculate the time during the transient    Independent numerical procedures or
                 at which the minimum change of total       by examining the intermediate output
                 hoop stress at the ID occurs
      RTIF-35    Calculate the rise time for axial stress   Independent numerical procedures or
                 at the ID for each segment and return      by examining the intermediate output
                 as 1-d array (θ)
      RTIF-36    Calculate the rise time for hoop stress    Independent numerical procedures or
                 at the ID                                  by examining the intermediate output
      RTIF-37    Calculate the maximum temperature at       Independent numerical procedures or
                 the ID during the transient                by examining the intermediate output
      RTIF-38    Calculate the minimum temperature at       Independent numerical procedures or
                 the ID during the transient                by examining the intermediate output
```

### Table 2. Inputs to Subroutine TIFFANY — PDF 28쪽 / 인쇄 18쪽

```text
Table 2.   Inputs to Subroutine TIFFANY

  Variable        Data Type                                Description
   TitleIn        Character      Analysis description (1≤characters≤60)
  IATypeIn          Integer      Transient type
                                 1 – Thermal Transient
                                 2 – Stratification Transient
                                 3 – Mechanical Transient
   IUnitsIn         Integer      1-US Customary
                                 2-SI
   IPrintIn         Integer      Print interval for intermediate output(Enter zero for no output)
  PipeODIn         Real (8)      Pipe Outside Diameter
   ThickIIn        Real (8)      Inside Material Thickness
  ThickOIn         Real (8)      Outside Material Thickness
  FlowXIn          Real (8)      Flow Rate
    NuIn           Real (8)      Poisson’s Ratio
    NHist           Integer      No. of data in the time-temperature-pressure history (<=10000)
  TimeA [ ]        Real (8)      NHist values of Time
 FlTempA [ ]       Real (8)      NHist values of Fluid temperature
   PrA [ ]         Real (8)      NHist values of Change in Pressure
 TimeStepIn        Real (8)      Time step for computing temperatures, stresses and stress
                                 intensity factors
   TzeroIn         Real (8)      Temperature at which clad/overlay stresses are zero
 Youngs1In         Real (8)      Elastic Modulus for inner material 1
   Rho1In          Real (8)      Density
   Cp1In           Real (8)      Specific Heat
  Alpha1In         Real (8)      Thermal Expansion Coeff.
   K1T1In          Real (8)      Thermal Conductivity at Temperature T11
   K1T2In          Real (8)      Thermal Conductivity at Temperature T12
    T11In          Real (8)      Temperature T11
    T12In          Real (8)      Temperature T12
 Youngs2In         Real (8)      Elastic Modulus for outer material 2
   Rho2In          Real (8)      Density
   Cp2In           Real (8)      Specific Heat
  Alpha2In         Real (8)      Thermal Expansion Coeff.
   K2T1In          Real (8)      Thermal Conductivity at Temperature T21
   K2T2In          Real (8)      Thermal Conductivity at Temperature T22
    T21In          Real (8)      Temperature T21
```

### Table 2 계속 및 자료형 설명 — PDF 29쪽 / 인쇄 19쪽

```text
xLPR Models Subgroup Report—Cyclic Stress Intensity Factors

     Variable               Data Type                                            Description
       T22In                   Real (8)          Temperature T22
    SigMNOIn                   Real (8)          Normal thermal expansion membrane stress
    SigBNOIn                   Real (8)          Normal thermal expansion bending stress
    OpTempIn                   Real (8)          Operating Temperature (corresponding to SigMNO, SigBNO)
    SigMminIn                  Real (8)          Minimum membrane stress (only for IYType = 2 or 3)
    SigMmaxIn                  Real (8)          Maximum membrane stress (only for IYType = 2 or 3)
    SigBminIn                  Real (8)          Minimum bending stress (only for IYType = 2 or 3)
    SigBmaxIn                  Real (8)          Maximum bending stress (only for IYType = 2 or 3)
   DispFactorIn                Real (8)          Displacement control factor (only for IAType=2)
   NumSegsIn                   Integer           No. of Crack Initiation Segments (<=100)
     NAOCIn                    Integer           No. of a/c values for the evaluation of K for PW cracks (<=100)
      NAOTIn                   Integer           No. of a/h values for the evaluation of K for PW cracks (<=100)
   NCTWCircIn                  Integer           No. of c values for the evaluation of K for TW Circ. cracks
                                                 (<=100)
    NCTWAxIn                   Integer           No. of c values for the evaluation of K for TW Axial cracks
                                                 (<=100) (only for IAType=1)
     AOCa [ ]                  Real (8)          NAOC a/c values
     AOTa [ ]                  Real (8)          NAOT a/h values
   CTWCirca [ ]                Real (8)          NCTWCirc c values
   CTWAxa [ ]                  Real (8)          NCTWAx c values
Detailed description of the inputs needed by TIFFANY is given in this section. Note on the data types:
Integer – A whole number without a decimal point
Real (8) – A floating point number
Character – Any alpha-numeric characters except @#$%^&*()
[] – Indicates an array input
```

### Table 3. Outputs from Subroutine TIFFANY — PDF 30쪽 / 인쇄 20쪽

```text
Table 3.   Outputs from Subroutine TIFFANY

      Variable                         Description                             Notes
                                    Circumferential Cracks
   KCircDeepMxO[ ]       3-d array [a/t, a/c, Segment Number] of             PW Cracks
                         maximum K for the deepest point
   KCircDeepMnO[ ]       3-d array [a/t, a/c, Segment Number] of
                         minimum K for the deepest point
   KCircSurfMxO[ ]       3-d array [a/t, a/c, Segment Number] of
                         maximum K for the surface point
   KCircSurfMnO[ ]       3-d array [a/t, a/c, Segment Number] of
                         minimum K for the surface point
   KCircTWMxMO[ ]        2-d array [c, Segment Number] of                    TW Cracks
                         maximum K
   KCircTWMnMO[ ]        2-d array [c, Segment Number] of minimum
                         K
   KCircTWMxBO[ ]        2-d array[c, Segment Number] of maximum             TW Cracks
                         K
   KCircTWMnBO[ ]        2-d array [c, Segment Number] of minimum
                         K
     PaxStrMaxO          Maximum pressure stress change (axial)       Max. change for input PrA
                                                                                []
    AllAxStrMaxO[ ]      1-d array [Segment Number] of Maximum        Used for fatigue initiation
                         axial ID stress (included RGTS, Pr,
                         membrane, bending)
    AllAxStrMinO[ ]      1-d array [Segment Number] of Minimum        Used for fatigue initiation
                         axial ID stress (included RGTS, Pr,
                         membrane, bending)
  TimeMaxAllAxialO[ ]    1-d array [Segment Number] of Time at
                         which the maximum ID stress occurs
  TimeMinAllAxialO[ ]    1-d array [Segment Number] of Time at
                         which the minimum ID stress occurs
  RiseTimeAxStrO[ ]      1-d array [Segment Number] of Rise time
                         for axial stress at the ID
                                          Axial Cracks
   KAxDeepMxO[ ]        Two-d array [a/t, a/c] of maximum K for the          PW Cracks
                        deepest point
   KAxDeepMnO[ ]        Two-d array [a/t, a/c] of minimum K for the
                        deepest point
    KAxSurfMxO[ ]       Two-d array [a/t, a/c] of maximum K for the
                        surface point
    KAxSurfMnO[ ]       Two-d array [a/t, a/c] of minimum K for the
                        surface point
    KAxTWMxO[ ]         One-d array [c] of maximum K                         TW Cracks
    KAxTWMnO[ ]         One-d array [c] of minimum K
```

### Table 3 계속 — PDF 31쪽 / 인쇄 21쪽

```text
PhoopStrMaxO            Maximum pressure stress change (hoop)                 Max. change for input PrA
                                                                                              []
   AllHoopStrMaxO             Maximum hoop ID stress (included RGTS,                 Used for fatigue initiation
                              Pr, membrane, bending)
   AllHoopStrMinO             Minimum hoop ID stress (included RGTS,                 Used for fatigue initiation
                              Pr, membrane, bending)
  TimeMaxAllHoopO             Time at which the maximum ID hoop stress
                              occurs
  TimeMinAllHoopO             Time at which the minimum ID hoop stress
                              occurs
   RiseTimeHpStrO             Rise time for hoop stress at the ID


       TempMaxO               Maximum temperature at the ID                            Only for Type 1 input
       TempMinO               Minimum temperature at the ID
          Ierror              Integer, Error Flag                                     Value between 101-
                                                                                    120,123-128,131-144 or 0
 Note: K in this table is the excursion from normal operation.
```

### Table 4. Material Properties Required for TIFFANY — PDF 31쪽 / 인쇄 21쪽

| Name | Sym. | Units |
|---|---|---|
| thermal conductivity | $K$ | $\mathrm{W/(m\! -\! {}^{o}K)}$ |
| specific heat | $C$ | $\mathrm{J/(kg\! -\! {}^{o}K)}$ |
| Density | $\rho$ | $\mathrm{kg/m^3}$ |
| thermal diffusivity | $\kappa$ | $\mathrm{m^2/s}$ |
| Young’s modulus | $E$ | MPa |
| Poisson’s ratio | $\nu$ | -- |
| coeff of thermal exp | $\alpha$ | $ {}^{o}\mathrm{C}^{-1}$ |

## 4. Figure 1~3 구성요소·흐름 전사

### Figure 1 — PDF 15쪽 / 인쇄 5쪽

“Figure 1. Components of xLPR-TIFFANY Computer Code and their Interrelationships.”

상자와 화살표(원문 상자 문구):

- “Fluid Properties” → “Convective Heat Transfer Coefficient”.
- “Coolant Velocity History” → “Convective Heat Transfer Coefficient”.
- “Convective Heat Transfer Coefficient” → “Evaluation of Temperature Profiles”.
- “Coolant Temperature History” → “Evaluation of Temperature Profiles”.
- “Pipe Geometry and Materials” → “Evaluation of Temperature Profiles”.
- “Evaluation of Temperature Profiles” → “Evaluation of Radial Gradient Thermal Stresses”.
- “Evaluation of Radial Gradient Thermal Stresses” → “Evaluation of Stress Intensity Factors vs. Time”.
- “Additional Stresses” → 위 열응력에서 K 계산으로 내려가는 연결선.
- “Crack Size” → “Evaluation of Stress Intensity Factors vs. Time”.
- “Influence Functions” → “Evaluation of Stress Intensity Factors vs. Time”.
- “Evaluation of Stress Intensity Factors vs. Time” → “Sorting for Evaluation of Maximum and Minimum K”.
- 위 K 계산 출력선에서 오른쪽 분기 → “Resulting K_a, K_c”.

그림 내부 표기:

- “Coolant Temperature History”: 세로 T, 가로 t; 시간에 따라 내려가는 곡선.
- “Pipe Geometry and Materials”: 동심 원 단면, h₁, h₂, rₒ.
- “Evaluation of Temperature Profiles”: 세로 T, 가로 r; rᵢ, rₒ, t₀, t₁, t₂.
- “Evaluation of Radial Gradient Thermal Stresses”: σ_B, rᵢ, rₒ, t₁, t₂.
- “Crack Size”: 표면 균열 도식, a, 2c.
- “Evaluation of Stress Intensity Factors vs. Time”: 위 §1의 $K_I=\int_0^a\sigma(x)m(x,a)dx$; 시간 그래프의 Kₘ 축, t 축, a₁,c₁ 및 a₂,c₂ 곡선. Kₘ의 원문 정의 없음.
- “Sorting for Evaluation of Maximum and Minimum K”: K (max), a, c₁, c₂.

### Figure 2 — PDF 19쪽 / 인쇄 9쪽

“Figure 2. Cross-section of a clad pipe or with an inlay or overlay.”

원문 표기: “Mat 1”, “Mat 2”, “Insulated OD”, $r_o,r_c,r_i,h,h_1,h_2$.

동심 단면의 내부 층에 “Mat 1”, 외부 층에 “Mat 2”. 중심에서 내면까지 rᵢ, 재료 경계까지 r_c, 외면까지 rₒ의 화살표. 내면–재료 경계에 h₁, 재료 경계–외면에 h₂, 내면–외면에 h. 외면 옆에 “Insulated OD”.

### Figure 3 — PDF 33쪽 / 인쇄 23쪽

“Figure 3. TIFFANY Logic Control Flow”

상자와 화살표(원문 표기):

1. “Start” → “IAType”.
2. “IAType = 2 or 3” 분기 → “Calculate K (CalcK23)” → “Exit”.
3. “IAType = 1” 분기 → “Initialization (InitK, Initialize)” → “Start Timestep Iteration” → “Calculate Temp. Distribution (TEMPER)” → “Calculate Stress Distribution (STRESS)” → “Print Temp. & Stress (PRINTT)” → “Calculate K (CalcK)” → “End Timestep Iteration” → “Exit”.

## 5. 섹션별 원문 사실 문장

아래는 섹션 구조에 따른 영어 원문 인용이다. 쪽을 넘는 문장은 원문 페이지 경계에 따라 이어진다. 수식의 깨진 텍스트 레이어는 포함하지 않고 §1의 이미지 판독 전사를 적용한다. 표의 내용은 §3에 전사했다.

### PDF 11쪽 / 인쇄 1쪽

```text
1.       INTRODUCTION

1.1      Subgroup Roles & Responsibilities
The xLPR-TIFFANY Subgroup is responsible for developing the model for computing cyclic
stress intensity factors due to plant transients and user-specified minimum/maximum
stresses, as functions of crack size. Related information, such as transient rise-time and
cyclic stress at the pipe inner surface, is also generated. Output for each transient is
generated by xLPR-TIFFANY that is then used as inputs to xLPR for analysis of fatigue crack
initiation and growth.

TIFFANY is strictly a deterministic module. Any uncertainties associated with a TIFFANY
analysis are in the inputs, primarily in the time-temperature inputs. Treatment of such
uncertainties is beyond the scope of the TIFFANY module and are treated elsewhere. The
material properties that enter into TIFFANY evaluations (coefficient of thermal expansion,
thermal conductivity, etc.) are well defined.

The subgroup ensured incorporation of the best-estimate models currently available for
modeling cyclic stress intensity factors, cyclic stresses and transient rise-times into the
TIFFANY xLPR Module source code. The subgroup was also responsible for providing test
cases for use in verifying and validating the computation of cyclic stress intensity factors and
related information, and then performing the verification and validation of the TIFFANY
calculated results.

1.2      Subgroup Objectives
The primary objectives of the TIFFANY Subgroup were to:

     •   Define the best-estimate analytical model for computation of cyclic stress intensity
          factors due to pressure and thermal excursions of reactor primary coolant.

     •   Define procedures for extraction of related results, including: cyclic stress at inner
          surface of the pipe; rise time of transient, and changes in restraint of thermal
          expansion stress.

     •   Develop the associated software code to perform the calculations.

     •   Define, perform and document the necessary test cases for use in verifying and
          validating TIFFANY model performance.

     •   Produce TIFFANY model documentation.

     •   Interface with the xLPR Computational Group to ensure proper performance and
           integration of the TIFFANY module.
```

### PDF 12쪽 / 인쇄 2쪽

```text
1.3    Models Under Auspices of Subgroup
The TIFFANY Subgroup provided models for the computation of cyclic stress intensity factors
(and related cyclic data) due to plant operating transients. This involved development of
models for computation of transient temperature fields, which are then used in the
computation of transient stresses. The xLPR stress intensity factor (K) modules [1,2] are
then accessed to compute stress intensity factors, and results are sorted to define maximum
and minimum values of the stress intensity factor for a specified set of crack sizes and
orientations.
```

### PDF 13쪽 / 인쇄 3쪽

```text
2.    TIFFANY MODEL DESCRIPTION
TIFFANY is a stand-alone module for evaluation of cyclic stress intensity factors due to
temperature excursions as functions of crack size for axial and circumferential cracks in a
single or bimaterial pipe (such as pipe with an overlay)..

Excursions of the coolant temperature in nuclear power reactors produce stresses within the
walls of the pressure vessel and piping. These stresses are a result of the temperature
gradients produced and are referred to as radial gradient thermal stresses. Coolant
temperature changes are therefore a source of cyclic stress that can be an important
contributor to fatigue crack growth.

The necessary information for calculation of the cyclic stress intensity factors due to coolant
temperature excursions is typically the temperature-time history of the coolant. From this, it
is necessary to determine the history of the radial variation of temperature within the pipe
wall. The ability to treat the heat conduction aspect of the problem is required to be contained
within the code using the resulting temperature field to calculate the stresses. This is
accomplished by use of relationships derived from elasticity theory for axisymmetric bodies
subject to axisymmetric temperature fields. Once the stresses are known, the resulting stress
intensity factors for semi-elliptical cracks in the inside pipe surface are evaluated by the use
of influence functions. Axial and circumferential cracks are treated. The cyclic stress intensity
factors (ΔK) are found from the temporal variation of K. Important additional features of the
code include consideration of convective heat transfer and the ability to include the influences
of cladding, inlays or overlays on both the temperature fields and stresses.

2.1    Model requirements for xLPR
TIFFANY is a stand alone module that prepares inputs to xLPR related to cyclic conditions
arising from temperature and pressure excursions of the reactor coolant. These inputs are
used in fatigue crack initiation and growth calculations performed by xLPR.

2.2    Model Development
FIgure 1, which is from the TIFFANY Software Requirements Document (SRD) [3],
summarizes the components of the analysis performed by the TIFFANY module for xLPR
Version 2.

As depicted in Figure 1, TIFFANY is capable of analyzing a pipe composed of two materials
(with thicknesses h1 and h2), such as encountered in overlay or clad piping. Fluid properties
for liquid water are temperature-dependent and are described in Reference [4].

The outputs from a TIFFANY analysis are used as inputs to xLPR. A TIFFANY analysis must
be performed for each thermal transient in the fatigue history being analyzed by xLPR, with
a separate set of inputs to describe each transient.
```

### PDF 14쪽 / 인쇄 4쪽

```text
2.3    Basis for Selection
Computation of the changes in cyclic stress intensity factors (ΔK) due to temperature
excursions and other loadings can be accomplished by a variety of means, including
procedures ranging in complexity up to three-dimensional finite element analysis with cracks
included in the model. The approach in TIFFANY was selected for its simplicity and speed
of computation, plus its maximum use of software that was already available [5]. There is no
sacrifice in accuracy, other than TIFFANY’s restriction to straight sections of pipe.

2.4    Mathematical Description of Model
As Figure 1 shows, the TIFFANYanalysis for a given transient is composed of many discreet
steps:

   (1). computation of the transient temperature field,

   (2). computation of thermal stresses due to the radial gradient of the transient
        temperature field,

   (3). other loadings and related computations of the cyclic stress at the inner surface,
        the rise-time of the transient, contributions of changes in the average pipe wall
        temperature to the restraint of thermal expansion stress, and contributions of
        pressure excursions and stratification and mechanical loading during the transient,

   (4). computation of stress intensity factors and their changes for various crack sizes
        and orientation due to the stresses in steps 3 and 4,

   (5). sorting of the stress intensity factors to obtain the maximum and minimum
        changes for a given crack size and orientation.

The mathematical description of each of these steps is detailed in the the related TIFFANY
module documentation, primarily the TIFFANY SRD [3]. Each of these steps will be briefly
summarized here.
```

### 2.4.1 Assumptions — PDF 16쪽 / 인쇄 6쪽

```text
2.4.1 Assumptions

The usual assumptions of linear elasticity and classical heat conduction are made in the
TIFFANY analysis. The thermophysical properties are taken to be independent of
temperatuare, other than a linear variation with temperature of the thermal conductivity. The
thermal and elasticity analysis assumes a long circular cylinder with axisymmetric boundary
conditions. Plane cross-sections remain plane and there is no net axial force due to the radial
temperature gradient. The stress intensity factor solutions employed to obtain K from the
stresses are also for long circular cylinders. Hence, TIFFANY results are strictly applicable
only to long sections of pipe. They are assumed to be applicable to other piping components,
such as elbows, tees and nozzles.
```

### 2.4.2 Temperature Field — PDF 17쪽 / 인쇄 7쪽

```text
2.4.2   Temperature Field

The temperature field in the pipe is assumed to be independent of distance along the pipe
and to be axisymmetric. This is consistent with the usual treatment of radial gradient thermal
stresses in pipes [6]. The temperature field is therefore a function of radial coordinate and
time only, T(r, t). The one-dimensional heat conduction problem is very amenable to a
numerical procedure, and such an approach is therefore used. Consideration of temperature-
dependent material properties, such as thermal conductivity, is straightforward in the
numerical procedures. The thermal conductivity can be temperature-dependent in xLPR-
TIFFANY.

In the general case, the material properties k, csp and ρ (thermal conductivity, specific heat
and density) can be functions of temperature.

A convection heat transfer boundary condition is applied at the inner surface of the pipe. The
correlation provided in Edwards [7] (page 166), as described in theTIFFANY SRD [3], is
```

### 2.4.2 및 2.4.3 — PDF 18쪽 / 인쇄 8쪽

```text
incorporated into TIFFANY to define the convection heat transfer coefficient knowing the
coolant flow velocity and temperature. An insulated boundary condition is applied at the outer
surface of the pipe.

A numerical procedure for evaluation of the temperature in the pipe wall is employed. This
is accomplished by employing a finite difference procedure that utilizes second order correct
differing of the diffusion term (i.e., spatial variation) and first order correct backward differing
of the temporal term. This leads to equations such as

The “j” subscript refers to conditions at the “j-th” node. The “*” superscript refers to conditions
at the previous time-step. δ is the dimensionless nodal spacing, which equals [1/number of
spatial increments in the material 1]=[1/number of spatial increments in material 2]. h is the
total pipe wall thickness.

Equation 2, along with analogous formulations of the boundary conditions (and continuity
conditions at the material interface if cladding, inlay or overlay is considered), lead to a set of
simultaneous equations for the current nodal temperature in terms of material properties,
geometrical terms and temperature from the previous time-step. These equations are readily
and efficiently solved by the method of successive substitutions.

2.4.3 Thermal Stresses

The stresses in the pipe wall are evaluated by use of elasticity theory from the transient
temperature field determined by the finite difference procedure described in Section 2.4.2.
The idealization of only radial variations of the stresses and displacements leads to a
particularly simple one dimensional quasi-static elasticity problem. Such problems are
discussed in Ref. [8], and the case of interest here of a single material is treated in Section
135 of that reference. The discussion in Ref. [8] can easily be generalized to provide results
for a bimaterial pipe. The treatment here will be for the two materials to have the same elastic
constants E and μ (E can be weighted to get an equivalent value, see Equation 6), but
different coefficients of thermal expansion α. The structural behavior of radial bi-metallic
material is simulated by using a single constant value of E and µ. However, these values are
‘weighted,’ based on the cross-sectional areas of the two bimetallic materials. Therefore,
bimetallic structures with a relatively small ratio of bimetallic material, will behave more
strongly like the majority material. In addition, the variation of E and µ between typical steel
materials is relatively small when compared to the variation of µ, thermal conductivity and
diffusivity. The axial strain, εz, is taken to be constant (not zero) at any instant, and equal to
a value that produces a zero net axial load. This is consistent with the usual treatment of
radial gradient thermal stresses in piping [6,8]. This condition, along with the boundary
condition of zero radial stress at the inner and outer pipe wall and continuity of displacements
and radial stress at the bimaterial interface, allows the following end results to be obtained.
(Refer to Figure 2 for the notation employed.)
```

### 2.4.3 및 2.4.4 — PDF 20쪽 / 인쇄 10쪽

```text
In the above equations, μ is Poisson’s ratio. It is easily shown that these results reduce to
the corresponding ones in Timoshenko [7] for a uniform material when α1=α2.

It should be noted that the effective elastic modulus, E, used in the program is calculated as
a weighted average of the cross-sectional areas and elastic modulus values for the inner and
outer material:

[Eqn. 6: §1에 전사]


Where the variables denoted by the subscript 1 are for the inner material and denoted by the
subscript 2 for the outer material.

As a sidelight if α1=α2 and T = constant, all of the stresses are zero. However if α 1 ≠ α 2 , a
uniform temperature produces stresses except at the single temperature T=T0. Hence, the
selection of a reference temperature (T0) has an influence in the case of piping with 2 layers.
The value of T0 is somewhat arbitrary, but in the case of reactor components, is usually taken
to be the room temperature of 70°F so that the pipe would be stress-free when the plant was
shut down. In xLPR-TIFFANY, T0 is user specified.

The values of α, E, μ, ρ and csp are somewhat temperature-dependent, whereas
xLPR-TIFFANY takes them to be independent of temperature. It is suggested that values at
some intermediate temperature (e.g., average of maximum and minimum temperature) that
occurs during the transient being analyzed be input to the software. An additional question
arises concerning the coefficient of thermal expansion, α. Two values are possible for a
given temperature; the instantaneous value at the given temperature, or the average value
between 70oF and the given temperature. α is a user input, but the instantaneous value at
some intermediate temperature is suggested since it is generally conservative – especially
for pipes composed of a single material.

2.4.4 Other Loadings and Related Computations

The influence of thermal transients on stresses other than the radial gradient stresses is
included in the TIFFANY computations.

Global Stresses: Temperature-dependent global stresses, such as pipe system stresses due
to restraint of thermal expansion, can change during a thermal transient due to a change in
the average temperature through the wall. A tension stress and a bending stress are input
to TIFFANY ( σ T and σ B ) along with the temperature at which these values are applicable
(Tsig, usually the normal operating temperature). These are considered to be the non-
```

### PDF 21쪽 / 인쇄 11쪽

```text
pressure global stresses at the temperature Tsig. These stresses are zero at T0 = 70oF, and
vary linearly with the average temperature in the pipe wall. The average temperature is
computed by TIFFANY.

TIFFANY does not include the stresses that are present during normal operation, but only
deviations from these stresses. The time variation of the pressure is a TIFFANY input (the
deviation from the normal operating pressure is specified as Δp ) and the effects on stress
are computed by TIFFANY.

The circumference of the pipe is broken down into a user-defined number of segments, and
the global bending stress varies from segment to segment.

Stratification and Mechanical Transients: xLPR-TIFFANY can also be used to obtain
stresses and tables of maximum and minimum values of changes in stress intensity factors
for transient identified as “stratification” or “mechanical”.

In the case of stratification transients, the stresses at each angular location and stress
intensity factors due to bending stress are multiplied by a factor that is a user input
(DispFactorIn).

In case of mechanical transients, a maximum and minimum membrane and bending stress
are input and used to generate tables of the changes in maximum and minimum stress
intensity factors for the selected crack sizes and for the angular location of each segment.

2.4.5 Stress Intensity Factors

The stress intensity factors for semi-elliptical inner surface cracks subject to radial gradient
thermal stresses and other transients (pressure, mechanical and stratification) are evaluated
at the deepest and surface points of part-through-wall (PW) cracks and for through-wall (TW)
cracks [1,2].

In the following discussion Kmax and Kmin refer to the maximum and minimum values of the
stress intensity factor during the transient being analyzed, which as noted in the previous
subsection for stresses are excursions from the stress intensity factor during normal
operation.

The values of Kmax and Kmin can be evaluated for either circumferential or axial cracks by use
of the appropriate stress and influence functions. The axial stress is used in the evaluation
of the stress intensity factors for circumferential cracks and the hoop stress is used for the
axial cracks.

Values of stress intensity factor are evaluated for any crack size and for any time at which
the stresses are evaluated during the transient. The actual time-variation of stress intensity
factor for a given crack size is usually not of interest, with values of Kmax and Kmin being of
more use. These values are needed for fatigue crack growth analyses that involve the
transient change in cyclic stress intensity factors, ΔK (Kmax - Kmin). The times at which Kmax
occurs is not the same for all crack sizes. Values of Kmax, and Kmin are easily obtained from
the temporal variation of stress intensity factor. The maximum and minimum stress intensity
factors due to the radial gradient thermal stresses and other loading are output for a user-
specified list of crack sizes, and angular locations in the case of circumferential cracks.
```

### PDF 22쪽 / 인쇄 12쪽

```text
2.4.6 Sorting

The values of stress intensity factors as functions of time during the transient are available
from intermediate TIFFANY calculations for the user-specified list of crack sizes, and angular
locations in the case of circumferential cracks. These results are then sorted to obtain the
maximum and minimum values for each crack size, with the results printed to files of Kmax
and Kmin for the specified range of crack sizes.

2.4.7 Uncertainty Quantification

TIFFANY performs strictly deterministic computations. Uncertainties are present only in
inputs to TIFFANY. Uncertainties in material properties are considered to be minimal, being
available from the ASME Boiler and Pressure Vessel Code [9]. Uncertainties in time variation
of the temperature do exist, but are not treated in TIFFANY. They are handled by the xLPR
Framework using a procedure proposed in an appendix of the TIFFANY Model Validation
Report [10].
```

### 3 및 3.1 — PDF 23쪽 / 인쇄 13쪽

```text
3.    TIFFANY MODULE DEVELOPMENT
In this section the module design requirements, inputs, verification and validation activities
are described.

3.1     Module requirements
The functional and performance requirements for TIFFANY are identified in the SRD [3] and
summarized in Table 6 of that document, which is also included in Table 5 of the Software
Design Description (SDD) [11]. Table 6 of the TIFFANY SRD is included here as Table 1.
This table also includes a short description of each requirement and the associated
acceptance criterion. Note that the acronym DLL in this table refers to the dynamic link library
for TIFFANY.
```

### 3.1 끝, 3.2, 3.3 — PDF 26쪽 / 인쇄 16쪽

```text
TIFFANY has no requirements for linking to other xLPR modules. The Stress intensity values
are calculated using the stress intensity factor module embedded in TIFFANY which is
identical to that used within the xLPR Framework. The output files from TIFFANY must be
properly handled by xLPR, as discussed in Section 3.3.

3.2     Module Limitations
The TIFFANY module is capable of analyzing only one transient at a time. The module picks
out only the largest and smallest values of the change in stress intensity factors for a given
crack size and type. This means that intermediate maxima and minima are not captured. It
is the responsibility of the user to properly define the transients being analyzed.

3.3     Integration Requirements
The TIFFANY module communicates through the DLL wrapper with the TIFFANY pre-
processor which effectively provides a link to the xLPR computational framework. If the
TIFFANY module is called from the DLL wrapper, communication of inputs and outputs shall
be conducted with explicit passing of variables [RTIF-4]. This requirement is intended to
provide local control of all module variables.

To invoke the TIFFANY module, the input pre-processor shall call the TIFFANY DLL with a
set of inputs that are in conformance with the required units, range of validity and data types,
```

### 3.3 계속 및 3.4 — PDF 27쪽 / 인쇄 17쪽

```text
specified in Table 2 below [RTIF-6]. The framework shall also accept the outputs in
conformance with the required units, range of validity and data types, specified in Table 3
below [RTIF-7].

The TIFFANY pre-processor should consult the Error Flag output to ensure the call to the
TIFFANY module completed in a satisfactory manner. Table 5 of the TIFFANY SRD [3]
describes each error condition and provides guidance for appropriate range of validity for
each parameter.

3.4    Description of Inputs and Outputs
Tables 2 and 3, which are from the TIFFANY SRD [3], summarize the inputs and outputs for
TIFFANY.
```

### 3.4 끝 및 3.5 — PDF 31쪽 / 인쇄 21쪽

```text
Values of these properties for common piping materials are available in the TIFFANY STP
[12].

A key input to TIFFANY is the time/temperature/pressure history of the transient. This can
come from a variety of sources, such as design reports or actual plant measurements. This
input itself is one of the major causes of uncertainty in the TIFFANY output. However, the
transient input from design reports is typically very conservative and would be expected to
bound the transient input from actual plant measurements.

3.5     Module Verification and Validation
The verification of the proper functionality of the TIFFANY module is detailed in the Software
Test Plan (STP) [12]. The test plans define a set of test cases that are sufficient to determine
whether the module encompasses all of the functional requirements enumerated in the
```

### 3.5 계속 및 3.6 — PDF 32쪽 / 인쇄 22쪽

```text
TIFFANY SRD [3]. The tests for the computation of temperatures are based on closed form
solutions for transient temperature fields. Comparisons of TIFFANY temperature and stress
results with closed form solutions are provided in the TIFFANY test results report (STRR) [4].
Additionally, TIFFANY stress and temperature results are compared with finite element
calculations in the TIFFANY models validation report (MVR) [10].

The scope of the testing includes only the functionality of TIFFANY. The scope does not
include the wrapper code that is used to interface the module with the GoldSim Framework.
Tests on the interfacing of the pre-processor output with the Framework are expected to be
performed during integration testing defined in a separate framework test plan.

3.6    Flow Diagram
A summary of the basic process structure of TIFFANY is shown in Figure 3. The constituent
actions in the activity diagram are described in further detail in the TIFFANY SDD [11].
```

### PDF 34쪽 / 인쇄 24쪽

```text
4.   RECOMMENDATIONS FOR XLPR VERSION 3 MODIFICATIONS
No recommendatioins for xLPR Version 3 modifications of TIFFANY are made at this time.
Lessons learned during the interfacing of TIFFANY output with the Goldsim framework and
exercising the TIFFANY capability in xLPR runs will probably point to some desireable
modifications in the future.
```

### PDF 35쪽 / 인쇄 25쪽

```text
5.    LESSONS-LEARNED
None at this time.
```

### PDF 36쪽 / 인쇄 26쪽

```text
6.   SUMMARY
This model report describes the overall development of the TIFFANY module for xLPR
version 2. The software requirements and design description are defined in [3,11] and a
prescribed test plan in [12]. The test plan includes comparisons with closed form temperature
and stress solutions, as well as finite element computations [10]. The testing itself is
documented in the TIFFANY STRR [4]. A review of inputs and outputs is provided. TIFFANY
itself is deterministic, but there are uncertainties in the inputs – primarily the
time/temperature/pressure history of the transient.
```

### PDF 37쪽 / 인쇄 27쪽

```text
7.   REFERENCES
[1] xLPR-SRD-KPW: xLPR Software Requirements Specification for K Calculator for
    Circumferential and Axial Part-Through-Wall Cracks, Version 2.2.

[2] xLPR-SRD-KTW: xLPR Software Requirements Specification for K Calculator for
    Circumferential and Axial Through-Wall Cracks, Version 2.2.

[3] xLPR-SRD-TIFF: xLPR Software Requirements Description for the TIFFANY Module,
    Version 1.0.

[4] xLPR-STRR-TIFF: xLPR Software Test Results Report for the TIFFANY Module,
    Version 1.0.

[5] D.D. Dedhia, D.O. Harris, and V.E. Denny, “TIFFANY: A Computer Code for Thermal
    Stress Intensity Factors for Surface Cracks in Clad Piping,” Science Applications, Inc.
    Report SAI–331–82–PA, Palo Alto, California, November 1982 (LLNL Contract No.
    8679501, Task 2).

[6] J.F. Harvey, Theory and Design of Pressure Vessels, van Nostrand and Reinhold, New
    York, second edition, 1991

[7] D.K. Edwards, V.E. Denny and A.F. Mills, Transfer Processes, McGraw-Hill Book
    Company, 2nd Edition, New York 1978

[8] S. Timoshenko and J.N. Goodier, Theory of Elasticity, Second Edition, McGraw Hill
    Book Co., New York, 1951

[9] ASME Boiler and Pressure Vessel Code, Section II, Part D, Properties

[10] xLPR-MVR-TIFF: xLPR Module Validation Report for TIFFANY, Version 1.0.

[11] xLPR-SDD-TIFF: xLPR Software Design Description for the TIFFANY Module, Version
     1.0.

[12] xLPR-STP-TIFF: xLPR Software Test Plan for the TIFFANY Module, Version 1.0.
```

## 6. 원문 자체 이상

아래는 원문에서 관찰한 표기·참조 차이다. 교정식이나 대체 해석은 제시하지 않는다.

1. Eqn. 2(p.8): 마지막 $T_{j-1}(k_jr_j+k_{j-1}r_{j-1}$ 뒤에 소괄호 닫힘이 보이지 않고 대괄호로 끝난다.
2. Eqn. 3b(p.9)의 Ω 앞 분자는 $r^2+r_i^2$. Eqn. 5b(p.10)의 α₁ 적분 앞 분자는 $r^2+r_o^2$, α₂ 적분 앞 분자는 $r^2+r_i^2$다. 서로 바꾸거나 통일하지 않았다.
3. 기호표(p.viii): “H1”과 “h2”. Figure 1~2는 h₁, h₂다.
4. 기호표(p.viii): “K — Stress intensity factor”와 이탤릭 “K — Thermal conductivity”가 함께 있다. Eqn. 1~2와 p.7 본문은 소문자 k. Table 4(p.21)는 대문자 K.
5. 기호표(p.viii)/Eqn. 3~6 및 본문은 μ로 Poisson’s ratio를 표시한다. Table 4(p.21)는 ν. Table 2(p.18)는 NuIn이다.
6. specific heat: 기호표 csp, Eqn. 1~2 $c_{sp}$, Table 4는 C.
7. Table 2(p.18)는 “IATypeIn”; p.19의 SigMminIn, SigMmaxIn, SigBminIn, SigBmaxIn 설명은 “IYType = 2 or 3”; DispFactorIn 등은 “IAType”; Figure 3(p.23)는 “IAType”. 본문 p.11에는 “DispFactorIn”이 쓰인다.
8. Table 1 RTIF-6/7(p.13)는 입출력에 각각 “Table 1”, “Table 2”를 참조한다. 이 보고서의 입력 표는 Table 2, 출력 표는 Table 3이며, §3.3(pp.16–17)는 Table 2와 Table 3을 참조한다.
9. Table 1(p.14~15)의 배열 순서는 (a/c, a/h, θ) 또는 (a/c, a/h). Table 3(p.20)의 표기는 [a/t, a/c, Segment Number] 또는 [a/t, a/c]. 기호표(p.viii)는 t를 “Time”이라고 한다.
10. p.10: “Timoshenko [7]”. References(p.27)의 [7]은 Edwards, Denny and Mills의 Transfer Processes, [8]은 Timoshenko and Goodier의 Theory of Elasticity다. §2.4.3(p.8)는 Ref. [8]을 인용한다.
11. §2.4(p.4)의 단계 (4)는 “due to the stresses in steps 3 and 4”라고 쓴다.
12. §2.4.1(p.6): “temperatuare”(본문 및 가정표). §2.4(p.4): “TIFFANYanalysis”, “discreet”, “the the”. §2.4.2(p.7): “theTIFFANY”. p.8: “differing” 두 번. p.7 가정표: “modulii”. §4(p.24): “recommendatioins”, “desireable”. 원문 철자를 유지했다.
13. pp.7–8: “the variation of E and µ ... compared to the variation of µ, thermal conductivity and diffusivity”라고 µ가 양쪽에 반복된다.
14. §2 첫 문장(p.3)은 “overlay)..”로 끝난다.

## 7. 전사 확인 범위

- Eqn. 1, 2, 3a, 3b, 3c, 4, 5a, 5b, 5c, 6: PDF 17~21쪽 렌더링 직접 확인.
- Figure 1(PDF 15), Figure 2(PDF 19), Figure 3(PDF 33): 이미지 직접 확인.
- Nomenclature(PDF 9), Table 2~4(PDF 28~31): 텍스트와 이미지 대조.
- §2.4.1 가정표, Table 1 RTIF-1~38, 약어표 및 본문: 원문 텍스트 전사. 가정표의 PDF 16~17쪽은 이미지와도 대조.
- 해석·교정·외부 문헌 보충 없음. 원문에 직접 정의가 없는 기호에는 “원문 정의 없음”을 표시했다.
