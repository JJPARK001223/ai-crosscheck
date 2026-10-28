# Table 1–12 독립 전사

출처: `input/b050.pdf`. PDF 페이지 이미지를 육안으로 읽어 전사했다. PDF쪽은 파일의 1부터 센 쪽, 인쇄쪽은 본문에 인쇄된 쪽이다. 빈 셀은 빈 셀로 유지했다. 원문의 대소문자·표기·오탈자는 원문 그대로이며, 셀 내부 줄바꿈은 `<br>`로 표시했다.

## Table 1. SRD requirements for SC_fail module [1]

PDF 33–34쪽 / 인쇄 17–18쪽.

| Requirement | Short Description of Requirement |
|---|---|
| SCF-1 | Develop a software application that will determine if a circumferential surface crack instability has occurred and provide a ratio of current (applied) bending moment to bending moment which would result in an instability. |
| SCF-2 | The application must be designed in such a way that the design attributes of adaptability, modularity, maintainability, portability, and extensibility can be realized successfully by future developers who were not necessarily involved in the original task of creating the software. The module will minimize the need for computational resources. |
| SCF-3 | The application must comply with all xLPR Project Software Quality Assurance (SQA) requirements as specified in References [23] and [24], including evaluations for correctness, consistency, completeness, accuracy, readability, and testability, and be prepared to successfully meet the criteria of all SQA audits. |
| SCF-4* | Develop the SC_fail Module to be implemented as an external DLL element where the actor is the GoldSim xLPR application. |
| SCF-5 | The required inputs and outputs are presented in Tables 1 and 2 of the SRD [1]. |
| SCF-6 | Inputs will be required in the SI system of units (see Table 1 from the SC_fail SRD [1]) for xLPR, but the module will actually only need a consistent set of units. Additionally, the physical models will be implemented using the SI system of units. |
| SCF-7 | Develop a suite of tests that exercise all significant elements of the module. The agreement between the maximum moment values for a series of surface crack pipe experiments and the corresponding predicted maximum moments from the SC_fail module are to be within 10%, on average. |
| SCF-8 | Implement validity checks for all inputs and report invalid inputs to the user by returning a termination code flag. |
| SCF-9 | Identify those conditions where the implemented models are beyond the bounds of the known solutions and report these cases to the user by returning a warning code flag. Calculations will be implemented at the bounds and those values (along with the warning flag) will be returned. |

## Table 2. Description of circumferential surface crack stability module (SC_fail) input variables

PDF 34–35쪽 / 인쇄 18–19쪽.

| Input Variable Name | Type | Description | Units | Value | Limits / Comments |
|---|---|---|---|---|---|
| R_o | Real | Pipe outer radius | mm | Defined in Inputs Database | Ro > thick |
| Thick | Real | Pipe wall thickness | mm | Defined in Inputs Database | Thick > 0 |
| Step_size | Real | Step size for crack discretization | mm | Calculated in the Framework | Step_size>0 |
| Ncracks | Integer | Number of cracks | Unitless | Provided by the Framework | N>=0 |
| Depth(N)▪ | Real | Crack depth array | mm | Defined in Crack Growth Database | depth < thick |
| Theta(N)▪ | Real | Half crack length array | radians | Defined in Crack Growth Database | 0 < Theta < π |
| Gamma(N)▪ | Real | Crack location array | radians | Defined in Crack Growth Database | - π < Gamma < π |
| Sigy | Real | Pipe yield stress | MPa | Sampled by the Framework | sigy > 0 |
| Sigu | Real | Pipe ultimate stress | MPa | Sampled by the Framework | sigu >= sigy |
| RO_alpha | Real | Ramberg-Osgood coefficient | Unitless | Sampled by the Framework | RO_alpha > 0 |
| RO_sigo | Real | Ramberg-Osgood reference stress | MPa | Sampled by the Framework | RO_sigo > 0 |
| RO_epso | Real | Ramberg-Osgood reference strain | Unitless | Sampled by the Framework | RO_epso > 0 |
| RO_n | Real | Ramberg-Osgood exponent | Unitless | Sampled by the Framework | RO_n > 0 |
| Resist_Jic | Real | Pipe material initiation J-resistance | N/mm | Sampled by the Framework | Resist_Jic > 0 |
| Resist_C | Real | Pipe material J-resistance coefficient | N/mm<sup>(Resist_m+1)</sup> | Sampled by the Framework | Resist_C > 0 |
| Resist_m | Real | Pipe material initiation J-resistance exponent | Unitless | Sampled by the Framework | Resist_m > 0 |
| Step_phi♦ | Integer | Number of steps for discretization of phi over [-π,π] | Unitless | Not currently used in Framework | Step_phi>=0 |
| Uncert_Flag♦ | Integer | Uncertainty flag | Unitless | Not currently used in Framework | Uncert_Flag>=0 |
| usample♦ | Integer | Sample size for uncertainty | Unitless | Not currently used in Framework | Usample>=0 |
| Uampli♦ | Real | Amplitude of uncertainty | Unitless | Not currently used in Framework | Uampli>=0 |
| Rseed♦ | Integer | Random seed used for uncertainty | Unitless | Not currently used in Framework | Rseed>=0 |
| BM | Real | Applied bending moment | N-mm | Defined in Loads Database | BM>=0 |
| pressure | Real | Pipe internal pressure | MPa | Defined in Loads Database | Pressure>=0 |
| F_ax | Real | Applied axial force (excluding pressure effect) [force], N | N | Defined in Loads Database | F_ax >=0 |
| DMW_ratio | Real | Mixture Fraction for DMW analyses | Unitless | Constant value passed by Framework from Inputs Database | 0<=DMW_ratio<=1 |
| DMW_flag | Integer | Flag to indicate that a DMW analysis is being done | Unitless | Constant value passed by Framework from Inputs Database | =0, not DMW analysis<br>=1,DMW analysis |
| crack_morph | Integer | SC analysis method<br>= 1, constant depth surface crack NSC<br>= 2, parabolic surface crack NSC♦<br>= 3, semi-elliptical surface crack NSC♦ | Unitless | User Defined | crack_morph = 1<br>crack_morph = 2<br>crack_morph = 3 |
| i_write | Integer | Solution write flag<br>= 0, do not write<br>= 1, write solution values to file “SC_Fail.out” | Unitless | User Defined, not currently used in Framework | i_write = 0<br>i_write = 1 |
| Loopopt♦ | Integer | Looping options | Unitless | User Defined, not currently used in Framework | |

