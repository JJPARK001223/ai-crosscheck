# round59 독립 전사 (Codex)

## 범위와 표기

- 원문: `J:\Desktop\XLPR\xLPR참고문헌\(ML16341B052)Crack initiation.pdf` (93쪽).
- 대상: PDF 11~93쪽. Claude 결과 파일은 열지 않았다.
- PDF 원본을 300 dpi PNG(2550×3300)로 렌더링하고 쪽별로 직접 판독한다. 중간 이미지는 `tmp/pdfs/round59/page-11.png`~`page-93.png`.
- 대괄호는 `[인쇄쪽/PDF쪽, 식 번호 또는 위치]`. 번호 없는 수학 표기는 `I쪽-순번`, 그림 속 식은 `G쪽-순번`으로 식별한다. 변수명만 등장하는 경우도 포함한다. 하나의 원문 수학 구절을 한 항목으로 세며, 표의 반복 수치·축 눈금은 식 개수에 합산하지 않는다. 원문 식 번호 참조만 나오는 문장은 새 식으로 세지 않는다.
- 영문 표·그림 문구는 원문을 유지한다. `↳병합`은 바로 앞에 명시한 셀의 연속 영역이며, 원문에 적힌 글자가 아니다.
- 번호식은 원문의 번호를 유지한다. 여러 줄이 한 번호를 공유하면 1식으로 센다. 번호 없는 기호·정의·표의 수학 셀은 위의 식별 항목 단위로 센다. 동일한 식이 다른 쪽에 재등장하면 별도 항목이다.

## 인쇄 1~6쪽 / PDF 11~16쪽

### [1/11]

번호식·인라인 수식·표·그림 없음. 본문의 기준 깊이는 `6 mm`.

### [2/12]

번호식·인라인 수식·표·그림 없음.

### [3/13]

- [3/13, I3-1, subunit 설명] \(N\) (called “N” times), \(N\) (“N” circumferential subunits).
- [3/13, I3-2, 마지막 문단] \(2*N\).
- [3/13, G3-1, Figure 1 위쪽] \(l=\dfrac{2\pi r_i}{N_{sgment}}\). 원문 그대로: 그림의 작은 첨자는 `sgment`로 보임 (600 dpi 확대 확인, `segment`로 교정하지 않음).
- [3/13, G3-2, Figure 1 분할 번호] \(1,\ 2,\ N,\ N-1\).
- Figure 1 문구: `Equal Length Subunits`.
- 캡션: `Figure 1. Component circumferential segmentation into subunits.`

### [4/14]

- [4/14, I4-1, 첫 문단] \(N\).
- Figure 2: `Example of Time Interval Partitioning Required for Interfacing with the PWSCC CI Module`.

| Refueling Outage | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Operating Temperature | T=T1 | T=T1 | T=T1 | T=T1 | T=T2 | T=T2 | T=T2 | T=T2 | T=T3 | T=T3 |
| Operating Pressure | P=P1 | P=P1 | P=P1 | P=P1 | P=P2 | P=P2 | P=P2 | P=P2 | P=P3 | P=P3 |
| Zinc Concentration | Zn = Zn1 (1~3 병합) | ↳병합 | ↳병합 | Zn = Zn2 (4~10 병합) | ↳병합 | ↳병합 | ↳병합 | ↳병합 | ↳병합 | ↳병합 |
| Mitigation Status | Unmitigated (1~6 병합) | ↳병합 | ↳병합 | ↳병합 | ↳병합 | ↳병합 | Mitigated (7~10 병합) | ↳병합 | ↳병합 | ↳병합 |
| Time Interval | 1 (1~3 병합) | ↳병합 | ↳병합 | 2 | 3 (5~6 병합) | ↳병합 | 4 (7~8 병합) | ↳병합 | 5 (9~10 병합) | ↳병합 |

- [4/14, G4-1, Figure 2] \(T=T1,\ T=T2,\ T=T3\).
- [4/14, G4-2, Figure 2] \(P=P1,\ P=P2,\ P=P3\).
- [4/14, G4-3, Figure 2] \(Zn=Zn1,\ Zn=Zn2\).
- Figure 3: `Example of Time Interval Definitions Expected by the Fatigue CI Module`.

| Refueling Outage | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Dissolved Oxygen | DO = DO1 (1~3 병합) | ↳병합 | ↳병합 | DO = DO2 (4~10 병합) | ↳병합 | ↳병합 | ↳병합 | ↳병합 | ↳병합 | ↳병합 |
| Mitigation Status | Unmitigated (1~6 병합) | ↳병합 | ↳병합 | ↳병합 | ↳병합 | ↳병합 | Mitigated (7~10 병합) | ↳병합 | ↳병합 | ↳병합 |
| Time Interval | 1 (1~3 병합) | ↳병합 | ↳병합 | 2 (4~6 병합) | ↳병합 | ↳병합 | 3 (7~10 병합) | ↳병합 | ↳병합 | ↳병합 |

- [4/14, G4-4, Figure 3] \(DO=DO1,\ DO=DO2\).

### [5/15]

번호식·인라인 수식·표·그림 없음.

### [6/16]

Figure 4. `Flow Diagram of the Version 2.0 xLPR PWSCC Crack Initiation Module Key Internal Operations`.

그림 문구 (위에서 아래, 좌우 분기 포함):

`Computational Framework or PWSCC CI DLL`; `Definition of time intervals from inputs`; `Temporal and spatial attributes of component and environment (e.g., stress, temperature, chemical concentrations)`; `Subunit loop: I = I + 1`; `Set of parameters for specific material and component type`; `Temporal attributes associated with subunit I`; `Inputs validated?`; `yes`; `no`; `Error Message`; `Calculate crack location`; `Circumferential location for crack initiating in subunit I`; `Time interval loop`; `Loop until PWSCC initiation time and location is calculated for all subunits`; `Attributes associated with current subunit and time interval and parameters associated with selected model`; `Select model based on model flag`; `Has the end of component life been reached?`; `Initiation time for crack initiating in subunit I`; `Direct Model 1`; `Direct Model 2`; `Weibull Model`; `Is cumulative damage greater than unity?`; `Incorporate chemistry effects`; `Interpolate initiation time`; `Initiation time associated with current time interval`; `Cumulate damage with Miner's rule`; `PWSCC CI Subroutine`; `This dotted line designate boundary of PWSCC CI module` (원문 그대로: designate).

- [6/16, G6-1, Figure 4 subunit loop] \(I=I+1\).
- [6/16, G6-2, Figure 4 세 상자] \(I\) (subunit 식별자).

## 인쇄 7~12쪽 / PDF 17~22쪽

### [7/17]

Figure 5. `Flow Diagram of the Version 2.0 xLPR Fatigue Crack Initiation Calculations.`

그림 문구: `Input xLPR control parameters: (NU, MTS, TST(MTS) & NL)`; `Input CI Material Properties: (μ & σ of C₀ & ε∞ + SURF, LOAD, CAL, MAT)`; `Input Initial Flaw Size Distribution Parameters`; `Heat-to-heat MC Sampling for C₀ & ε∞`; `Include all Subunits: “NU”`; `MC Sampling for C₀ & ε∞ (within-heat) + flaw size & location`; `Output tᵢ + location`; `Boundary for Fatigue CI Module Calculations`; `Include all Time Intervals: “MTS”`; `Include all Cyclic Transient loads: “NL”`; `Cyclic Transient Load Input: (n, σₐ, T, S, O, εdot)`; `Calculate Cenv & N`; `Calculate total damage, D for the current time`; `∑D > 1 for the current time?`; `All time intervals evaluated?`; `yes`; `no`; `Calculate tᵢ`; `Calculate location`.

- [7/17, G7-1, control parameters] \((NU,MTS,TST(MTS)\ \&\ NL)\).
- [7/17, G7-2, material properties] \((\mu\ \&\ \sigma\text{ of }C_0\ \&\ \varepsilon_\infty+SURF,LOAD,CAL,MAT)\).
- [7/17, G7-3, heat-to-heat] \(C_0\ \&\ \varepsilon_\infty\).
- [7/17, G7-4, within-heat] \(C_0\ \&\ \varepsilon_\infty\).
- [7/17, G7-5, output] \(t_i\).
- [7/17, G7-6, transient input] \((n,\sigma_a,T,S,O,\varepsilon_{dot})\).
- [7/17, G7-7, Calculate] \(C_{env}\ \&\ N\).
- [7/17, G7-8, damage] \(D\).
- [7/17, G7-9, 판정] \(\sum D>1\).
- [7/17, G7-10, Calculate] \(t_i\).

### [8/18] 2.3 Model Assumptions (번호 없는 가정표, 1/3)

병합 셀 없음. 다음 두 쪽으로 표가 이어진다.

| Assumption | Technical Support/ Reason for Assumption | Implication |
|---|---|---|
| PWSCC crack initiation is modeled separately from fatigue crack initiation, i.e., the effects are not superimposed and it is assumed that there is no interaction between the two models. | Industry experience has shown that these two initiation mechanism are generally observed separately at different locations and are caused by very different loading conditions. There is no clear technical basis defining the superposition of, or the interaction between these two initiation mechanisms. | The CI models developed for xLPR define a functional dependence of initiation time on the predominant drivers of fatigue **OR** PWSCC initiation. Other dependencies that are not explicitly used are captured with model uncertainty so this assumption is not believed to have any effect on the overall predictions of crack initiation. |
| To accommodate multiple crack initiation sites on a single component/weldment, the xLPR program divides each component/weldment into multiple subunits and assumes a single crack initiates within each subunit. | Industry experience shows that multiple cracks initiate at weld locations and coalescence into larger cracks during service. | None. CI Modules replicate observed cracking behavior. |
| All CI-specific conditions are assumed to remain constant within each time interval. Distinct time intervals are defined for each change in an operating load (e.g., operational pressure, operational temperature), residual stress or component thickness (which can be altered by surface stress improvement (SSI) or weld application), or zinc concentration. | To accommodate changes in initiation-relevant operating conditions, | As many of these changes occur over time intervals that are relatively short when compared to the simulation plant lifetime, this discretization is expected to have minimal impact on pipe leakage and rupture probabilities. |
| Miner's Rule assumed to represent damage accumulation towards initiation. | Miner's Rule is well-established method. | None. |
| Circumferential and axial cracks are assumed to behave independent of one another. | Observed field cracking does not show a significant degree of interaction between axial and circumferential cracks. | CI module is used to calculate initiation times for axial or circumferential cracks, but can only consider a single orientation each time it is called. |
| PWSCC crack initiation is assumed to be dependent on surface stress and operational temperature for all three crack initiation models developed. | It is widely accepted in the technical community that SCC is influenced by both temperature and surface stress | None. Any SCC initiation model needs to include both temperature and surface stress in the calculation of initiation times. |

`mechanism`, `coalescence`, `conditions,`, `independent`는 원문 그대로.

### [9/19] 가정표 (2/3)

| Assumption | Technical Support/ Reason for Assumption | Implication |
|---|---|---|
| The Direct Model 2 crack initiation model further assumes that cold work and other mechanical properties influence crack initiation times. | Test data and field experience show that cold work can influence initiation SCC times. | Provides additional capability and flexibility to the initiation capabilities of the xLPR Code. |
| The fatigue crack initiation model is assumed to be appropriately represented by a strain-based model suitable for low cycle fatigue applications with environmental effects limited to temperature, sulfur content, dissolved oxygen content and strain rate. | The fatigue model leverages the development work documented in NUREG/CR-6909. | The NUREG/CR-6909 work represents the best available model for low cycle fatigue however questions remain about its capability to include high cycle fatigue behavior. |
| Initiated cracks are assumed to be located on the center plane of the component/weldment. | This assumption is necessary for subsequent crack coalescence calculations for circumferential cracks and results in both ends of axial cracks reaching base metal at the same points in time. | The alternative approach to include random locations of cracks in the axial direction would require a three dimensional approach that is beyond the capabilities of the xLPR program. |
| Axial cracks are assumed to have symmetrical axial growth. | This assumption is necessary for axial cracks reaching base metal at the same points in time. | Including different crack growth rates at each end of axial cracks would double the amount of tracking required by the xLPR framework with very little additional insight into rupture behavior expected as a result. |
| Uncertainty characterization for the Direct Model 1 PWSCC crack initiation model is included by assuming the variables A and σth to be random variables. | This is a common approach in probabilistic modeling and has been shown to provide accurate predictions of initiation times as compared to laboratory data. | Keeps probabilistic initiation models simple and accurate. |
| Similar to the treatment of uncertainty in the Direct Model 1 crack initiation model, uncertainty characterization for the Direct Model 2 PWSCC crack initiation model is included by assuming the proportionality constant B to be a random variable. | This is a common approach in probabilistic modeling and has been shown to provide accurate predictions of initiation times as compared to laboratory data. | Keeps probabilistic initiation models simple and accurate. |
| Uncertainty characterization for the Weibull PWSCC crack initiation model is included by assuming the Weibull slope and adjusted scale parameters are random variables. Additionally there is uncertainty in the vertical intercept parameter, □c. | This is a common approach in probabilistic modeling and has been shown to provide accurate predictions of initiation times as compared to laboratory data. | Keeps probabilistic initiation models simple and accurate. |

