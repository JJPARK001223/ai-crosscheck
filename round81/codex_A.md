# B044 독립 전사 A

대상: `round81/input/b044.pdf`, 65쪽. PDF 전 쪽을 150 dpi 이미지로 열어 확인하였다. 본문 인쇄쪽은 PDF쪽 − 11이다. `round81/claude*.md`는 열지 않았다. 영어 문맥·제목은 원문을 유지하고, 수식은 LaTeX로 옮겼다. 원문에 없는 절댓값·교정식은 추가하지 않았다.

집계 기준: 번호식은 Eq. 1~18의 식 번호 단위, 번호 없는 식은 아래 U 목록의 **각 행** 단위이다. 연쇄 등식·연쇄 부등식·한 줄의 열거 조건은 한 행으로 세고, 같은 식의 다른 위치 재등장은 별도 행으로 기록하였다. 표 전 칸 전사는 Table 1~11의 11개이다. Table 17~21에서는 이번 범위인 수식·조건식만 별도로 옮겼다. 기호만 있는 축 이름, 눈금, 표의 단순 수치 데이터는 번호 없는 식 수에 넣지 않는다.

## 1. Numbered equations

### Eq. 1 — PDF 15 / 인쇄 4

Context: “The TWC length can be calculated by”

$$c'=\frac{\pi c_o}{2}\frac{R_i}{R_o+R_i}$$

원문 그대로: 오른쪽 번호 앞에 여분의 `s`가 있어 `s(Eq. 1)`로 인쇄되어 있다.

### Eq. 2 — PDF 18 / 인쇄 7

Context: “the K values at the ID and OD surface points (Point 1 and Point 2 in Figure 3, respectively)”

$$K_{\mathrm{I,ID}}^{\text{Non-idealized}}=\sigma\sqrt{\pi R_m\theta_1}\cdot F\cdot G_1=K_{\mathrm I}^{\text{Idealized}}\cdot G_1$$

### Eq. 3 — PDF 18 / 인쇄 7

Context: “These values were represented using the following equations.”

$$K_{\mathrm{I,OD}}^{\text{Non-idealized}}=\sigma\sqrt{\pi R_m\theta_1}\cdot F\cdot G_2=K_{\mathrm I}^{\text{Idealized}}\cdot G_2$$

### Eq. 4 — PDF 18 / 인쇄 7

Context: “Here, the applied stress (σ) is defined as,”

$$\sigma=\frac{N}{2\pi R_m t}\quad\text{for axial tension (N)}$$

### Eq. 5 — PDF 18 / 인쇄 7

Context: “Here, the applied stress (σ) is defined as,”

$$\sigma=\frac{M}{\pi R_m^2t}\quad\text{for global bending (M)}$$

### Eq. 6 — PDF 18 / 인쇄 7

Context: “the COD values at the center of the crack at OD and ID surfaces”

$$\mathrm{COD}_{\mathrm{ID}}^{\text{Non-idealized}}=\frac{4\sigma R_m\theta_1}{E}\cdot V\cdot H_1=\mathrm{COD}^{\text{Idealized}}\cdot H_1$$

### Eq. 7 — PDF 18 / 인쇄 7

Context: “were calculated from the FE analyses and were represented using the following equations.”

$$\mathrm{COD}_{\mathrm{OD}}^{\text{Non-idealized}}=\frac{4\sigma R_m\theta_1}{E}\cdot V\cdot H_2=\mathrm{COD}^{\text{Idealized}}\cdot H_2$$

### Eq. 8 — PDF 19 / 인쇄 8

Context: “Hence, Equations 6 and 7 can be rewritten as”

$$\mathrm{COD}_{\mathrm{ID}}^{\text{Non-idealized}}=\frac{4\sigma R_m\theta_1}{E}\cdot V_1\cdot H_1=\mathrm{COD}^{\text{Idealized}}\cdot H_1$$

### Eq. 9 — PDF 19 / 인쇄 8

Context: “V values for idealized TWCs were provided at the ID and OD surfaces as V1 and V2”

$$\mathrm{COD}_{\mathrm{OD}}^{\text{Non-idealized}}=\frac{4\sigma R_m\theta_1}{E}\cdot V_2\cdot H_2=\mathrm{COD}^{\text{Idealized}}\cdot H_2$$

### Eq. 10 — PDF 35 / 인쇄 24

Context: “The two half-crack lengths (a1 and a2, where a1 > a2) are normalized as”

$$\rho_1=\frac{a_1}{\sqrt{R_m t}},\qquad\rho_2=\frac{a_2}{\sqrt{R_m t}}$$

### Eq. 11 — PDF 36 / 인쇄 25

Context: “the K values for the non-idealized TWC were represented using the idealized TWC solutions along with K correction factors (G1 and G2).”

$$K_{\mathrm{I,ID}}^{\text{Non-idealized}}=\sigma\sqrt{\pi a_1}\cdot F\cdot G_1=K_{\mathrm I}^{\text{Idealized}}\cdot G_1$$

### Eq. 12 — PDF 36 / 인쇄 25

Context: “along with K correction factors (G1 and G2)”

$$K_{\mathrm{I,OD}}^{\text{Non-idealized}}=\sigma\sqrt{\pi a_1}\cdot F\cdot G_2=K_{\mathrm I}^{\text{Idealized}}\cdot G_2$$

### Eq. 13 — PDF 36 / 인쇄 25

Context: “where,”

$$\sigma=\frac{pR_i}{2t}$$

### Eq. 14 — PDF 36 / 인쇄 25

Context: “Similarly, the COD values for the non-idealized TWC can be represented as,”

$$\mathrm{COD}_{\mathrm{ID}}^{\text{Non-idealized}}=\frac{4\sigma a_1}{E}\cdot V_1\cdot H_1=\mathrm{COD}^{\text{Idealized}}\cdot H_1$$

### Eq. 15 — PDF 36 / 인쇄 25

Context: “V1 and V2 are the shape functions for the idealized TWC at the ID and OD surfaces, respectively.”

$$\mathrm{COD}_{\mathrm{OD}}^{\text{Non-idealized}}=\frac{4\sigma a_1}{E}\cdot V_2\cdot H_2=\mathrm{COD}^{\text{Idealized}}\cdot H_2$$

### Eq. 16 — PDF 54 / 인쇄 43

Context: “the FCGR parameters reported in [3] were employed as shown in Equation 16”

$$\mathrm{FCGR}=\mathrm da/\mathrm dN=C(\Delta K)^n=3.20\times10^{-10}(\Delta K)^{3.72}\quad[\mathrm{mm/cycle}]$$

### Eq. 17 — PDF 54 / 인쇄 43

Context: “The acceptance criterion for surface crack was specified as follows.”

$$\frac{[a/c_{,\mathrm{Exp.}}-a/c_{,\mathrm{Pred.}}]}{[a/c_{,\mathrm{Exp.}}]}<0.1\quad\text{(at wall penetration, }a/t=0.95\text{)}$$

원문 그대로: `[a/c,Exp. - a/c,Pred.] / [a/c,Exp.] < 0.1 (at wall penetration, a/t=0.95)`; 절댓값 없음. Exp./Pred.는 원문의 쉼표 이후 아래첨자 위치를 유지하였다.

### Eq. 18 — PDF 54 / 인쇄 43

Context: “The acceptance criterion for through-wall cracks was specified as follows.”

$$\frac{[\theta_1/\theta_{2,\mathrm{Exp.}}-\theta_1/\theta_{2,\mathrm{Pred.}}]}{[\theta_1/\theta_{2,\mathrm{Exp.}}]}<0.1\quad\text{(during through-wall crack growth)}$$

원문 그대로: `[θ1/θ2,Exp. - θ1/θ2,Pred.] / [θ1/θ2,Exp.] < 0.1`; 절댓값 없음.

## 2. Unnumbered equations, definitions and conditions

