# round57 Claude 독립 전사 — B048 Cyclic Stress Intensity Factors (xLPR-MSGR-TIFF v1.0)

방법: PDF 텍스트 전체 + 식 페이지(PDF 17~21)·Fig.1~3(PDF 15, 19, 33)을 170~300dpi 이미지로 직접 판독. 인쇄쪽 = PDF쪽 − 10 (본문 1쪽 = PDF 11쪽). 해석·보충 없음.

## 1. 식 전사 (LaTeX, 지면 그대로)
| 식 | 인쇄쪽 | LaTeX |
|---|---|---|
| Eqn.1 | 7 | `\rho c_{sp}\dfrac{\partial T}{\partial t}=\dfrac{1}{r}\dfrac{\partial}{\partial r}\left(kr\dfrac{\partial T}{\partial r}\right)` |
| Eqn.2 | 8 | `\dfrac{\delta^2 h^2\rho c_{sp}}{\Delta t}(T_j-T^*_j)=\dfrac{1}{r_j}\left[T_{j+1}(k_{j+1}r_{j+1}+k_j r_j)-T_j(k_{j+1}r_{j+1}+2k_j r_j+k_{j-1}r_{j-1})+T_{j-1}(k_j r_j+k_{j-1}r_{j-1})\right]` |
| Eqn.3a | 9 | `\sigma_r=\dfrac{E}{1-\mu}\dfrac{1}{r^2}\left\{-\alpha_1\int_{r_i}^{r} r(T-T_0)dr+\dfrac{r^2-r_i^2}{r_o^2-r_i^2}\Omega\right\}` |
| Eqn.3b | 9 | `\sigma_\theta=\dfrac{E}{1-\mu}\dfrac{1}{r^2}\left\{\alpha_1\int_{r_i}^{r} r(T-T_0)dr-\alpha_1 r^2(T-T_0)+\dfrac{r^2+r_i^2}{r_o^2-r_i^2}\Omega\right\}` |
| Eqn.3c | 9 | `\sigma_z=\dfrac{E}{1-\mu}\left\{\dfrac{2}{r_o^2-r_i^2}\Omega-\alpha_1(T-T_0)\right\}` |
| Eqn.4 | 9 | `\Omega=\alpha_1\int_{r_i}^{r_c} r(T-T_0)dr+\alpha_2\int_{r_c}^{r_o} r(T-T_o)dr` (둘째 적분 피적분함수는 지면에 `T_o`로 인쇄) |
| Eqn.5a | 9 | `\sigma_r=\dfrac{E}{1-\mu}\dfrac{1}{r^2}\left\{-\alpha_2\int_{r_c}^{r} r(T-T_0)dr-\dfrac{r_o^2-r^2}{r_o^2-r_i^2}\alpha_1\int_{r_1}^{r_c} r(T-T_o)dr+\dfrac{r^2-r_i^2}{r_o^2-r_i^2}\alpha_2\int_{r_c}^{r_o} r(T-T_o)dr\right\}` (지면: 둘째 적분 하한 `r_1`, 피적분 `T_o`) |
| Eqn.5b | 10 | `\sigma_\theta=\dfrac{E}{1-\mu}\dfrac{1}{r^2}\left\{\alpha_2\int_{r_c}^{r} r(T-T_0)dr-\alpha_2 r^2(T-T_0)+\dfrac{r^2+r_o^2}{r_o^2-r_i^2}\alpha_1\int_{r_i}^{r_c} r(T-T_0)dr+\dfrac{r^2+r_i^2}{r_o^2-r_i^2}\alpha_2\int_{r_c}^{r_o} r(T-T_0)dr\right\}` |
| Eqn.5c | 10 | `\sigma_z=\dfrac{E}{1-\mu}\left\{\dfrac{2}{r_o^2-r_i^2}\Omega-\alpha_2(T-T_0)\right\}` |
| Eqn.6 | 10 | `E=\dfrac{E_1A_1+E_2A_2}{A_1+A_2}` |
| (Fig.1 내) | 5 | `K_I=\int_0^a \sigma(x)\,m(x,a)\,dx` |
| (본문) | 11 | `\Delta K\ (K_{max}-K_{min})` |