- [9/19, I9-1, 가정표 5행] \(A,\ \sigma\mathrm{th}\) (th는 본문 크기; 원문 그대로).
- [9/19, I9-2, 가정표 6행] \(B\).
- [9/19, I9-3, 가정표 마지막 행] \(\square_{\mathrm c}\). 원문 그대로: 해당 글리프는 빈 네모로 보임. 원래 기호는 확인 불가.

### [10/20] 가정표 (3/3)

| Assumption | Technical Support/ Reason for Assumption | Implication |
|---|---|---|
| Uncertainty in the fatigue crack initiation model is included by considering Cₒ and ε∞ to be normally distributed random variables. | This is a common approach in probabilistic modeling and has been shown to provide accurate predictions of initiation times as compared to laboratory data. | Keeps probabilistic initiation models simple and accurate. |

- [10/20, I10-1, 가정표] \(C_o,\ \varepsilon_\infty\) (표의 C 첨자는 영문 o처럼 보임; 원문 그대로).
- [10/20, I10-2, 식 전 문장] \(\sigma\).
- [10/20, Eqn. 2-1]
\[
\frac{1}{t_{INI,nom}}=Ae^{-Q/RT}\sigma^n\qquad\sigma\geq\sigma_{th}
\]
- [10/20, I10-3, where 1] \(t_{INI,nom}=\text{initiation time under fixed set of conditions (output)}\).
- [10/20, I10-4, where 2] \(T=\text{temperature (input)}\).
- [10/20, I10-5, where 3] \(\sigma=\text{surface stress (input)}\).
- [10/20, I10-6, where 4] \(\sigma_{th}=\text{stress threshold parameter (input)}\).
- [10/20, I10-7, where 5] \(A=\text{Direct Model 1 proportionality constant (input)}\).
- [10/20, I10-8, where 6] \(n=\text{stress exponent (input)}\).
- [10/20, I10-9, where 7] \(Q=\text{activation energy for initiation (input)}\).
- [10/20, I10-10, where 8] \(R=\text{universal gas constant (input)}\).
- [10/20, I10-11, 마지막 문단 첫 문장] \(A,\ \sigma_{th}\).
- [10/20, I10-12, 마지막 문단 둘째 문장] \(Q,\ \sigma_{th}\) (원문 그대로: 온도·응력 효과 설명에 이 기호 사용).
- [10/20, I10-13, 마지막 문단 끝] \(A,\ \sigma_{th}\).

### [11/21]

Figure 6. `Example of Statistical Treatment of Initiation Time with Direct Method 1`.

그림 문구: `Stress (Mpa)` (원문 그대로); `Exposure Time (Hours)`; `90ᵗʰ Percentile`; `Mean`; `10ᵗʰ Percentile`. 세로 눈금 `1.E+02`, `1.E+03`, `1.E+04`; 가로 눈금 `1.E+02`, `1.E+03`, `1.E+04`, `1.E+05`, `1.E+06`.

- [11/21, I11-1, 첫 문단] \(N_{subunit}\).

### [12/22]

- [12/22, Eqn. 2-2]
\[
\begin{aligned}
\sigma_{th}&=z\sigma_{ys}\\
z&=z_1+z_2\ln(\xi)\\
\zeta&=\frac{\sigma_{ult}}{\sigma_{ys}}
\end{aligned}
\]
원문 그대로: 로그 안은 \(\xi\), 비율 정의 왼쪽은 \(\zeta\)로 보이며 혼용됨.

- [12/22, I12-1, where] \(\sigma_{ys}=\text{local yield stress (input)}\).
- [12/22, I12-2, where] \(\sigma_{ult}=\text{local ultimate stress (input)}\).
- [12/22, I12-3, where] \(z_1,z_2=\text{Direct Model 2 CW-SCC threshold parameters (input)}\).
- [12/22, Eqn. 2-3]
\[
\begin{aligned}
\sigma_{\max}&=D\sigma_{ys}\\
D&=v\cdot e^{w\cdot\zeta}\\
\zeta&=\frac{\sigma_{ult}}{\sigma_{ys}}
\end{aligned}
\]
- [12/22, I12-4, where] \(v,w=\text{Direct Model 2 cold work microcracking resistance parameters (input)}\).
- [12/22, Eqn. 2-4]
\[
t_{INI,nom}=BGe^{Q/RT}\ln\left[\frac{D-z}{\dfrac{\sigma}{\sigma_{ys}}-z}\right]
\]
- [12/22, Eqn. 2-5]
\[
G=m^{-q}\frac{\ln(D)}{\ln\left(\dfrac{D-z}{1-z}\right)}
\]
- [12/22, Eqn. 2-6] \(D=v\cdot e^{w\zeta}\).

## 인쇄 13~18쪽 / PDF 23~28쪽

### [13/23]

- [13/23, Eqn. 2-7] \(z=z_1+z_2\ln(\zeta)\).
- [13/23, Eqn. 2-8] \(m=k\left(\dfrac{\sigma_{ys}}{E}\right)^a(\zeta-1)^b(\zeta)^c\).
- [13/23, Eqn. 2-9] \(\zeta=\dfrac{\sigma_{ult}}{\sigma_{ys}}\).
- [13/23, I13-1, and] \(t_{INI,nom}=\text{initiation time under fixed set of conditions (output)}\).
- [13/23, I13-2] \(T=\text{temperature (input)}\).
- [13/23, I13-3] \(\sigma=\text{surface stress (input)}\).
- [13/23, I13-4] \(E=\text{local elastic modulus (input)}\).
- [13/23, I13-5] \(Q=\text{activation energy for initiation (input)}\).
- [13/23, I13-6] \(R=\text{universal gas constant (input)}\).
- [13/23, I13-7] \(B=\text{Direct Model 2 proportionality constant (input)}\).
- [13/23, I13-8] \(q=\text{Direct Model 2 environment-cold-work exponent (input)}\).
- [13/23, I13-9] \(a,b,c,k=\text{Direct Model 2 general cold work parameters (input)}\).
- [13/23, I13-10, calibration 문단] \(N_{subunit}\).

### [14/24]

- [14/24, Eqn. 2-10]
\[
\begin{aligned}
\ln(-\ln(1-F))&=\beta\ln(t)-\beta\ln(\theta)\\
y&=\beta x+c
\end{aligned}
\]
- [14/24, I14-1] \(F=\text{cumulative distribution function}\).
- [14/24, I14-2] \(t=\text{time}\).
- [14/24, I14-3] \(\beta=\text{general Weibull slope parameter}\).
- [14/24, I14-4] \(\theta=\text{Weibull scale parameter}\).
- [14/24, I14-5] \(c=\text{“vertical intercept parameter”}\).
- [14/24, I14-6] \(x=\text{general independent variable used in regression}\).
- [14/24, I14-7] \(y=\text{general dependent variable used in regression}\).
- [14/24, I14-8, Estimation 문단] \(\beta,\ c\).

### [15/25]

- [15/25, Eqn. 2-11]
\[
c=-\hat\beta\ln\left(\frac{t_1}{\left(-\ln(1-F_1)\right)^{1/\hat\beta}}\right)+\varepsilon_c
\]
- [15/25, I15-1] \(\hat\beta=\text{best fit Weibull slope (input)}\).
- [15/25, I15-2] \(t_1=\text{pivot time (input)}\).
- [15/25, I15-3] \(F_1=\text{percent of components with flaw at pivot time (input)}\).
- [15/25, I15-4] \(\varepsilon_c=\text{vertical intercept error (input)}\).
- [15/25, Eqn. 2-12] \(\theta_{ref}=\exp[-c/\beta]\).
- [15/25, I15-5] \(\beta=\text{random Weibull slope (input)}\).
- [15/25, Eqn. 2-13]
\[
\theta=\exp\left[\frac{Q}{R}\left(\frac1T-\frac1{T_{ref}}\right)\right]\left(\frac{\sigma}{\sigma_{ref}}\right)^{-n}(N_{subunit})^{1/\beta}\theta_{ref}
\]

### [16/26]

- [16/26, I16-1] \(T=\text{temperature (input)}\).
- [16/26, I16-2] \(\sigma=\text{surface stress (input)}\).
- [16/26, I16-3] \(n=\text{stress exponent (input)}\).
- [16/26, I16-4] \(Q=\text{activation energy for initiation (input)}\).
- [16/26, I16-5] \(R=\text{universal gas constant (input)}\).
- [16/26, I16-6] \(N_{subunit}=\text{number of subunits (input)}\).
- [16/26, I16-7] \(T_{ref},\sigma_{ref}=\text{reference temperature and stress parameters (inputs)}\).
- [16/26, Eqn. 2-14]
\[
t_{INI,nom}=\theta\left(( -\ln(U_{INI}))^{1/\beta}\right)
\]
- [16/26, I16-8] \(t_{INI,nom}=\text{initiation time under fixed set of conditions (output)}\).
- [16/26, I16-9] \(U_{INI}=\text{uniform random seed used to sample Weibull distribution (input)}\).
- [16/26, Eqn. 2-15] \(\varepsilon_a=\dfrac{B}{N^b}+\varepsilon_\infty\).
- [16/26, I16-10, 마지막 문장] \(B\) (scaling parameter).

### [17/27]

- [17/27, Eqn. 2-16]
\[
\ln(N)=C_o+C_{env}-\frac1b\ln(\varepsilon_a-\varepsilon_\infty)-\ln(F_{Surf})-\ln(F_{Load})-\ln(F_{Cal})\ ,
\]
원문 그대로: 이 식과 본문의 첨자는 영문 \(o\), Figure 5 등에서는 숫자 \(0\)으로 보임.

아래 where는 원문의 정렬된 정의 목록을 3열로 전사 (병합 없음).

| 기호 | 원문 연산자 | 정의 |
|---|---|---|
| \(N\) | = | Number of cycles to fatigue crack initiation |
| \(C_o\) | = | Low-cycle fatigue variable (normal distribution) |
| \(C_{env}\) | = | Deterministic environmental variable |
| \(b\) | = | Slope of low-cycle fatigue (material-dependent constant) |
| \(\varepsilon_a\) | = | Strain amplitude |
| \(\varepsilon_\infty\) | = | Strain endurance limit (normal distribution) |
| \(F_{Surf}\) | = | Factor capturing effects of surface finish (log-normal distribution) |
| \(F_{Load}\) | = | Factor capturing the uncertainty in the loading history (log-normal distribution) |
| \(F_{Cal}\) | = | User-defined factor used to calibrate the fatigue crack initiation model to match empirical component data or other user requirements (constant or log-normal distribution) |

- [17/27, I17-1~I17-9, where] 위 표의 9개 기호 정의를 각 1식으로 센다.
- [17/27, I17-10, probabilistic 문단 1문장] \(C_o,\varepsilon_\infty\).
- [17/27, I17-11, 2문장] \(\varepsilon_a,\varepsilon_\infty\).
- [17/27, I17-12, 3문장] \(C_o,\varepsilon_\infty\).
- [17/27, I17-13, 4문장] \(C_{env}\).
- [17/27, I17-14, 5문장] \(F_{Surf},F_{Load}\).
- [17/27, I17-15, 2.5 첫 문단] \(t_{INI,i}\).
- [17/27, I17-16, bulleted requirements 전] \(D\).
- [17/27, I17-17, 마지막 bullet] \(D_i\).

### [18/28]