U 번호는 이 전사에서 위치를 찾기 위한 번호이며 원문 식 번호가 아니다. 표에 같은 조건이 반복되면 변수·행별로 보존하였다. 원문의 영어 비교문은 영어 문장을 함께 적어 대수식으로 바꾼 부분과 구분하였다.

| ID | PDF / 인쇄 | Equation / condition | Context |
|---|---|---|---|
| U001 | 16 / 5 | $\theta_1=\theta_2$ | Figure 2(a), idealized circumferential TWC. |
| U002 | 16 / 5 | $a_1=a_2$ | Figure 2(b), idealized axial TWC. |
| U003 | 18 / 7 | $\theta_1/\theta_2=1$ | “the crack is an idealized TWC.” |
| U004 | 19 / 8 | $\theta_1/\theta_2=1$ | “For the idealized TWCs” |
| U005 | 19 / 8 | $G_1=G_2=1.0$ | “G1 and G2 values are 1.0 for all idealized TWC cases.” (원문 비교문) |
| U006 | 20 / 9 | $R_m/t=5$ | Figure 6, global bending. |
| U007 | 20 / 9 | $\theta_1/\pi=0.25$ | Figure 6, global bending. |
| U008 | 20 / 9 | $\theta_1/\theta_2=1,\ 1.5,\ 2,\ 3,\ 4$ | Figure 6 curve labels. |
| U009 | 21 / 10 | $\theta_1/\theta_2=2$ | Figure 7(a), Axial tension. |
| U010 | 21 / 10 | $\theta_1/\theta_2=4$ | Figure 7(a), Axial tension. |
| U011 | 21 / 10 | $\theta_1/\theta_2=2$ | Figure 7(a), Global bending. |
| U012 | 21 / 10 | $\theta_1/\theta_2=4$ | Figure 7(a), Global bending. |
| U013 | 21 / 10 | $\theta_1/\theta_2=2$ | Figure 7(b), Axial tension. |
| U014 | 21 / 10 | $\theta_1/\theta_2=4$ | Figure 7(b), Axial tension. |
| U015 | 21 / 10 | $\theta_1/\theta_2=2$ | Figure 7(b), Global bending. |
| U016 | 21 / 10 | $\theta_1/\theta_2=4$ | Figure 7(b), Global bending. |
| U017 | 21 / 10 | $R_m/t=5$ | Figure 7 caption. |
| U018 | 21 / 10 | $\theta_1/\pi=0.25$ | Figure 7 caption. |
| U019 | 22 / 11 | $\theta_1/\theta_2=4$ | Figure 8 plot label. |
| U020 | 22 / 11 | $R_m/t=5$ | Figure 8 caption. |
| U021 | 22 / 11 | $\theta_1/\pi=0.25$ | Figure 8 caption. |
| U022 | 22 / 11 | $R_m/t=5$ | “Figure 9 shows the trend of the G values” |
| U023 | 23 / 12 | $R_m/t=5$ | Figure 9(a), Global bending. |
| U024 | 23 / 12 | $\theta_1/\pi=0.125,\ 0.25,\ 0.3,\ 0.4,\ 0.5$ | Figure 9(a), five legend entries. |
| U025 | 23 / 12 | $R_m/t=5$ | Figure 9(b), Global bending. |
| U026 | 23 / 12 | $\theta_1/\pi=0.125,\ 0.25,\ 0.3,\ 0.4,\ 0.5$ | Figure 9(b), five legend entries. |
| U027 | 23 / 12 | $R_m/t=5$ | Figure 9 caption (원문에 Figure 9가 PDF 28쪽에서도 재등장). |
| U028 | 28 / 17 | $R_m/t=5$ | Figure 9(a), Global bending. |
| U029 | 28 / 17 | $\theta_1/\pi=0.125,\ 0.25,\ 0.3,\ 0.4,\ 0.5$ | Figure 9(a), five legend entries. |
| U030 | 28 / 17 | $R_m/t=5$ | Figure 9(b), Global bending. |
| U031 | 28 / 17 | $\theta_1/\pi=0.125,\ 0.25,\ 0.3,\ 0.4,\ 0.5$ | Figure 9(b), five legend entries. |
| U032 | 28 / 17 | $R_m/t=5$ | Figure 9 caption. |
| U033 | 31 / 20 | $R_m/t=5$ | Figure 10(a), Global bending. |
| U034 | 31 / 20 | $\theta_1/\pi=0.125,\ 0.25,\ 0.3,\ 0.4,\ 0.5$ | Figure 10(a) curve label. |
| U035 | 31 / 20 | $R_m/t=5$ | Figure 10(b), Global bending. |
| U036 | 31 / 20 | $\theta_1/\pi=0.125,\ 0.25,\ 0.3,\ 0.4,\ 0.5$ | Figure 10(b), five legend entries. |
| U037 | 31 / 20 | $R_m/t=5$ | Figure 10 caption. |
| U038 | 35 / 24 | $a_1=\text{ID crack length}$ | Figure 15(a), definition. |
| U039 | 35 / 24 | $a_2=\text{OD crack length}$ | Figure 15(a), definition. |
| U040 | 35 / 24 | $a_1/a_2=3.15$ | Figure 15(a), first crack shape. |
| U041 | 35 / 24 | $a_1/a_2=1.92$ | Figure 15(a), second crack shape. |
| U042 | 35 / 24 | $a_1/a_2=1.56$ | Figure 15(a), third crack shape. |
| U043 | 35 / 24 | $a_1/a_2=3.15,\ 1.92,\ 1.56,\ 1.36,\ 1.20,\ 1.09,\ 1.02$ | Figure 15(b), “for the entire crack transition”. |
| U044 | 35 / 24 | $a_1=\text{ID crack length}$ | Figure 15(b), definition. |
| U045 | 35 / 24 | $a_2=\text{OD crack length}$ | Figure 15(b), definition. |
| U046 | 35 / 24 | $a_1>a_2$ | “The two half-crack lengths” before Eq. 10. |
| U047 | 36 / 25 | $\rho_1/\rho_2=1$ | “represents an idealized TWC.” |
| U048 | 36 / 25 | $a_1=a_2$ | “F denotes the shape function for the idealized TWC” |
| U049 | 36 / 25 | $\rho_1=\rho_2$ | “(a1= a2 or ρ1= ρ2)” |
| U050 | 36 / 25 | $a_1=\rho_1\sqrt{R_m t}$ | “with a half-crack length of a1 [=ρ1√(Rmt)].” |
| U051 | 37 / 26 | $R_m/t=2$ | Figure 16(a) legend. |
| U052 | 37 / 26 | $R_m/t=20$ | Figure 16(a) legend. |
| U053 | 37 / 26 | $R_m/t=2$ | Figure 16(b) legend, V1 and V2. |
| U054 | 37 / 26 | $R_m/t=20$ | Figure 16(b) legend, V1 and V2. |
| U055 | 38 / 27 | $R_m/t=5$ | “The trends of the K correction factors” |
| U056 | 38 / 27 | $G_1<1.0$ | “values of the correction factor at the ID surface (G1) are less than 1.0” (원문 비교문). |
| U057 | 38 / 27 | $G_2>1.0$ | “values of the correction factor at the OD surface (G2) are greater than 1.0.” (원문 비교문). |
| U058 | 38 / 27 | $H_1<1.0,\ H_2<1.0$ | “where both values are less than 1.0 for all cases.” (원문 비교문). |
| U059 | 41 / 30 | $R_m/t=5$ | Figure 17 plot label. |
| U060 | 41 / 30 | $\rho_1=0.5,\ 1.0,\ 2.0,\ 3.0$ | Figure 17 legend, G1 and G2. |
| U061 | 41 / 30 | $R_m/t=5$ | Figure 17 caption. |
| U062 | 42 / 31 | $R_m/t=5$ | Figure 18(a). |
| U063 | 42 / 31 | $\rho_1=0.5,\ 1.0,\ 2.0,\ 3.0$ | Figure 18(a) legend. |
| U064 | 42 / 31 | $R_m/t=5$ | Figure 18(b). |
| U065 | 42 / 31 | $\rho_1=0.5,\ 1.0,\ 2.0,\ 3.0$ | Figure 18(b) legend. |
| U066 | 42 / 31 | $R_m/t=5$ | Figure 18 caption. |
| U067 | 43 / 32 | $\theta_1/\theta_2=1.05$ | “This process is repeated until” (위첨자 b는 각주). |
| U068 | 44 / 33 | $c_1^*=c_1$ | Figure 19, initial ID half-crack length. |
| U069 | 44 / 33 | $c_2^*=\min(t,c_1/4)$ | Figure 19, initial OD half-crack length. |
| U070 | 44 / 33 | $K_{\mathrm{I,ID}}^{\text{Non-idealized}}=K_{\mathrm I}^{\text{Idealized}}\cdot G_1$ | Figure 20, ID surface. |
| U071 | 44 / 33 | $K_{\mathrm{I,OD}}^{\text{Non-idealized}}=K_{\mathrm I}^{\text{Idealized}}\cdot G_2$ | Figure 20, OD surface. |
| U072 | 46 / 35 | $A/t\ge0.95$ | Table 17, RTC-16*: “Any active surface crack where” |
| U073 | 46 / 35 | $\theta_1/\theta_2\ \text{or}\ a_1/a_2>1.05$ | Table 17, RTC-16*: “Any transitioning crack where” (원문 그대로, >1.05는 or 뒤에 한 번만 인쇄). |
| U074 | 46 / 35 | $\theta_1=\theta=c/R_i$ | Table 17, RTC-17*: “Circumferential crack” |
| U075 | 46 / 35 | $\theta_2=\min(t/R_o,\theta/4)$ | Table 17, RTC-17*: “Circumferential crack” |
| U076 | 46 / 35 | $a_1=a$ | Table 17, RTC-17*: “Axial crack” |
| U077 | 46 / 35 | $a_2=\min(t,a/4)$ | Table 17, RTC-17*: “Axial crack” |
| U078 | 47 / 36 | $A/t\ge0.95$ | Figure 22(a), first decision. |
| U079 | 47 / 36 | $\mathrm{cflag}=0$ | Figure 22(a), crack orientation decision. |
| U080 | 47 / 36 | $\theta_1=\theta=c/R_i$ | Figure 22(a), circumferential initial crack. |
| U081 | 47 / 36 | $\theta_2=\min(t/R_o,\theta/4)$ | Figure 22(a), circumferential initial crack. |
| U082 | 47 / 36 | $a_1=a$ | Figure 22(a), axial initial crack. |
| U083 | 47 / 36 | $a_2=\min(t,a_1/4)$ | Figure 22(a), axial initial crack (원문은 a1/4). |
| U084 | 47 / 36 | $\mathrm{cflag}=0$ | Figure 22(a), K Transition decision. |
| U085 | 47 / 36 | $\mathrm{cflag}=0$ | Figure 22(a), COD Transition decision. |
| U086 | 48 / 37 | $\mathrm{Kb}_{\mathrm{inner}}=G1_{\mathrm{inner}}*\mathrm{Kb}_{\mathrm{idealized}}$ | Figure 22(b), circumferential next time step. |
| U087 | 48 / 37 | $\mathrm{Km}_{\mathrm{inner}}=G2_{\mathrm{inner}}*\mathrm{Km}_{\mathrm{idealized}}$ | Figure 22(b), circumferential next time step. |
| U088 | 48 / 37 | $K_{\mathrm{inner}}=\mathrm{Kb}_{\mathrm{inner}}+\mathrm{Km}_{\mathrm{inner}}$ | Figure 22(b), circumferential next time step. |
| U089 | 48 / 37 | $\mathrm{Kb}_{\mathrm{outer}}=G1_{\mathrm{outer}}*\mathrm{Kb}_{\mathrm{idealized}}$ | Figure 22(b), circumferential next time step. |
| U090 | 48 / 37 | $\mathrm{Km}_{\mathrm{outer}}=G2_{\mathrm{outer}}*\mathrm{Km}_{\mathrm{idealized}}$ | Figure 22(b), circumferential next time step. |
| U091 | 48 / 37 | $K_{\mathrm{outer}}=\mathrm{Kb}_{\mathrm{outer}}+\mathrm{Km}_{\mathrm{outer}}$ | Figure 22(b), circumferential next time step. |
| U092 | 48 / 37 | $\mathrm{Kh}_{\mathrm{inner}}=G1_{\mathrm{inner}}*K_{\mathrm{idealized}}$ | Figure 22(b), axial next time step. |
| U093 | 48 / 37 | $\mathrm{Kh}_{\mathrm{outer}}=G1_{\mathrm{outer}}*K_{\mathrm{idealized}}$ | Figure 22(b), axial next time step. |
| U094 | 48 / 37 | $\theta_1/\theta_2\le1.05$ | Figure 22(b), circumferential decision (`<=` in source). |
| U095 | 48 / 37 | $a_1/a_2\le1.05$ | Figure 22(b), axial decision (`<=` in source). |
| U096 | 48 / 37 | $\text{Crack type}=\text{transition}$ | Figure 22(b), No branch. |
| U097 | 48 / 37 | $\text{Crack type}=\mathrm{TWC}$ | Figure 22(b), Yes branch. |
| U098 | 48 / 37 | $\mathrm{CODb}_{\mathrm{inner}}=H1_{\mathrm{inner}}*\mathrm{CODb}_{\mathrm{idealized}}$ | Figure 22(b), circumferential current time step. |
| U099 | 48 / 37 | $\mathrm{CODm}_{\mathrm{inner}}=H2_{\mathrm{inner}}*\mathrm{CODm}_{\mathrm{idealized}}$ | Figure 22(b), circumferential current time step. |
| U100 | 48 / 37 | $\mathrm{COD}_{\mathrm{inner}}=\mathrm{CODm}_{\mathrm{inner}}+\mathrm{CODb}_{\mathrm{inner}}$ | Figure 22(b), circumferential current time step. |
| U101 | 48 / 37 | $\mathrm{CODb}_{\mathrm{outer}}=H1_{\mathrm{outer}}*\mathrm{CODb}_{\mathrm{idealized}}$ | Figure 22(b), circumferential current time step. |
| U102 | 48 / 37 | $\mathrm{CODm}_{\mathrm{outer}}=H2_{\mathrm{outer}}*\mathrm{CODm}_{\mathrm{idealized}}$ | Figure 22(b), circumferential current time step. |
| U103 | 48 / 37 | $\mathrm{COD}_{\mathrm{outer}}=\mathrm{CODm}_{\mathrm{outer}}+\mathrm{CODb}_{\mathrm{outer}}$ | Figure 22(b), circumferential current time step. |
| U104 | 48 / 37 | $\mathrm{CODh}_{\mathrm{inner}}=H1_{\mathrm{inner}}*\mathrm{COD}_{\mathrm{idealized}}$ | Figure 22(b), axial current time step. |
| U105 | 48 / 37 | $\mathrm{CODh}_{\mathrm{outer}}=H1_{\mathrm{outer}}*\mathrm{COD}_{\mathrm{idealized}}$ | Figure 22(b), axial current time step. |
| U106 | 49 / 38 | $2\le R_m/t\le20$ | Table 18, Rm / Pipe mean radius; `2 <= Rm/t <= 20`. |
| U107 | 49 / 38 | $2\le R_m/t\le20$ | Table 18, T / Pipe wall thickness; `2 <= Rm/t <= 20`. |
| U108 | 49 / 38 | $\mathrm{CLID}<\pi$ | Table 18, CLID: `< π – Circ crack`. |
| U109 | 49 / 38 | $\mathrm{CLID}<25t$ | Table 18, CLID: `< 25t – Axial crack`. |
| U110 | 49 / 38 | $\mathrm{CLOD}<\pi$ | Table 18, CLOD: `< π – Circ crack`. |
| U111 | 49 / 38 | $\mathrm{CLOD}<25t$ | Table 18, CLOD: `<25t – Axial crack`. |
| U112 | 49 / 38 | $\mathrm{Cflag}=0$ | Table 18, “Circ crack”. |
| U113 | 49 / 38 | $\mathrm{Cflag}=1$ | Table 18, “Axial Crack”. |
| U114 | 49 / 38 | $G1=\mathrm{Gbending}\ \text{for cflag}=0$ | Table 19, G1i. |
| U115 | 49 / 38 | $G1=\mathrm{Ghoop}\ \text{for cflag}=1$ | Table 19, G1i. |
| U116 | 49 / 38 | $G1=\mathrm{Gbending}\ \text{for cflag}=0$ | Table 19, G1o. |
| U117 | 49 / 38 | $G1=\mathrm{Ghoop}\ \text{for cflag}=1$ | Table 19, G1o. |
| U118 | 49 / 38 | $G2=\mathrm{Gtension}\ \text{for cflag}=0$ | Table 19, G2i. |
| U119 | 49 / 38 | $G2=0\ \text{for cflag}=1$ | Table 19, G2i. |
| U120 | 49 / 38 | $G2=\mathrm{Gtension}\ \text{for cflag}=0$ | Table 19, G2o. |
| U121 | 49 / 38 | $G2=0\ \text{for cflag}=1$ | Table 19, G2o. |
| U122 | 49 / 38 | $H1=\mathrm{Gbending}\ \text{for cflag}=0$ | Table 19, H1i (원문 그대로: Gbending). |
| U123 | 49 / 38 | $H1=\mathrm{Ghoop}\ \text{for cflag}=1$ | Table 19, H1i (원문 그대로: Ghoop). |
| U124 | 49 / 38 | $H1=\mathrm{Gbending}\ \text{for cflag}=0$ | Table 19, H1o (원문 그대로: Gbending). |
| U125 | 49 / 38 | $H1=\mathrm{Ghoop}\ \text{for cflag}=1$ | Table 19, H1o (원문 그대로: Ghoop). |
| U126 | 49 / 38 | $H2=\mathrm{Htension}\ \text{for cflag}=0$ | Table 19, H2i. |
| U127 | 49 / 38 | $H2=0\ \text{for cflag}=1$ | Table 19, H2i. |
| U128 | 49 / 38 | $H2=\mathrm{Gtension}\ \text{for cflag}=0$ | Table 19, H2o (원문 그대로: Gtension). |
| U129 | 49 / 38 | $H2=0\ \text{for cflag}=1$ | Table 19, H2o. |
| U130 | 50 / 39 | $R_m/t<2\ \text{or}\ R_m/t>20$ | Table 20, 301: “Rm/t is less than 2 or greater than 20”. |
| U131 | 50 / 39 | $R_m/t=2$ | Table 20, 301, lower bound solution. |
| U132 | 50 / 39 | $R_m/t=20$ | Table 20, 301, upper bound solution. |
| U133 | 50 / 39 | $R_m/t<2$ | Table 20, 301, “will be used for”. |
| U134 | 50 / 39 | $R_m/t>20$ | Table 20, 301, “respectively.” |
| U135 | 50 / 39 | $\mathrm{CLID\_over\_CLOD}>4$ | Table 20, 302: “CLID_over_CLOD is greater than 4”. |
| U136 | 50 / 39 | $\mathrm{CLID\_over\_CLOD}=4$ | Table 20, 302, bound solution. |
| U137 | 50 / 39 | $\mathrm{CLID\_over\_CLOD}>4$ | Table 20, 302, “will be used for”. |
| U138 | 50 / 39 | $\mathrm{CLID\_over\_pi}<0.125\ \text{or}\ \mathrm{CLID\_over\_pi}>0.5$ | Table 20, 303: “is less than 0.125 or greater than 0.5 for circumferential transitioning crack”. |
| U139 | 50 / 39 | $\mathrm{CLID\_over\_pi}=0.125$ | Table 20, 303, lower bound solution. |
| U140 | 50 / 39 | $\mathrm{CLID\_over\_pi}=0.5$ | Table 20, 303, upper bound solution. |
| U141 | 50 / 39 | $\mathrm{CLID\_over\_pi}<0.125$ | Table 20, 303, “will be used for”. |
| U142 | 50 / 39 | $\mathrm{CLID\_over\_pi}>0.5$ | Table 20, 303, “respectively.” |
| U143 | 50 / 39 | $\mathrm{CLID\_over\_}\sqrt{R_m t}<0.5\ \text{or}\ \mathrm{CLID\_over\_}\sqrt{R_m t}>3$ | Table 20, 304: “is less than 0.5 or greater than 3 for axial transitioning crack”. |
| U144 | 50 / 39 | $\mathrm{CLID\_over\_}\sqrt{R_m t}=0.5$ | Table 20, 304, lower bound solution. |
| U145 | 50 / 39 | $\mathrm{CLID\_over\_}\sqrt{R_m t}=3$ | Table 20, 304, upper bound solution. |
| U146 | 50 / 39 | $\mathrm{CLID\_over\_}\sqrt{R_m t}<0.5$ | Table 20, 304, “will be used for”. |
| U147 | 50 / 39 | $\mathrm{CLID\_over\_}\sqrt{R_m t}>3$ | Table 20, 304, “respectively.” |
| U148 | 50 / 39 | $2\le R_m/t\le20$ | Table 21, “Circumferential and Axial”. |
| U149 | 50 / 39 | $1\le\theta_1/\theta_2\le4$ | Table 21, “Circumferential”. |
| U150 | 50 / 39 | $0.125\le\theta_1/\pi\le0.5$ | Table 21, “Circumferential”. |
| U151 | 50 / 39 | $1\le a_1/a_2\le4$ | Table 21, “Axial”. |
| U152 | 50 / 39 | $0.5\le a_1/\sqrt{R_m t}\le3$ | Table 21, “Axial”. |
| U153 | 52 / 41 | $R=0.1$ | “Fatigue load was applied using a sine wave loading with a stress ratio” |
| U154 | 53 / 42 | $\mathrm{FCGR}=3.20\times10^{-10}(\Delta K)^{3.72}$ | Figure 24(a), mm/cycle. |
| U155 | 53 / 42 | $\mathrm{FCGR}=3.20\times10^{-10}(\Delta K)^{3.72}$ | Figure 24(b), mm/cycle. |
| U156 | 54 / 43 | $a/t=0.95$ | “Once the depth of the surface crack reaches 95% of the wall thickness” |
| U157 | 54 / 43 | $\theta_1/\theta_2=1.05$ | “until an idealized through-wall crack is approximated” |
| U158 | 54 / 43 | $a/t=0.95$ | Validation Criteria, “at wall penetration”. |
| U159 | 54 / 43 | $a/t=0.95$ | Validation Results, “The predicted results are provided up to”. |
| U160 | 55 / 44 | $a/c=0.5$ | “initial surface cracks ... (TB-2 and TB-6)” |
| U161 | 55 / 44 | $a/c=1.0$ | “initial value ... (TB-3 and TB-5)” |
| U162 | 55 / 44 | $\theta_1=\theta_2$ | “for an idealized through-wall crack.” |
| U163 | 55 / 44 | $\theta_1=\theta_2$ | “Once an idealized through-wall crack is formed” |
| U164 | 57 / 46 | $\mathrm{FCGR}=3.20\times10^{-10}(\Delta K)^{3.72}\ \mathrm{mm/cycle}$ | Figure 28. |
| U165 | 58 / 47 | $\mathrm{FCGR}=2.30\times10^{-11}(\Delta K)^{4.8}\ \mathrm{mm/cycle}$ | Figure 29, optimized FCGR. |
| U166 | 58 / 47 | $3.20\times10^{-10}(\Delta K)^{3.72}\ \mathrm{mm/cycle}$ | Figure 30(a), “FCGR”, first legend expression. |
| U167 | 58 / 47 | $2.30\times10^{-11}(\Delta K)^{4.8}\ \mathrm{mm/cycle}$ | Figure 30(a), “FCGR”, second legend expression. |
| U168 | 58 / 47 | $3.20\times10^{-10}(\Delta K)^{3.72}\ \mathrm{mm/cycle}$ | Figure 30(b), “FCGR”, first legend expression. |
| U169 | 58 / 47 | $2.30\times10^{-11}(\Delta K)^{4.8}\ \mathrm{mm/cycle}$ | Figure 30(b), “FCGR”, second legend expression. |
| U170 | 59 / 48 | $R_m/t=5$ | Module Limitations, “The pipe size was fixed to”. |
| U171 | 59 / 48 | $\theta_1/\pi=0.125$ | Module Limitations, “the ID crack size was fixed to”. |
| U172 | 59 / 48 | $\alpha=1$ | Module Limitations, “Ramberg-Osgood parameters”. |
| U173 | 59 / 48 | $n=5$ | Module Limitations, “were used.” |
| U174 | 59 / 48 | $\sigma_b/\sigma_y=0.2,\ 0.4,\ 0.6,\ 0.8,\ 1.0$ | Module Limitations, “five different global bending stresses”. |
| U175 | 59 / 48 | $R_m/t=5$ | Figure 31, H1 plot. |
| U176 | 59 / 48 | $\theta_1/\pi=0.125$ | Figure 31, H1 plot. |
| U177 | 59 / 48 | $\sigma_b/\sigma_y=0.2,\ 0.4,\ 0.6,\ 0.8,\ 1.0$ | Figure 31, H1 plot. |
| U178 | 59 / 48 | $R_m/t=5$ | Figure 31, H2 plot. |
| U179 | 59 / 48 | $\theta_1/\pi=0.125$ | Figure 31, H2 plot. |
| U180 | 59 / 48 | $\sigma_b/\sigma_y=0.2,\ 0.4,\ 0.6,\ 0.8,\ 1.0$ | Figure 31, H2 plot. |
| U181 | 20 / 9 | $R_m/t=5$ | Figure 6 caption (plot label U006과 별도 인쇄). |
| U182 | 20 / 9 | $\theta_1/\pi=0.25$ | Figure 6 caption (plot label U007과 별도 인쇄). |

