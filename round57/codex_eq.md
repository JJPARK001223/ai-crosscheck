# round57 Codex 4단계: B048 수식·수학 표기 전수 대조

## 점검 기준과 근거

- 대상 PDF: `J:\Desktop\XLPR\xLPR참고문헌\(ML16341B048)Cyclic stress intensity factors.pdf` (37쪽).
- 대상 HTML: `J:\Desktop\XLPR\2026_10_21_B048_주기응력확대계수\XLPR_주기응력확대계수_B048.html` (페이지 카드 `p1`~`p29`). HTML 페이지는 브라우저 인쇄 매수가 아니라 카드에 적힌 번호이다.
- PDF SHA-256: `3aaf46e98c5819a86a98fc1a3e29cf64b7b6cf94ab23c8433ca91f9e34cd764a`.
- HTML SHA-256: `95e89ba604c4a75b62536aa38cbdcf9d31d5539e4cb147261ae5d93e94b2eed5`.
- 방법: PyMuPDF로 PDF 1~37쪽 전부를 1.5배 PNG로 렌더링하여 순서대로 직접 이미지 확인. Figure 1, Eqn.2, Eqn.3~5는 3배 영역 이미지로 추가 확인. 텍스트 추출은 검색 보조로만 사용했다. HTML의 각 카드 본문·표·`data-tex`를 원문 이미지에 대조했다. 다른 AI 보고서는 읽지 않았다. 외부 문헌·물리적 타당성 판단은 사용하지 않았다.
- 범위: 번호 식 10개(1, 2, 3a~c, 4, 5a~c, 6), Figure 1 적분식, 문장 속 기호·조건, 그림의 축·치수, 표의 배열·부등식·단위. 같은 식 안의 기호는 식 전체에 포함한다. 반복 기호는 같은 페이지·동일 위치군에서 묶되 RTIF 행과 출력 배열은 행별로 기록했다. 문서 버전·날짜·목차 쪽수·참고문헌 번호는 수식으로 세지 않았다.
- 판정: **일치**는 수학적 문자·상하첨자·부호·배열 순서 대조 결과이다. 글꼴·공백까지 동일한 복제라는 뜻은 아니다. **재구성**은 원문 문장을 새 등식·기호열로 만든 경우이다. 원문 식 자체의 비정상 표기는 교정하지 않는다.
- HTML은 수정하지 않았다. 루트 `PROBLEM.md`는 round28 B051 문제여서 이번 사용자 지정 B048 범위를 우선했다. 시작 `git pull` 결과는 `Already up to date.`였으며 기존 사용자 변경은 포함하지 않는다.

## (A) PDF 수식 전수 목록

아래는 PDF쪽(인쇄쪽) 순서이다. `—`는 해당 수학 표기가 없다는 뜻이다. 표의 식은 읽기 쉬운 선형 표기/TeX로 기록한다.