원문 정의(영문): Eqn.1 "the material properties k, c_sp and ρ (thermal conductivity, specific heat and density) can be functions of temperature"; Eqn.2 "The 'j' subscript refers to conditions at the 'j-th' node. The '*' superscript refers to conditions at the previous time-step. δ is the dimensionless nodal spacing, which equals [1/number of spatial increments in the material 1]=[1/number of spatial increments in material 2]. h is the total pipe wall thickness."; Eqn.3·5 "μ is Poisson's ratio", region 1 = inner material, region 2 = outer material, 표기는 Figure 2 참조; Eqn.6 "weighted average of the cross-sectional areas and elastic modulus values for the inner and outer material… subscript 1 inner, 2 outer". r, r_i, r_o, r_c, h, h_1, h_2는 Figure 2 라벨(r_0 = Fig.2에 `r0`, 식에는 `r_o`). Ω, T_0는 식 안에서 정의 문장 없음(T_0는 "reference temperature (T0) … user specified"). A_1, A_2는 "cross-sectional areas" 외 정의 없음. E, α_1, α_2: 단일 재료일 때 α1=α2.

## 2. 구조·핵심 사실 (영문 인용, 인쇄쪽)
- 표지/개정(iv 앞): xLPR-MSGR-TIFF Version 1.0, 저자 David O. Harris(SIA), 검토 Dilip Dedhia(SIA), 승인 Marjorie Erickson(PEAI)·Craig D Harrington(EPRI), 01/27~01/31/16. 2021 행정 개정: 제목이 "Cyclic Stress Intensity Factors Due to Operating Transients—Module Development (TIFFANY)"에서 변경.
- Executive Summary (iv): "TIFFANY is a standalone module that prepares inputs to xLPR related to cyclic conditions arising from temperature and pressure excursions of the reactor coolant." 입력물 = "cyclic stress intensity factors and the related information", 용도 "fatigue crack initiation and growth calculations". "radial gradient thermal stresses". "relationships derived from elasticity theory for axisymmetric bodies subject to axisymmetric temperature fields", "semi-elliptical cracks in the inside pipe surface … influence functions. Axial and circumferential cracks are treated. ΔK … from the temporal variation of K." "TIFFANY module is called by a pre-processor".
- §1.1 (1): "strictly a deterministic module… uncertainties … in the inputs, primarily in the time-temperature inputs." §1.2 목표 6개 항목(best-estimate model; cyclic stress at inner surface, rise time, changes in restraint of thermal expansion stress 추출 절차; 코드 개발; 테스트 케이스; 문서; Computational Group와 인터페이스). §1.3 "xLPR stress intensity factor (K) modules [1,2] are then accessed… sorted to define maximum and minimum values".
- §2 (3): single or bimaterial pipe, axial·circumferential crack. §2.2: Fig.1은 SRD [3]에서; 두 재료(두께 h1, h2); 물 물성은 온도 의존, Ref.[4]; "A TIFFANY analysis must be performed for each thermal transient… separate set of inputs".
- §2.3 (4): 3D FEA까지 다양한 방법 중 "selected for its simplicity and speed of computation, plus its maximum use of software that was already available [5]. There is no sacrifice in accuracy, other than TIFFANY's restriction to straight sections of pipe."
- §2.4 (4): 5단계 (1) transient temperature field (2) thermal stresses due to radial gradient (3) other loadings … cyclic stress at inner surface, rise-time, average pipe wall temperature 기여, pressure/stratification/mechanical (4) K 및 변화 계산 (5) sorting max/min.
- §2.4.1 (6~7) 가정표 5행: linear elasticity & classical heat conduction(영향: No bias or uncertainty expected); thermophysical properties independent of temperature except linear k(T)(some bias, minimal); long circular cylinder axisymmetric(minimal); plane cross-sections remain plane, no net axial force(minimal; "differences may be small (?)"); effective E weighted average(minimal). "TIFFANY results are strictly applicable only to long sections of pipe. They are assumed to be applicable to other piping components, such as elbows, tees and nozzles."
- §2.4.2 (7~8): T(r,t); 1D; "The thermal conductivity can be temperature-dependent in xLPR-TIFFANY." 내면 대류 경계 — Edwards [7] p.166, SRD [3]; 외면 insulated; 유한차분 "second order correct differing of the diffusion term… first order correct backward differing of the temporal term"; "method of successive substitutions".
- §2.4.3 (8~10): Timoshenko & Goodier [8] §135; 두 재료 동일 E, μ·다른 α; "axial strain, εz, is taken to be constant (not zero)… zero net axial load"; 경계 "zero radial stress at the inner and outer pipe wall and continuity of displacements and radial stress at the bimaterial interface". "reduce to the corresponding ones in Timoshenko [7] for a uniform material when α1=α2". "if α1=α2 and T = constant, all of the stresses are zero. However if α1≠α2, a uniform temperature produces stresses except at the single temperature T=T0." T0 "usually taken to be the room temperature of 70°F… In xLPR-TIFFANY, T0 is user specified." α·E·μ·ρ·c_sp는 온도 독립으로 취급, "values at some intermediate temperature (e.g., average of maximum and minimum temperature)" 권장; α는 "instantaneous value at some intermediate temperature is suggested since it is generally conservative".
- §2.4.4 (10~11): Global Stresses — σ_T, σ_B + T_sig; "These stresses are zero at T0 = 70°F, and vary linearly with the average temperature in the pipe wall."; Δp; 둘레를 사용자 정의 개수 segment로 분할; Stratification: DispFactorIn 곱; Mechanical: max/min membrane·bending stress 입력.
- §2.4.5 (11): deepest/surface point of PW, TW cracks [1,2]; "The axial stress is used in the evaluation of the stress intensity factors for circumferential cracks and the hoop stress is used for the axial cracks." "The times at which Kmax occurs is not the same for all crack sizes."
- §2.4.6 (12) Sorting; §2.4.7 (12) 결정론적, 불확실성은 입력(ASME Sec.II Part D [9]), 시간-온도 불확실성은 xLPR Framework가 MVR [10] 부록 절차로 처리.
- §3.1 (13~16) Table 1 RTIF-1~38; "TIFFANY has no requirements for linking to other xLPR modules… stress intensity factor module embedded in TIFFANY which is identical to that used within the xLPR Framework." §3.2 (16): "capable of analyzing only one transient at a time… intermediate maxima and minima are not captured. It is the responsibility of the user to properly define the transients." §3.3 (16~17): DLL wrapper, pre-processor, Error Flag, SRD Table 5. §3.4 (17~21) Table 2/3/4. §3.5 (21~22): STP [12], 폐형해 비교(STRR [4]), FE 비교(MVR [10]); GoldSim wrapper 제외. §3.6 (22) Fig.3. §4 (24) "No recommendatioins… at this time." §5 (25) "None at this time." §6 (26) Summary. §7 (27) Ref.[1]~[12].