♦ Variables used in the implementation of the work found in [16] that provide additional flexibility to handle crack profile uncertainty and possible future enhancements for later versions

▪ Depth, theta, and gamma may be passed as a matrix to the source code

## Table 3. Description of circumferential surface crack stability module (SC_fail) output variables

PDF 36쪽 / 인쇄 20쪽.

| Output Variable Name | Type | Description | Units | Value | Limits / Comments |
|---|---|---|---|---|---|
| if_flag | Integer | Solution return code [integer], unitless<br>= 0, the SC does not fail<br>= 1, the SC will fail under the applied loads<br>= -1, no solution due to an error | Unitless | Set in Module | |
| i_error | Integer | Solution return code [integer], unitless<br>= 101, Crack depth greater than or equal to thickness for any crack<br>= 102, Outer radius less than or equal to 2*thick<br>= 103, Crack half-length less than or equal to 0 or greater than or equal to π for any crack<br>= 104, Crack location less than −π or greater than π<br>= 105, Overlapping cracks<br>= 106, Yield stress less than or equal to 0 or ultimate stress less than or equal to zero or yield stress greater than ultimate stress<br>= 107, Any of the four Ramberg-Osgood parameters (Ro_alpha, RO_sigo, RO_epso, RO_n) less than 0<br>= 108, And of three J-R curve constants (resist_Jic, resist_C, resist_m) less than zero<br>= 109, Applied internal pressure less than 0 or applied bending moment less than 0<br>= 110, Loading and/or crack size put neutral axis out of range | Unitless | Set in Module | |
| ratio_BM | Real | Bending moment ratio [real], unitless<br>≥ 0.0, BM/BM_max<br>= -1.0, if_flag <0 | Unitless | Calculated in Module | |

## Table 4. Errors and warnings for the SC_fail module

PDF 37쪽 / 인쇄 21쪽.

| If_flag value | Error / Warning | Description |
|---|---|---|
| 0 | N / A | Valid Solution - SC does not fail |
| 1 | N / A | Valid Solution – single SC fails under the applied loads |
| -1 | Error | No Solution |
| **i_error value** | **Error / Warning** | **Description** |
| 101 | I/O Error | Crack depth greater than or equal to thickness for any crack |
| 102 | I/O Error | Outer radius less than or equal to 2*thick |
| 103 | I/O Error | Crack half-length less than or equal to 0 or greater than or equal to π for any crack |
| 104 | I/O Error | Crack location less than −π or greater than π |
| 105 | I/O Error | Overlapping cracks |
| 106 | I/O Error | Yield stress less than or equal to 0 or ultimate stress less than or equal to zero or yield stress greater than ultimate stress |
| 107 | I/O Error | Any of the four Ramberg-Osgood parameters (Ro_alpha, RO_sigo, RO_epso, RO_n) less than 0 |
| 108 | I/O Error | And of three J-R curve constants (resist_Jic, resist_C, resist_m) less than zero |
| 109 | I/O Error | Applied internal pressure less than 0 or applied bending moment less than 0 |
| 110 | I/O Error | Loading and/or crack size put neutral axis out of range |