| PDF쪽(인쇄쪽) | 수식/표기 및 지면 위치 | HTML 페이지 | 일치 여부 |
|---|---|---|---|
| 1~4(쪽번호 없음) | 표지·면책·서명·개정 이력: 점검 대상 수학 표기 없음 | 1 | 해당 없음 |
| 5(iv) | Executive Summary: ΔK, K | 2 | 일치 |
| 6(v) | 목차: 수학 표기 없음 | 목차 | 해당 없음 |
| 7(vi) | 그림 목록: 수학 표기 없음 | — | 해당 없음 |
| 8(vii) | 표 목록: 수학 표기 없음 | — | 해당 없음 |
| 9(viii) | 기호표 `a`: Crack depth | 28 | 일치 |
| 9(viii) | 기호표 `c`: Half crack length | 28 | 일치 |
| 9(viii) | 기호표 `csp`: Specific heat | 28 | 일치 |
| 9(viii) | 기호표 `E`: Elastic modulus | 28 | 일치 |
| 9(viii) | 기호표 `H1`: Inner pipe thickness | 28 | 일치 |
| 9(viii) | 기호표 `h2`: Outer pipe thickness | 28 | 일치 |
| 9(viii) | 기호표 `K`: Stress intensity factor | 28 | 일치 |
| 9(viii) | 기호표 `r`: Radial coordinate | 28 | 일치 |
| 9(viii) | 기호표 `r_i`: Inside radius | 28 | 일치 |
| 9(viii) | 기호표 `r_o`: Outside radius | 28 | 일치 |
| 9(viii) | 기호표 `r_c`: Interface radius | 28 | 일치 |
| 9(viii) | 기호표 `t`: Time | 28 | 일치 |
| 9(viii) | 기호표 `T`: Temperature | 28 | 일치 |
| 9(viii) | 기호표 `α`: Coefficient of thermal expansion | 28 | 일치 |
| 9(viii) | 기호표 `ΔK`: Cyclic stress intensity factor | 28 | 일치 |
| 9(viii) | 기호표 `Δp`: Deviation from operating pressure | 28 | 일치 |
| 9(viii) | 기호표 `K(이탤릭)`: Thermal conductivity | 28 | 일치 |
| 9(viii) | 기호표 `ρ`: Density | 28 | 일치 |
| 9(viii) | 기호표 `θ`: Angular location | 28 | 일치 |
| 9(viii) | 기호표 `σ_T`: Global membrane stress | 28 | 일치 |
| 9(viii) | 기호표 `σ_B`: Global bending stress | 28 | 일치 |
| 9(viii) | 기호표 `μ`: Poisson’s Ratio | 28 | 일치 |
| 10(ix) | 약어표: 별도 수식·단위·배열 없음 | 28 | 해당 없음 |
| 11(1) | §1.1~1.2: 별도 기호식 없음 | 3~4 | 해당 없음 |
| 12(2) | §1.3: stress intensity factor (K) | 4 | 일치 |
| 13(3) | §2: ΔK, K; §2.2: 재료 두께 h1, h2 | 5 | 일치 |
| 14(4) | §2.3: ΔK | 6 | 일치 |
| 15(5) | Figure 1: 냉각재 이력 그래프: T, t | 7 | 일치 |
| 15(5) | Figure 1: 온도분포 그래프: T, r, t₀, t₁, t₂, r₁, r₀ | 7 | 일치 |
| 15(5) | Figure 1: 배관 동심원: h₁, h₂, r₀ | 7 | 일치 |
| 15(5) | Figure 1: 열응력 그래프: σ_B, η, t₁, t₂, r₀ | 7 | 일치 |
| 15(5) | Figure 1 Crack Size: 2c | 7 | 일치 |
| 15(5) | Figure 1 Crack Size: 작은 세로 치수 문자(하단 화살표 옆) | — | 확인 불가/전사 없음: C1 |
| 15(5) | Figure 1: `K_I=∫₀ᵃ σ(x)m(x,a)dx` | 7 | 일치 |
| 15(5) | Figure 1 K 이력 그래프: K_m, t, a₁,c₁ / a₂,c₂ | 7 | 일치 |
| 15(5) | Figure 1 Resulting K_a, K_c | 7 | 일치 |
| 15(5) | Figure 1 정렬 그래프: K(max), a, c₁, c₂ | 7 | 일치 |
| 16(6) | §2.4.1 본문: 응력으로부터 K를 구함 | 8 | 일치 |
| 17(7) | 가정표 마지막 행: E, μ (반복 포함) | 8 | 일치 |
| 17(7) | §2.4.2: T(r, t) | 9, 16 | 일치 |
| 17(7) | Eqn.1: `\rho c_{sp}\,\dfrac{\partial T}{\partial t}=\dfrac{1}{r}\,\dfrac{\partial}{\partial r}\!\left(k\,r\,\dfrac{\partial T}{\partial r}\right)` | 9 | 일치 |
| 17(7) | 식 1 아래 문장: k, c_sp, ρ | 9 | 일치 |
| 18(8) | Eqn.2: `\dfrac{\delta^{2}h^{2}\rho c_{sp}}{\Delta t}\left(T_j-T^{*}_{j}\right)=\dfrac{1}{r_j}\Bigl[T_{j+1}\left(k_{j+1}r_{j+1}+k_jr_j\right)-T_j\left(k_{j+1}r_{j+1}+2k_jr_j+k_{j-1}r_{j-1}\right)+T_{j-1}(k_jr_j+k_{j-1}r_{j-1}\,\Bigr]` | 10 | 일치 |
| 18(8) | 식 2 아래: 하첨자 j, “j-th” node, 상첨자 * | 10 | 일치 |
| 18(8) | δ: [1/number of spatial increments in the material 1]=[1/number of spatial increments in material 2] | 10, 16 | 10의 정의 일치; 16은 δ=를 추가한 재구성(B2) |
| 18(8) | h: total pipe wall thickness | 10 | 일치 |
| 18(8) | §2.4.3: E, μ, α; 뒤 문장 E와 μ 반복 | 11 | 일치 |
| 18(8) | 축변형률 εz; constant (not zero), zero net axial load라는 문장 | 11, 16 | 11 내용 일치; 16 등식 재구성(B2) |
| 19(9) | Figure 2: r₀, r_i, r_c, h, h₁, h₂; Mat 1, Mat 2; Insulated OD | 11 | 일치 |
| 19(9) | Eqn.3a: `\sigma_r=\dfrac{E}{1-\mu}\,\dfrac{1}{r^{2}}\left\{-\alpha_1\int_{r_i}^{r}r\,(T-T_0)\,dr+\dfrac{r^{2}-r_i^{2}}{r_o^{2}-r_i^{2}}\,\Omega\right\}` | 12 | 일치 |
| 19(9) | Eqn.3b: `\sigma_\theta=\dfrac{E}{1-\mu}\,\dfrac{1}{r^{2}}\left\{\alpha_1\int_{r_i}^{r}r\,(T-T_0)\,dr-\alpha_1 r^{2}(T-T_0)+\dfrac{r^{2}+r_i^{2}}{r_o^{2}-r_i^{2}}\,\Omega\right\}` | 12 | 일치 |
| 19(9) | Eqn.3c: `\sigma_z=\dfrac{E}{1-\mu}\left\{\dfrac{2}{r_o^{2}-r_i^{2}}\,\Omega-\alpha_1(T-T_0)\right\}` | 12 | 일치 |
| 19(9) | Eqn.4: `\Omega=\alpha_1\int_{r_i}^{r_c}r\,(T-T_0)\,dr+\alpha_2\int_{r_c}^{r_o}r\,(T-T_{o})\,dr` | 12 | 일치 |
| 19(9) | Eqn.5a: `\sigma_r=\dfrac{E}{1-\mu}\,\dfrac{1}{r^{2}}\left\{-\alpha_2\int_{r_c}^{r}r\,(T-T_0)\,dr-\dfrac{r_o^{2}-r^{2}}{r_o^{2}-r_i^{2}}\,\alpha_1\int_{r_1}^{r_c}r\,(T-T_{o})\,dr+\dfrac{r^{2}-r_i^{2}}{r_o^{2}-r_i^{2}}\,\alpha_2\int_{r_c}^{r_o}r\,(T-T_{o})\,dr\right\}` | 13 | 일치 |
| 20(10) | Eqn.5b: `\sigma_\theta=\dfrac{E}{1-\mu}\,\dfrac{1}{r^{2}}\left\{\alpha_2\int_{r_c}^{r}r\,(T-T_0)\,dr-\alpha_2 r^{2}(T-T_0)+\dfrac{r^{2}+r_o^{2}}{r_o^{2}-r_i^{2}}\,\alpha_1\int_{r_i}^{r_c}r\,(T-T_0)\,dr+\dfrac{r^{2}+r_i^{2}}{r_o^{2}-r_i^{2}}\,\alpha_2\int_{r_c}^{r_o}r\,(T-T_0)\,dr\right\}` | 13 | 일치 |
| 20(10) | Eqn.5c: `\sigma_z=\dfrac{E}{1-\mu}\left\{\dfrac{2}{r_o^{2}-r_i^{2}}\,\Omega-\alpha_2(T-T_0)\right\}` | 13 | 일치 |
| 20(10) | 식 5 아래 문장: μ, α1=α2 | 13 | 일치 |
| 20(10) | 유효 탄성계수 E | 14 | 일치 |
| 20(10) | Eqn.6: `E=\dfrac{E_1A_1+E_2A_2}{A_1+A_2}` | 14 | 일치 |
| 20(10) | 식 6 뒤: subscript 1 / subscript 2 (inner / outer) | 14 | 일치 |
| 20(10) | 조건 α₁=α₂ and T = constant; all stresses are zero는 문장 | 15, 16 | 15 일치; 16의 ⇒는 원문에 없음(B1) |
| 20(10) | 조건 α₁ ≠ α₂; 문장 속 T=T₀ | 15, 16 | 15 일치; 16은 콜론으로 재구성(B3) |
| 20(10) | reference temperature (T₀), T₀ 반복; 70°F (상온); α 값 설명의 70°F 반복 | 15 | 일치; 16의 T₀=70°F는 PDF21에도 실제로 존재 |
| 20(10) | 물성 나열: α, E, μ, ρ, c_sp; 이어 α 반복 | 15 | 일치 |
| 20(10) | §2.4.4: (σ_T and σ_B); 별도 괄호의 (T_sig, usually …) | 17, 16 | 17 기호 일치; 16의 (σ_T, σ_B, T_sig)는 새 묶음(B3) |
| 21(11) | §2.4.4: T_sig; T₀ = 70°F | 17, 16 | 일치 |
| 21(11) | 압력 편차 Δp | 17, 16 | 일치 |
| 21(11) | 사용자 입력 DispFactorIn | 17 | 일치 |
| 21(11) | §2.4.5: K_max, K_min (정의와 후속 문장 반복) | 18 | 일치 |
| 21(11) | 문장 속 ΔK (K_max - K_min): 등호 없음 | 18, 16 | 일치 |
| 22(12) | §2.4.6: K_max, K_min (출력 파일) | 19 | 일치 |
| 23(13) | Table 1 RTIF-3: SI units (특정 수식·수치 단위 없음) | 20 | 일치 |
| 24(14) | Table 1 RTIF-9: T(r, t) | 20, 16 | 일치 |
| 24(14) | Table 1 RTIF-10: σ(r, t) | 20, 16 | 일치 |
| 24(14) | Table 1 RTIF-11: K, a/h, a/c; 3-d array (a/c, a/h, θ) | 20, 16 | 일치 |
| 24(14) | Table 1 RTIF-12: K, a/h, a/c; 3-d array (a/c, a/h, θ) | 20, 16 | 일치 |
| 24(14) | Table 1 RTIF-13: K, a/h, a/c; 3-d array (a/c, a/h, θ) | 20, 16 | 일치 |
| 24(14) | Table 1 RTIF-14: K, a/h, a/c; 3-d array (a/c, a/h, θ) | 20, 16 | 일치 |
| 24(14) | Table 1 RTIF-15: K, c; 2-d array (c, θ) | 20, 16 | 일치 |
| 24(14) | Table 1 RTIF-16: K, c; 2-d array (c, θ) | 20, 16 | 일치 |
| 24(14) | Table 1 RTIF-17: K, c; 2-d array (c, θ) | 20, 16 | 일치 |
| 25(15) | Table 1 RTIF-18: K, c; 2-d array (c, θ) | 20, 16 | 일치 |
| 25(15) | Table 1 RTIF-19: K, a/h, a/c; 2-d array (a/c, a/h) | 20, 16 | 일치 |
| 25(15) | Table 1 RTIF-20: K, a/h, a/c; 2-d array (a/c, a/h) | 20, 16 | 일치 |
| 25(15) | Table 1 RTIF-21: K, a/h, a/c; 2-d array (a/c, a/h) | 20, 16 | 일치 |
| 25(15) | Table 1 RTIF-22: K, a/h, a/c; 2-d array (a/c, a/h) | 20, 16 | 일치 |
| 25(15) | Table 1 RTIF-23: K; 1-d array (c) | 20, 16 | 일치 |
| 25(15) | Table 1 RTIF-24: K; 1-d array (c) | 20, 16 | 일치 |
| 25(15) | Table 1 RTIF-27: 1-d array(지면에는 (θ) 없음) | 20 | 일치 |
| 25(15) | Table 1 RTIF-28: 1-d array (θ) | 20, 16 | 일치 |
| 25(15) | Table 1 RTIF-29: 1-d array (θ) | 20, 16 | 일치 |
| 26(16) | Table 1 RTIF-30: 1-d array (θ) | 20, 16 | 일치 |
| 26(16) | Table 1 RTIF-35: 1-d array (θ) | 20, 16 | 일치 |
| 26(16) | RTIF-31~34,36~38·§3.2~3.3: 추가 기호식 없음 | 20~21 | 해당 없음 |
| 27(17) | §3.3~3.4: 추가 기호식 없음 | 21~22 | 해당 없음 |
| 28(18) | Table 2 TitleIn: (1≤characters≤60) | 22, 16 | 일치 |
| 28(18) | IATypeIn: 1 – Thermal; 2 – Stratification; 3 – Mechanical | 22 | 일치 |
| 28(18) | IUnitsIn: 1-US Customary; 2-SI; IPrintIn: Enter zero for no output | 22 | 일치 |
| 28(18) | NHist: (<=10000) | 22, 16 | 일치 |
| 28(18) | Table 2 TimeA [ ]: NHist values of Time | 22 | 일치 |
| 28(18) | Table 2 FlTempA [ ]: NHist values of Fluid temperature | 22 | 일치 |
| 28(18) | Table 2 PrA [ ]: NHist values of Change in Pressure | 22 | 일치 |
| 28(18) | 자료형 Real (8): PipeODIn, ThickIIn, ThickOIn, FlowXIn, NuIn, TimeA, FlTempA, PrA, TimeStepIn, TzeroIn, Youngs1In, Rho1In, Cp1In, Alpha1In, K1T1In, K1T2In, T11In, T12In, Youngs2In, Rho2In, Cp2In, Alpha2In, K2T1In, K2T2In, T21In | 22 | 일치 |
| 28(18) | 온도 표기 T11, T12, T21, T22 (열전도도·온도 행 설명에 반복) | 22 | 일치 |
| 29(19) | Table 2 T22In, SigMNOIn, SigBNOIn, OpTempIn, SigMminIn, SigMmaxIn, SigBminIn, SigBmaxIn, DispFactorIn: Real (8) | 22 | 일치 |
| 29(19) | OpTempIn 설명: SigMNO, SigBNO | 22 | 일치 |
| 29(19) | SigMminIn: (only for IYType = 2 or 3) | 22 | 일치 |
| 29(19) | SigMmaxIn: (only for IYType = 2 or 3) | 22 | 일치 |
| 29(19) | SigBminIn: (only for IYType = 2 or 3) | 22 | 일치 |
| 29(19) | SigBmaxIn: (only for IYType = 2 or 3) | 22 | 일치 |
| 29(19) | DispFactorIn: (only for IAType=2) | 22 | 일치 |
| 29(19) | NumSegsIn: (<=100);  | 22, 16(상한) | 일치 |
| 29(19) | NAOCIn: (<=100); a/c, K | 22, 16(상한) | 일치 |
| 29(19) | NAOTIn: (<=100); a/h, K | 22, 16(상한) | 일치 |
| 29(19) | NCTWCircIn: (<=100); c, K | 22, 16(상한) | 일치 |
| 29(19) | NCTWAxIn: (<=100); c, K; only for IAType=1 | 22, 16(상한) | 일치 |
| 29(19) | AOCa [ ]: Real (8); NAOC a/c values | 22 | 일치 |
| 29(19) | AOTa [ ]: Real (8); NAOT a/h values | 22 | 일치 |
| 29(19) | CTWCirca [ ]: Real (8); NCTWCirc c values | 22 | 일치 |
| 29(19) | CTWAxa [ ]: Real (8); NCTWAx c values | 22 | 일치 |
| 29(19) | 자료형 주석: Integer; Real (8); Character; 제외 문자 @#$%^&*(); [] = array input | 22 | 일치 |
| 30(20) | Table 3 KCircDeepMxO[ ]: 3-d array [a/t, a/c, Segment Number]; maximum/minimum K | 23, 16(배열) | 일치 |
| 30(20) | Table 3 KCircDeepMnO[ ]: 3-d array [a/t, a/c, Segment Number]; maximum/minimum K | 23, 16(배열) | 일치 |
| 30(20) | Table 3 KCircSurfMxO[ ]: 3-d array [a/t, a/c, Segment Number]; maximum/minimum K | 23, 16(배열) | 일치 |
| 30(20) | Table 3 KCircSurfMnO[ ]: 3-d array [a/t, a/c, Segment Number]; maximum/minimum K | 23, 16(배열) | 일치 |
| 30(20) | KCircTWMxMO[ ]: 2-d array [c, Segment Number]; maximum/minimum K | 23, 16(배열) | 일치 |
| 30(20) | KCircTWMnMO[ ]: 2-d array [c, Segment Number]; maximum/minimum K | 23, 16(배열) | 일치 |
| 30(20) | KCircTWMxBO[ ]: 2-d array [c, Segment Number]; maximum/minimum K | 23, 16(배열) | 일치 |
| 30(20) | KCircTWMnBO[ ]: 2-d array [c, Segment Number]; maximum/minimum K | 23, 16(배열) | 일치 |
| 30(20) | PaxStrMaxO: input PrA [ ] | 23 | 일치 |
| 30(20) | AllAxStrMaxO[ ]: 1-d array [Segment Number] | 23, 16(배열) | 일치 |
| 30(20) | AllAxStrMinO[ ]: 1-d array [Segment Number] | 23, 16(배열) | 일치 |
| 30(20) | TimeMaxAllAxialO[ ]: 1-d array [Segment Number] | 23, 16(배열) | 일치 |
| 30(20) | TimeMinAllAxialO[ ]: 1-d array [Segment Number] | 23, 16(배열) | 일치 |
| 30(20) | RiseTimeAxStrO[ ]: 1-d array [Segment Number] | 23, 16(배열) | 일치 |
| 30(20) | AllAxStrMaxO, AllAxStrMinO 설명의 Pr | 23 | 일치 |
| 30(20) | KAxDeepMxO[ ]: Two-d array [a/t, a/c]; maximum/minimum K | 23, 16(배열) | 일치 |
| 30(20) | KAxDeepMnO[ ]: Two-d array [a/t, a/c]; maximum/minimum K | 23, 16(배열) | 일치 |
| 30(20) | KAxSurfMxO[ ]: Two-d array [a/t, a/c]; maximum/minimum K | 23, 16(배열) | 일치 |
| 30(20) | KAxSurfMnO[ ]: Two-d array [a/t, a/c]; maximum/minimum K | 23, 16(배열) | 일치 |
| 30(20) | KAxTWMxO[ ]: One-d array [c]; maximum/minimum K | 23, 16(배열) | 일치 |
| 30(20) | KAxTWMnO[ ]: One-d array [c]; maximum/minimum K | 23, 16(배열) | 일치 |
| 31(21) | PhoopStrMaxO: input PrA [ ]; AllHoopStrMaxO/MinO 설명의 Pr | 23 | 일치 |
| 31(21) | TimeMaxAllHoopO, TimeMinAllHoopO, RiseTimeHpStrO, TempMaxO, TempMinO: 배열 괄호 없는 출력 이름; TempMaxO/MinO에 Only for Type 1 input | 23 | 일치 |
| 31(21) | Ierror: Integer; Value between 101-120,123-128,131-144 or 0 | 23 | 일치 |
| 31(21) | Table 3 주: K = 정상 운전으로부터의 excursion (설명 문장, 실제 등호 없음) | 23 | 일치 |
| 31(21) | Table 4: K; 단위 W/(m-°K) | 24, 16(단위; ν의 --는 24) | 일치 |
| 31(21) | Table 4: C; 단위 J/(kg-°K) | 24, 16(단위; ν의 --는 24) | 일치 |
| 31(21) | Table 4: ρ; 단위 kg/m³ | 24, 16(단위; ν의 --는 24) | 일치 |
| 31(21) | Table 4: κ; 단위 m²/s | 24, 16(단위; ν의 --는 24) | 일치 |
| 31(21) | Table 4: E; 단위 MPa | 24, 16(단위; ν의 --는 24) | 일치 |
| 31(21) | Table 4: ν; 단위 -- | 24, 16(단위; ν의 --는 24) | 일치 |
| 31(21) | Table 4: α; 단위 °C⁻¹ | 24, 16(단위; ν의 --는 24) | 일치 |
| 32(22) | §3.5~3.6: 추가 수학 표기 없음 | 25 | 해당 없음 |
| 33(23) | Figure 3 분기: IAType; IAType = 2 or 3; IAType = 1 | 25, 16 | 일치 |
| 33(23) | Figure 3: Calculate K (CalcK23); InitK; Calculate K (CalcK) | 25 | 일치 |
| 34(24) | 권고: 추가 수학 표기 없음 | 26 | 해당 없음 |
| 35(25) | Lessons-Learned: 추가 수학 표기 없음 | 26 | 해당 없음 |
| 36(26) | Summary: 추가 수학 표기 없음 | 26 | 해당 없음 |
| 37(27) | 참고문헌 [1], [2] 제목: K Calculator | 27 | 일치 |