## 3. 표
- Nomenclature(viii): a, c, c_sp, E, H1("Inner pipe thickness (in case of overlay or clad piping)"), h2("Outer pipe thickness…"), K, r, r_i, r_o, r_c("Interface radius"), t, T, α, ΔK("Cyclic stress intensity factor"), Δp("Deviation from the operating pressure"), κ("Thermal conductivity" — 지면 기호 `K`), ρ, θ("Angular location"), σ_T("Global membrane stress"), σ_B("Global bending stress"), μ("Poisson's Ratio").
- Acronyms(ix): DLL, DMW, FE, FEA, EPRI, MVR, NRC, PWC(Part-Wall Crack), RTM, SDD, SI, SRD, STP, STRR, TWC(Through-Wall Crack), V&V, xLPR.
- Table 1 (13~16): RTIF-1…38 전체 (PDF 텍스트 레이어에 완전; 별도 전사 파일 `scratchpad/b048/b048_text.txt` PDF p23~26 참조). RTIF-1 Fortran DLL / 2 maintainability·portability / 3 SI units(IEEE/ASTM SI 10 2010) / 4 explicit passing / 5 best practices [8] / 6 pre-processor inputs per Table 1(원문 표기; 실제는 Table 2) / 7 outputs per Table 2(원문 표기; 실제 Table 3) / 8 error → framework terminates / 9 T(r,t) / 10 σ(r,t) / 11–14 circ PW K max/min deepest/surface (a/c, a/h, θ) / 15–18 circ TW K membrane/bending (c, θ) / 19–22 axial PW (a/c, a/h) / 23–24 axial TW pressure (c) / 25–26 max change axial/hoop stress due to pressure / 27–30 ID total axial stress max/min & time per segment / 31–34 hoop ID / 35–36 rise time axial(θ)/hoop / 37–38 max/min ID temperature.
- Table 2 (18~19) 입력 변수 전체, Table 3 (20~21) 출력 변수 전체, Table 4 (21) 물성: k W/(m·°K), c J/(kg·°K), ρ kg/m³, κ(thermal diffusivity) m²/s, E MPa, ν –, α °C⁻¹ — 전사본은 b048_text.txt PDF p28~31.