## Table 5. SRD requirements for TWC_fail module [2]

PDF 40쪽 / 인쇄 24쪽.

| Requirement | Short Description of Requirement |
|---|---|
| TWCF-1 | Develop a software application that will determine if a through-wall crack instability has occurred and provide a ratio of current crack angle (θ) to the critical crack angle (θ<sub>crit</sub>) which would result in instability. |
| TWCF-2 | The application must be designed in such a way that the design attributes of adaptability, modularity, maintainability, portability, and extensibility can be realized successfully by future developers who were not necessarily involved in the original task of creating the software. The module will minimize the need for computational resources. |
| TWCF-3 | The application must comply with all xLPR Project Software Quality Assurance (SQA) requirements as specified in References [23] and [24], including evaluations for correctness, consistency, completeness, accuracy, readability, and testability, and be prepared to successfully meet the criteria of all SQA audits. |
| TWCF-4 | Develop the TWC_fail Module to be implemented as an external DLL element where the actor is the GoldSim xLPR application |
| TWCF-5 | The required inputs and outputs are presented in Tables 1 and 2 of the TWC_fail SRD [2]. |
| TWCF-6 | Inputs will be required in the SI system of units (see Table 1 of the TWC_fail SRD) for xLPR, but the module will actually only need a consistent set of units. Additionally, the physical models will be implemented using the SI system of units |
| TWCF-7 | Develop a suite of tests that exercise all significant elements of the module. The agreement between the through-wall crack sizes for a series of through-wall crack pipe experiments and the predicted critical crack sizes from TWC_fail are to be within 10%, on average. |
| TWCF-8 | Implement validity checks for all inputs and report invalid inputs to the user by returning a termination code flag. |
| TWCF-9 | Identify those conditions where the implemented models are beyond the bounds of the known solutions and report these cases to the user by returning an error code. Calculations will be implemented at the bounds and those values (along with the warning flag) will be returned. |
| TWCF-10* | The xLPR Framework shall call the TWC_fail module when any of the following conditions are met:<br>• The first time a TWC or a transitioning crack appears<br>• Any time the applied loads change<br>• Any time the material properties change, such as when mitigation is applied<br>• After a TWC exists and when the crack size has grown by PWSCC, fatigue, etc. to 95% or more of θ<sub>crit</sub> calculated when TWC_fail is first called. |
| TWCF-11* | The xLPR framework shall pass input geometry to the module |
| TWCF-12* | The xLPR framework shall pass the appropriate sampled material properties to the module. If a DM weld is being analyzed, the appropriate mixture percentage shall be applied to the sampled material properties before passing them to the module. |
| TWCF-13* | If a crack is transitioning from a surface crack to an idealized through-wall crack, the framework must calculate an equivalent idealized through wall crack length/angle by averaging the transitioning cracks ID and OD crack lengths/angles. |
| TWCF-14* | The framework shall pass the appropriate moments and forces to the module per the stress requirement document |
| TWCF-15* | The Framework shall terminate either the realization or the simulation if the if_flag is negative. For all other flags, the framework shall note the message and continue. |

## Table 6. Description of circumferential through-wall crack stability module (TWC_fail) input variables

PDF 41쪽 / 인쇄 25쪽.

| Input Variable Name | Type | Description | Units | Value | Limits/ Comments |
|---|---|---|---|---|---|
| Ro | Real*8 | Pipe outer radius | mm | Defined in Inputs Database | Ro > thick |
| Thick | Real*8 | Pipe wall thickness | mm | Defined in Inputs Database | Thick > 0 |
| Theta | Real*8 | Half crack length | Radians | Defined in Crack Growth Database | 0 < Theta < pi |
| sigy | Real*8 | Pipe yield stress | MPa | Sampled by the Framework | sigy > 0 |
| sigu | Real*8 | Pipe ultimate stress | MPa | Sampled by the Framework | sigu >= sigy |
| RO_alpha | Real*8 | Ramberg-Osgood coefficient | Unitless | Sampled by the Framework | RO_alpha > 0 |
| RO_sigo | Real*8 | Ramberg-Osgood reference stress | MPa | Sampled by the Framework | RO_sigo > 0 |
| RO_epso | Real*8 | Ramberg-Osgood reference strain | Unitless | Sampled by the Framework | RO_epso > 0 |
| RO_n | Real*8 | Ramberg-Osgood exponent | Unitless | Sampled by the Framework | RO_n > 0 |
| Resist_Jic | Real*8 | Pipe material initiation J-resistance | N/mm<br>(or kJ/m²) | Sampled by the Framework | Resist_Jic > 0 |
| Resist_C | Real*8 | Pipe material J-resistance coefficient | N/mm<sup>(Resist_m+1)</sup> | Sampled by the Framework | Resist_C > 0 |
| Resist_m | Real*8 | Pipe material initiation J-resistance exponent | Unitless | Sampled by the Framework | Resist_m > 0 |
| pressure | Real*8 | Pipe internal pressure | MPa | Defined in Loads Database | pressure >= 0 |
| BM | Real*8 | Applied bending moment | N-mm | Defined in Loads Database | BM >= 0 |
| F_ax | Real*8 | Applied axial force (excluding pressure effect) | N | Defined in Loads Database | F_ax >=0 |
| i_write | Integer | Solution debug write flag<br>=0, do not save<br>=1, save analysis results for NSC and ENG2 calculations to file TWC_fail.out | Unitless | User Defined | i_write = 0<br>i_write = 1 |