## (B) 누락·오류

### B1. 16쪽에 원문에 없는 ⇒ 추가 (확인 사실)

HTML 16쪽 세 번째 수식은 `α₁=α₂ and T=constant ⇒ all stresses are zero`이다. PDF20(인쇄10)의 원문은 조건식 `α1=α2`, `T = constant`를 문장에 넣고 응력이 영이라는 결과를 말한다. **원문에 ⇒는 없다.** HTML 자체도 바로 아래에 “원문은 ⇒ 기호 없이 문장으로 서술”이라고 적고 있다. 따라서 16쪽 마지막의 “지면 그대로”, “원문에 없는 수식은 추가하지 않았다”는 설명과 양립하지 않는다. 여기서는 내용의 물리적 옳고 그름을 판정하지 않았다.

### B2. 문장 설명을 새 등식으로 바꿈 (확인 사실)

- 16쪽 첫 행: 원문 PDF18(8)은 δ라는 기호 뒤에 “is … which equals”를 쓰고 두 역수의 `[...] = [...]`를 인쇄했다. HTML은 문장 첫 부분을 `δ=`로 바꾸었다. 두 역수의 동등 관계와 값은 일치하지만 **δ 바로 뒤 등호는 원문 인쇄 기호가 아니다.** 10쪽에는 원문 정의가 문장으로 들어 있다.
- 16쪽 둘째 행: `ε_z=constant (not zero)`라는 등식은 원문 PDF18(8)에 인쇄되지 않았다. 원문은 축변형률 εz가 매 순간 일정하고(영이 아님), 순 축하중을 영으로 만드는 값이라는 문장이다. **εz 뒤 등호는 추가 기호**이다. 11쪽은 이 조건을 문장으로 설명한다.