- [18/28, Eqn. 2-17] \(D=\displaystyle\sum_{i=1}D_i\). 원문 그대로: 합의 상한 없음.
- [18/28, I18-1, 첫 bullet 끝] \(m\).
- [18/28, Eqn. 2-18] \(\displaystyle\sum_{i=1}^{m-1}D_i<1\leq\sum_{i=1}^{m}D_i\).
- [18/28, I18-2, 둘째 bullet] \(m\).
- [18/28, Eqn. 2-19]
\[
t_{INI}=\sum_{i=1}^{m-1}\Delta t_i+\frac{\Delta t_m}{D_m-D_{m-1}}(1-D_{m-1})
\]
- [18/28, Eqn. 2-20] \(D_i=\dfrac{\Delta t_i}{t_{INI,i}}\).
- [18/28, I18-3] \(\Delta t_i=\text{duration of time interval }i\text{ (input)}\).
- [18/28, I18-4] \(t_{INI,i}=\text{initiation time under conditions of time interval }i\text{ (calculated)}\).
- [18/28, Eqn. 2-21]
\[
D_i=\Delta t_i\sum_j^{NL}\frac{n_j}{N_j(\sigma_{a,j})}
\]
원문 그대로: 합의 하한은 \(j\)만 있고 등호·시작값 없음.

## 인쇄 19~24쪽 / PDF 29~34쪽

### [19/29]

- [19/29, I19-1] \(NL=\text{number of loads in each interval}\).
- [19/29, I19-2] \(n_j=\text{number of applied cycles per year for each load “}j\text{”}\).
- [19/29, I19-3] \(N_j(\sigma_{a,j})=\text{allowable cycles for the load “}j\text{” with stress amplitude }\sigma_{a,j}\).
- [19/29, I19-4, Use 문단] \(N_j(\sigma_{a,j}),\ \sigma_{a,j}\).
- [19/29, I19-5, 2.6 첫 문단] \(0,\ 2\pi\).
- [19/29, I19-6, 2.6 둘째 문단] \(N_{subunit}\).
- [19/29, I19-7, 2.7 첫 문단] \(a,\ b\) (crack depth, half crack length).
- [19/29, I19-8, During sampling 문장] \(b,\ a,\ b,\ a\). 원문은 “b” is less than “a”, then “b” should be set equal to “a”.
- [19/29, I19-9, For initial PWSCC 문단] \(a,\ b\).

번호 없는 초기 균열 분포 매개변수 배열 (병합 없음):

| 원문 행 이름 | 평균 | 표준편차 |
|---|---|---|
| Crack depth “a”: | \(\mu_a=6.5\ \mathrm{mm};\) | \(\sigma_a=0.35\ \mathrm{mm}\) |
| Crack length “b” | \(\mu_b=5.34\ \mathrm{mm};\) | \(\sigma_b=0.8\ \mathrm{mm}\) |

- [19/29, I19-10, 위 배열 1행] \(\mu_a=6.5\ \mathrm{mm};\ \sigma_a=0.35\ \mathrm{mm}\).
- [19/29, I19-11, 위 배열 2행] \(\mu_b=5.34\ \mathrm{mm};\ \sigma_b=0.8\ \mathrm{mm}\).
- 하한 절단값 원문: `0.5 mm`.
- [19/29, I19-12, 마지막 문단] \(a,\ b\).

### [20/30]

번호 없는 초기 fatigue 분포 매개변수 배열 (병합 없음):

| 원문 행 이름 | 평균 | 표준편차 |
|---|---|---|
| Crack depth “a”: | \(\mu_a=3.0\ \mathrm{mm};\) | \(\sigma_a=0.05\ \mathrm{mm}\) |
| Crack length “b” | \(\mu_b=8.608\ \mathrm{mm};\) | \(\sigma_b=4.849\ \mathrm{mm}\) |

- [20/30, I20-1, 배열 1행] \(\mu_a=3.0\ \mathrm{mm};\ \sigma_a=0.05\ \mathrm{mm}\).
- [20/30, I20-2, 배열 2행] \(\mu_b=8.608\ \mathrm{mm};\ \sigma_b=4.849\ \mathrm{mm}\).
- [20/30, I20-3, 2.8.1 첫 문장] \(A,\sigma_{th}\).
- [20/30, I20-4, 둘째 문장] \(A,\sigma_{th}\).
- [20/30, I20-5, Additionally] \(A\).
- [20/30, I20-6, temperature and stress effects] \(Q,\sigma_{th}\) (원문 그대로).
- [20/30, I20-7, 둘째 문단 첫 문장] \(B\).
- [20/30, I20-8, 둘째 문단 Additionally] \(B\).
- [20/30, I20-9, 둘째 문단 끝] \(B\).
- [20/30, I20-10, Weibull 문단] \(\varepsilon_c\).
- [20/30, I20-11, 마지막 문단 slope] \(\beta\).
- [20/30, I20-12, scale] \(\theta\).
- [20/30, I20-13, 두 independent parameters] \(\beta,\theta\).

### [21/31]

- [21/31, I21-1, 첫 문단 numerical estimates] \(\beta,\theta\).
- [21/31, I21-2, i.e.] \(\beta,c\).
- [21/31, I21-3, correlation term] \(\beta,c\).
- [21/31, I21-4, 2.8.2 첫 문장] \(C_o,\varepsilon_\infty\).
- [21/31, I21-5, 둘째 문장] \(C_o,\varepsilon_\infty\).
- [21/31, I21-6, environmental term] \(C_{env}\).
- [21/31, I21-7, factors] \(F_{Surf},F_{Load}\).
- [21/31, I21-8, 마지막 문단 proportionality constants] \(A,B\).
- [21/31, I21-9, fatigue random variables] \(C_o,\varepsilon_\infty\).
- [21/31, I21-10, first step mean values] \(A,B,C_o,\varepsilon_\infty\).
- [21/31, I21-11, heat-to-heat standard deviations] \(\sigma_{h-h}\).
- [21/31, I21-12, These terms] \(A'_0,B'_0,C'_0,\varepsilon'_\infty\).
- [21/31, I21-13, second step terms] \(A'_0,B'_0,C'_0,\varepsilon'_\infty\).
- [21/31, I21-14, within-heat standard deviations] \(\sigma_{w-h}\).
- [21/31, I21-15, sampled values] \(A,B,C_o,\varepsilon_\infty\).

### [22/32]

번호식·인라인 수식·표·그림 없음 (서브루틴명은 일반 코드 식별자).

### [23/33]

Figure 7. `Use Case Diagram of CI_PWSCC subroutine and outside actors`.

그림 문구: `Computational Group`; `Initiation Subgroup`; `xLPR GoldSim Framework`; `PWSCC CI DLL Wrapper`; `CI_PWSCC Subroutine`; `PWSCC CI Calculation`.

Figure 8. `Component diagram of PWSCC CI module logical and deployment architecture`.

그림 문구: `PWSCC CI DLL File`; `xLPR GoldSim Framework`; `PWSCC CI DLL Wrapper`; `CI_PWSCC Subroutine`; `DirectModel1 Function`; `DirectModel2 Subroutine`; `WeibullModel Function`. 수학식 없음.

### [24/34]

번호식·인라인 수식·표·그림 없음.

## 인쇄 25~30쪽 / PDF 35~40쪽

### [25/35] Table 1. PWSCC CI Subroutine Arguments List

구분 행 `General Initiation Time Model Inputs`, `Direct 1 Model Inputs`, `Direct 2 Model Inputs`, `Weibull Model Inputs`, `Outputs`는 각각 7열 전체 병합.

| # | Description | Symbol Used in this SRD | Required Units | Range of Validity¹ | Data Type | Sample Frequency |
|---|---|---|---|---|---|---|
| 1 | Number of subunits | \(N_{subunit}\) | - | \(0<N_{subunit}\leq100\) | integer | - |
| 2 | Current subunit number | \(I_{subunit}\) | - | \(0<I_{subunit}\leq N_{subunit}\) | integer | - |
| 3 | Number of time intervals in operating history | \(MTS\) | - | \(0<MTS\leq10\) | integer | - |
| 4 | Initiation time model flag | \(I_{method}\) | - | \(I_{method}=1,2,3\) | integer | - |
| 5 | Material flag | \(I_{material}\) | - | \(I_{material}=1,2\) | integer | - |
| 6 | Initiation location random variable | \(U_{loc}\) | - | \(0\leq U_{loc}<1\) | real | per subunit |
| 7 | Duration for each time interval | \(\Delta t(MTS)\) | EFPY | \(\Delta t(ITS)>0\) | real array | - |
| 8 | Zinc concentration | \(C_{Zn}(MTS)\) | ppb | \(C_{Zn}(ITS)\geq0\) | real array | - |
| 9 | Zinc concentration threshold | \(C_{Zn,th}\) | ppb | \(C_{Zn,th}\geq0\) | real | - |
| 10 | Zinc factor of improvement | \(FOI_{Zn}\) | - | \(FOI_{Zn}>0\) | real | per weld |
| General Initiation Time Model Inputs (7열 병합) | ↳병합 | ↳병합 | ↳병합 | ↳병합 | ↳병합 | ↳병합 |
| 11 | Surface stress in subunit | \(\sigma(MTS)\) | MPa | - | real array | - |
| 12 | Component temperature | \(T(MTS)\) | K | \(T(ITS)>0\) | real array | - |
| 13 | Activation energy | \(Q\) | kJ/mol | \(Q>0\) | real | - |
| 14 | Universal gas constant | \(R\) | kJ/K-mol | \(R>0\) | real | - |
| Direct 1 Model Inputs (7열 병합) | ↳병합 | ↳병합 | ↳병합 | ↳병합 | ↳병합 | ↳병합 |
| 15 | Proportionality constant | \(A\) | \((1/\mathrm{EFPY})(1/\mathrm{MPa}^{n})\) | \(A>0\) | real | per weld / per subunit |
| 16 | Stress threshold | \(\sigma_{th}\) | MPa | \(\sigma_{th}>0\) | real | per weld |
| 17 | Direct Model 1 stress exponent | \(n\) | - | \(n\geq0\) | real | - |
| Direct 2 Model Inputs (7열 병합) | ↳병합 | ↳병합 | ↳병합 | ↳병합 | ↳병합 | ↳병합 |
| 18 | Proportionality constant | \(B\) | EFPY | \(B>0\) | real | per weld / per subunit |
| 19 | CW-SCC threshold parameter 1 | \(z_1\) | - | \(z_1>0\) | real | - |
| 20 | CW-SCC threshold parameter 2 | \(z_2\) | - | \(z_2>0\) | real | - |
| 21 | cold work microcracking resistance parameter 1 | \(v\) | - | \(v>0\) | real | - |
| 22 | cold work microcracking resistance parameter 2 | \(w\) | - | \(w>0\) | real | - |
| 23 | environment-cold-work exponenet | \(q\) | - | \(q>0\) | real | - |
| 24 | general cold work parameter 1 | \(a\) | - | \(a>0\) | real | - |
| 25 | general cold work parameter 2 | \(b\) | - | \(b<0\) | real | - |
| 26 | general cold work parameter 3 | \(c\) | - | \(c<0\) | real | - |
| 27 | general cold work parameter 4 | \(k\) | - | \(k>0\) | real | - |
| 28 | Yield stress for subunit | \(\sigma_{ys}\) | MPa | \(\sigma_{ys}>0\) | real | - |
| 29 | Ultimate stress for subunit | \(\sigma_{uts}\) | MPa | \(\sigma_{uts}\geq\sigma_{ys}\) | real | - |
| 30 | Elastic modulus | \(E\) | MPa | \(E>0\) | real | - |
| Weibull Model Inputs (7열 병합) | ↳병합 | ↳병합 | ↳병합 | ↳병합 | ↳병합 | ↳병합 |
| 31 | Best fit Weibull slope | \(\hat\beta\) | - | \(\hat\beta>0\) | real | - |
| 32 | Pivot time | \(t_1\) | EDY | \(t_1>0\) | real | - |
| 33 | Percent of components with crack at pivot time | \(F_1\) | - | \(0<F_1<1\) | real | - |
| 34 | Vertical intercept error | \(\varepsilon_c\) | - | - | real | per weld |
| 35 | Weibull slope | \(\beta\) | - | \(\beta>0\) | real | per weld |
| 36 | Weibull model stress exponent | \(n\) | - | \(n\geq0\) | real | - |
| 37 | Reference temperature | \(T_{ref}\) | K | \(T_{ref}>0\) | real | - |
| 38 | Reference stress | \(\sigma_{ref}\) | MPa | \(\sigma_{ref}>0\) | real | - |
| 39 | Initiation time random variable | \(U_{INI}\) | - | \(0<U_{INI}\leq1\) | real | per subunit |
| Outputs (7열 병합) | ↳병합 | ↳병합 | ↳병합 | ↳병합 | ↳병합 | ↳병합 |
| 40 | Initiation location for subunit | \(\theta_{INI}\) | rad | - | real | - |
| 41 | Initiation time for subunit | \(t_{INI}\) | EFPY | - | real | - |
| 42 | Error flag | \(I_{error}\) | - | - | integer | - |