## Table 7. Description of circumferential through-wall crack stability module (TWC_fail) output variables

PDF 42쪽 / 인쇄 26쪽.

| Output Variable Name | Type | Description | Units | Value | Limits/ Comments |
|---|---|---|---|---|---|
| if_flag | Integer | Solution return code<br>=-1, no solution has been found<br>= 0, the TWC does not fail<br>= 1, the TWC will fail under the applied loads | unitless | Set in Module | |
| ratio_theta | Real*8 | Crack size ratio, normally≥0.0, theta/theta_max<br>=-1.0, no valid solution, see if_flag and i_err_code values<300 | unitless | Calculated in Module | |
| i_err_code | Integer | See Table 3 of TWC_fail SDD [4] | unitless | Set in Module | |

## Table 8. TWC_fail module error code (i_err_code) values

PDF 42–43쪽 / 인쇄 26–27쪽.

| i_err_code | Condition | if_flag | ratio_theta |
|---|---|---|---|
| 100 | R_o <= 2*thick | -1 | -1.0 |
| 101 | theta<=0 OR theta>=π | -1 | -1.0 |
| 102 | sigy<=0 OR sigu<=0 OR sigy>sigu | -1 | -1.0 |
| 103 | RO_alpha<0 OR RO_sigo<0 OR RO_epso<0 OR RO_n<0 | -1 | -1.0 |
| 104 | RO_alpha=0 AND RO_sigo=0 AND RO_epso=0 AND RO_n=0 | -1 | -1.0 |
| 105 | Resist_Jic<0 OR Resist_C<0 OR Resist_m<0 | -1 | -1.0 |
| 106 | Resist_Jic=0 AND Resist_C=0 AND Resist_m=0 | -1 | -1.0 |
| 107 | pressure<0 OR BM<0 | -1 | -1.0 |
| 200 | NSC solution produced a negative infinity result | -1 | -1.0 |
| 201 | NSC solution produced a positive infinity result | -1 | -1.0 |
| 202 | NSC solution produced a not-a-number result | -1 | -1.0 |
| 203 | ENG2 solution produced a negative infinity result | -1 | -1.0 |
| 204 | ENG2 solution produced a positive infinity result | -1 | -1.0 |
| 205 | ENG2 solution produced a not-a-number result | -1 | -1.0 |
| 206 | NSC and ENG2 solutions produced a negative infinity result | -1 | -1.0 |
| 207 | NSC and ENG2 solutions produced a positive infinity result | -1 | -1.0 |
| 208 | NSC and ENG2 solutions produced a not-a-number result | -1 | -1.0 |
| 209 | NSC iteration limit (5000) exceeded | -1 | -1.0 |
| 210 | NSC solution not in range of 0.0<theta_max<π | -1 | -1.0 |
| 211 | ENG2 initial crack size starting guess could not be found in 5000 iterations | -1 | -1.0 |
| 212 | ENG2 solution not in range of 0.0<theta_max<π | -1 | -1.0 |
| 213 | ENG2 Newton's Method iteration limit exceeded and stress is intermediate but could not find a solution for minimum error of J and dJ_da equations | -1 | -1.0 |
| 300 | no failure with limit defined by NSC | 0 | 0<=value<1 |
| 301 | no failure with limit defined by ENG2 | 0 | 0<=value<1 |
| 302 | failure by NSC | 1 | value>=1 |
| 303 | failure by ENG2 | 1 | value>=1 |
| 304 | no failure with limit defined by NSC. ENG2 critical crack size has stress on remaining ligament>sigu. | 0 | 0<=value<1 |
| 305 | no failure with limit defined by ENG2. ENG2 critical crack size stress on remaining ligament>sigu. | 0 | 0<=value<1 |
| 306 | failure by NSC. ENG2 critical crack size stress on remaining ligament>sigu. | 1 | value>=1 |
| 307 | failure by ENG2. ENG2 critical crack size stress on remaining ligament>sigu. | 1 | value>=1 |
| 308 | no failure with limit defined by NSC. ENG2 reached a Newton's Method iteration limit and stress is intermediate: ENG2 theta solution is a minimum of error of J and dJ_da equations. | 0 | 0<=value<1 |
| 309 | no failure with limit defined by ENG2. ENG2 reached a Newton's Method iteration limit and stress is intermediate: ENG2 theta solution is a minimum of error of J and dJ_da equations. | 0 | 0<=value<1 |
| 310 | failure by NSC. ENG 2 reached a Newton's Method iteration limit and stress is intermediate: ENG2 theta solution is a minimum of error of J and dJ_da equations. | 1 | value>=1 |
| 311 | failure by ENG2. ENG2 reached a Newton's Method iteration limit and stress is intermediate: ENG2 theta solution is a minimum of error of J and dJ_da equations. | 1 | value>=1 |
| 312 | no failure with limit defined by NSC. ENG2 reached a Newton's Method iteration limit and stress is high: ENG2 theta solution is assumed to be theta_max=0.0. | 0 | 0<=value<1 |
| 313 | no failure with limit defined by ENG2. ENG2 reached a Newton's Method iteration limit and stress is high: ENG2 theta solution is assumed to be theta_max=0.0. | 0 | 0<=value<1 |
| 314 | failure by NSC. ENG2 reached a Newton's Method iteration limit and stress is high: ENG2 theta solution is assumed to be theta_max=0.0. | 1 | value>=1 |
| 315 | failure by ENG2. ENG2 reached a Newton's Method iteration limit and stress is high: ENG2 theta solution is assumed to be theta_max=0.0. | 1 | value>=1 |
| 316 | no failure with limit defined by NSC. ENG2 reached a Newton's Method iteration limit and stress is low: ENG2 theta solution is assumed to be theta_max=π. | 0 | 0<=value<1 |
| 317 | no failure with limit defined by ENG2. ENG2 reached a Newton's Method iteration limit and stress is low: ENG2 theta solution is assumed to be theta_max=π. | 0 | 0<=value<1 |
| 318 | failure by NSC. ENG2 reached a Newton's Method iteration limit and stress is low: ENG2 theta solution is assumed to be theta_max=π. | 1 | value>=1 |
| 319 | failure by ENG2. ENG2 reached a Newton's Method iteration limit and stress is low: ENG2 theta solution is assumed to be theta_max=π. | 1 | value>=1 |