### B3. 문장 속 별도 기호를 새 기호열로 묶음 (확인 사실)

- 16쪽 넷째 행의 `α₁≠α₂:` 뒤 **콜론은 원문 PDF20(10)의 그 위치에 없다.** 원문은 “However if …, a uniform temperature …” 형식이다. α₁≠α₂와 T=T₀ 자체는 원문과 일치한다.
- 16쪽 여섯째 행 `(σ_T, σ_B, T_sig)`는 원문에 없는 세 원소 괄호열이다. PDF20(10)은 두 응력을 `(σ_T and σ_B)`로 묶고, 적용 온도는 뒤의 별도 괄호 `(T_sig, usually …)`에 적었다. 각 기호는 원문에 있지만 **세 기호를 하나의 괄호 안에 쉼표로 나열한 표기는 원문에 없다.** 17쪽에는 기호와 설명이 들어 있다.

### B4. 16쪽의 “지면 순서대로”는 실제 배열 순서와 다름 (확인 사실)

16쪽은 원문 p.8 → p.10 → p.11을 진행한 뒤, p.7의 `T(r,t)`로 되돌아간다. 원문 순서는 T(r,t) → δ 설명 → εz 설명 → p.10의 조건들·응력/온도 기호 → p.11의 압력·ΔK → p.14의 σ(r,t)이다. 페이지 출처 자체는 각 행 아래에 대부분 기재되어 있으나, “지면 순서대로”라는 문구는 현재 배치와 다르다.