¹ `The symbol ITS is intended to indicate each entry in an array`.

- [25/35, T1-1~T1-42, Table 1 행 번호 대응] 각 행의 기호·단위식·유효범위를 하나의 수학 항목으로 계수한다 (42항목).
- [25/35, I25-1, 각주] \(ITS\).
- 원문 그대로: `exponenet` 오타, \(\sigma_{uts}\) (앞의 본문 \(\sigma_{ult}\)와 다름), `EDY` 단위.

### [26/36] Table 2. Fatigue Crack Initiation Module Arguments List

`Inputs`, `Outputs` 구분 행은 각각 6열 병합.

| DLL Element | Input Variable | Description (units) | Sample Value | Limits | Data Type |
|---|---|---|---|---|---|
| Inputs (6열 병합) | ↳병합 | ↳병합 | ↳병합 | ↳병합 | ↳병합 |
| 1 | NU | Number of sub-units (none) | 19 | \(0<NU\leq100\) | Integer |
| 2 | NSUB | Subunit number | 3 | \(1\leq NSUB\leq NU\) | Integer |
| 3 | MTS | Number of time intervals (none) | 3 | \(0<MTS\leq10\) | Integer |
| 4 | NL | Number of loads in operating history (none) | 9 | \(0<NL\leq30\) | Integer |
| 5 | MAT | Material type ID: 1-LAS, 2-CS, 3-Austenitic, 4-Ni-Cr-Fe, 5-other (none) | 3 | 1 - 5 | Integer |
| 6 | RAND | Random number for location | .3 | \(0\leq RAND<1\) | Real(8) |
| 7 | TST(MTS) | Time Intervals (EFPY) | 9.85 | \(>0\) | Real(8) |
| 8 | O2(MTS) | Oxygen Term for each load (ppm) | .002 | \(>0\) | Real(8) |
| 9 | NCYC(NL) | Cycles/year for each load (\(\mathrm{EFPY}^{-1}\)) | 125 | \(>0\) | Real(8) |
| 10 | DELT(NL,MTS) | Rise Time for each load (sec) | 100 | \(>0\) | Real(8) |
| 11 | STRMX(NL,MTS) | Maximum Stress for each load (MPa) | 75 | \(\geq STRMN\) | Real(8) |
| 12 | STRMN(NL,MTS) | Minimum Stress for each load (MPa) | 30 | none | Real(8) |
| 13 | TEMAX(NL,MTS) | Maximum Temperature for each load (°C) | 200 | \(\geq TEMIN\) | Real(8) |
| 14 | TEMIN(NL,MTS) | Minimum Temperature for each load (°C) | 200 | none | Real(8) |
| 15 | CENV(NL,MTS) | Environmental Factor: MAT=5 (none) | .05 | \(>0\) | Real(8) |
| 16 | SUL | Sulfur Content (wt. %) | .015 | 0 - 100 | Real(8) |
| 17 | E | Elastic Modulus (MPa) | 200,000 | \(>0\) | Real(8) |
| 18 | B | Exponent in ε-N relationship (none) | 0.553 | \(>0\) | Real(8) |
| 19 | STH | Sampled value of \(\varepsilon_\infty\) (%) | .151 | \(>0\) | Real(8) |
| 20 | C0 | Sampled value of \(C_0\) (none) | 5.747 | \(>0\) | Real(8) |
| 21 | FSURF | Surface Factor (none) | 2.21 | \(>0\) | Real(8) |
| 22 | FLOAD | Load Factor (none) | 1.28 | \(>0\) | Real(8) |
| 23 | FCAL | Calibration Factor (none) | 1.0 | \(>0\) | Real(8) |
| Outputs (6열 병합) | ↳병합 | ↳병합 | ↳병합 | ↳병합 | ↳병합 |
| 24 | INITIME | Initiation time (EFPY) | 3.5 | \(>0\) | Real(8) |
| 25 | LOCCRACK | Location of initiated crack (radians) | 0.261 | \(0\mathrel{<=}LocCrack\mathrel{<=}2\pi\) | Real(8) |
| 26 | IERROR | Error code (none) | 0 | \(0\mathrel{<=}Ierror\mathrel{<=}399\) | Integer |

- [26/36, T2-1~T2-26, Table 2 행 번호 대응] 각 행의 변수·수학 표기·제한을 1항목으로 계수 (26항목). 원문 그대로: 마지막 두 행은 실제 `<`와 `=`를 연이어 표기, Input Variable과 대소문자 다름.

### [27/37]

- [27/37, Eqn. 3-1] \(t=\Lambda\cdot g(T,\sigma,\ldots;Q,n,\ldots)\).
- [27/37, I27-1, Dependent variable] \(t\).
- [27/37, I27-2, Explanatory variables] \(T,\sigma\).
- [27/37, I27-3, Effects model] \(g\).
- [27/37, I27-4, Effects model parameters] \(Q,n\).
- [27/37, I27-5, thermal activation energy] \(Q\).
- [27/37, I27-6, Failure time model random variable] \(\Lambda\).

### [28/38]

- [28/38, I28-1, 마지막에서 둘째 문단] \(Q,\ n,\ \sigma_{th}\) (activation energy, surface stress exponent, surface stress threshold).
- [28/38, I28-2, 첫 bullet] \(Q=185\ \mathrm{kJ/mole}\).
- [28/38, I28-3, 둘째 bullet] \(n=5\).
- [28/38, I28-4, 셋째 bullet] \(\sigma_{th}=0\) for the Direct Model 1 and Weibull Models.

### [29/39]

- [29/39, I29-1, probabilistic component 문단] \(A\).
- [29/39, I29-2, 같은 문장] \(B\).
- [29/39, I29-3, Weibull distribution parameters] \(\beta,\theta\).

### [30/40]

- [30/40, I30-1, 둘째 bullet] \(N\) subunits.

## 인쇄 31~36쪽 / PDF 41~46쪽

### [31/41] Table 3. Effects Model Parameters for Base Cases

| Description | Units | Distribution Parameter | Value for Base Case |
|---|---|---|---|
| Activation energy | kJ/mol | deterministic | 185.0 |
| Stress exponent for Direct Model 1 and Weibull model | Nondim | deterministic | 5.0 |
| Reference temperature parameter for Weibull model | K | deterministic | 588.7 |
| Reference stress parameter for Weibull model | MPa | deterministic | 325.0 |
| Stress threshold for Direct Model 1 | MPa | deterministic | 0.0 |
| Direct Model 2 cold work parameters (9행 병합) | Nondim (9행 병합) | \(z_1\) | 0.35 |
| ↳병합 | ↳병합 | \(z_2\) | 0.333 |
| ↳병합 | ↳병합 | \(v\) | 0.66 |
| ↳병합 | ↳병합 | \(w\) | 0.5 |
| ↳병합 | ↳병합 | \(q\) | 0.375 |
| ↳병합 | ↳병합 | \(a\) | 0.25 |
| ↳병합 | ↳병합 | \(b\) | -0.75 |
| ↳병합 | ↳병합 | \(c\) | -0.25 |
| ↳병합 | ↳병합 | \(k\) | 8.20 |
| Zinc factor of improvement (4행 병합) | Nondim (4행 병합) | type | Shifted Log-normal |
| ↳병합 | ↳병합 | log-\(\mu\) | -0.29 |
| ↳병합 | ↳병합 | log-\(\sigma\) | 0.93 |
| ↳병합 | ↳병합 | shift | 1.00 |

- [31/41, T3-1~T3-11, Table 3 수학 기호 행] \(z_1,z_2,v,w,q,a,b,c,k,\log\text{-}\mu,\log\text{-}\sigma\)를 위 행 순서대로 11항목으로 계수.
- [31/41, Eqn. 3-2]
\[
\begin{aligned}
t&=\Lambda\cdot g(T,\sigma;Q,n)\\
g&=e^{Q/(RT)}\sigma^{-n}
\end{aligned}
\]

### [32/42]

- [32/42, I32-1, where 첫 줄] \(\Lambda=\dfrac1A\).
- [32/42, I32-2, where 둘째 줄] \(A\sim\log\text{-}N\ (\mu_A,\sigma_A)\).

Table 4. `Direct Model 1 Parameter Recommendations`.

| Description | Units | Characterization of Uncertainty | Distribution Parameters | Model Parameters |
|---|---|---|---|---|
| Number of subunits | - | deterministic | best-estimate | 19 |
| Thermal activation energy | kJ/mol | deterministic | best-estimate | 185.0 |
| Inverse proportionality constant, \(A\) (component-to-component) (3행 병합) | - (3행 병합) | distributed (epistemic) (3행 병합) | type | Log-Normal |
| ↳병합 | ↳병합 | ↳병합 | log-norm \(\mu\) | 0.00 |
| ↳병합 | ↳병합 | ↳병합 | log-norm \(\sigma\) | 2.89 |
| Inverse proportionality constant, \(A\) (within-component) (3행 병합) | \((1/\mathrm{EFPY})(1/\mathrm{MPa}^{5})\) (3행 병합) | distributed (aleatory) (3행 병합) | type | Log-Normal |
| ↳병합 | ↳병합 | ↳병합 | log-norm \(\mu\) | -4.40 |
| ↳병합 | ↳병합 | ↳병합 | log-norm \(\sigma\) | 3.66 |
| Stress threshold | MPa | deterministic | best-estimate | 0.0¹ |
| Stress exponent | - | deterministic | best-estimate | 5.0 |

Notes (1): `The PWSCC initiation module of xLPR Version 2.0 does not allow the stress threshold input to be less than or equal to zero. Therefore, the Direct Model 1 stress threshold input to xLPR should be set to an arbitrarily small positive value to emulate this report's recommendation of 0 MPa.`

- [32/42, T4-1~T4-6, Table 4] \(A\) (component), \(\mu\), \(\sigma\), \(A\) 및 단위식 (within), \(\mu\), \(\sigma\)의 6항목.

### [33/43]

- [33/43, Eqn. 3-3]
\[
\begin{aligned}
t&=\Lambda\cdot g(T,\sigma,\sigma_{ys},\sigma_{ult},E;Q,z_1,z_2,v,w,q,a,b,c,k)\\
g&=Ge^{Q/RT}\ln\left[\frac{D-z}{\dfrac{\sigma}{\sigma_{ys}}-z}\right]
\end{aligned}
\]
- [33/43, I33-1, where] \(\Lambda=B\).
- [33/43, I33-2, where] \(B\sim\log\text{-}N\ (\mu_B,\sigma_B)\).

Table 5. `Direct Model 2 Parameter Recommendations`.

| Description | Units | Characterization of Uncertainty | Distribution Parameters | Model Parameters |
|---|---|---|---|---|
| Number of subunits | - | deterministic | best-estimate | 19 |
| Thermal activation energy | kJ/mol | deterministic | best-estimate | 185.0 |
| Inverse proportionality constant, \(B\) (component-to-component) (3행 병합) | - (3행 병합) | distributed (epistemic) (3행 병합) | type | Log-Normal |
| ↳병합 | ↳병합 | ↳병합 | log-norm \(\mu\) | 0.00 |
| ↳병합 | ↳병합 | ↳병합 | log-norm \(\sigma\) | 1.49 |
| Inverse proportionality constant, \(B\) (within-component) (3행 병합) | EFPY (3행 병합) | distributed (aleatory) (3행 병합) | type | Log-Normal |
| ↳병합 | ↳병합 | ↳병합 | log-norm \(\mu\) | -28.43 |
| ↳병합 | ↳병합 | ↳병합 | log-norm \(\sigma\) | 1.91 |
| Cold work parameters | - | deterministic | best-estimate | see Table 3 |