## Table 9. SRD requirements for axial surface crack and axial through-wall crack modules [11]

PDF 45쪽 / 인쇄 29쪽.

| Requirement | Short Description of Requirement |
|---|---|
| RACS-1* | The xLPR Framework shall call the Axial TWC Stability Module when any of the following conditions are met:<br>• Any active axial through-wall crack is initiated<br>• When a through-wall crack is found and the ratio c/ccrit > 0.9<br>• The xLPR Framework shall call the Axial SC when any active axial surface crack is found<br>• |
| RACS-2* | The xLPR Framework shall calculate/confirm the following before passing to the respective Axial SC or TWC Module:<br>• Half-crack length, [c] of the axial SC or TWC<br>Note: For transitioning TWC, average the ID and OD crack lengths before calculating the half-crack length (c)<br>• Determine the crack type, [i_ctype] before passing the corresponding SC or TWC module DLL wrapper code. |
| RACS-3 | Tables 1 and 2 of the SRD [11] provide the inputs and outputs to the Axial SC and TWC Stability modules. |
| RACS-4* | The xLPR Framework shall call the Axial SC or TWC Stability modules with a set of inputs that are in conformance with the required units, data types, and within the valid range, as specified in Table 1 of the SRD [11]. |
| RACS-5* | The xLPR Framework shall accept the outputs in conformance with the required units, data types, and within the valid range, as specified in Table 2 of the SRD [11]. |
| RACS-6 | Figure 1 of the SRD [11] provides a schematic of the Axial SC and TWC Stability modules. |
| RACS-7* | If the Axial SC or TWC Stability module is called by the DLL wrapper, the inputs and outputs shall be communicated with explicit passing of variables as shown in Figure 1 of the SRD [11]. |
| RACS-8* | The xLPR Framework shall be able to accept the following output if the incoming crack type, [i_ctype] is SC:<br>• Number: [Axial_SC_Ratio]<br>• Flag: [i_sc_pc]<br>• Flag: [if_flag_sc]<br>• Error Code: [i_err_code]<br>If the incoming crack type [i_ctype] is TWC, then the xLPR Framework should be able to accept the following outputs:<br>• Number: [Axial_TWC_Ratio]<br>• Flag: [i_twc_ll]<br>• Flag: [i_twc_epfm]<br>• Flag: [if_flag_twc]<br>• Error Code: [i_err_code] |
| RACS-9* | If the pressure is greater than or equal to the critical pressure [p/pcrit ≥ 1], [Axial_SC_fail]=1 is to be passed to xLPR Framework, and the xLPR Framework will be required to set [i_ctype]=1, because the axial SC has now become an axial TWC, and [c_over_ccrit] is set equal to its initial value of 1.<br>The xLPR Framework also has to set the initial TWC crack length to be equal to the SC crack length before SC plastic collapse failure. |
| RACS-10* | The c/ccrit is calculated and passed to the xLPR Framework as [Axial_TWC_ratio], the first time the Axial TWC module is called. Once this is passed to the xLPR Framework, the Axial TWC module is only called when the TWC crack length becomes such that c/ccrit ≥ 0.9.<br>The xLPR Framework is to check the variable [c_over_ccrit] and call the Axial TWC Module again, only when [c_over_ccrit] ≥ 0.9. |
| RACS-11 | Coding follows guidelines established in Recommended Programming Practices for the xLPR Pilot Project (2010) |
| RACS-12 | The Axial SC and TWC Stability modules must be developed such that the resulting DLL to be integrated into the GoldSim Probabilistic SW Program can be replaced easily by another similar functioning DLL module. |
| RACS-13 | The shape factors and influence coefficients as described in Reference [21] shall be used for the EPFM solution. |
| RACS-14 | The User Manual shall contain minimum requirements. |