### B5. Figure 1 작은 세로 치수 문자의 전사 없음 (일부 확인 불가)

PDF15(5) Crack Size 그림은 `2c` 외에도 세로 치수 화살표 옆에 작은 문자가 있다. HTML7은 `Crack Size(2c 표시)`만 기록하고 그 작은 문자는 옮기지 않았다. **해당 문자 위치가 전사되지 않은 사실은 확인된다.** 문자가 정확히 무엇인지는 C1에 유보한다.

### 번호 식 및 그 밖의 표기에 대한 확인 결과

- Eqn.1, 2, 3a~c, 4, 5a~c, 6은 HTML9·10·12·13·14에 모두 있으며, 이번 이미지 대조에서 추가 누락·부호/계수 오류를 확인하지 않았다.
- Figure 1 적분식은 HTML7에 있다. Figure 2의 반경·두께 표기와 Table 1~4의 배열·상한·단위는 위 A의 대응 카드에 있다.
- Eqn.2 마지막 항의 소괄호 닫힘 없음, Eqn.4 둘째 적분의 T_o, Eqn.5a 둘째 적분의 하한 r_1와 T_o, Eqn.5b의 서로 다른 분자(r²+r_o² / r²+r_i²)는 실제 지면과 맞는다. 물리적으로 바르게 고치라는 판정을 하지 않는다.
- 16쪽 `T₀=70°F`는 PDF21(11)에 실제로 인쇄되어 있으므로 새로 만든 등식으로 분류하지 않았다. PDF20(10)에는 T₀ 값과 70°F가 문장으로 서술되어 있다.
- 16·18쪽 `ΔK (K_max-K_min)`은 원문처럼 등호가 없다. 16쪽의 `T(r,t)`, `σ(r,t)`, `Δp`도 원문에 있는 기호식이다.
- 전 페이지 이미지에서 별도의 번호 식 7 이상은 확인되지 않았다. 번호 식은 세부문자 식을 각각 세면 10개이다.