번호 없는 식의 원문 표기 보충: U108~111은 원문 Limits / Comments 셀에 `<π`, `<25t`만 있고 좌변은 같은 행의 CLID/CLOD이다. U130, U135, U138, U143은 원문이 영어 비교문이며, 그 영어를 Context에 함께 보존했다. U143~147의 `CLID_over_√(Rmt)`는 원문의 변수명 표기를 유지한 것으로, 곱셈식으로 읽지 않는다.

### 본문에서 말로 제시한 수학적 조건·정의 (누락 점검용)

아래는 등호가 인쇄되지 않은 원문 서술·수치 조건이다. 원문에 없던 등식을 만들지 않고 영어 그대로 옮겼으며, U 행 집계에는 포함하지 않는다.

| PDF / 인쇄 | Context / original wording |
|---|---|
| 18 / 7 | “the θ1/π and θ1/θ2 values ranged from 0.125 to 0.375 and 1 to 4, respectively.” |
| 18 / 7 | “where E is the elastic modulus.” |
| 19 / 8 | “the Rm/t and θ1/π values were fixed to 5 and 0.25, respectively.” |
| 19 / 8 | “Three values of crack angle ratio (θ1/θ2), 1, 2, and 4, were selected.” |
| 19 / 8 | “the elastic modulus (E) and Poisson’s ratio (ν) were 190 GPa and 0.3, respectively.” |
| 36 / 25 | “Five different values of ρ1/ρ2, 1, 1.5, 2, 3 and 4, were considered” |
| 36 / 25 | “four different values of Rm/t (2, 5, 10, and 20) and four different values of ρ1 (0.5, 1, 2 and 3) were selected.” |
| 36 / 25 | “The elastic modulus and the Poisson’s ratio were set to 190 GPa and 0.3, respectively.” |
| 43 / 32 | “the crack transition occurs once the surface crack depth reaches 95% of the wall thickness.” |
| 43 / 32 | “the ID crack length (c1*) remains identical to the final surface crack length (c1).” |
| 43 / 32 | “The OD crack length (c2*) is determined as either the pipe thickness (t) or ¼ of the final surface crack length (c1/4), whichever is less.” |
| 52 / 41 | “The two Rm/t values of the pipes tested are 5.8 and 3.52” |
| 52 / 41 | “The K and CTM modules in xLPR Ver. 2.0 can handle Rm/t values from 2 to 20.” |
| 52 / 41 | “at a frequency of 1~5 Hz.” |
| 54 / 43 | “the step increment used in the crack growth calculations was fixed to 100 cycles/increment.” |
| 59 / 48 | “four different values of θ1/θ2, 1, 2, 3 and 4, were considered.” |
| 59 / 48 | “yield strength (σy) of 380 MPa” |