## Table 10. Description of Axial TWC and SC stability input variables

PDF 46쪽 / 인쇄 30쪽.

| Input Variable Name | Type | Description | Units | Value | Limits / Comments |
|---|---|---|---|---|---|
| R_o | Real(8) | Pipe outer radius | mm | Defined in Inputs Database | R_o > 0 |
| thick | Real(8) | Pipe wall thickness | mm | Defined in Inputs Database | 0 < thick < R_o |
| depth | Real(8) | Surface crack depth | mm | Defined in Inputs Database | 0 < depth < thick |
| axial_c | Real(8) | Half axial crack length | mm | Defined in Inputs Database | axial_c > 0 |
| sigy | Real(8) | Pipe yield stress | MPa | Defined in Inputs Database | sigy > 0 |
| sigu | Real(8) | Pipe ultimate stress | MPa | Defined in Inputs Database | sigu > 0 |
| RO_alpha | Real(8) | Ramberg-Osgood coefficient | unitless | Defined in Inputs Database | RO_alpha > 0 |
| RO_sigo | Real(8) | Ramberg-Osgood reference stress | MPa | Defined in Inputs Database | RO_sigo > 0 |
| RO_epso | Real(8) | Ramberg-Osgood reference strain | unitless | Defined in Inputs Database | RO_epso > 0 |
| RO_n | Real(8) | Ramberg-Osgood exponent | unitless | Defined in Inputs Database | RO_n > 1 |
| Resist_Jic | Real(8) | Pipe material initiation J-resistance | N/mm | Defined in Inputs Database | Resist_Jic > 0 |
| Resist_C | Real(8) | Pipe material J-resistance coefficient | N/mm<sup>(Resist_m+1)</sup> | Defined in Inputs Database | Resist_C > 0 |
| Resist_m | Real(8) | Pipe material initiation J-resistance exponent | unitless | Defined in Inputs Database | Resist_m > 0 |
| pressure | Real(8) | Pipe internal pressure | MPa | Defined in Loads Database | pressure >= 0 |

## Table 11. Description of Axial TWC and SC stability output variables

PDF 47–50쪽 / 인쇄 31–34쪽. 이어지는 쪽의 제목: “Table 11. Description of Axial TWC and SC stability output variables (Cont)”.