- [33/43, T5-1~T5-6, Table 5] \(B,\mu,\sigma,B,\mu,\sigma\)의 6항목.

### [34/44]

- [34/44, Eqn. 3-4]
\[
\begin{aligned}
t&=\Lambda\cdot g(T,\sigma,N;Q,n,T_{ref},\sigma_{ref})\\
g&=\exp\left[\frac{Q}{R}\left(\frac1T-\frac1{T_{ref}}\right)\right]\left(\frac\sigma{\sigma_{ref}}\right)^{-n}N^{1/\beta}
\end{aligned}
\]
- [34/44, I34-1, where] \(\Lambda\sim W(\beta,c)\).
- [34/44, I34-2, where] \(F_W(t;\beta,c)=1-\exp\left[-t^\beta\exp(c)\right]\).

### [35/45] Table 6. Weibull Model Parameter Recommendations

| Description | Units | Characterization of Uncertainty | Distribution Parameters | Model Parameters |
|---|---|---|---|---|
| Number of subunits | - | deterministic | best-estimate | 19 |
| Thermal activation energy | kJ/mol | deterministic | best-estimate | 185.0 |
| Pivot time¹˒² | EFPY | deterministic | best-estimate | 10.4 |
| Percent of components with crack at pivot time² | % | deterministic | best-estimate | 10.0 |
| Vertical intercept error (3행 병합) | - (3행 병합) | distributed (epistemic) (3행 병합) | type | Normal |
| ↳병합 | ↳병합 | ↳병합 | mean | 0.00 |
| ↳병합 | ↳병합 | ↳병합 | st dev | 0.38 |
| Weibull slope (3행 병합) | - (3행 병합) | distributed (epistemic) (3행 병합) | type | Normal |
| ↳병합 | ↳병합 | ↳병합 | mean | 0.45 |
| ↳병합 | ↳병합 | ↳병합 | st dev | 0.08 |
| Correlation between vertical intercept error and Weibull slope³ | - | deterministic | best-estimate | -0.800 |
| Stress exponent | - | deterministic | best-estimate | 5.0 |
| Reference temperature | K | deterministic | best-estimate | 588.7 |
| Reference stress | MPa | deterministic | best-estimate | 325.0 |

Notes:

(1) `The adjustment in Eq. 3-4 requires that N is the number of independent samples taken (i.e., two times the number of subunits when both orientations are simulated). However, the implementation in xLPR uses the number of subunits, resulting in a factor of 2¹/ᵝ bias in the initiation time prediction. This bias is corrected by subtracting ln(2) from the vertical intercept derived in Section 7 of [4].`

(2) `The pivot time and the percent of components with a crack at the pivot time are inputs to xLPR Version 2.0. These parameters may be interpreted as follows: given a best-estimate slope of 0.45 and a best-estimate vertical intercept of -3.30, the percent of components (10.0%) is expected to experience PWSCC by the pivot time (10.4 EFPY). They are directly related to the best-estimate vertical intercept (c) and slope (β) used throughout this report with a simple algebraic equation (e.g., Eq. 3-4).`

(3) `Correlation expressed here and elsewhere in this report refers to Pearson's correlation coefficient for two normal distributions.`

- [35/45, I35-1, note 1] \(N\).
- [35/45, I35-2, note 1] \(2^{1/\beta}\).
- [35/45, I35-3, note 1] \(\ln(2)\).
- [35/45, I35-4, note 2] \(c,\beta\).
- [35/45, I35-5, 3.2.5 inputs] \(C_{env}\).
- [35/45, I35-6, inputs] \(S^*,O^*,T^*,\dot\varepsilon^*\).
- [35/45, I35-7, calculated] \(C_{env}\).
- [35/45, I35-8, 마지막 문장] \(0.02,10^{-6}\) curves.

### [36/46]

번호식·인라인 수식·표·그림 없음 (기존 식 번호에 대한 참조만 있음).

## 인쇄 37~42쪽 / PDF 47~52쪽

### [37/47] Table 7. Constants in Fatigue Life Relation in Water¹

위 표의 상위 머리글 `NUREG/CR-6909 [14]`는 LAS~Ni-Cr-Fe의 4열 병합. `Generic` 머리글은 2행 병합. 맨 왼쪽 기호열은 Cₒ·ε∞ 행에서만 별도로 돌출된다. 아래의 빈 셀은 실제 무기재 영역.

| 기호 | 세부 항목 | LAS² | CS² | Austenitic² | Ni-Cr-Fe² | Generic (머리글 2행 병합) |
|---|---|---|---|---|---|---|
| (외곽 셀 없음) | \(1/b\) | 1.808 | 1.975 | 1.920 | 1.920 | (빈 셀) |
| \(C_o\) (3행 병합) | Mean | 5.747 | 5.951 | 6.157 | 6.157 | TBD (Mean Cₒ~Cenv까지 7행 병합) |
| ↳병합 | h-h Stdev. | 0.484 | 0.488 | 0.411 | 0.411 | ↳병합 |
| ↳병합 | w-h Stdev. | 0.534 | 0.430 | 0.368 | 0.368 | ↳병합 |
| \(\varepsilon_\infty\) (3행 병합) | Mean | 0.151 | 0.113 | 0.112 | 0.112 | ↳병합 |
| ↳병합 | h-h Stdev. | 0.017 | 0.020 | 0.019 | 0.019 | ↳병합 |
| ↳병합 | w-h Stdev. | 0.019 | 0.017 | 0.017 | 0.017 | ↳병합 |
| (외곽 셀 없음) | \(C_{env}\) | \(0.101S^*T^*O^*\dot\varepsilon^*\) (LAS·CS 병합) | ↳병합 | \(T^*O^*\dot\varepsilon^*\) | \(T^*O^*\dot\varepsilon^*+0.734\) | ↳병합 |

하단 표 (3열, 병합 없음). 수식을 모두 해당 셀에 전사한다.

| CS & LAS | Austenitic | Ni-Cr-Fe |
|---|---|---|
| \(S^*=\begin{cases}0.015&DO>1.0\,ppm\\0.001&DO\leq1.0\,ppm\ \&\ S\leq0.001\,wt\%\\S&DO\leq1.0\,ppm\ \&\ 0.001<S\leq0.015\,wt\%\\0.015&DO\leq1.0\,ppm\ \&\ S>0.015\,wt\%\end{cases}\) | Not applicable | Not applicable |
| \(T^*=\begin{cases}0&T\leq150^{\circ}C\\T-150&150<T\leq350^{\circ}C\end{cases}\) | \(T^*=\begin{cases}0&T<150^{\circ}C\\(T-150)/175&150\leq T<325^{\circ}C\\1&T\geq325^{\circ}C\end{cases}\) | \(T^*=\begin{cases}T/325&T<325^{\circ}C\\1&T\geq325^{\circ}C\end{cases}\) |
| \(O^*=\begin{cases}0&DO\leq0.04\,ppm\\\ln(DO/0.04)&.04\,ppm<DO\leq0.5\,ppm\\\ln(12.5)&DO>0.5\,ppm\end{cases}\) | \(O^*=0.281\quad\text{All DO Levels}\) | \(O^*=0.16\quad\text{All DO Levels}\) |
| \(\dot\varepsilon^*=\begin{cases}0&\dot\varepsilon>1\%/s\\\ln(\dot\varepsilon)&.001\leq\dot\varepsilon\leq1\%/s\\\ln(0.001)&\dot\varepsilon<0.001\%/s\end{cases}\) | \(\dot\varepsilon^*=\begin{cases}0&\dot\varepsilon>0.4\%/s\\\ln(\dot\varepsilon/0.4)&.0004\leq\dot\varepsilon\leq0.4\%/s\\\ln(0.0004/0.4)&\dot\varepsilon<0.0004\%/s\end{cases}\) | \(\dot\varepsilon^*=\begin{cases}0&\dot\varepsilon>5.0\%/s\\\ln(\dot\varepsilon/5.0)&.0004\leq\dot\varepsilon\leq5.0\%/s\\\ln(0.0004/5.0)&\dot\varepsilon<0.0004\%/s\end{cases}\) |

- [37/47, T7-1~T7-7, 상단 표 수학 셀] \(1/b\), \(C_o\), \(\varepsilon_\infty\), \(C_{env}\), CS·LAS의 Cenv 식, Austenitic의 Cenv 식, Ni-Cr-Fe의 Cenv 식 (7항목).
- [37/47, T7-8~T7-17, 하단 표] S*의 CS&LAS 1식, T*의 3식, O*의 3식, ε̇*의 3식, 행 우선 순서 (10항목).
- 원문 그대로: CS & LAS strain-rate 셀 둘째 조건 시작값 `.001`에는 단위가 붙지 않음. CS&LAS T* 표의 상한은 350°C.

### [38/48] Table 7의 계속

| (빈 머리글) | □ (Log Space) | □ (Log Space) | Distribution |
|---|---|---|---|
| Surface Factor, \(F_{surf}\) | 0.973 | 0.170 | Log-normal |
| Surface Factor, \(F_{load}\) | 0.438 | 0.155 | Log-normal |
| Surface Factor, \(F_{cal}\) | User Defined³ | User Defined³ | Constant or Log-normal |

병합 셀 없음. 원문 그대로: 세 행 모두 `Surface Factor`라고 적혀 있고 머리글 두 기호는 빈 네모로 렌더링됨. 해당 네모의 의도된 기호는 확인 불가.

각주:

1. `All values in Table 7 calculated using the supporting data for NUREG/CR-6909 as described in Attachment A of Reference [20].`
2. `Units are as follows: Temperatures in degrees Celsius, strains in %, strain rates in %/sec, oxygen concentration in parts per million (ppm), and sulfur content in wt. %.`
3. `Default to constant Fcal = 1.0, assuming subunits are approximately 2 inches in length.`

- [38/48, T7-18, 머리글] \(\square,\square\).
- [38/48, T7-19~T7-21, 세 행] \(F_{surf},F_{load},F_{cal}\) (각 1항목).
- [38/48, I38-1, 각주 3] \(F_{cal}=1.0\).

### [39/49]

Figure 9. `Strain-Life Curves at Various Probability Levels for Low Alloy Steel [15]`.

그림 문구: 세로 `Strain Amplitude, %`, 가로 `Cycles`; 곡선 표지 `.5`, `.02`, `10⁻⁶`. 세로 눈금 `1`, `0.5`, `0.1`, `5 x 10⁻²`; 가로 `1`, `10`, `10²`, `10³`, `10⁴`, `10⁵`, `10⁶`, `10⁷`.

- [39/49, G39-1, Figure 9 곡선 표지] \(.5,\ .02,\ 10^{-6}\).

### [40/50]

번호식·인라인 수식·표·그림 없음 (`t-test`는 검사 명칭).

### [41/51]

Figure 10. `Orientation-Specific Analysis: Time to First Flaw Statistics (19 Subunits), Reference Conditions are 318°C and 200 MPa.`

그림 문구: 세로 `Cumulative Probability`, 가로 `First Initiation Time (EFPY)`; 범례 `All Flaws`, `Axial Flaws Only`, `Circumferential Flaws Only`; 세로 눈금 `0`, `0.02`, `0.04`, `0.06`, `0.08`, `0.1`, `0.12`; 가로 눈금 `0`, `20`, `40`, `60`, `80`. 그림 속 식 없음.

### [42/52]

Figure 11. `Near-Surface Stress Sensitivity Cases: Initiation Time Distributions (19 Subunits), Reference Condition is 318°C`.

그림 문구: 세로 `Probability of Initiation`, 가로 `First Initiation Time (EFPY)`; 범례 `Base Case`, `Assuming 100 MPa`, `Assuming 200 MPa`, `Assuming 300 MPa`; 세로 눈금 0~1, 0.1 간격; 가로 `0`, `20`, `40`, `60`, `80`. 그림 속 식 없음.

## 인쇄 43~48쪽 / PDF 53~58쪽

### [43/53]

- [43/53, Eqn. 3-5] \(D=\sqrt n\left(\sup\left|\hat S(t)-S_\Lambda(t)\right|\right)\).
- [43/53, I43-1, where] \(n=\text{total number of data points.}\).
- [43/53, I43-2, early times] \(<80\ \text{years}\).