## 3. Table 1–11: full cell transcription

병합된 Rm/t 셀은 마크다운에서 각 행에 반복했다. Table 4~11의 상단 병합 머리글 θ1/θ2는 각 숫자 열 머리글에 반복했다. 값의 끝자리 0도 보존했다.

### Table 1. Summary of pipe and crack geometries and loading conditions for circumferential crack

PDF 19 / 인쇄 8.

| Loading condition | $R_m/t$ | $\theta_1/\pi$ | $\theta_1/\theta_2$ |
|---|---|---|---|
| Axial tension,<br>Global bending | 2, 5, 10, 20 | 0.125, 0.25,<br>0.3, 0.4, 0.5 | 1, 1.5, 2, 3, 4 |

### Table 2. F, V1 and V2 values for idealized circumferential TWC under axial tension

PDF 25 / 인쇄 14.

| $R_m/t$ | $\theta_1/\pi$ | $F$ | $V_1$ | $V_2$ |
|---|---|---|---|---|
| 2 | 0.125 | 1.163 | 0.882 | 1.412 |
| 2 | 0.25 | 1.518 | 1.189 | 1.905 |
| 2 | 0.3 | 1.738 | 1.429 | 2.247 |
| 2 | 0.4 | 2.373 | 2.255 | 3.369 |
| 2 | 0.5 | 3.407 | 3.963 | 5.630 |
| 5 | 0.125 | 1.226 | 0.999 | 1.404 |
| 5 | 0.25 | 1.677 | 1.520 | 2.110 |
| 5 | 0.3 | 1.935 | 1.901 | 2.559 |
| 5 | 0.4 | 2.668 | 3.163 | 3.997 |
| 5 | 0.5 | 3.872 | 5.747 | 6.895 |
| 10 | 0.125 | 1.315 | 1.108 | 1.527 |
| 10 | 0.25 | 1.885 | 1.962 | 2.523 |
| 10 | 0.3 | 2.188 | 2.540 | 3.140 |
| 10 | 0.4 | 3.009 | 4.361 | 5.052 |
| 10 | 0.5 | 4.352 | 7.906 | 8.770 |
| 20 | 0.125 | 1.458 | 1.315 | 1.763 |
| 20 | 0.25 | 2.169 | 2.717 | 3.229 |
| 20 | 0.3 | 2.525 | 3.586 | 4.098 |
| 20 | 0.4 | 3.477 | 6.190 | 6.712 |
| 20 | 0.5 | 5.021 | 11.105 | 11.708 |