## (C) 확인 불가 및 점검 한계

1. **C1: Figure 1 세로 균열 치수 문자.** PDF15(5) 그림의 작은 세로 치수 문자는 확대 이미지에서도 흐릿하다. 모양은 소문자 b처럼 보이지만 a/b 등 정확한 문자로 확정하지 않는다. 원본에 그 위치의 문자가 존재하며 HTML7에는 대응 전사가 없다는 것까지만 확인한다. 같은 그림의 2c, 적분식, 축 기호는 읽어 대조했다.
2. HTML은 파일 본문·표·수식 `data-tex`를 점검했다. 브라우저의 KaTeX 실행 결과나 최종 인쇄 레이아웃을 렌더링하여 확인한 작업은 아니다. 따라서 폰트/CDN 실패, 화면 잘림, 인쇄 시 식의 실제 가시성은 이번 결과로 보증하지 않는다. 수학 내용의 존재 대응은 HTML 카드 번호 기준이다.
3. 원문에 없는 변수 정의·물리적 유도·원문 식의 정오 판단은 수행하지 않았다. 원문이 H1/h2, K/k, μ/ν, a/h와 a/t 등을 달리 쓴 것은 그대로 대조했으며 이를 임의로 통일하지 않았다.

## Git 인계 기록 범위

이 보고서만 인계 대상이다. 커밋 SHA 및 원격 반영 결과는 커밋·push 후 대화 최종 응답으로 분리 보고한다(자기 커밋 SHA를 보고서에 넣어 후속 커밋이 필요해지는 상황을 피함).