### [44/54]

Figure 12. `Weibull Plot Validation`.

그림 문구: 세로 `Cumulative Fraction of Welds with Initiations`; 가로 `Time at 315°C and 325 MPa (yr)`; 범례 `Weibull Model (Best-Estimate)`, `Weibull Model (5th and 95th Percentile)`, `Realization 1`, `Realization 2`, `Realization 3`, `Realization 4`. 세로 눈금 `0.90`, `0.63`, `0.50`, `0.20`, `0.10`, `0.05`, `0.02`, `0.01`, `0.005`, `0.002`, `0.001`; 가로 `0.1`, `1`, `10`, `100`, `1000`, `10000` (왼쪽 아래 0.001/0.1 겹침은 원문 그대로).

- [44/54, Eqn. 3-6] \(y(t)=\Phi^{-1}(F_\Lambda(t))\).
- [44/54, I44-1, where] \(\Phi^{-1}=\text{inverse standard normal cumulative distribution function}\).

### [45/55]

Figure 13. `Validation for Direct Model 1 (N=19): Comparing Time-to-First Flaw Prediction against Kaplan-Meier Statistic for Independent International Field Experience`.

그림 문구: 세로 `Cumulative Fraction of Welds with Initiations (Log-Normal-Transformed)`; 가로 `Time at 315°C and 325 MPa (yr)`; 범례 `Direct Model 1`, `International Data: Realization 1`, `Realization 2`, `Realization 3`, `Realization 4`. 세로 눈금 `0.90`, `0.63`, `0.50`, `0.20`, `0.10`, `0.05`, `0.02`, `0.01`, `0.005`, `0.002`, `0.001`; 가로 `0.1`, `1`, `10`, `100`, `1000`, `10000`.

- [45/55, G45-1, Figure 13 캡션] \(N=19\).

### [46/56]

Figure 14. `Direct Model 1 (N=19): Comparing Time-to-First Flaw Prediction against Kaplan-Meier Statistic for Independent Laboratory Experience`.

그림 문구: 세로 `Cumulative Fraction of Welds with Initiations (Log-Normal-Transformed)`; 가로 `Time at 315°C and 325 MPa (yr)`; 범례 `Direct Model 1`, `Laboratory Initiation Data (Kaplan-Meier)`. 세로 눈금 `0.90`, `0.63`, `0.50`, `0.20`, `0.10`, `0.05`, `0.02`, `0.01`, `0.005`, `0.002`, `0.001`; 가로 `0.1`, `1`, `10`, `100`, `1000`, `10000`.

- [46/56, G46-1, Figure 14 캡션] \(N=19\).

### [47/57]

- [47/57, I47-1, 첫 문단 fatigue data] \(\varepsilon\text{-}N\).
- [47/57, I47-2, key LWR parameters] \(T,S,DO,\dot\varepsilon\).
- [47/57, I47-3, strain amplitude] \(\varepsilon\).
- [47/57, I47-4, 둘째 문단 environmental effects] \(C_{env}\).
- [47/57, I47-5, user-defined terms] \(F_{Surf},F_{Load},F_{Cal}\).
- [47/57, I47-6, recommended factors] \(F_{Surf},F_{Load}\).
- [47/57, I47-7, 셋째 문단 fatigue data] \(\varepsilon\text{-}N\).
- [47/57, I47-8, comparisons factors] \(F_{surf},F_{load},F_{cal}\) (원문은 이 위치에서 소문자 첨자).

### [48/58]

Figure 15. `Experimentally observed and predicted fatigue lives of carbon steels in LWR environments without any adjustments for actual plant operation [14]`.

그림 문구: `Carbon Steels`; `100-300°C`; `LWR Environments`; 세로 `Predicted Life (Cycles)`; 가로 `Observed Life (Cycles)`; 범례 `A106-Gr. B` (빨간 △), `A333-Gr. 6` (녹색 ○), `A516` (보라 ◇), `A508-1` (황색 ▽); 양축 눈금 \(10^1,10^2,10^3,10^4,10^5,10^6\). 그림 속 식 없음.

## 인쇄 49~54쪽 / PDF 59~64쪽

### [49/59]

Figure 16. `Activity Diagram of CI_PWSCC Subroutine Process Flow`.

그림 문구: `CI_PWSCC subroutine`; `IMTS = time interval index`; `MTS = number of time intervals (input)`; `CumDam = cumulative total of damage across time intervals`; `Imethod = flag for selection of initiation model`; `Allocate Variables`; `Validate Inputs`; `Calculate Intermediate Variables`; `Calculate Crack Location`; `[Imethod=1]`; `[Imethod=2]`; `[Imethod=3]`; `Run Direct Model 1`; `Run Direct Model 2`; `Run Weibull Model`; `Update Cumulative Damage and Time`; `[CumDam ≥ 1 OR CumDam = -1]`; `[0 < CumDam < 1]`; `[IMTS < MTS]`; `[IMTS = MTS]`; `Save Conditions at End of Cycle`; `IMTS = IMTS + 1`; `Calculate Initiation Time for Initiated Crack`; `Calculate Initiation Time for No Initiation`.

- [49/59, G49-1~G49-4, 범례 정의 4줄] \(IMTS=\text{time interval index}\); \(MTS=\text{number of time intervals (input)}\); \(CumDam=\text{cumulative total of damage across time intervals}\); \(Imethod=\text{flag for selection of initiation model}\) (각 줄 1항목).
- [49/59, G49-5] \([Imethod=1]\).
- [49/59, G49-6] \([Imethod=2]\).
- [49/59, G49-7] \([Imethod=3]\).
- [49/59, G49-8] \([CumDam\geq1\ \mathrm{OR}\ CumDam=-1]\).
- [49/59, G49-9] \([0<CumDam<1]\).
- [49/59, G49-10] \([IMTS<MTS]\).
- [49/59, G49-11] \([IMTS=MTS]\).
- [49/59, G49-12] \(IMTS=IMTS+1\).

### [50/60]

Figure 17. `Activity Diagram of CI_F Subroutine Process Flow`.

그림 문구: `CI_F subroutine`; `IMTS = time interval index`; `INL = load index`; `MTS = number of time intervals (input)`; `NL = number of loads in operating history (input)`; `EpsAmp = strain amplitude`; `EpsTh = sampled value of ε∞ (input)`; `CumDamRate = cumulative damage rate across all time intervals`; `CumDam = cumulative damage across all time intervals`; `Initialize Variables`; `Validate Inputs`; `Calculate Crack Location`; `Calculate Material-Specific Parameters`; `CumDamRate = 0`; `Calculate Time Interval-Specific Parameters`; `Calculate Load-Dependent Parameters`; `[EpsAmp < EpsTh]`; `[EpsAmp ≥ EpsTh]`; `INL = INL + 1`; `IMTS = IMTS + 1`; `Calculate Environmental Factor`; `Update Cumulative Damage Rate`; `[INL < NL]`; `[INL = NL]`; `Save Conditions at End of Cycle`; `[IMTS < MTS]`; `Calculate Fatigue Damage`; `[CumDam < 1]`; `[CumDam ≥ 1]`; `[IMTS = MTS]`; `Calculate Initiation Time for Initiated Crack`; `Set Initiation Time for No Initiation`.

- [50/60, G50-1, 범례] \(IMTS=\text{time interval index}\).
- [50/60, G50-2, 범례] \(INL=\text{load index}\).
- [50/60, G50-3, 범례] \(MTS=\text{number of time intervals (input)}\).
- [50/60, G50-4, 범례] \(NL=\text{number of loads in operating history (input)}\).
- [50/60, G50-5, 범례] \(EpsAmp=\text{strain amplitude}\).
- [50/60, G50-6, 범례] \(EpsTh=\text{sampled value of }\varepsilon_\infty\text{ (input)}\).
- [50/60, G50-7, 범례] \(CumDamRate=\text{cumulative damage rate across all time intervals}\).
- [50/60, G50-8, 범례] \(CumDam=\text{cumulative damage across all time intervals}\).
- [50/60, G50-9] \(CumDamRate=0\).
- [50/60, G50-10] \([EpsAmp<EpsTh]\).
- [50/60, G50-11] \([EpsAmp\geq EpsTh]\).
- [50/60, G50-12] \(INL=INL+1\).
- [50/60, G50-13] \(IMTS=IMTS+1\).
- [50/60, G50-14] \([INL<NL]\).
- [50/60, G50-15] \([INL=NL]\).
- [50/60, G50-16] \([IMTS<MTS]\).
- [50/60, G50-17] \([CumDam<1]\).
- [50/60, G50-18] \([CumDam\geq1]\).
- [50/60, G50-19] \([IMTS=MTS]\).

### [51/61]

- [51/61, I51-1, 4.1 첫 문단] \(F_{surf},F_{load}\).
- [51/61, I51-2, 4.1 둘째 문단] \(F_{Surf},F_{Load},F_{Cal}\).
- [51/61, I51-3, 4.2 slope·scale] \(\beta,\theta\).
- [51/61, I51-4, distribution function] \(\beta,c\).
- [51/61, I51-5, uncertainty assigned] \(\beta,c\).
- [51/61, I51-6, characteristic time] \(\theta\).
- [51/61, I51-7, uncertainty] \(\beta,c\).
- [51/61, I51-8, 마지막 문장 uncertainty in] \(c\).
- [51/61, I51-9, 마지막 adjust] \(\theta\).

### [52/62]

- [52/62, I52-1, 첫 문장 model form] \(\beta,\theta\).
- [52/62, I52-2, 첫 문장 uncertainty] \(\beta,\theta\).
- [52/62, I52-3, correlation i.e.] \(\beta\text{ and }c\text{ or }\theta\).
- [52/62, I52-4, 4.3 첫 문단 coefficients] \(z_1,z_2\).

### [53/63]

- [53/63, I53-1, material factor] \(I_m\).

### [54/64]

- [54/64, I54-1, 마지막 bullet] \(\mathrm{stress}^{-5}\) (원문 문장: initiation time is proportional to stress⁻⁵).

## 인쇄 55~59쪽 및 A-1 / PDF 65~70쪽

| 인쇄쪽/PDF쪽 | 직접 확인 결과 |
|---|---|
| 55/65 | 본문 계속. 수식·표·그림 없음. |
| 56/66 | SUMMARY. 수식·표·그림 없음. |
| 57/67 | REFERENCES [1]~[14]. 수식·표·그림 없음. |
| 58/68 | REFERENCES [15]~[32]. 수식·표·그림 없음. |
| 59/69 | REFERENCES [33]~[39]. 수식·표·그림 없음. |
| A-1/70 | 부록 구분지 `ATTACHMENT A: PIB VERTICAL SLICE REVIEW PWSCC INITIATION`. 수식·표·그림 없음. |

위 표는 원문 표가 아닌 확인 기록이다.

## 부록 A-2~A-7 / PDF 71~76쪽

### [A-2/71]

수식·표·그림 없음.

### [A-3/72]

- [A-3/72, IA3-1, Current subunit number 문단] \(\pm2\pi/N\). 원문 그대로 (subunit 1의 top dead center 범위).
- [A-3/72, IA3-2, Number of subunits 문단] \(K\)-controlled cracks.

### [A-4/73]

수식·표·그림 없음.

### [A-5/74]

수식·표·그림 없음.

### [A-6/75]

수식·표·그림 없음.

### [A-7/76]

- [A-7/76, IA7-1, Zinc factor c)] \(\log\text{-}\mu=-0.29,\quad\log\text{-}\sigma=0.93\).
- [A-7/76, IA7-2, e)] \(z\)-scores (문장 속 기호).

각주 4: 위 매개변수는 log-normal random variable의 natural logarithm에 대한 mean 및 standard deviation (또는 자연로그로 변환한 자료의 sample mean 및 standard deviation)을 뜻한다. 별도 식 없음.

## 부록 A-8~A-13 / PDF 77~82쪽

### [A-8/77]

- [A-8/77, IA8-1, 마지막 d)] \(\log\text{-}\mu=7.12\).
- [A-8/77, IA8-2, 마지막 d), weld-to-weld] \(\log\text{-}\sigma=1.16\).
- [A-8/77, IA8-3, 마지막 d), within-weld] \(\log\sigma=1.07\) (원문 그대로: 이 위치는 log와 σ 사이 하이픈 없음).