### Table 3. F, V1 and V2 values for idealized circumferential TWC under global bending

PDF 25 / 인쇄 14.

| $R_m/t$ | $\theta_1/\pi$ | $F$ | $V_1$ | $V_2$ |
|---|---|---|---|---|
| 2 | 0.125 | 1.080 | 0.719 | 1.477 |
| 2 | 0.25 | 1.288 | 1.012 | 1.826 |
| 2 | 0.3 | 1.405 | 1.207 | 2.071 |
| 2 | 0.4 | 1.721 | 1.807 | 2.838 |
| 2 | 0.5 | 2.201 | 2.912 | 4.265 |
| 5 | 0.125 | 1.178 | 0.947 | 1.418 |
| 5 | 0.25 | 1.471 | 1.406 | 2.005 |
| 5 | 0.3 | 1.620 | 1.715 | 2.356 |
| 5 | 0.4 | 2.009 | 2.659 | 3.409 |
| 5 | 0.5 | 2.607 | 4.404 | 5.349 |
| 10 | 0.125 | 1.270 | 1.080 | 1.521 |
| 10 | 0.25 | 1.669 | 1.838 | 2.385 |
| 10 | 0.3 | 1.852 | 2.315 | 2.885 |
| 10 | 0.4 | 2.299 | 3.705 | 4.329 |
| 10 | 0.5 | 2.976 | 6.146 | 6.872 |
| 20 | 0.125 | 1.411 | 1.291 | 1.744 |
| 20 | 0.25 | 1.934 | 2.553 | 3.048 |
| 20 | 0.3 | 2.155 | 3.281 | 3.768 |
| 20 | 0.4 | 2.684 | 5.297 | 5.776 |
| 20 | 0.5 | 3.472 | 8.722 | 9.241 |