| Output Variable Name | Type | Description | Units | Value | Limits / Comments |
|---|---|---|---|---|---|
| Axial_TWC_fail | Integer | Predicted failure of TWC | - | 0 or 1 | 0, TWC does not fail<br>1, TWC will fail under the applied pressure |
| Axial_TWC_ratio | Real(8) | Ratio of the current crack size to the critical crack size | - | Calculated in Axial TWC Module | c/c<sub>crit</sub> |
| Axial_SC_fail | Integer | Predicted failure of SC | - | 0 or 1 | 0, SC does not fail<br>1, SC will fail under the applied pressure |
| Axial_SC_ratio | Real(8) | Ratio of the current pressure to the critical pressure | - | Calculated in Axial SC Module | p/p<sub>crit</sub> |
| i_err_code | Integer | Input error code returned to framework | - | 101 to 109 | 101, pipe outer radius, [R<sub>o</sub>] is less than 0<br>102, 2x[thick], wall thickness exceeds pipe diameter<br>103, crack length, c is less than 0.0 or greater than 100×R<sub>mean</sub><br>104, yield strength, [sigy] is less than 0, or ultimate strength [sigu] is less than 0, or [sigy]>=[sigu]<br>105, one or more of Ramberg-Osgood parameters is/are less than 0<br>106, one or more of material fracture resistance, J-R curve parameters is/are less than 0<br>107, applied internal pressure, [pressure] is less than 0.0<br>108, pipe wall thickness [thick] is less than 0<br>109, Depth of surface crack, [depth] is less than 0 |
| if_flag_twc | Integer | Failure indication flag for TWC | - | -2 to 2 | 0, Axial TWC does not fail<br>1, Axial TWC fails under applied loads by limit load<br>2, Axial TWC fails under applied loads by EPFM<br>-1, no solution from limit load or EPFM and [i_err_code] = 204 is returned to framework<br>-2, Input error has occurred and corresponding [i_err_code] in the range from 101 – 109 is returned to the xLPR Framework |
| if_flag_sc | Integer | Failure indication flag for SC | - | -3 to 1 | 0, Axial SC does not fail<br>1, Axial SC fails under the applied loads<br>-1, not a surface crack, since [depth] ≥ [thick], and [i_err_code]=201 is returned to the xLPR Framework to set [i_ctype] = 1<br>-2, Input error has occurred and corresponding [i_err_code] in the range from 101 – 109 is returned to the xLPR Framework<br>-3, loading and/or crack such that no solution found for the pressure, and [i_err_code] = 202 is returned to the xLPR Framework |
| i_twc_ll | Integer | Limit load solution status flag for TWC | - | -3 to 0 | 0, unqualified good solution and [i_err_code] = 302 is returned to the xLPR Framework<br>-1, solution not attempted because of bad input data, and the corresponding [i_err_code] = 101 – 109 is returned to the xLPR Framework<br>-2, iteration limit of 5000 is exceeded, and [i_err_code] = 205 is returned to xLPR Framework<br>-3, solution for the maximum crack length outside the range. [c_max] is less than 0.0 or greater than 100xmean radius, R_mean, and the [i_err_code] = 303 is returned to the xLPR Framework |
| i_twc_epfm | Integer | EPFM solution status flag for TWC | - | -4 to 4 | 0, unqualified good solution, and the [i_err_code] = 304 is returned to the xLPR Framework. [i_err_code] = 309 is returned when one or more of the R<sub>m</sub>/t, rho, n, is beyond the range for which influence coefficients (h₁,F) are available [21]<br>1, good solution, but stress in ligament at maximum crack length, [c_max] exceeds ultimate strength, [sigu], and [i_err_code] = 305 is returned to xLPR Framework<br>2, solution found, but iteration limit exceeded and [c_max] solution is minimum of error of J and dJ/da equations, and [i_err_code] = 306 is returned to xLPR Framework<br>3, Numerical solution method iteration limit exceeded and stress is high, then [c_max] = 0.0 is assumed, and [i_err_code] = 307 is returned to xLPR Framework<br>4, Numerical solution method’s iteration limit exceeded and stress is low, [c_max] = 100× R<sub>mean</sub>, mean radius is assumed, and [i_err_code] = 308 is returned to xLPR Framework<br>-1, solution not attempted due to faulty input data, and the corresponding [i_err_code] in the range from 101 – 108 is returned to xLPR Framework<br>-2, initial crack size starting guess could not be found in 5000 iterations, , and [i_err_code] = 206 is returned to xLPR Framework<br>-3, initial crack size starting estimate not within the bounds of 0.0 and 100xmean radius, R<sub>mean</sub>, , and [i_err_code] = 207 is returned to xLPR Framework<br>-4, numerical solution iteration limit exceeded and could not find solution for minimum error of J and dJ/da equations, , and [i_err_code] = 310 is returned to xLPR Framework |
| i_sc_pc | Integer | Plastic Collapse solution status flag for SC | - | -2 to 0 | 0, unqualified good solution, and the [i_err_code] = 301 is returned to xLPR Framework<br>-1, solution not attempted because of bad input data, and the corresponding [i_err_code] = 101 – 109 is returned to xLPR Framework<br>-2, solution for the maximum pressure, [p_max] outside the range. [p_max] is less than 0.0 or greater than 1000xapplied pressure, [pressure], and [i_err_code] = 203 is returned to the xLPR Framework |