### [A-9/78]

수학 기호로 된 식·표·그림 없음. 수치로 서술된 분포: Weibull slope normal distribution average `1.419`, standard deviation `0.082`; vertical intercept error normal distribution average `zero`, standard deviation `0.304` (c항).

### [A-10/79]

- [A-10/79, IA10-1, Initial Crack Depth b)] \(K\)-calculation.
- 각주 5의 검출 크기 범위: laboratory `0.4-2 mm`, field `1-3 mm`.

### [A-11/80]

- [A-11/80, IA11-1, initial depth d)] \(\log\text{-}\mu\text{ of }-6.50\).
- [A-11/80, IA11-2, 같은 문장] \(\log\text{-}\sigma\text{ of }0.35\). 원문 수치: median `1.5 mm`, lower truncation `0.5 mm`.
- [A-11/80, IA11-3, 두번째 원형 bullet] \(K\)-solution.
- [A-11/80, IA11-4, Initial Crack Half-Length c)] \(\log\text{-}\mu\text{ of }-5.34\).
- [A-11/80, IA11-5, 같은 문장] \(\log\text{-}\sigma\text{ of }0.8\). median `4.8 mm`.

### [A-12/81]

수식·표·그림 없음.

### [A-13/82]

- [A-13/82, IA13-1, References 5의 명칭] \(\beta\mathrm{xLPR}\) (원문 문헌 제목 속 표기).

## 부록 A-14 및 B-1~B-5 / PDF 83~88쪽

### [A-14/83]

참고문헌 계속. 수식·표·그림 없음.

### [B-1/84]

부록 구분지 `ATTACHMENT B: PIB VERTICAL SLICE REVIEW FATIGUE INITIATION`. 수식·표·그림 없음.

### [B-2/85]

- [B-2/85, 식 (1)]
\[
\ln(N)=C_o+C_{env}-\frac1b\ln(\varepsilon_a-\varepsilon_\infty)-\ln(F_{Surf})-\ln(F_{load})-\ln(F_{cal})
\]
원문 그대로: \(C_o\)의 첨자는 영문 o로 보임. F 첨자 Surf는 대문자 S이며 load와 cal은 소문자.

- [B-2/85, IB2-1, random variable 목록 1] \(C_0\).
- [B-2/85, IB2-2, 목록 2] \(\varepsilon_\infty\).
- [B-2/85, IB2-3, 목록 3] \(F_{surf}\).
- [B-2/85, IB2-4, 목록 4] \(F_{load}\).
- [B-2/85, IB2-5, 목록 5] \(F_{cal}\).
- [B-2/85, IB2-6, 마지막 문단 constants] \(C_{env},b\).
- [B-2/85, IB2-7, input variable] \(\varepsilon_a\).
- [B-2/85, IB2-8, 마지막 문장] \(C_{env}\).

### [B-3/86]

- [B-3/86, IB3-1, 둘째 문단 treatment] \(C_0,\varepsilon_\infty\).
- [B-3/86, IB3-2, RVs reviewed] \(F_{surf},F_{load},F_{cal}\).
- [B-3/86, IB3-3, 소제목] \(C0,\varepsilon\infty\) (원문 그대로: 제목의 0와 ∞는 본문 크기).
- [B-3/86, IB3-4, 마지막 문단 RVs] \(C_0,\varepsilon_\infty\).
- [B-3/86, IB3-5, constant] \(C_{env},b\).
- [B-3/86, IB3-6, coefficient] \(C\).
- [B-3/86, IB3-7, slope] \(b\).

### [B-4/87]

Figure B-1. `Distributions of C₀ and ε∞ showing the 10% and 90% probability levels.`

그림 문구: 세로 `Strain Amplitude, (%)`; 가로 `Fatigue Life, (Cycles)`; `90ᵗʰ Percentile`, `Mean`, `10ᵗʰ Percentile`. 세로 눈금 `10`, `1`, `0.1`; 가로 `1.E+03`, `1.E+04`, `1.E+05`, `1.E+06`, `1.E+07`.

- [B-4/87, GB4-1, Figure B-1 캡션] \(C_0,\varepsilon_\infty\).
- [B-4/87, IB4-1, primary quantities] \(C_0,\varepsilon_\infty\).
- [B-4/87, IB4-2, remaining quantities] \(F_{surf},F_{load},F_{cal}\).
- [B-4/87, IB4-3, fatigue life] \(N\).
- [B-4/87, IB4-4, variances] \(C_0,\varepsilon_\infty\).
- [B-4/87, IB4-5, Following Reference 5] \(C_0,\varepsilon_\infty\).
- [B-4/87, IB4-6, lognormal] \(N\).

Table B-1. `Summary of Development of Values of Distribution Parameters` (1/2).

| (빈 머리글) | Carbon Steel (CS) | Low-Alloy Steel (LAS) | Stainless steel (SS) | Ni-Cr-Fe |
|---|---|---|---|---|
| \(C_0\) (5열 전체 병합) | ↳병합 | ↳병합 | ↳병합 | ↳병합 |
| Mean | Taken directly from NUREG/CR-6909, Equations 20, 21 & 34 for CS, LAS & SS respectively [2,3] (CS~SS 3열 병합) | ↳병합 | ↳병합 | Assumed same as stainless steel as recommended by NUREG-6909. (3행 병합) |
| Variance (heat-to-heat) | Calculated from heat specific data provided by G. Stevens. Heat-to-heat variance calculated using the mean \(C_0\) values for each heat provided in [3]. (CS~SS 3열 병합) | ↳병합 | ↳병합 | ↳병합 |
| Variance (within-heat) | Calculated from heat specific data provided by G. Stevens. Within-heat variance calculated as the average of all individual heat variances in [3]. (CS~SS 3열 병합) | ↳병합 | ↳병합 | ↳병합 |
| \(\varepsilon_\infty\) (5열 전체 병합) | ↳병합 | ↳병합 | ↳병합 | ↳병합 |

- [B-4/87, TB1-1, C₀ 구분행] \(C_0\).
- [B-4/87, TB1-2, heat-to-heat 설명] \(C_0\).
- [B-4/87, TB1-3, ε∞ 구분행] \(\varepsilon_\infty\).

### [B-5/88] Table B-1 계속 (2/2)

위쪽에서 머리글 반복 없이 이어짐. 원문 그대로 `NUREG-6909`.

| (행 이름) | Carbon Steel (CS) | Low-Alloy Steel (LAS) | Stainless steel (SS) | Ni-Cr-Fe |
|---|---|---|---|---|
| Mean | Taken directly from NUREG/CR-6909, Equations 20, 21 & 34 for CS, LAS & SS respectively [2,3] (CS~SS 3열 병합) | ↳병합 | ↳병합 | Assumed same as stainless steel as recommended by NUREG-6909. (3행 병합) |
| Variance (heat-to-heat) | Total variance taken from NUREG/CR-6335 [6]. Due to insufficient data for \(\varepsilon_\infty\), the heat-to-heat and within-heat variances are proportioned to be same as relative proportion defined for \(C_0\) for the CS, LAS & SS materials (CS~SS 3열 및 2행 병합) | ↳병합 | ↳병합 | ↳병합 |
| Variance (within-heat) | ↳병합 | ↳병합 | ↳병합 | ↳병합 |

- [B-5/88, TB1-4, 병합 설명셀] \(\varepsilon_\infty,C_0\).

Table B-2. `Constants in Fatigue Life Relation in Water`.

상위 머리글 `NUREG/CR-6909 [3]`는 LAS~Ni-Cr-Fe 4열 병합. 기호열은 Cₒ·ε∞ 부분에만 별도 돌출.

| 기호 | 세부 항목 | LAS | CS | Austenitic | Ni-Cr-Fe |
|---|---|---|---|---|---|
| (외곽 셀 없음) | \(1/b\) | 1.808 | 1.975 | 1.920 | 1.920 |
| \(C_o\) (3행 병합) | Mean | 5.747 | 5.951 | 6.157 | 6.157 |
| ↳병합 | h-h Stdev. | 0.484 | 0.488 | 0.411 | 0.411 |
| ↳병합 | w-h Stdev. | 0.534 | 0.430 | 0.368 | 0.368 |
| \(\varepsilon_\infty\) (3행 병합) | Mean | 0.151 | 0.113 | 0.112 | 0.112 |
| ↳병합 | h-h Stdev. | 0.017 | 0.020 | 0.019 | 0.019 |
| ↳병합 | w-h Stdev. | 0.019 | 0.017 | 0.017 | 0.017 |

- [B-5/88, TB2-1~TB2-3, Table B-2 기호] \(1/b,C_o,\varepsilon_\infty\) (각 1항목).
- [B-5/88, IB5-1, iii 응답] \(C_0,\varepsilon_\infty\).
- [B-5/88, IB5-2, iv 응답 distributions] \(C_0,\varepsilon_\infty\).
- [B-5/88, IB5-3, parameters for] \(C_0,\varepsilon_\infty\).
- [B-5/88, IB5-4, e.g. 목록] \(\mu\_\mathrm{C0},\ \sigma\_\mathrm{C0}\ (h\text{-}h),\ \sigma\_\mathrm{C0}\ (w\text{-}h),\ \mu\_\varepsilon\infty,\ \sigma\_\varepsilon\infty\ (h\text{-}h),\ \sigma\_\varepsilon\infty\ (w\text{-}h)\). 원문 그대로: 이 목록은 실제 밑줄 문자 `_`와 본문 크기 C0·ε∞ 표기를 사용.

## 부록 B-6~B-10 / PDF 89~93쪽

### [B-6/89]

- [B-6/89, IB6-1, 첫 문장 coefficient] \(C\).
- [B-6/89, IB6-2, 첫 문장 slope] \(b\).
- [B-6/89, IB6-3, Alternatively] \(b\).
- [B-6/89, IB6-4, both parameters] \(C_0,b\).
- [B-6/89, IB6-5, correlation between] \(C_0,b\).
- [B-6/89, IB6-6, 마지막 문장] \(C_0,b\).
- [B-6/89, IB6-7, This question] \(F_{surf},F_{load},F_{cal}\).
- [B-6/89, IB6-8, 소제목 Random Variables] \(F_{surf},F_{load},F_{cal}\).
- [B-6/89, IB6-9, development of RV models] \(C_0,\varepsilon_\infty\).
- [B-6/89, IB6-10, uncertainty factors] \(F_{surf},F_{load},F_{cal}\).
- [B-6/89, IB6-11, i 응답 RVs] \(C_0,\varepsilon_\infty\).
- [B-6/89, IB6-12, i 응답 factors] \(F_{surf},F_{load},F_{cal}\). 원문 그대로: \(F_{cal}\) 다음에 문장 중간 마침표가 붙어 `Fcal.are`로 보임.
- [B-6/89, IB6-13, ii 응답 treatment] \(F_{surf},F_{load}\).
- [B-6/89, IB6-14, surface finish] \(F_{surf}\).
- [B-6/89, IB6-15, load sequence] \(F_{load}\).
- [B-6/89, IB6-16, e.g. input values] \(\mu\text{'s}\ \&\ \sigma\text{'s}\).

Table B-3. `Fsurf, Fload and Fcal Factors` (머리글은 B-6, 데이터는 B-7).

| (빈 머리글) | \(\mu\) (Log Space) | \(\sigma\) (Log Space) | Distribution |
|---|---|---|---|

- [B-6/89, TB3-1, 캡션] \(F_{surf},F_{load},F_{cal}\).
- [B-6/89, TB3-2, 머리글] \(\mu,\sigma\).

### [B-7/90] Table B-3 데이터 계속

아래 머리글은 위쪽 B-6의 머리글을 독자의 열 대응을 위해 반복한 것. 병합 셀 없음.

| (빈 머리글) | \(\mu\) (Log Space) | \(\sigma\) (Log Space) | Distribution |
|---|---|---|---|
| Surface Factor, \(F_{surf}\) | 0.973 | 0.170 | Log-normal |
| Load Factor, \(F_{load}\) | 0.438 | 0.155 | Log-normal |
| Calibration Factor, \(F_{cal}\) | User Defined¹ | User Defined¹ | Constant or Log-normal |