### Table 4. G1 values for non-idealized circumferential TWC under axial tension

PDF 26 / 인쇄 15.

| $R_m/t$ | $\theta_1/\pi$ | $\theta_1/\theta_2=1$ | $\theta_1/\theta_2=1.5$ | $\theta_1/\theta_2=2$ | $\theta_1/\theta_2=3$ | $\theta_1/\theta_2=4$ |
|---|---|---|---|---|---|---|
| 2 | 0.125 | 1.000 | 0.556 | 0.471 | 0.399 | 0.367 |
| 2 | 0.25 | 1.000 | 0.364 | 0.242 | 0.165 | 0.139 |
| 2 | 0.3 | 1.000 | 0.311 | 0.187 | 0.118 | 0.096 |
| 2 | 0.4 | 1.000 | 0.225 | 0.112 | 0.062 | 0.049 |
| 2 | 0.5 | 1.000 | 0.159 | 0.066 | 0.034 | 0.026 |
| 5 | 0.125 | 1.000 | 0.276 | 0.174 | 0.119 | 0.101 |
| 5 | 0.25 | 1.000 | 0.119 | 0.063 | 0.042 | 0.037 |
| 5 | 0.3 | 1.000 | 0.093 | 0.050 | 0.033 | 0.029 |
| 5 | 0.4 | 1.000 | 0.061 | 0.032 | 0.021 | 0.018 |
| 5 | 0.5 | 1.000 | 0.041 | 0.020 | 0.012 | 0.011 |
| 10 | 0.125 | 1.000 | 0.091 | 0.071 | 0.062 | 0.058 |
| 10 | 0.25 | 1.000 | 0.072 | 0.048 | 0.034 | 0.029 |
| 10 | 0.3 | 1.000 | 0.064 | 0.039 | 0.026 | 0.023 |
| 10 | 0.4 | 1.000 | 0.046 | 0.024 | 0.015 | 0.013 |
| 10 | 0.5 | 1.000 | 0.030 | 0.013 | 0.008 | 0.007 |
| 20 | 0.125 | 1.000 | 0.068 | 0.063 | 0.048 | 0.043 |
| 20 | 0.25 | 1.000 | 0.059 | 0.033 | 0.021 | 0.018 |
| 20 | 0.3 | 1.000 | 0.047 | 0.024 | 0.015 | 0.013 |
| 20 | 0.4 | 1.000 | 0.028 | 0.012 | 0.007 | 0.006 |
| 20 | 0.5 | 1.000 | 0.014 | 0.005 | 0.003 | 0.003 |

### Table 5. G2 values for non-idealized circumferential TWC under axial tension

PDF 26 / 인쇄 15.

| $R_m/t$ | $\theta_1/\pi$ | $\theta_1/\theta_2=1$ | $\theta_1/\theta_2=1.5$ | $\theta_1/\theta_2=2$ | $\theta_1/\theta_2=3$ | $\theta_1/\theta_2=4$ |
|---|---|---|---|---|---|---|
| 2 | 0.125 | 1.000 | 1.196 | 1.235 | 1.188 | 1.116 |
| 2 | 0.25 | 1.000 | 1.513 | 1.627 | 1.564 | 1.461 |
| 2 | 0.3 | 1.000 | 1.604 | 1.719 | 1.620 | 1.494 |
| 2 | 0.4 | 1.000 | 1.717 | 1.780 | 1.578 | 1.402 |
| 2 | 0.5 | 1.000 | 1.745 | 1.696 | 1.381 | 1.175 |
| 5 | 0.125 | 1.000 | 1.637 | 1.801 | 1.761 | 1.662 |
| 5 | 0.25 | 1.000 | 2.343 | 2.592 | 2.424 | 2.188 |
| 5 | 0.3 | 1.000 | 2.526 | 2.747 | 2.455 | 2.157 |
| 5 | 0.4 | 1.000 | 2.733 | 2.737 | 2.201 | 1.847 |
| 5 | 0.5 | 1.000 | 2.735 | 2.413 | 1.751 | 1.397 |
| 10 | 0.125 | 1.000 | 2.297 | 2.517 | 2.401 | 2.214 |
| 10 | 0.25 | 1.000 | 3.206 | 3.366 | 2.849 | 2.425 |
| 10 | 0.3 | 1.000 | 3.418 | 3.388 | 2.685 | 2.201 |
| 10 | 0.4 | 1.000 | 3.538 | 3.030 | 2.100 | 1.629 |
| 10 | 0.5 | 1.000 | 3.305 | 2.378 | 1.429 | 1.042 |
| 20 | 0.125 | 1.000 | 3.138 | 3.282 | 2.886 | 2.520 |
| 20 | 0.25 | 1.000 | 3.884 | 3.417 | 2.408 | 1.898 |
| 20 | 0.3 | 1.000 | 3.879 | 3.068 | 2.031 | 1.523 |
| 20 | 0.4 | 1.000 | 3.481 | 2.241 | 1.263 | 0.947 |
| 20 | 0.5 | 1.000 | 2.779 | 1.468 | 0.772 | 0.521 |

### Table 6. G1 values for non-idealized circumferential TWC under global bending

PDF 27 / 인쇄 16.