## 4. 그림
- Fig.1 (5): 박스: Fluid Properties, Coolant Velocity History → Convective Heat Transfer Coefficient → Evaluation of Temperature Profiles(← Coolant Temperature History, ← Pipe Geometry and Materials) → Evaluation of Radial Gradient Thermal Stresses → (Crack Size, Additional Stresses, Influence Functions) → Evaluation of Stress Intensity Factors vs. Time [K_I=∫σ(x)m(x,a)dx] → Resulting K_a, K_c / Sorting for Evaluation of Maximum and Minimum K.
- Fig.2 (9): r_0, r_i, r_c, h, h_1, h_2, Mat 1(내측), Mat 2(외측), Insulated OD.
- Fig.3 (23): Start → IAType 분기 [=1: Initialization(InitK, Initialize) → Start Timestep Iteration → Calculate Temp. Distribution(TEMPER) → Calculate Stress Distribution(STRESS) → Print Temp. & Stress(PRINTT) → Calculate K(CalcK) → End Timestep Iteration → Exit] / [=2 or 3: Calculate K(CalcK23) → Exit].

## 5. 원문 자체 이상 (슬라이드/정리 오류로 세지 않음)
- Eqn.4·5a·5b 일부 항에 `T_o`와 `T_0` 혼용, Eqn.5a 둘째 적분 하한 `r_1`.
- 본문 "Timoshenko [7]" 인용이나 참고문헌 [7]은 Edwards, Timoshenko & Goodier는 [8].
- Table 1 RTIF-6/7: "Table 1/Table 2"로 기재(본문 3.3은 Table 2/3).
- 변수명 `IATypeIn`(Table 2) vs `IYType`(Table 2 설명 "only for IYType = 2 or 3"); Fig.3은 `IAType`.
- Nomenclature: H1(대문자) vs h2(소문자), κ 기호 `K`와 응력확대계수 K 동일 표기; 2.4.1 표에 "variation of µ" 문구 중복, "temperatuare", "discreet", "differing" 등 철자.
- Ref.[8]을 RTIF-5 "best practices defined in [8]"에서도 인용(참고문헌 [8]은 Timoshenko).