각주 원문: `5. Default to constant Fcal = 1.0, assuming subunits are approximately 2 inches in length.` 원문 그대로: 표의 참조는 ¹인데 각주 앞 번호는 `5.`.

- [B-7/90, TB3-3~TB3-5, 데이터 세 행] \(F_{surf},F_{load},F_{cal}\) (각 1항목).
- [B-7/90, IB7-1, 각주] \(F_{cal}=1.0\).
- [B-7/90, IB7-2, 첫 문단 시작] \(F_{cal}\).
- [B-7/90, IB7-3, application] \(F_{cal}\).
- [B-7/90, IB7-4, iii 응답] \(F_{surf},F_{load},F_{cal}\).
- [B-7/90, IB7-5, iv 응답 evaluate] \(F_{surf},F_{load}\).
- [B-7/90, IB7-6, iv 응답 nature] \(F_{surf},F_{load}\).
- [B-7/90, IB7-7, v 응답 첫 문장] \(C_0\).
- [B-7/90, IB7-8, For parameters] \(F_{surf},F_{load}\).
- [B-7/90, IB7-9, factors can be defined] \(F_{surf},F_{load}\).
- [B-7/90, IB7-10, uncertainty associated] \(C_0,\varepsilon_\infty\).
- [B-7/90, IB7-11, uncertainty with] \(F_{surf},F_{load}\).
- [B-7/90, IB7-12, distribution parameters] \(F_{surf},F_{load}\).
- [B-7/90, IB7-13, uncertainty assigned] \(F_{surf},F_{load}\).
- [B-7/90, IB7-14, sampled values] \(N\).
- [B-7/90, IB7-15, 마지막 문단] \(F_{load}\).

### [B-8/91]

- [B-8/91, IB8-1, Question 3 응답 RV 목록] \(C_0,\varepsilon_\infty,F_{surf},F_{load},F_{cal}\).
- [B-8/91, IB8-2, mean values] \(C_0,\varepsilon_\infty\).
- [B-8/91, IB8-3, constant] \(C_{env}\).
- [B-8/91, IB8-4, comparisons effects] \(F_{surf},F_{load}\).
- [B-8/91, IB8-5, Simulation studies] \(F_{surf},F_{load}\).

### [B-9/92]

- [B-9/92, IB9-1, fatigue exponent] \(1/b\).
- [B-9/92, IB9-2, environmental factor] \(C_{env}\).

### [B-10/93]

References. 수식·표·그림 없음.


## 식 총 개수 및 쪽별 식 목록

식 총 개수: **456항목**. 이 중 원문 번호식은 **28식** (2-1~2-21: 21식, 3-1~3-6: 6식, 부록 B 식 (1): 1식), 번호 없는 식·정의·인라인 기호·표·그림 수학 항목은 **428항목**이다. 이는 위에서 정한 전사 항목 단위의 개수이며, 한 항목 안의 개별 변수·반복 등장 수를 별도로 더한 개수가 아니다. 표의 순수 수치 및 그래프 축 눈금은 전사했지만 이 개수에서는 제외했다.

| 인쇄쪽/PDF쪽 | 식 번호 또는 위치 식별자 | 항목 수 |
|---|---|---:|
| 1/11 | 없음 | 0 |
| 2/12 | 없음 | 0 |
| 3/13 | I3-1; I3-2; G3-1; G3-2 | 4 |
| 4/14 | I4-1; G4-1; G4-2; G4-3; G4-4 | 5 |
| 5/15 | 없음 | 0 |
| 6/16 | G6-1; G6-2 | 2 |
| 7/17 | G7-1; G7-2; G7-3; G7-4; G7-5; G7-6; G7-7; G7-8; G7-9; G7-10 | 10 |
| 8/18 | 없음 | 0 |
| 9/19 | I9-1; I9-2; I9-3 | 3 |
| 10/20 | I10-1; I10-2; Eqn. 2-1; I10-3; I10-4; I10-5; I10-6; I10-7; I10-8; I10-9; I10-10; I10-11; I10-12; I10-13 | 14 |
| 11/21 | I11-1 | 1 |
| 12/22 | Eqn. 2-2; I12-1; I12-2; I12-3; Eqn. 2-3; I12-4; Eqn. 2-4; Eqn. 2-5; Eqn. 2-6 | 9 |
| 13/23 | Eqn. 2-7; Eqn. 2-8; Eqn. 2-9; I13-1; I13-2; I13-3; I13-4; I13-5; I13-6; I13-7; I13-8; I13-9; I13-10 | 13 |
| 14/24 | Eqn. 2-10; I14-1; I14-2; I14-3; I14-4; I14-5; I14-6; I14-7; I14-8 | 9 |
| 15/25 | Eqn. 2-11; I15-1; I15-2; I15-3; I15-4; Eqn. 2-12; I15-5; Eqn. 2-13 | 8 |
| 16/26 | I16-1; I16-2; I16-3; I16-4; I16-5; I16-6; I16-7; Eqn. 2-14; I16-8; I16-9; Eqn. 2-15; I16-10 | 12 |
| 17/27 | Eqn. 2-16; I17-1~I17-9; I17-10; I17-11; I17-12; I17-13; I17-14; I17-15; I17-16; I17-17 | 18 |
| 18/28 | Eqn. 2-17; I18-1; Eqn. 2-18; I18-2; Eqn. 2-19; Eqn. 2-20; I18-3; I18-4; Eqn. 2-21 | 9 |
| 19/29 | I19-1; I19-2; I19-3; I19-4; I19-5; I19-6; I19-7; I19-8; I19-9; I19-10; I19-11; I19-12 | 12 |
| 20/30 | I20-1; I20-2; I20-3; I20-4; I20-5; I20-6; I20-7; I20-8; I20-9; I20-10; I20-11; I20-12; I20-13 | 13 |
| 21/31 | I21-1; I21-2; I21-3; I21-4; I21-5; I21-6; I21-7; I21-8; I21-9; I21-10; I21-11; I21-12; I21-13; I21-14; I21-15 | 15 |
| 22/32 | 없음 | 0 |
| 23/33 | 없음 | 0 |
| 24/34 | 없음 | 0 |
| 25/35 | T1-1~T1-42; I25-1 | 43 |
| 26/36 | T2-1~T2-26 | 26 |
| 27/37 | Eqn. 3-1; I27-1; I27-2; I27-3; I27-4; I27-5; I27-6 | 7 |
| 28/38 | I28-1; I28-2; I28-3; I28-4 | 4 |
| 29/39 | I29-1; I29-2; I29-3 | 3 |
| 30/40 | I30-1 | 1 |
| 31/41 | T3-1~T3-11; Eqn. 3-2 | 12 |
| 32/42 | I32-1; I32-2; T4-1~T4-6 | 8 |
| 33/43 | Eqn. 3-3; I33-1; I33-2; T5-1~T5-6 | 9 |
| 34/44 | Eqn. 3-4; I34-1; I34-2 | 3 |
| 35/45 | I35-1; I35-2; I35-3; I35-4; I35-5; I35-6; I35-7; I35-8 | 8 |
| 36/46 | 없음 | 0 |
| 37/47 | T7-1~T7-7; T7-8~T7-17 | 17 |
| 38/48 | T7-18; T7-19~T7-21; I38-1 | 5 |
| 39/49 | G39-1 | 1 |
| 40/50 | 없음 | 0 |
| 41/51 | 없음 | 0 |
| 42/52 | 없음 | 0 |
| 43/53 | Eqn. 3-5; I43-1; I43-2 | 3 |
| 44/54 | Eqn. 3-6; I44-1 | 2 |
| 45/55 | G45-1 | 1 |
| 46/56 | G46-1 | 1 |
| 47/57 | I47-1; I47-2; I47-3; I47-4; I47-5; I47-6; I47-7; I47-8 | 8 |
| 48/58 | 없음 | 0 |
| 49/59 | G49-1~G49-4; G49-5; G49-6; G49-7; G49-8; G49-9; G49-10; G49-11; G49-12 | 12 |
| 50/60 | G50-1; G50-2; G50-3; G50-4; G50-5; G50-6; G50-7; G50-8; G50-9; G50-10; G50-11; G50-12; G50-13; G50-14; G50-15; G50-16; G50-17; G50-18; G50-19 | 19 |
| 51/61 | I51-1; I51-2; I51-3; I51-4; I51-5; I51-6; I51-7; I51-8; I51-9 | 9 |
| 52/62 | I52-1; I52-2; I52-3; I52-4 | 4 |
| 53/63 | I53-1 | 1 |
| 54/64 | I54-1 | 1 |
| 55/65 | 없음 | 0 |
| 56/66 | 없음 | 0 |
| 57/67 | 없음 | 0 |
| 58/68 | 없음 | 0 |
| 59/69 | 없음 | 0 |
| A-1/70 | 없음 | 0 |
| A-2/71 | 없음 | 0 |
| A-3/72 | IA3-1; IA3-2 | 2 |
| A-4/73 | 없음 | 0 |
| A-5/74 | 없음 | 0 |
| A-6/75 | 없음 | 0 |
| A-7/76 | IA7-1; IA7-2 | 2 |
| A-8/77 | IA8-1; IA8-2; IA8-3 | 3 |
| A-9/78 | 없음 | 0 |
| A-10/79 | IA10-1 | 1 |
| A-11/80 | IA11-1; IA11-2; IA11-3; IA11-4; IA11-5 | 5 |
| A-12/81 | 없음 | 0 |
| A-13/82 | IA13-1 | 1 |
| A-14/83 | 없음 | 0 |
| B-1/84 | 없음 | 0 |
| B-2/85 | 식 (1); IB2-1; IB2-2; IB2-3; IB2-4; IB2-5; IB2-6; IB2-7; IB2-8 | 9 |
| B-3/86 | IB3-1; IB3-2; IB3-3; IB3-4; IB3-5; IB3-6; IB3-7 | 7 |
| B-4/87 | GB4-1; IB4-1; IB4-2; IB4-3; IB4-4; IB4-5; IB4-6; TB1-1; TB1-2; TB1-3 | 10 |
| B-5/88 | TB1-4; TB2-1~TB2-3; IB5-1; IB5-2; IB5-3; IB5-4 | 8 |
| B-6/89 | IB6-1; IB6-2; IB6-3; IB6-4; IB6-5; IB6-6; IB6-7; IB6-8; IB6-9; IB6-10; IB6-11; IB6-12; IB6-13; IB6-14; IB6-15; IB6-16; TB3-1; TB3-2 | 18 |
| B-7/90 | TB3-3~TB3-5; IB7-1; IB7-2; IB7-3; IB7-4; IB7-5; IB7-6; IB7-7; IB7-8; IB7-9; IB7-10; IB7-11; IB7-12; IB7-13; IB7-14; IB7-15 | 18 |
| B-8/91 | IB8-1; IB8-2; IB8-3; IB8-4; IB8-5 | 5 |
| B-9/92 | IB9-1; IB9-2 | 2 |
| B-10/93 | 없음 | 0 |

## 확인 기록

- PDF 11~93쪽 83쪽 모두 300 dpi, 2550×3300 PNG로 렌더링한 뒤 각 쪽 전체 이미지를 직접 확인했다. 작은 글씨는 PDF 13쪽 600 dpi 및 PDF 22·43·47·85쪽 300 dpi 영역 렌더링으로 추가 대조했다.
- Table 1~7, Table B-1~B-3, 번호 없는 가정표와 초기 크기 배열, Figure 2·3의 표 형태 그림을 전사했다. Figure 1~17 및 Figure B-1의 문자·기호·축·범례를 기록했으며 그래프 곡선 자체는 옮기지 않았다.
- 확인 불가: [9/19] 가정표 마지막 행의 빈 네모 글리프가 뜻하는 기호; [38/48] Table 7 계속 표의 두 빈 네모 머리글이 뜻하는 기호. 보이는 네모는 그대로 표시했다.
- 전사 오류 정정 기록: 최종 확대 대조에서 Table 7 CS·LAS 변형률 속도 하한을 `0.001`로, 부록 B 식 (1)의 두 C를 대문자로 확정했다. 원문을 교정한 것이 아니라 초벌 전사의 오독을 수정한 것이다.
- 원문에 없는 수학적 유도·모델 검증·정정은 추가하지 않았다. Claude 결과 열람과 다른 AI·오케스트레이터 호출을 하지 않았다.