| $R_m/t$ | $\theta_1/\pi$ | $\theta_1/\theta_2=1$ | $\theta_1/\theta_2=1.5$ | $\theta_1/\theta_2=2$ | $\theta_1/\theta_2=3$ | $\theta_1/\theta_2=4$ |
|---|---|---|---|---|---|---|
| 2 | 0.125 | 1.000 | 0.445 | 0.373 | 0.313 | 0.286 |
| 2 | 0.25 | 1.000 | 0.314 | 0.200 | 0.130 | 0.106 |
| 2 | 0.3 | 1.000 | 0.276 | 0.157 | 0.091 | 0.071 |
| 2 | 0.4 | 1.000 | 0.211 | 0.096 | 0.045 | 0.032 |
| 2 | 0.5 | 1.000 | 0.155 | 0.056 | 0.022 | 0.013 |
| 5 | 0.125 | 1.000 | 0.256 | 0.160 | 0.108 | 0.092 |
| 5 | 0.25 | 1.000 | 0.113 | 0.058 | 0.037 | 0.031 |
| 5 | 0.3 | 1.000 | 0.089 | 0.045 | 0.028 | 0.023 |
| 5 | 0.4 | 1.000 | 0.060 | 0.028 | 0.015 | 0.012 |
| 5 | 0.5 | 1.000 | 0.040 | 0.016 | 0.007 | 0.004 |
| 10 | 0.125 | 1.000 | 0.089 | 0.069 | 0.059 | 0.055 |
| 10 | 0.25 | 1.000 | 0.070 | 0.045 | 0.030 | 0.025 |
| 10 | 0.3 | 1.000 | 0.064 | 0.036 | 0.022 | 0.018 |
| 10 | 0.4 | 1.000 | 0.046 | 0.021 | 0.010 | 0.008 |
| 10 | 0.5 | 1.000 | 0.028 | 0.009 | 0.003 | 0.001 |
| 20 | 0.125 | 1.000 | 0.068 | 0.062 | 0.046 | 0.041 |
| 20 | 0.25 | 1.000 | 0.059 | 0.031 | 0.018 | 0.015 |
| 20 | 0.3 | 1.000 | 0.047 | 0.022 | 0.012 | 0.010 |
| 20 | 0.4 | 1.000 | 0.026 | 0.009 | 0.004 | 0.003 |
| 20 | 0.5 | 1.000 | 0.011 | 0.002 | 0.000 | 0.000 |

### Table 7. G2 values for non-idealized circumferential TWC under global bending

PDF 27 / 인쇄 16.

| $R_m/t$ | $\theta_1/\pi$ | $\theta_1/\theta_2=1$ | $\theta_1/\theta_2=1.5$ | $\theta_1/\theta_2=2$ | $\theta_1/\theta_2=3$ | $\theta_1/\theta_2=4$ |
|---|---|---|---|---|---|---|
| 2 | 0.125 | 1.000 | 1.384 | 1.446 | 1.408 | 1.333 |
| 2 | 0.25 | 1.000 | 1.732 | 1.917 | 1.891 | 1.787 |
| 2 | 0.3 | 1.000 | 1.844 | 2.055 | 2.002 | 1.874 |
| 2 | 0.4 | 1.000 | 2.009 | 2.213 | 2.063 | 1.873 |
| 2 | 0.5 | 1.000 | 2.082 | 2.198 | 1.921 | 1.685 |
| 5 | 0.125 | 1.000 | 1.738 | 1.929 | 1.901 | 1.802 |
| 5 | 0.25 | 1.000 | 2.540 | 2.880 | 2.750 | 2.504 |
| 5 | 0.3 | 1.000 | 2.778 | 3.124 | 2.871 | 2.551 |
| 5 | 0.4 | 1.000 | 3.105 | 3.285 | 2.760 | 2.358 |
| 5 | 0.5 | 1.000 | 3.201 | 3.055 | 2.363 | 1.935 |
| 10 | 0.125 | 1.000 | 2.376 | 2.621 | 2.518 | 2.328 |
| 10 | 0.25 | 1.000 | 3.416 | 3.671 | 3.166 | 2.715 |
| 10 | 0.3 | 1.000 | 3.703 | 3.793 | 3.082 | 2.552 |
| 10 | 0.4 | 1.000 | 3.980 | 3.596 | 2.598 | 2.049 |
| 10 | 0.5 | 1.000 | 3.855 | 2.996 | 1.916 | 1.431 |
| 20 | 0.125 | 1.000 | 3.209 | 3.379 | 2.987 | 2.615 |
| 20 | 0.25 | 1.000 | 4.106 | 3.696 | 2.650 | 2.103 |
| 20 | 0.3 | 1.000 | 4.175 | 3.408 | 2.312 | 1.749 |
| 20 | 0.4 | 1.000 | 3.900 | 2.647 | 1.554 | 1.185 |
| 20 | 0.5 | 1.000 | 3.240 | 1.848 | 1.035 | 0.715 |

### Table 8. H1 values for non-idealized circumferential TWC under axial tension

PDF 29 / 인쇄 18.

| $R_m/t$ | $\theta_1/\pi$ | $\theta_1/\theta_2=1$ | $\theta_1/\theta_2=1.5$ | $\theta_1/\theta_2=2$ | $\theta_1/\theta_2=3$ | $\theta_1/\theta_2=4$ |
|---|---|---|---|---|---|---|
| 2 | 0.125 | 1.000 | 0.876 | 0.822 | 0.773 | 0.749 |
| 2 | 0.25 | 1.000 | 0.721 | 0.611 | 0.525 | 0.490 |
| 2 | 0.3 | 1.000 | 0.660 | 0.531 | 0.435 | 0.397 |
| 2 | 0.4 | 1.000 | 0.546 | 0.391 | 0.285 | 0.248 |
| 2 | 0.5 | 1.000 | 0.442 | 0.277 | 0.176 | 0.144 |
| 5 | 0.125 | 1.000 | 0.819 | 0.737 | 0.663 | 0.629 |
| 5 | 0.25 | 1.000 | 0.653 | 0.510 | 0.400 | 0.357 |
| 5 | 0.3 | 1.000 | 0.600 | 0.440 | 0.323 | 0.280 |
| 5 | 0.4 | 1.000 | 0.505 | 0.328 | 0.210 | 0.170 |
| 5 | 0.5 | 1.000 | 0.411 | 0.236 | 0.132 | 0.099 |
| 10 | 0.125 | 1.000 | 0.760 | 0.651 | 0.558 | 0.518 |
| 10 | 0.25 | 1.000 | 0.595 | 0.427 | 0.304 | 0.258 |
| 10 | 0.3 | 1.000 | 0.551 | 0.372 | 0.245 | 0.199 |
| 10 | 0.4 | 1.000 | 0.473 | 0.286 | 0.163 | 0.122 |
| 10 | 0.5 | 1.000 | 0.388 | 0.212 | 0.107 | 0.074 |
| 20 | 0.125 | 1.000 | 0.686 | 0.548 | 0.439 | 0.395 |
| 20 | 0.25 | 1.000 | 0.547 | 0.361 | 0.227 | 0.179 |
| 20 | 0.3 | 1.000 | 0.513 | 0.322 | 0.188 | 0.141 |
| 20 | 0.4 | 1.000 | 0.446 | 0.258 | 0.134 | 0.092 |
| 20 | 0.5 | 1.000 | 0.365 | 0.194 | 0.092 | 0.059 |

### Table 9. H2 values for non-idealized circumferential TWC under axial tension

PDF 29 / 인쇄 18.

| $R_m/t$ | $\theta_1/\pi$ | $\theta_1/\theta_2=1$ | $\theta_1/\theta_2=1.5$ | $\theta_1/\theta_2=2$ | $\theta_1/\theta_2=3$ | $\theta_1/\theta_2=4$ |
|---|---|---|---|---|---|---|
| 2 | 0.125 | 1.000 | 0.723 | 0.579 | 0.427 | 0.344 |
| 2 | 0.25 | 1.000 | 0.665 | 0.509 | 0.364 | 0.293 |
| 2 | 0.3 | 1.000 | 0.633 | 0.471 | 0.327 | 0.261 |
| 2 | 0.4 | 1.000 | 0.557 | 0.385 | 0.249 | 0.193 |
| 2 | 0.5 | 1.000 | 0.466 | 0.292 | 0.173 | 0.129 |
| 5 | 0.125 | 1.000 | 0.702 | 0.550 | 0.399 | 0.323 |
| 5 | 0.25 | 1.000 | 0.644 | 0.471 | 0.316 | 0.246 |
| 5 | 0.3 | 1.000 | 0.613 | 0.435 | 0.283 | 0.216 |
| 5 | 0.4 | 1.000 | 0.537 | 0.354 | 0.213 | 0.157 |
| 5 | 0.5 | 1.000 | 0.441 | 0.264 | 0.146 | 0.103 |
| 10 | 0.125 | 1.000 | 0.681 | 0.516 | 0.358 | 0.283 |
| 10 | 0.25 | 1.000 | 0.617 | 0.435 | 0.276 | 0.207 |
| 10 | 0.3 | 1.000 | 0.585 | 0.399 | 0.245 | 0.180 |
| 10 | 0.4 | 1.000 | 0.507 | 0.321 | 0.184 | 0.130 |
| 10 | 0.5 | 1.000 | 0.413 | 0.238 | 0.126 | 0.086 |
| 20 | 0.125 | 1.000 | 0.656 | 0.480 | 0.317 | 0.242 |
| 20 | 0.25 | 1.000 | 0.584 | 0.395 | 0.238 | 0.172 |
| 20 | 0.3 | 1.000 | 0.551 | 0.361 | 0.211 | 0.149 |
| 20 | 0.4 | 1.000 | 0.473 | 0.289 | 0.158 | 0.108 |
| 20 | 0.5 | 1.000 | 0.381 | 0.212 | 0.108 | 0.071 |