## Table 12. AxCS error code description and module guidance to xLPR framework

PDF 50–51쪽 / 인쇄 34–35쪽.

| Error Code | Description | Module Guidance to xLPR Framework |
|---|---|---|
| 101 | Pipe Outer Radius is less than 0 | Move to next case while specifying Input Error for this case in the Output file |
| 102 | 2×Wall Thickness Exceeds Pipe Diameter | Move to next case while specifying Input Error for this case in the Output File |
| 103 | Axial half-crack length is less than 0 or greater than 100×R<sub>m</sub> | Write Input error message in the Output file, and Call the Axial Crack Stability Module when change in crack length occurs |
| 104 | One or more of the material yield, ultimate stress is less than 0, Or yield stress is greater than ultimate stress | Move to next case while specifying Input Error for this case in the Output File |
| 105 | One or more of the Ramberg-Osgood parameters is less than 0 | Move to next case while specifying Input Error for this case in the Output File |
| 106 | One or more of the material fracture resistance, J–R curve is less than 0 | Move to next case while specifying Input Error for this case in the Output File |
| 107 | Applied internal pressure is less than 0 | Write Input error message in the Output file, and Call the Axial Crack Stability Module when change in pressure occurs |
| 108 | Pipe wall thickness is less than 0 | Move to next case while specifying Input Error for this case in the Output File |
| 109 | Surface crack depth is less than 0 | Write Input error message in the Output file, and Call the Axial Crack Stability Module when change in surface crack depth occurs |
| 201 | Crack is not a surface crack since crack depth is greater than pipe wall thickness | Write logical error message and Call the Axial Through-wall Crack Stability module |
| 202 | Loading and/or crack such that no solution is found for axial SC stability | Write logical error message and Call the Axial Crack Stability Module when crack and/or loading change occurs |
| 203 | Solution for maximum pressure is outside the range of [0, 1000×applied pressure] | Write logical error message and Call the Axial Crack Stability Module when crack and/or loading change occurs |
| 204 | Solution not found for axial TWC stability from limit load or EPFM methods | Write logical error message and Call the Axial Crack Stability Module when crack and/or loading change occurs |
| 205 | Iteration limit of 5000 exceeded but no limit load solution found for axial TWC stability | Write logical error message and Call the Axial Crack Stability Module when crack and/or loading change occurs |
| 206 | Initial crack size starting estimate for axial TWC stability from EPFM solution could not be found in 5000 iterations | Write logical error message and Call the Axial Crack Stability Module when crack and/or loading change occurs |
| 207 | Initial crack size starting estimate for axial TWC stability not within bounds, [0, 100×R<sub>m</sub>] | Write logical error message and Call the Axial Crack Stability Module when crack and/or loading change occurs |
| 301 | Unqualified good solution or trivial case solution found for the axial SC stability | Write informational message to output file and move to next case |
| 302 | Unqualified good solution or trivial case solution found for the axial TWC stability using limit load Calculations | Write informational message to output file and move to next case |
| 303 | Axial TWC limit load solution not in the range, [0,100×R<sub>m</sub>] | Write informational message to output file and move to next case |
| 304 | Unqualified good solution or trivial case solution found for the axial TWC stability from EPFM Calculations | Write informational message to output file and move to next case |
| 305 | Solution found for axial TWC stability using EPFM, but stress in ligament at c_max (maximum crack length for failure) exceeds ultimate stress | Write informational message to output file and move to next case |
| 306 | Solution found for axial TWC stability using EPFM, but numerical method’s iteration limit has been exceeded and stress is intermediate, c_max solution is from minimum error of J and dJ/da equations | Write informational message to output file and move to next case |
| 307 | Numerical solution method’s iteration limit exceeded when performing axial TWC stability using EPFM calculations, and stress is high, c_max = 0 is assumed | Write informational message to output file and move to next case |
| 308 | Numerical solution method’s iteration limit exceeded when performing axial TWC stability using EPFM calculations, and stress is low. Hence c_max = 100×R<sub>m</sub> is assumed | Write informational message to output file and move to next case |
| 309 | One or more of R<sub>m</sub>/t, rho, Ramberg-Osgood hardening exponent n, is beyond the range for which influence coefficients (h₁,F) are available [21] | Write informational message to output file and move to next case |
| 310 | Numerical iteration limit exceeded for axial TWC stability from EPFM solution, and stress is intermediate, but solution for minimum error of J and dJ/da equations could not be found | Write logical error message and Call the Axial Crack Stability Module when crack and/or loading change occurs |

표 12개 전사