### Table 10. H1 values for non-idealized circumferential TWC under global bending

PDF 30 / 인쇄 19.

| $R_m/t$ | $\theta_1/\pi$ | $\theta_1/\theta_2=1$ | $\theta_1/\theta_2=1.5$ | $\theta_1/\theta_2=2$ | $\theta_1/\theta_2=3$ | $\theta_1/\theta_2=4$ |
|---|---|---|---|---|---|---|
| 2 | 0.125 | 1.000 | 0.860 | 0.800 | 0.746 | 0.721 |
| 2 | 0.25 | 1.000 | 0.709 | 0.593 | 0.501 | 0.463 |
| 2 | 0.3 | 1.000 | 0.658 | 0.523 | 0.420 | 0.380 |
| 2 | 0.4 | 1.000 | 0.566 | 0.405 | 0.291 | 0.250 |
| 2 | 0.5 | 1.000 | 0.480 | 0.307 | 0.195 | 0.158 |
| 5 | 0.125 | 1.000 | 0.815 | 0.730 | 0.654 | 0.620 |
| 5 | 0.25 | 1.000 | 0.661 | 0.517 | 0.404 | 0.360 |
| 5 | 0.3 | 1.000 | 0.615 | 0.455 | 0.334 | 0.288 |
| 5 | 0.4 | 1.000 | 0.535 | 0.355 | 0.230 | 0.186 |
| 5 | 0.5 | 1.000 | 0.452 | 0.270 | 0.155 | 0.117 |
| 10 | 0.125 | 1.000 | 0.760 | 0.650 | 0.557 | 0.517 |
| 10 | 0.25 | 1.000 | 0.607 | 0.439 | 0.313 | 0.266 |
| 10 | 0.3 | 1.000 | 0.569 | 0.389 | 0.258 | 0.210 |
| 10 | 0.4 | 1.000 | 0.503 | 0.313 | 0.182 | 0.137 |
| 10 | 0.5 | 1.000 | 0.428 | 0.244 | 0.128 | 0.089 |
| 20 | 0.125 | 1.000 | 0.688 | 0.550 | 0.440 | 0.396 |
| 20 | 0.25 | 1.000 | 0.560 | 0.373 | 0.236 | 0.187 |
| 20 | 0.3 | 1.000 | 0.532 | 0.339 | 0.199 | 0.150 |
| 20 | 0.4 | 1.000 | 0.476 | 0.283 | 0.149 | 0.103 |
| 20 | 0.5 | 1.000 | 0.405 | 0.225 | 0.110 | 0.071 |

### Table 11. H2 values for non-idealized circumferential TWC under global bending

PDF 30 / 인쇄 19.

| $R_m/t$ | $\theta_1/\pi$ | $\theta_1/\theta_2=1$ | $\theta_1/\theta_2=1.5$ | $\theta_1/\theta_2=2$ | $\theta_1/\theta_2=3$ | $\theta_1/\theta_2=4$ |
|---|---|---|---|---|---|---|
| 2 | 0.125 | 1.000 | 0.734 | 0.594 | 0.443 | 0.360 |
| 2 | 0.25 | 1.000 | 0.686 | 0.534 | 0.388 | 0.316 |
| 2 | 0.3 | 1.000 | 0.660 | 0.501 | 0.355 | 0.286 |
| 2 | 0.4 | 1.000 | 0.596 | 0.425 | 0.284 | 0.223 |
| 2 | 0.5 | 1.000 | 0.517 | 0.339 | 0.210 | 0.159 |
| 5 | 0.125 | 1.000 | 0.709 | 0.558 | 0.408 | 0.331 |
| 5 | 0.25 | 1.000 | 0.660 | 0.489 | 0.333 | 0.260 |
| 5 | 0.3 | 1.000 | 0.635 | 0.459 | 0.302 | 0.233 |
| 5 | 0.4 | 1.000 | 0.571 | 0.387 | 0.240 | 0.178 |
| 5 | 0.5 | 1.000 | 0.486 | 0.304 | 0.175 | 0.126 |
| 10 | 0.125 | 1.000 | 0.686 | 0.522 | 0.363 | 0.288 |
| 10 | 0.25 | 1.000 | 0.632 | 0.450 | 0.289 | 0.218 |
| 10 | 0.3 | 1.000 | 0.605 | 0.419 | 0.261 | 0.193 |
| 10 | 0.4 | 1.000 | 0.539 | 0.351 | 0.205 | 0.147 |
| 10 | 0.5 | 1.000 | 0.456 | 0.275 | 0.151 | 0.104 |
| 20 | 0.125 | 1.000 | 0.661 | 0.485 | 0.321 | 0.246 |
| 20 | 0.25 | 1.000 | 0.598 | 0.409 | 0.249 | 0.181 |
| 20 | 0.3 | 1.000 | 0.570 | 0.379 | 0.224 | 0.160 |
| 20 | 0.4 | 1.000 | 0.504 | 0.316 | 0.176 | 0.122 |
| 20 | 0.5 | 1.000 | 0.423 | 0.246 | 0.129 | 0.087 |

## 4. 전 쪽 확인 및 집계

- PDF 1~11: 표지·면책·서명·개정·요약·목차·기호·약어. 본문의 번호식은 없음.
- PDF 12~17: Introduction, Model Description, Figure 1~4. Eq. 1 및 Figure 2의 이상화 균열 등식 확인.
- PDF 18~31: Circumferential Crack. Eq. 2~9, Table 1~11, Figure 5~10의 조건 확인.
- PDF 32~42: Axial Crack. Eq. 10~15, Figure 11~18 및 본문 정의식 확인. Table 12~16은 수치표이며 이번 전 칸 전사 대상은 아님.
- PDF 43~50: Crack Transition Model 및 Module Development. 초기 균열 정의식, Table 17의 RTC-16*/17*, Figure 19~22, Table 18~21의 조건식 확인.
- PDF 51~58: Verification and Validation. Eq. 16~18, 본문 조건, Figure 24 및 28~30의 FCGR식 확인.
- PDF 59~65: Module Limitations, Table 23, Recommendations, Lessons Learned, Summary, References. 한계 절과 Figure 31의 수치 조건 확인. Table 23에는 별도의 대수식 없음.

Table 2~11은 각각 20개 데이터 행으로, F/V 표 2개에는 각각 60개 결과값, G/H 표 8개에는 각각 100개 결과값을 옮겼다. 따라서 Table 2~11의 결과값은 총 920개이며 Rm/t와 θ1/π의 행 좌표도 모든 행에 보존했다. Table 1은 원문의 네 데이터 칸을 모두 옮겼다.

번호식 18개, 번호 없는 식 182개, 표 11개 전사

