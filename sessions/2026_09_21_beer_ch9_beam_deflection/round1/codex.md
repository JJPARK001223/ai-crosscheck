# Ch.9 보의 처짐: 짝수 62문제 blind 독립 풀이

## 범위, 출처, 부호와 단위

- 대상: 9.2부터 9.124까지 모든 짝수 문제 62개. 사용자 지정 `PROBLEM.md`와 원본 문제 스캔만 읽었다. 다른 사람의 풀이·정답·검토 파일은 읽지 않았다.
- 일차 출처: 사용자 제공 `J:/Desktop/문제풀이/0921/0921_문제.pdf`, 18페이지, 「보의 처짐」 연습문제. 각 항목에 PDF 페이지와 그림 번호를 적었다. 스캔에는 표지·판권지가 없어 **정확한 저자 명단·판·발행연도는 확인할 수 없다**. Beer/Pytel 계열이라는 과제 설명 이상의 서지정보를 추정하지 않았다.
- 기존에 원본에서 렌더링된 18개 페이지 이미지를 모두 직접 판독하고 필요한 부분을 확대했다. 웹 검색 및 표준형강 제원의 외부 조회는 하지 않았다.
- 이 문서의 공식은 아래 지배방정식에서 직접 적분하거나 그 적분을 하중별로 더해서 유도했다. 출처를 확인하지 않은 처짐공식표·해답집을 사용하지 않았다.
- 작은 변형, 선형탄성 Euler–Bernoulli 보를 가정한다. 직선 보에서는 축변형과 전단변형을 제외한다. 9.90은 케이블 축변형, 9.94는 봉의 비틀림을 별도로 포함한다.
- 기본 좌표는 왼쪽 끝에서 오른쪽으로 $x$, 위쪽 처짐 $y>0$, $\theta=y'$이다. 따라서 $\theta>0$는 반시계방향 기울기다. 양의 내부 굽힘모멘트는 sagging이고 $EIy''=M$이다. **외부 반력 모멘트**는 $C_A,C_B$ 등으로 쓰며 반시계방향을 양으로 한다. 내부 단면모멘트와 외부 지점모멘트의 부호를 구별한다.
- **수치식의 단위 약속:** 길이는 m, 힘은 kN, 모멘트는 kN·m. $K=EI$를 kN·m²로 넣으면 수치식의 $y$는 m, $\theta$는 rad이다. 예를 들어 $y=-200/K\;\mathrm m$는 $EIy=-200\;\mathrm{kN\,m^3}$라는 뜻이다. $E=200\;\mathrm{GPa}=2.00\times10^8\;\mathrm{kN/m^2}$. 기호식에서는 일관된 어떤 단위계도 가능하다.
- 수치가 주어지지 않은 이론 문제는 $P,w,L,E,I$에 의한 닫힌 식이 최종 답이다. W/S형강의 $I$가 없는 문제는 **부록 참조 필요**로 표시한다. 형강 명칭의 공칭 높이를 실제 높이나 $I$로 대체하지 않는다.

### 공통 유도식

직접적분법 및 특이함수법의 출발점은

$$
EIy''=M(x),\quad EI\theta=\int M(x)dx+C_1,\quad EIy=\iint M(x)dx^2+C_1x+C_2.
$$

$\langle x-a\rangle^n=0\;(x<a),\;(x-a)^n\;(x\ge a)$로 정의한다. 집중력·집중모멘트 위치에서도 보가 연속이면 $y,\theta$가 연속이다. 내부힌지에서는 $y$가 연속이고 $M=0$이나 두 보의 기울기는 같을 필요가 없다.

모멘트-면적법은 같은 곡률식을 적분한

$$
\theta_b-\theta_a=\int_a^b\frac{M}{EI}dx,\qquad
y_b-y_a-\theta_a(b-a)=\int_a^b(b-x)\frac{M}{EI}dx
$$

를 사용한다. 오른쪽 끝 $x=L$이 고정된 외팔보는 특히

$$
\theta_A=-\int_0^L\frac{M(x)}{EI(x)}dx,\qquad
y_A=\int_0^L\frac{xM(x)}{EI(x)}dx.
$$

이하 모든 반력에서 수평 외력이 없으면 수평반력은 0이다.

## 9.2–9.24

### 9.2

**원문:** PDF 1, 그림 P9.2. 오른쪽 B 고정, 왼쪽 A에 시계방향 $M_0$.

**방법·경계조건:** 직접적분. $x=0$은 A, $y(L)=\theta(L)=0$. 내부모멘트는 $M=M_0$.

$$
EI\theta=M_0(x-L),\qquad EIy=\frac{M_0}{2}(x-L)^2.
$$

**답:** 탄성곡선은 위 식. 자유단은

$$
\boxed{y_A=\frac{M_0L^2}{2EI}\;(\uparrow),\qquad
\theta_A=-\frac{M_0L}{EI}\;(\text{시계})}.
$$

반력 $R_B=0,\ C_B=M_0$.

### 9.4

**원문:** PDF 1, 그림 P9.4. A 고정, B 자유, 아래쪽 $w(x)=w_0x/L$.

**방법·경계조건:** 직접적분, $y(0)=\theta(0)=0$, 자유단 $M(L)=V(L)=0$.

$$
M=-\frac{w_0L^2}{3}+\frac{w_0Lx}{2}-\frac{w_0x^3}{6L},
$$
$$
EIy=-\frac{w_0L^2x^2}{6}+\frac{w_0Lx^3}{12}-\frac{w_0x^5}{120L}.
$$

**답:**

$$
\boxed{y_B=-\frac{11w_0L^4}{120EI},\qquad
\theta_B=-\frac{w_0L^3}{8EI}}.
$$

$R_A=w_0L/2,\ C_A=w_0L^2/3$.

### 9.6

**원문:** PDF 1, 그림 P9.6. $AB=2a,\ BC=a$. AB에 위쪽 균일하중 $w$, C에 아래쪽 $P=2wa/3$.

**방법·경계조건:** 직접적분. $y_A=\theta_A=0$. 전체 평형에서 $R_A=-4wa/3,\ C_A=0$.

AB 구간 $0\le x\le2a$에서

$$
M=-\frac{4wa}{3}x+\frac{wx^2}{2},\quad
EIy=-\frac{2wa}{9}x^3+\frac{w}{24}x^4.
$$

**답:**

$$
\boxed{y_B=-\frac{10wa^4}{9EI},\qquad
\theta_B=-\frac{4wa^3}{3EI}}.
$$

분포하중이 위쪽이어도 C의 끝하중까지 함께 고려하면 B는 아래로 처진다.

### 9.8

**원문:** PDF 2, 그림 P9.8. A와 B 지지, $AB=L,\ BC=L/2$. A에서 0, B에서 $w_0$, C에서 0인 아래쪽 분포하중.

**방법·경계조건:** 직접적분, $y(0)=y(L)=0$. 전체 하중과 모멘트 평형으로 $R_A=w_0L/8,\ R_B=5w_0L/8$.

AB에서

$$
M=\frac{w_0Lx}{8}-\frac{w_0x^3}{6L},\quad
EIy=\frac{w_0Lx^3}{48}-\frac{w_0x^5}{120L}-\frac{w_0L^3x}{80}.
$$

**답:** AB 중앙점과 B의 기울기는

$$
\boxed{y(L/2)=-\frac{w_0L^4}{256EI},\qquad
\theta_B=\frac{w_0L^3}{120EI}}.
$$

여기서 중앙점은 문항이 지정한 AB 구간의 중앙이다.

### 9.10

**원문:** PDF 2, 그림 P9.10. 단순지지 S200×27.4, $L=2.7$ m, $w_0=60$ kN/m, $E=200$ GPa. 대칭 삼각형하중, 중앙 C에서 $w_0$.

**방법·경계조건:** 직접적분, $y_A=y_B=0,\ \theta_C=0$. $R_A=R_B=w_0L/4$. 왼쪽 절반에서

$$
M=\frac{w_0Lx}{4}-\frac{w_0x^3}{3L},\quad
EIy=\frac{w_0Lx^3}{24}-\frac{w_0x^5}{60L}-\frac{5w_0L^3x}{192}.
$$

**답:**

$$
\boxed{\theta_A=-\frac{5w_0L^3}{192EI}
=-\frac{30.7546875}{K}\;\mathrm{rad}},
$$
$$
\boxed{y_C=-\frac{w_0L^4}{120EI}
=-\frac{26.57205}{K}\;\mathrm m}.
$$

$R_A=R_B=40.5$ kN. **부록 참조 필요:** S200×27.4의 강축 $I$.

### 9.12

**원문:** PDF 2, 그림 P9.12. 단순지지, 아래쪽 $w=w_0x/L$. 수치 조건 W460×74, $w_0=60$ kN/m, $L=6$ m, $E=200$ GPa.

**방법·경계조건:** 직접적분, $y(0)=y(L)=0$. $R_A=w_0L/6,\ R_B=w_0L/3$.

$$
EIy=w_0\left(\frac{Lx^3}{36}-\frac{x^5}{120L}-\frac{7L^3x}{360}\right).
$$

$u=x/L$로 놓고 $\theta=0$을 풀면 $15u^4-30u^2+7=0$.

$$
\boxed{\frac{x_{\max}}L=\sqrt{1-\sqrt{\frac8{15}}}=0.5193296224},
$$
$$
\boxed{y_{\min}=-0.006522184232\frac{w_0L^4}{EI}}.
$$

따라서 **최대 아래쪽 처짐 위치** $x=3.115977734$ m (A 기준),

$$
\boxed{y_{\min}=-\frac{507.1650459}{K}\;\mathrm m}.
$$

**부록 참조 필요:** W460×74의 강축 $I$. 위치는 $I$ 없이 확정된다.

### 9.14

**원문:** PDF 3, 그림 P9.14. $L=6$ m, $a=2$ m, AC에 $w=50$ kN/m, W310×38.7, $E=200$ GPa.

**방법·경계조건:** 구간 직접적분, $y_A=y_B=0$, C에서 $y,\theta$ 연속. $R_A=83.333333$ kN, $R_B=16.666667$ kN.

한 식으로 쓰면

$$
EIy=\frac{83.333333}{6}x^3-\frac{50}{24}x^4
+\frac{50}{24}\langle x-2\rangle^4-\frac{1250}{9}x.
$$

**답:**

$$
\boxed{\theta_A=-\frac{138.8888889}{K}\;\mathrm{rad},\qquad
y_C=-\frac{200}{K}\;\mathrm m}.
$$

**부록 참조 필요:** W310×38.7의 강축 $I$.

### 9.16

**원문:** PDF 3, 그림 P9.16. 단순지지 AE, B와 D에 각각 $P=17.5$ kN. $a=0.8$ m, $L=2.5$ m, S200×27.4, $E=200$ GPa.

> 판독 주: 스캔의 $L$ 숫자 부분이 옅다. 확대 판독값 $L=2.5$ m를 사용했으며, 아래 일반식은 $L$이 달라도 그대로 적용된다.

**방법·경계조건:** 직접적분, $y(0)=y(L)=0$, 대칭조건 $\theta(L/2)=0$, B,D에서 $y,\theta$ 연속. 반력은 각 $P$.

BD 구간 $a\le x\le L-a$에서 $M=Pa$이므로

$$
\boxed{EIy=\frac{Pa}{2}\left(x-\frac L2\right)^2
-\frac{Pa(3L^2-4a^2)}{24}}.
$$

**답:**

$$
\boxed{y_C=-\frac{Pa(3L^2-4a^2)}{24EI}
=-\frac{9.444166667}{K}\;\mathrm m},\qquad \theta_C=0.
$$

**부록 참조 필요:** S200×27.4의 강축 $I$.

### 9.18

**원문:** PDF 4, 그림 P9.18. 단순지지, $w=4w_0[x/L-(x/L)^2]$.

**방법·경계조건:** 직접적분, $y_A=y_B=0$, 대칭 $\theta_C=0$. $R_A=R_B=w_0L/3$.

$$
M=w_0\left(\frac{Lx}{3}-\frac{2x^3}{3L}+\frac{x^4}{3L^2}\right),
$$
$$
\boxed{EIy=w_0\left(\frac{Lx^3}{18}-\frac{x^5}{30L}
+\frac{x^6}{90L^2}-\frac{L^3x}{30}\right)}.
$$

**답:**

$$
\boxed{\theta_A=-\frac{w_0L^3}{30EI},\qquad
y_C=-\frac{61w_0L^4}{5760EI}}.
$$

### 9.20

**원문:** PDF 4, 그림 P9.20. A 고정, B 롤러, 전 구간 균일하중 $w$.

**방법·경계조건:** 부정정보 직접적분. $y_A=\theta_A=y_B=0$, $M(L)=0$. B 반력을 미지수로 두면

$$
M=R_B(L-x)-\frac w2(L-x)^2.
$$

적분하여 $y_B=0$을 적용하면

$$
0=\frac{R_BL^3}{3EI}-\frac{wL^4}{8EI}.
$$

**답:**

$$
\boxed{R_B=\frac{3wL}{8}\;(\uparrow)},\quad
R_A=\frac{5wL}{8},\quad C_A=\frac{wL^2}{8}.
$$

### 9.22

**원문:** PDF 4, 그림 P9.22. A 고정, B 롤러, $w=w_0x/L$.

**방법·경계조건:** 부정정보 직접적분, $y_A=\theta_A=y_B=0$, $M_B=0$. 9.4의 자유단 처짐에 B의 위쪽 반력 항을 더해도 같은 적분식이 된다.

$$
0=-\frac{11w_0L^4}{120EI}+\frac{R_BL^3}{3EI}.
$$

**답:**

$$
\boxed{R_B=\frac{11w_0L}{40}\;(\uparrow)},\quad
R_A=\frac{9w_0L}{40},\quad C_A=\frac{7w_0L^2}{120}.
$$

### 9.24

**원문:** PDF 4, 그림 P9.24. A 롤러, B 고정, $w=w_0(x/L)^2$, $w_0=65$ kN/m, $L=4$ m.

**방법·경계조건:** 직접적분, $y(0)=y(L)=\theta(L)=0$.

$$
M=R_Ax-\frac{w_0x^4}{12L^2},\quad
EIy=\frac{R_Ax^3}{6}-\frac{w_0x^6}{360L^2}+C_1x.
$$

기울기 조건으로 $C_1=-R_AL^2/2+w_0L^3/60$, 처짐 조건으로 $R_A=w_0L/24$.

**답:**

$$
\boxed{R_A=10.833333\;\mathrm{kN}\;(\uparrow)}.
$$

추가 반력 $R_B=75.833333$ kN 위쪽, $C_B=-43.333333$ kN·m (시계방향).

## 9.26–9.48

### 9.26

**원문:** PDF 4, 그림 P9.26. A 고정, B 롤러, 중앙 C에 아래쪽 $P$.

**방법·경계조건:** 직접적분, $y_A=\theta_A=y_B=0$, $M_B=0$.

$$
EIy=-\frac{3PLx^2}{32}+\frac{11Px^3}{96}
-\frac P6\langle x-L/2\rangle^3.
$$

**답:**

$$
\boxed{R_B=\frac{5P}{16}},\quad R_A=\frac{11P}{16},\quad C_A=\frac{3PL}{16}.
$$

굽힘모멘트 선도는 아래 두 직선이다.

$$
\boxed{M(x)=-\frac{3PL}{16}+\frac{11P}{16}x-P\langle x-L/2\rangle}.
$$

```text
 M/(PL)
  5/32                    C
                         / \
  0 -----------o--------/-----\---- B
              x=3L/11                x=L
 -3/16  A
        x=0
```

정확한 꼭짓점은 ((0,-3PL/16),(L/2,5PL/32),(L,0))이고 첫 직선의 영점은 $3L/11$이다.

### 9.28

**원문:** PDF 5, 그림 P9.28. A 롤러, B 고정. AC=$L/2$에만 A에서 0, C에서 $w_0$인 삼각형하중.

**방법·경계조건:** 구간 직접적분, $y_A=y_B=\theta_B=0$, C에서 $y,\theta$ 연속.

$$
EIy=\frac{R_Ax^3}{6}-\frac{w_0x^5}{60L}
+\frac{w_0}{24}\langle x-L/2\rangle^4
+\frac{w_0}{60L}\langle x-L/2\rangle^5-\frac{w_0L^3x}{120}.
$$

**답:**

$$
\boxed{R_A=\frac{21w_0L}{160}},\quad
R_B=\frac{19w_0L}{160},\quad C_B=-\frac{17w_0L^2}{480}.
$$

굽힘모멘트 선도:

$$
M(x)=\begin{cases}
\dfrac{21w_0Lx}{160}-\dfrac{w_0x^3}{3L},&0\le x\le L/2,\\
\dfrac{w_0L^2}{12}-\dfrac{19w_0Lx}{160},&L/2\le x\le L.
\end{cases}
$$

```text
 M
        곡선의 최대점
       /------ C(+23w0L²/960)
 A(0) /        \
 0 -------------o---------------- x
                40L/57 \
                         B(-17w0L²/480)
```

AC는 3차곡선, CB는 직선. 최대점은 $x=L\sqrt{21/160}$, 내부 영점은 $x=40L/57$이다.

### 9.30

**원문:** PDF 5, 그림 P9.30. A 롤러, B 고정, 왼쪽 절반 AC에만 균일하중 $w$.

**방법·경계조건:** 직접적분, $y_A=y_B=\theta_B=0$, C에서 처짐과 기울기 연속.

$$
EIy=\frac{41wLx^3}{768}-\frac{wx^4}{24}
+\frac{w}{24}\langle x-L/2\rangle^4-\frac{11wL^3x}{768}.
$$

**답:**

$$
\boxed{R_A=\frac{41wL}{128},\qquad y_C=-\frac{19wL^4}{6144EI}}.
$$

$R_B=23wL/128,\ C_B=-7wL^2/128$.

### 9.32

**원문:** PDF 5, 그림 P9.32. A 롤러, B 고정. $AD=a=L/3$, D에 $P$.

**방법·경계조건:** 직접적분, $y_A=y_B=\theta_B=0$, D에서 $y,\theta$ 연속.

$$
EIy=\frac{7Px^3}{81}-\frac P6\langle x-L/3\rangle^3-\frac{PL^2x}{27}.
$$

**답:**

$$
\boxed{R_A=\frac{14P}{27},\qquad y_D=-\frac{20PL^3}{2187EI}}.
$$

$R_B=13P/27,\ C_B=-4PL/27$.

### 9.34

**원문:** PDF 5, 그림 P9.34. 양단고정, 전 구간 균일하중 $w$.

**방법·경계조건:** 직접적분, $y_A=\theta_A=y_B=\theta_B=0$.

$$
\boxed{y=-\frac{w}{24EI}x^2(L-x)^2}.
$$

**A의 반력:**

$$
\boxed{R_A=\frac{wL}{2},\qquad C_A=\frac{wL^2}{12}}.
$$

$R_B=wL/2,\ C_B=-wL^2/12$. 내부모멘트 선도는

$$
\boxed{M=-\frac{wL^2}{12}+\frac{wLx}{2}-\frac{wx^2}{2}}.
$$

```text
 M                         C(+wL²/24)
                           .---.
 0 --------------------o--'-----'--o---------------- x
 A(-wL²/12) ________.-'             '-.________ B(-wL²/12)
```

포물선의 영점은 $x/L=(1\pm1/\sqrt3)/2$, 중앙 최대모멘트는 $wL^2/24$이다.

### 9.36

**원문:** PDF 6, 그림 P9.36. 단순지지, $AC=a,\ CB=b,\ L=a+b$, C에 $P$.

**방법·경계조건:** 특이함수법, $y_A=y_B=0$. $R_A=Pb/L,\ R_B=Pa/L$.

$$
\boxed{EIy=\frac{Pb}{6L}x^3-\frac P6\langle x-a\rangle^3
-\frac{Pab(a+2b)}{6L}x}.
$$

**답:**

$$
\boxed{\theta_A=-\frac{Pab(a+2b)}{6LEI},\qquad
y_C=-\frac{Pa^2b^2}{3LEI}}.
$$

### 9.38

**원문:** PDF 6, 그림 P9.38. 단순지지 AE, 길이 $4a$, B,C,D에 각각 $P$.

**방법·경계조건:** 특이함수법, $y(0)=y(4a)=0$. 반력은 각각 $3P/2$.

$$
EIy=\frac{Px^3}{4}-\frac P6\sum_{j=1}^{3}\langle x-ja\rangle^3-\frac{5Pa^2x}{2}.
$$

**답:**

$$
\boxed{y_B=y_D=-\frac{9Pa^3}{4EI},\qquad y_C=-\frac{19Pa^3}{6EI}}.
$$

대칭성 검산: $\theta_C=0$.

### 9.40

**원문:** PDF 6, 그림 P9.40. $AB=BC=CD=a$, B,D 지지, A와 C에 각각 $P$.

**방법·경계조건:** 특이함수법, $y(a)=y(3a)=0$. 평형으로 $R_B=2P,\ R_D=0$.

$$
EIy=-\frac{Px^3}{6}+\frac P3\langle x-a\rangle^3
-\frac P6\langle x-2a\rangle^3+\frac{11Pa^2x}{12}-\frac{3Pa^3}{4}.
$$

**답:**

$$
\boxed{y_A=-\frac{3Pa^3}{4EI},\quad y_C=\frac{Pa^3}{12EI}\;(\uparrow),
\quad\theta_D=-\frac{Pa^2}{12EI}}.
$$

CD에서는 $M=0$이므로 탄성곡선은 기울기가 일정한 직선이다.

### 9.42

**원문:** PDF 7, 그림 P9.42. A,C 지지. $AB=BC=CD=L/2$, AB와 CD에 각각 균일하중 $w$.

**방법·경계조건:** 특이함수법, $y(0)=y(L)=0$, D 자유단 $M_D=V_D=0$. $R_A=wL/4,\ R_C=3wL/4$.

$$
\boxed{EIy=\frac{wLx^3}{24}-\frac{wx^4}{24}
+\frac w{24}\langle x-L/2\rangle^4
+\frac{wL}{8}\langle x-L\rangle^3
-\frac w{24}\langle x-L\rangle^4-\frac{wL^3x}{384}}.
$$

**답:**

$$
\boxed{y_B=\frac{wL^4}{768EI}\;(\uparrow),\qquad
y_D=-\frac{5wL^4}{256EI}}.
$$

### 9.44

**원문:** PDF 7, 그림 P9.44. 단순지지 AB, 중앙에서 0, 양 끝에서 $w_0$인 대칭 V자 분포하중.

**방법·경계조건:** 특이함수법, $y_A=y_B=0$, $\theta_C=0$. $R_A=R_B=w_0L/4$.

$$
\boxed{EIy=\frac{w_0Lx^3}{24}-\frac{w_0x^4}{24}
+\frac{w_0x^5}{60L}-\frac{w_0}{30L}\langle x-L/2\rangle^5
-\frac{w_0L^3x}{64}}.
$$

**답:**

$$
\boxed{y_C=-\frac{3w_0L^4}{640EI}}.
$$

### 9.46

**원문:** PDF 7, 그림 P9.46. $L=5.4$ m, $x=1.8$부터 B까지 $3$ kN/m, $x=3.6$에 $6.2$ kN. C는 $x=2.7$. W310×60, $E=200$ GPa.

**방법·경계조건:** 특이함수법, $y(0)=y(5.4)=0$. $R_A=17/3$ kN, $R_B=34/3$ kN.

$$
EIy=\frac{17x^3}{18}-\frac18\langle x-1.8\rangle^4
-\frac{31}{30}\langle x-3.6\rangle^3-22.536x.
$$

**답:**

$$
\boxed{\theta_A=-\frac{22.536}{K}\;\mathrm{rad},\qquad
y_C=-\frac{42.3397125}{K}\;\mathrm m}.
$$

**부록 참조 필요:** W310×60의 강축 $I$.

### 9.48

**원문:** PDF 8, 그림 P9.48. 단순지지 AD, 길이 2 m. $x=0.5$ m인 B에 4 kN, C=$x=1$ m부터 D까지 5 kN/m. 직사각형 폭 50 mm, 높이 150 mm, $E=12$ GPa.

**방법·경계조건:** 특이함수법, $y(0)=y(2)=0$. $R_A=4.25$ kN, $R_D=4.75$ kN.

$$
I=\frac{0.05(0.15)^3}{12}=1.40625\times10^{-5}\;\mathrm{m^4},\quad
EI=168.75\;\mathrm{kN\,m^2},
$$
$$
EIy=\frac{17x^3}{24}-\frac23\langle x-0.5\rangle^3
-\frac5{24}\langle x-1\rangle^4-\frac{77x}{48}.
$$

**답:**

$$
\boxed{\theta_A=-0.00950617\;\mathrm{rad},\qquad y_C=-5.80247\;\mathrm{mm}}.
$$

## 9.50–9.72

### 9.50

**원문:** PDF 8, 그림 P9.50. A 고정, B 롤러, 중앙 C에 $P$.

**방법·경계조건:** 특이함수법, $y_A=\theta_A=y_B=0$.

$$
EIy=-\frac{3PLx^2}{32}+\frac{11Px^3}{96}
-\frac P6\langle x-L/2\rangle^3.
$$

**답:**

$$
\boxed{R_B=\frac{5P}{16}\;(\uparrow),\qquad
y_C=-\frac{7PL^3}{768EI}}.
$$

$R_A=11P/16,\ C_A=3PL/16$. 9.26과 동일한 지지·하중조건으로 반력이 일치한다.

### 9.52

**원문:** PDF 8, 그림 P9.52. A 고정, D 롤러, 총길이 $L$. $x=L/3,2L/3$인 B,C에 각각 $P$.

**방법·경계조건:** 특이함수법, $y_A=\theta_A=y_D=0$.

$$
EIy=-\frac{PLx^2}{6}+\frac{2Px^3}{9}
-\frac P6\left[\langle x-L/3\rangle^3+\langle x-2L/3\rangle^3\right].
$$

**답:**

$$
\boxed{R_D=\frac{2P}{3},\qquad y_B=-\frac{5PL^3}{486EI}}.
$$

$R_A=4P/3,\ C_A=PL/3$.

### 9.54

**원문:** PDF 8, 그림 P9.54. A 롤러, B 고정, $L=3.6$ m, C=$1.8$ m. AC에서 하중이 0부터 36 kN/m까지 선형 증가, CB에서 36 kN/m 일정. W250×32.7, $E=200$ GPa.

**방법·경계조건:** 특이함수법, $y(0)=y(3.6)=\theta(3.6)=0$.

$$
EIy=\frac{24.0975}{6}x^3-\frac{x^5}{6}
+\frac{\langle x-1.8\rangle^5}{6}-24.9318x.
$$

하중 합력은 97.2 kN, A에 대한 하중모멘트는 213.84 kN·m이다.

**답:**

$$
\boxed{R_A=24.0975\;\mathrm{kN}\;(\uparrow),\qquad
y_C=-\frac{24.60375}{K}\;\mathrm m}.
$$

$R_B=73.1025$ kN 위쪽, $C_B=-49.329$ kN·m. **부록 참조 필요:** W250×32.7의 강축 $I$.

### 9.56

**원문:** PDF 9, 그림 P9.56. A 고정, E 롤러, 길이 2 m. B,C,D는 $x=0.5,1,1.5$ m, 각각 $P=40$ kN. W200×46.1, $E=200$ GPa.

**방법·경계조건:** 특이함수법, $y_A=\theta_A=y_E=0$.

$$
EIy=-18.75x^2+13.125x^3
-\frac{20}{3}\sum_{a\in\{0.5,1,1.5\}}\langle x-a\rangle^3.
$$

**답:**

$$
\boxed{R_A=78.75\;\mathrm{kN}\;(\uparrow),\qquad
C_A=37.50\;\mathrm{kN\,m}\;(\text{반시계})},
$$
$$
\boxed{y_C=-\frac{6.458333333}{K}\;\mathrm m}.
$$

$R_E=41.25$ kN. **부록 참조 필요:** W200×46.1의 강축 $I$.

### 9.58

**원문:** PDF 9, 그림 P9.58. 양단고정, 오른쪽 절반 CB에만 $w$.

**방법·경계조건:** 특이함수법, $y_A=\theta_A=y_B=\theta_B=0$.

$$
EIy=-\frac{5wL^2x^2}{384}+\frac{wLx^3}{64}
-\frac w{24}\langle x-L/2\rangle^4.
$$

**답:**

$$
\boxed{R_A=\frac{3wL}{32},\quad C_A=\frac{5wL^2}{192},\quad
y_C=-\frac{wL^4}{768EI}}.
$$

$R_B=13wL/32,\ C_B=-11wL^2/192$. 고정단 외부모멘트 방향은 A 반시계, B 시계이다.

### 9.60

**원문:** PDF 9, 9.46의 보와 하중에서 최대처짐 및 위치.

**방법·경계조건:** 9.46의 특이함수 탄성곡선을 미분한다. $y_A=y_B=0$. 아래쪽 하중만 있는 단순보이므로 구간 내부의 양의 $M$에 따라 $\theta$가 증가하며, 내부 영점이 최대 아래쪽 처짐점이다.

영점은 $1.8<x<3.6$에 있으므로

$$
EI\theta=\frac{17x^2}{6}-\frac{(x-1.8)^3}{2}-22.536=0.
$$

**답:**

$$
\boxed{x_{\max}=2.856967428\;\mathrm m\quad(\mathrm A\text{에서})},
\qquad
\boxed{y_{\min}=-\frac{42.516827925}{K}\;\mathrm m}.
$$

$E=200$ GPa. **부록 참조 필요:** W310×60의 강축 $I$. 위치는 확정 수치이다.

### 9.62

**원문:** PDF 9, 9.48의 보와 하중에서 최대처짐 및 위치.

**방법·경계조건:** 9.48의 탄성곡선에 $y_A=y_D=0$을 유지하고 $\theta=0$을 푼다. 영점은 $0.5<x<1$이므로

$$
EI\theta=\frac{17x^2}{8}-2(x-0.5)^2-\frac{77}{48}=0,
\quad 6x^2+96x-101=0.
$$

**답:**

$$
\boxed{x_{\max}=0.990735973\;\mathrm m\quad(\mathrm A\text{에서})},
\qquad
\boxed{y_{\min}=-5.80304089\;\mathrm{mm}}.
$$

$EI=168.75$ kN·m²를 사용했다. 중앙 C의 처짐보다 최대처짐의 절댓값이 조금 더 크다.

### 9.64

**원문:** PDF 9, 그림 P9.64. $AB=4.8$ m. AC=$2.4$ m에 30 kN/m, D=$3.6$ m에 강체 DEF가 용접되며 F에서 아래로 50 kN. D에서 F까지 수평거리 1.2 m. W460×52, $E=200$ GPa.

**방법·경계조건:** 강체 하중 전달 후 특이함수법. $y_A=y_B=0$. D에 전달되는 하중은 **50 kN 아래쪽 및 60 kN·m 반시계 모멘트**이다. F의 힘을 D로 이동하면서 이 모멘트를 빠뜨리면 안 된다.

$$
R_A=79\;\mathrm{kN},\quad R_B=43\;\mathrm{kN},
$$
$$
EIy=\frac{79x^3}{6}-\frac{30x^4}{24}
+\frac{30}{24}\langle x-2.4\rangle^4
-\frac{50}{6}\langle x-3.6\rangle^3
-30\langle x-3.6\rangle^2-161.76x.
$$

**답:**

$$
\boxed{\theta_A=-\frac{161.76}{K}\;\mathrm{rad},\qquad
y_C=-\frac{247.68}{K}\;\mathrm m}.
$$

**부록 참조 필요:** W460×52의 강축 $I$.

### 9.66

**원문:** PDF 10, 그림 P9.66. A 고정, $AB=BC=L/2$, B,C에 각각 $P$.

**방법·경계조건:** 겹침원리. $y_A=\theta_A=0$, C 자유. 고정단에서 $a$에 작용하는 집중하중 하나를 적분하면 자유단에서

$$
\theta_C^{(a)}=-\frac{Pa^2}{2EI},\qquad
y_C^{(a)}=-\frac{Pa^2(3L-a)}{6EI}.
$$

$a=L/2,L$의 두 항을 더한다.

**답:**

$$
\boxed{\theta_C=-\frac{5PL^2}{8EI},\qquad
y_C=-\frac{7PL^3}{16EI}}.
$$

$R_A=2P,\ C_A=3PL/2$.

### 9.68

**원문:** PDF 10, 그림 P9.68. A 고정, 전체 AC=$L$에 아래쪽 균일하중 $w$, 중앙 B에 **위쪽** $P=wL$.

**방법·경계조건:** 겹침원리, $y_A=\theta_A=0$. B에서 균일하중의 효과는
$\theta_B^{(w)}=-7wL^3/(48EI)$, $y_B^{(w)}=-17wL^4/(384EI)$.
위쪽 집중하중의 효과는
$\theta_B^{(P)}=wL^3/(8EI)$, $y_B^{(P)}=wL^4/(24EI)$.

**답:**

$$
\boxed{\theta_B=-\frac{wL^3}{48EI},\qquad
y_B=-\frac{wL^4}{384EI}}.
$$

전체 힘과 모멘트가 상쇄되어 $R_A=C_A=0$이지만, 보 내부의 모멘트와 처짐은 0이 아니다.

### 9.70

**원문:** PDF 10, 그림 P9.70. 단순지지 AD, $AB=BC=CD=L/3$, B,C에 각각 아래쪽 $P$.

**방법·경계조건:** 두 단순보 집중하중 해의 겹침. $y_A=y_D=0$, 대칭축에서 $\theta(L/2)=0$. 각각의 반력 기여를 합하면 $R_A=R_D=P$.

$$
EIy=\frac{Px^3}{6}
-\frac P6\left[\langle x-L/3\rangle^3+\langle x-2L/3\rangle^3\right]
-\frac{PL^2x}{9}.
$$

**답:**

$$
\boxed{y_C=-\frac{5PL^3}{162EI},\qquad
\theta_A=-\frac{PL^2}{9EI}}.
$$

### 9.72

**원문:** PDF 10, 그림 P9.72. 단순지지 AB, 균일하중 $w$.A에 반시계, B에 시계 모멘트가 각각 $wL^2/12$.

**방법·경계조건:** 균일하중과 두 끝모멘트의 겹침. 지지조건은 $y_A=y_B=0$이며, 고정단을 가정하지 않는다.

$$
\theta_A=-\frac{wL^3}{24EI}+\frac{(wL^2/12)L}{2EI}=0,
$$
$$
y_C=-\frac{5wL^4}{384EI}+\frac{(wL^2/12)L^2}{8EI}.
$$

**답:**

$$
\boxed{\theta_A=0,\qquad y_C=-\frac{wL^4}{384EI}}.
$$

$R_A=R_B=wL/2$.주어진 외부모멘트 때문에 결과적으로 $\theta_B=0$도 성립한다.

## 9.74–9.94

### 9.74

**원문:** PDF 11, 그림 P9.73 및 P9.74. A 고정, $AB=a=0.75$ m, $AC=b=1.25$ m. B,C에 각각 $P=3$ kN. S100×11.5, $E=200$ GPa.

**방법·경계조건:** 겹침원리, $y_A=\theta_A=0$. B에서 각 집중하중의 적분 결과를 합하면

$$
\theta_B=-\frac{Pa^2}{2EI}-\frac{Pa(2b-a)}{2EI}=-\frac{Pab}{EI},
$$
$$
y_B=-\frac{Pa^3}{3EI}-\frac{Pa^2(3b-a)}{6EI}.
$$

**답:**

$$
\boxed{\theta_B=-\frac{2.8125}{K}\;\mathrm{rad},\qquad
y_B=-\frac{1.265625}{K}\;\mathrm m}.
$$

$R_A=6$ kN, $C_A=6$ kN·m. **부록 참조 필요:** S100×11.5의 강축 $I$.

### 9.76

**원문:** PDF 11, 그림 P9.75 및 P9.76. A 고정, $AB=a=0.75$ m, $AC=L=1$ m. AB에 $w=2.6$ kN/m, C에 $P=0.5$ kN. 원형 지름 44 mm, $E=200$ GPa.

**방법·경계조건:** 겹침원리, $y_A=\theta_A=0$. B에서

$$
\theta_B=-\frac{wa^3}{6EI}-\frac{Pa(2L-a)}{2EI},\qquad
y_B=-\frac{wa^4}{8EI}-\frac{Pa^2(3L-a)}{6EI}.
$$

$$
I=\frac{\pi(0.044)^4}{64}=1.839842322\times10^{-7}\;\mathrm{m^4},
\quad EI=36.79684643\;\mathrm{kN\,m^2}.
$$

**답:**

$$
\boxed{\theta_B=-0.01133759\;\mathrm{rad},\qquad
y_B=-5.66083242\;\mathrm{mm}}.
$$

$R_A=2.45$ kN, $C_A=1.23125$ kN·m.

### 9.78

**원문:** PDF 11, 그림 P9.78. 단순지지, $L=3.9$ m, $AC=a=1.3$ m, $CB=b=2.6$ m. 전체에 $w=8$ kN/m, C에 $P=35$ kN. W360×39, $E=200$ GPa.

**방법·경계조건:** 균일하중과 편심 집중하중의 겹침, $y_A=y_B=0$.

$$
\theta_A=-\frac{wL^3}{24EI}-\frac{Pab(a+2b)}{6LEI},
$$
$$
y_C=-\frac{wa(L^3-2La^2+a^3)}{24EI}-\frac{Pa^2b^2}{3LEI}.
$$

**답:**

$$
\boxed{\theta_A=-\frac{52.634111111}{K}\;\mathrm{rad},\qquad
y_C=-\frac{55.120288889}{K}\;\mathrm m}.
$$

$R_A=38.933333$ kN, $R_B=27.266667$ kN.
**부록 참조 필요:** W360×39의 강축 $I$.

### 9.80

**원문:** PDF 11, 그림 P9.80. A,C,B의 세 지점 지지, C는 중앙, B에 시계방향 $M_0$.

**방법·경계조건:** C 지점을 해제한 단순보에 겹침원리 적용. 실제 조건은 $y_A=y_C=y_B=0$.

단순보의 B 끝모멘트에 의한 중앙 처짐은 위쪽 $M_0L^2/(16EI)$이고, 위쪽을 양으로 정한 C 반력의 기여는 $R_CL^3/(48EI)$이다.

$$
0=\frac{M_0L^2}{16EI}+\frac{R_CL^3}{48EI}.
$$

**답:**

$$
\boxed{R_A=\frac{M_0}{2L}\;(\uparrow),\qquad
R_C=-\frac{3M_0}{L}\;(\downarrow),\qquad
R_B=\frac{5M_0}{2L}\;(\uparrow)}.
$$

C는 그림의 핀 지지로서 아래쪽 반력도 전달한다. 세 반력의 합은 0이고 B의 외부모멘트와 모멘트 평형을 이룬다.

### 9.82

**원문:** PDF 12, 그림 P9.82. A 롤러, B 고정, $AC=a$, $AB=L$.C에 반시계방향 $M_0$.

**방법·경계조건:** A 지점을 해제한 오른쪽 고정 외팔보에 반력 겹침. $y_A=y_B=\theta_B=0$.

$$
M=R_Ax-M_0\langle x-a\rangle^0.
$$

이를 두 번 적분하고 B의 고정조건을 적용한 A의 적합조건은

$$
-\frac{R_AL^3}{3}+\frac{M_0(L^2-a^2)}2=0.
$$

**답:**

$$
\boxed{R_A=\frac{3M_0(L^2-a^2)}{2L^3},\qquad R_B=-R_A},
$$
$$
\boxed{C_B=\frac{M_0}{2}\left(1-\frac{3a^2}{L^2}\right)}.
$$

모멘트 반력의 방향은 괄호의 부호에 따른다.

### 9.84

**원문:** PDF 12, 그림 P9.84. 양단고정, 중앙 C에 반시계방향 $M_0$.

**방법·경계조건:** 끝반력의 겹침과 적합조건, $y_A=\theta_A=y_B=\theta_B=0$.

$$
M=-C_A+R_Ax-M_0\langle x-L/2\rangle^0,
$$
$$
EIy=-\frac{C_Ax^2}{2}+\frac{R_Ax^3}{6}
-\frac{M_0}{2}\langle x-L/2\rangle^2.
$$

B의 $y,\theta=0$에서 $R_A=3M_0/(2L)$, $C_A=M_0/4$.

**B의 반력:**

$$
\boxed{R_B=-\frac{3M_0}{2L}\;(\downarrow),\qquad
C_B=\frac{M_0}{4}\;(\text{반시계})}.
$$

### 9.86

**원문:** PDF 12, 그림 P9.86. A 롤러, C 내부힌지, D 고정. $AB=0.30$ m, $BC=0.15$ m, $CD=0.30$ m. B에 $P=3.5$ kN. 두 보 모두 30×30 mm 정사각형, $E=200$ GPa.

**방법·경계조건:** 힌지 평형, 외팔보 처짐, 지점침하의 겹침. $y_A=0$, $y_D=\theta_D=0$, $M_{C^-}=M_{C^+}=0$, $y_{C^-}=y_{C^+}$.힌지 양쪽의 기울기를 같게 놓지 않는다.

$$
I=\frac{0.03^4}{12}=6.75\times10^{-8}\;\mathrm{m^4},\quad EI=13.5\;\mathrm{kN\,m^2}.
$$

왼쪽 AC의 평형에서 $R_A=1.1666667$ kN, C의 위쪽 힘 $Q=2.3333333$ kN. 따라서 CD에는 C에서 아래로 $Q$가 작용한다.

$$
y_C=-\frac{Q(0.3)^3}{3EI}=-1.5555556\;\mathrm{mm}.
$$

$\ell=0.45,\ a=0.30,\ b=0.15$로 놓으면

$$
\theta_A=-\frac{Pb(\ell^2-b^2)}{6\ell EI}+\frac{y_C}{\ell},
\qquad
y_B=-\frac{Pa^2b^2}{3\ell EI}+\frac a\ell y_C.
$$

**답:**

$$
\boxed{\theta_A=-0.006049383\;\mathrm{rad},\qquad
y_B=-1.42592593\;\mathrm{mm}}.
$$

D의 반력은 $R_D=2.3333333$ kN 위쪽, $C_D=-0.7000$ kN·m이다.

### 9.88

**원문:** PDF 13, 그림 P9.88. 위쪽 AC 길이 4.4 m에 $w=30$ kN/m. A 지지, C는 아래 보 DE 위의 롤러 접촉점. 아래 보는 E 고정, $EC=CD=2.2$ m. 두 보 W410×38.8, $E=200$ GPa. B는 위쪽 보 중앙.

**방법·경계조건:** 접촉력 평형과 처짐 겹침. $y_A=0,\ y_E=\theta_E=0,\ y_C^{AC}=y_C^{DE}$.접촉은 수직력만 전달한다.

AC의 평형으로 C 접촉력은 $Q=w(4.4)/2=66$ kN. 아래 보에는 아래로 작용한다.

$$
y_C=-\frac{66(2.2)^3}{3K}=-\frac{234.256}{K},
$$
$$
y_B=-\frac{5(30)(4.4)^4}{384K}+\frac{y_C}{2},
\qquad
y_D=-\frac{66(2.2)^2[3(4.4)-2.2]}{6K}.
$$

**답:**

$$
\boxed{y_B=-\frac{263.538}{K}\;\mathrm m,\qquad
y_D=-\frac{585.640}{K}\;\mathrm m}.
$$

**부록 참조 필요:** W410×38.8의 강축 $I$.상부 보의 지지점 C가 내려가는 효과를 포함했다.

### 9.90

**원문:** PDF 13, 그림 P9.90. C 고정 외팔보 BC 길이 $L=6$ m, $w=20$ kN/m. 자유단 B에 수직 강철케이블 AB, 길이 $\ell_c=3$ m, 면적 $A_c=255$ mm². 처음부터 팽팽함. 보 W410×46.1, 모두 $E=200$ GPa.

**방법·경계조건:** 외팔보 처짐 겹침과 케이블 축변형 적합조건. $y_C=\theta_C=0$, A 변위 0, B의 아래쪽 변위가 케이블 신장과 같다.

$$
\frac{wL^4}{8EI}-\frac{TL^3}{3EI}
=\frac{T\ell_c}{EA_c}.
$$

**답:**

$$
\boxed{T=
\frac{wL^4/8}{L^3/3+I\ell_c/A_c}
=\frac{45}{1+163.39869281\,I_{[\mathrm{m^4}]}}\;\mathrm{kN}}.
$$

여기서 $I_{[\mathrm{m^4}]}$는 보의 $I$를 m⁴로 표시한 수치이다. $T>0$이므로 팽팽한 케이블 가정과 부합한다. **부록 참조 필요:** W410×46.1의 강축 $I$.이 문제는 케이블의 단면적이 주어져도 보의 $I$가 필요하므로 유일한 인장력 수치까지 정할 수 없다.

### 9.92

**원문:** PDF 14, 그림 P9.92. **굽은 봉이 아니라 교차하는 두 단순보의 하중 분담 문제**이다. $AC=CB=a=1.2$ m, $DC=CE=b=1.5$ m, C에 $P=25$ kN. AB와 DE의 $EI$는 같다.

**방법·경계조건:** 겹침원리와 C의 처짐 적합조건. $y_A=y_B=y_D=y_E=0$, 두 보의 $y_C$가 같다. 각 보는 중앙 집중하중을 받는다.

AB가 분담하는 하중을 $P_1$, DE의 분담을 $P_2$라 하면

$$
P_1+P_2=P,\qquad
\frac{P_1(2a)^3}{48EI}=\frac{P_2(2b)^3}{48EI}.
$$

$$
P_1=\frac{Pb^3}{a^3+b^3},\qquad
P_2=\frac{Pa^3}{a^3+b^3}.
$$

**답:**

$$
\boxed{R_B=\frac{P_1}{2}=8.26719577\;\mathrm{kN}\;(\uparrow)},
$$
$$
\boxed{R_E=\frac{P_2}{2}=4.23280423\;\mathrm{kN}\;(\uparrow)}.
$$

$R_A=R_B,\ R_D=R_E$.동일한 $EI$가 적합조건에서 소거된다.

### 9.94

**원문:** PDF 14, 그림 P9.94. A 고정, 서로 직각인 두 수평 봉 AB,BC의 길이는 각각 $L=250$ mm. 원형 지름 16 mm. C에 수직 아래쪽 $P=200$ N. $E=200$ GPa, $G=80$ GPa.

**방법·경계조건:** 굽힘·비틀림 변형에너지에 대한 카스틸리아노 정리. A의 이동과 회전은 0, B의 절점은 강접이며 C는 자유단이다.

> 모델 주: 그림의 둥근 코너에 별도의 곡률반경이나 호 길이가 주어지지 않았다. 두 직선 구간이 강접된 직각 봉의 선형 보·비틀림 모델을 사용한다. 코너 국부변형은 이 자료만으로 별도 계산할 수 없다.

$$
I=\frac{\pi d^4}{64}=3216.990877\;\mathrm{mm^4},\qquad
J=\frac{\pi d^4}{32}=6433.981755\;\mathrm{mm^4}.
$$

AB를 A에서 $s$, BC를 B에서 $t$로 재면 굽힘모멘트 크기는
$M_{AB}=P(L-s)$, $M_{BC}=P(L-t)$이고, AB에는 일정 비틀림 $T_{AB}=PL$이 작용한다. BC의 비틀림은 0이다.

$$
U=\int_0^L\frac{P^2(L-s)^2}{2EI}ds
+\int_0^L\frac{P^2L^2}{2GJ}ds
+\int_0^L\frac{P^2(L-t)^2}{2EI}dt.
$$

하중 방향 변위는

$$
\delta_C=\frac{\partial U}{\partial P}
=\frac{2PL^3}{3EI}+\frac{PL^3}{GJ}
=3.23801561+6.07127926\;\mathrm{mm}.
$$

**답:**

$$
\boxed{y_C=-9.30929487\;\mathrm{mm}\quad(\text{아래쪽})}.
$$

굽힘만 계산하면 3.238 mm가 되어 비틀림 기여를 누락한다.

## 9.96–9.116

### 9.96

**원문:** PDF 15, 그림 P9.96. B 고정, A 자유단에 시계방향 $M_0$.

**방법·경계조건:** 모멘트-면적법, $y_B=\theta_B=0$.$M/EI=M_0/EI$인 직사각형 면적을 사용한다.

$$
0-\theta_A=\frac{M_0L}{EI},\qquad
y_A=\frac{M_0L}{EI}\frac L2.
$$

**답:**

$$
\boxed{\theta_A=-\frac{M_0L}{EI},\qquad
y_A=\frac{M_0L^2}{2EI}\;(\uparrow)}.
$$

9.2의 직접적분 결과와 일치한다.

### 9.98

**원문:** PDF 15, 그림 P9.98. B 고정, A 자유, 전체에 아래쪽 균일하중 $w$.

**방법·경계조건:** 모멘트-면적법, $y_B=\theta_B=0$.A 기준 $M(x)=-wx^2/2$인 포물선 면적과 그 1차 모멘트:

$$
\theta_A=-\int_0^L\frac{-wx^2/2}{EI}dx,\qquad
y_A=\int_0^L\frac{x(-wx^2/2)}{EI}dx.
$$

**답:**

$$
\boxed{\theta_A=\frac{wL^3}{6EI},\qquad
y_A=-\frac{wL^4}{8EI}}.
$$

$R_B=wL,\ C_B=-wL^2/2$.

### 9.100

**원문:** PDF 15, 그림 P9.100. A 고정, C 중앙, B 자유. C에 반시계 $2M_0$, B에 시계 $M_0$.

**방법·경계조건:** 모멘트-면적법, $y_A=\theta_A=0$.
$M=+M_0$ $AC$, $M=-M_0$ $CB$. 두 직사각형의 면적과 면적모멘트를 합한다.

$$
\theta_B=\frac{M_0(L/2)-M_0(L/2)}{EI}=0,
$$
$$
y_B=\frac{M_0}{EI}\left(\frac L2\frac{3L}{4}-\frac L2\frac L4\right),
\quad
\theta_C=\frac{M_0L}{2EI},\quad
y_C=\frac{M_0}{EI}\frac L2\frac L4.
$$

**답:**

$$
\boxed{\theta_B=0,\quad y_B=\frac{M_0L^2}{4EI}\;(\uparrow)},
\qquad
\boxed{\theta_C=\frac{M_0L}{2EI},\quad y_C=\frac{M_0L^2}{8EI}\;(\uparrow)}.
$$

### 9.102

**원문:** PDF 15, 그림 P9.102. C 고정, A 자유.$AB=1$ m, $BC=2.5$ m. A에 5 kN, BC에 4 kN/m. W250×22.3, $E=200$ GPa.

**방법·경계조건:** 모멘트-면적법, $y_C=\theta_C=0$.A에서 $x$를 재면

$$
M=-5x-2\langle x-1\rangle^2,\quad 0\le x\le3.5.
$$

$$
\theta_A=-\frac1K\int_0^{3.5}Mdx,\qquad
y_A=\frac1K\int_0^{3.5}xMdx.
$$

**답:**

$$
\boxed{\theta_A=\frac{41.041666667}{K}\;\mathrm{rad},\qquad
y_A=-\frac{101.40625}{K}\;\mathrm m}.
$$

$R_C=15$ kN, $C_C=-30$ kN·m.
**부록 참조 필요:** W250×22.3의 강축 $I$.

### 9.104

**원문:** PDF 16, 그림 P9.104. C 고정, A 자유, $AC=3$ m, $BC=2.1$ m. 전체에 A에서 0, C에서 120 kN/m인 아래쪽 삼각형하중. B에 **위쪽 20 kN**. W360×64, $E=200$ GPa.

**방법·경계조건:** 모멘트-면적법, $y_C=\theta_C=0$.$AB=0.9$ m이며

$$
M(x)=-\frac{20}{3}x^3+20\langle x-0.9\rangle.
$$

**답:**

$$
\boxed{\theta_A=-\frac1K\int_0^3Mdx
=\frac{90.9}{K}\;\mathrm{rad}},
$$
$$
\boxed{y_A=\frac1K\int_0^3xMdx
=-\frac{222.57}{K}\;\mathrm m}.
$$

$R_C=160$ kN, $C_C=-138$ kN·m.
**부록 참조 필요:** W360×64의 강축 $I$.

### 9.106

**원문:** PDF 16, 그림 P9.106. D 고정, A 자유단에 시계방향 $M_0$.$AB=BC=CD=a$.굽힘강성은 AB:$EI$, BC:$2EI$, CD:$3EI$.

**방법·경계조건:** 변단면 모멘트-면적법, $y_D=\theta_D=0$.B,C에서 $y,\theta$ 연속. 전 구간 $M=M_0$이나 곡률은 세 구간마다 다르다.

$$
\theta_A=-\frac{M_0a}{EI}\left(1+\frac12+\frac13\right),
$$
$$
y_A=\frac{M_0a^2}{EI}
\left(\frac12+\frac{1}{2}\frac32+\frac{1}{3}\frac52\right).
$$

**답:**

$$
\boxed{\theta_A=-\frac{11M_0a}{6EI},\qquad
y_A=\frac{25M_0a^2}{12EI}\;(\uparrow)}.
$$

### 9.108

**원문:** PDF 16, 그림 P9.108. C 고정, A 자유, $AC=2.7$ m, $BC=2.1$ m, 따라서 $AB=0.6$ m. A에 40 kN, BC에 90 kN/m. 원래 단면 W410×60, BC에 위아래 각 12×200 mm 덮개판, $E=200$ GPa.

**방법·경계조건:** 구간별 $M/EI$ 모멘트-면적법. $y_C=\theta_C=0$, B에서 $y,\theta$ 연속.

원래 강축 단면2차모멘트를 $I_s$, 실제 형강 높이를 $d_s$라 한다. 판 폭 $b_p=0.200$ m, 두께 $t_p=0.012$ m일 때 보강구간은

$$
I_c=I_s+2\left[
\frac{b_pt_p^3}{12}+b_pt_p\left(\frac{d_s+t_p}{2}\right)^2
\right].
$$

A 기준

$$
M=-40x-45\langle x-0.6\rangle^2,\quad
I(x)=\begin{cases}I_s,&0\le x<0.6,\\I_c,&0.6<x\le2.7.\end{cases}
$$

**답:** $K_s=EI_s,\ K_c=EI_c$를 kN·m²로 넣으면

$$
\boxed{\theta_A=\frac{7.200}{K_s}+\frac{277.515}{K_c}\;\mathrm{rad}},
$$
$$
\boxed{y_A=-\frac{2.880}{K_s}-\frac{561.700125}{K_c}\;\mathrm m}.
$$

두 결과는 각각 (-\int M/(EI)dx), $\int xM/(EI)dx$의 구간 적분이다.
**부록 참조 필요:** W410×60의 $I_s$와 실제 높이 $d_s$.명칭의 410 mm를 실제 $d_s$로 단정하지 않았다.

### 9.110

**원문:** PDF 17, 그림 P9.110. 단순지지 AE 길이 $L$.B,C,D는 사분점이며 각각 $P$.

**방법·경계조건:** 모멘트-면적법, $y_A=y_E=0$, 대칭 ( \theta_C=0).$R_A=R_E=3P/2$.

왼쪽 절반의
$$
M=\frac{3P}{2}x-P\langle x-L/4\rangle
$$
에 대하여
$$
\theta_A=-\int_0^{L/2}\frac{M}{EI}dx,\qquad
y_C=-\int_0^{L/2}\frac{xM}{EI}dx.
$$

**답:**

$$
\boxed{\theta_A=-\frac{5PL^2}{32EI},\qquad
y_C=-\frac{19PL^3}{384EI}}.
$$

9.38의 $a=L/4$와도 일치한다.

### 9.112

**원문:** PDF 17, 그림 P9.112. 단순지지, 중앙 최대강도 $w_0$의 대칭 삼각형하중.

**방법·경계조건:** 모멘트-면적법, $y_A=y_B=0,\ \theta_C=0$.왼쪽 절반의
$$
M=\frac{w_0Lx}{4}-\frac{w_0x^3}{3L}
$$
에 대해 $\theta_A=-\int_0^{L/2}M/(EI)dx$, $y_C=-\int_0^{L/2}xM/(EI)dx$.

**답:**

$$
\boxed{\theta_A=-\frac{5w_0L^3}{192EI},\qquad
y_C=-\frac{w_0L^4}{120EI}}.
$$

9.10의 직접적분 결과와 일치한다.

### 9.114

**원문:** PDF 17, 그림 P9.114. 단순지지 AE.B,D 사분점에 아래쪽 $P$, 중앙 C에 위쪽 $P$.

**방법·경계조건:** 모멘트-면적법, $y_A=y_E=0,\ \theta_C=0$.평형에서 $R_A=R_E=P/2$.

왼쪽 절반은
$$
M=\frac P2x-P\langle x-L/4\rangle.
$$
따라서
$$
\theta_A=-\frac1{EI}\int_0^{L/2}Mdx,\qquad
y_C=-\frac1{EI}\int_0^{L/2}xMdx.
$$

**답:**

$$
\boxed{\theta_A=-\frac{PL^2}{32EI},\qquad
y_C=-\frac{PL^3}{128EI}}.
$$

중앙에 위쪽 힘이 있어도 C의 순처짐은 아래쪽이다.

### 9.116

**원문:** PDF 17, 그림 P9.116. $AB=BC=CD=DE=a$.A,E 단순지지.B,D에 $P$, C에 $2P$.AB,DE의 강성 $EI$, BD의 강성 $3EI$.

**방법·경계조건:** 구간별 모멘트-면적법, $y_A=y_E=0,\ \theta_C=0$, B,D에서 $y,\theta$ 연속. $R_A=R_E=2P$.

왼쪽 절반은 $M=2Px\;(0<x<a)$, $M=P(x+a)\;(a<x<2a)$.

$$
\theta_A=-\frac1{EI}\left[
\int_0^a2Px\,dx+\frac13\int_a^{2a}P(x+a)dx\right],
$$
$$
y_C=-\frac1{EI}\left[
\int_0^a2Px^2dx+\frac13\int_a^{2a}Px(x+a)dx\right].
$$

**답:**

$$
\boxed{\theta_A=-\frac{11Pa^2}{6EI},\qquad
y_C=-\frac{35Pa^3}{18EI}}.
$$

## 9.118–9.124

### 9.118

**원문:** PDF 18, 그림 P9.118. 단순지지 AE, $L=3.6$ m, $AB=DE=0.6$ m, BD에 40 kN/m.E의 끝모멘트는 시계방향 10 kN·m.S250×37.8, $E=200$ GPa.

> **원본 판독 한계:** A의 외부모멘트 크기 숫자는 제공된 스캔의 왼쪽 가장자리 밖으로 잘렸다. E와 같은 값이라고 임의로 가정하지 않았다. A의 모멘트를 반시계방향 양의 부호 있는 수치 $m_A$ $kN·m$로 정의하여 최종식을 제시한다. 원본에서 누락된 모멘트 값 확인과 형강 부록이 모두 필요하다.

**방법·경계조건:** 모멘트-면적법, $y_A=y_E=0$.$x=0$은 A.

$$
R_A=\frac{162.8+m_A}{3.6},\qquad
R_E=\frac{182.8-m_A}{3.6}\quad[\mathrm{kN}],
$$
$$
M(x)=-m_A+R_Ax-20\langle x-0.6\rangle^2
+20\langle x-3.0\rangle^2.
$$

양 끝 처짐을 같게 하는 접선조건은
$$
\theta_A=-\frac1{LK}\int_0^L(L-x)M(x)\,dx.
$$
중앙 C=$1.8$ m의 처짐은
$$
y_C=\theta_A(1.8)+\frac1K\int_0^{1.8}(1.8-x)M(x)dx.
$$

**주어진 스캔으로 확정 가능한 답:**

$$
\boxed{\theta_A=\frac{-60.24+1.2m_A}{K}\;\mathrm{rad},\qquad
y_C=\frac{-67.932+0.81m_A}{K}\;\mathrm m}.
$$

**부록 참조 필요:** S250×37.8의 강축 $I$.$m_A$도 판독되지 않아 순수 수치값이나 처짐 방향을 하나로 단정할 수 없다.

### 9.120

**원문:** PDF 18, 그림 P9.120. B,D 지지, $AB=DE=1$ m, $BC=CD=1.7$ m.A,E에 $P=8$ kN, 중앙 C에 10 kN.W200×19.3, $E=200$ GPa.

**방법·경계조건:** 모멘트-면적법, $y_B=y_D=0,\ \theta_C=0$.반력은 $R_B=R_D=13$ kN.

A 기준 $x$를 쓰면 왼쪽 절반에서
$$
M=-8x+13\langle x-1\rangle,\qquad0\le x\le2.7.
$$

$$
EI\theta_A=-\int_0^{2.7}Mdx=10.375.
$$

B의 처짐을 0으로 두어 적분상수를 결정하면
$$
EIy=-\frac{8x^3}{6}+\frac{13}{6}\langle x-1\rangle^3
-\frac{10}{6}\langle x-2.7\rangle^3
+\frac{13}{6}\langle x-4.4\rangle^3
+10.375x-\frac{217}{24}.
$$

**답:**

$$
\boxed{\theta_A=\frac{10.375}{K}\;\mathrm{rad},\qquad
y_C=\frac{3.371666667}{K}\;\mathrm m\;(\uparrow)}.
$$

참고로 $y_A=y_E=-9.041666667/K$ m.
**부록 참조 필요:** W200×19.3의 강축 $I$.

### 9.122

**원문:** PDF 18, 9.120의 보에서 A의 처짐이 0이 되게 하는 두 끝하중 $P$.

**방법·경계조건:** 모멘트-면적법과 선형 겹침. $y_B=y_D=0,\ \theta_C=0$에 추가하여 $y_A=0$.가운데 하중은 10 kN로 유지하고 두 끝의 $P$를 함께 바꾼다.

9.120과 같은 좌표에서 $R_B=R_D=P+5$이고
$$
EI\theta_A=2.2P-7.225.
$$
AB 구간 $M=-Px$를 적분하여 $y(1)=0$을 대입하면
$$
EIy_A=7.225-\frac{61}{30}P.
$$

**답:**

$$
\boxed{P=\frac{7.225(30)}{61}
=3.553278689\;\mathrm{kN}\quad(\text{각 끝, 아래쪽})}.
$$

적합조건에서 $EI$가 소거되므로 단면 부록 없이 하중 수치가 결정된다. 대칭으로 $y_E=0$도 성립한다.

### 9.124

**원문:** PDF 18, 그림 P9.123 및 P9.124. 길이 $L$의 균일한 봉 AE를 양 끝에서 각각 거리 $a$인 B,D에서 지지한다. A,C,E의 아래쪽 처짐이 같도록 $a$를 구한다.

**방법·하중 해석·경계조건:** 모멘트-면적법. 별도의 외부하중 화살표나 크기가 없는 균일한 봉이므로 **균일한 자중 $w>0$**에 의한 처짐으로 해석한다. $y_B=y_D=0$, 중앙 대칭조건 $\theta_C=0$, 자유단의 $M,V=0$.자중 크기와 $EI$는 최종 위치식에서 소거된다.

각 반력은 $wL/2$.A 기준 왼쪽 절반에서
$$
M=-\frac{wx^2}{2}+\frac{wL}{2}\langle x-a\rangle,
$$
$$
EIy=-\frac{wx^4}{24}+\frac{wL}{12}\langle x-a\rangle^3+C_1x+C_2,
$$
$$
C_1=\frac{wL^3}{48}-\frac{wL}{4}(L/2-a)^2.
$$

$r=a/L,\ s=1/2-r$로 두고 $y_C-y_A=0$을 적용하면
$$
0=\frac{EI(y_C-y_A)}{wL^4}
=\frac1{128}+\frac{s^3}{12}-\frac{s^2}{8},
$$
$$
32r^3-24r+5=0.
$$

**답:** 지점이 양 끝과 중앙 사이에 있는 $0<r<1/2$의 해는

$$
\boxed{a=0.2231491011\,L}.
$$

확인하면
$$
y_A=y_C=y_E=-0.0002697282480\,\frac{wL^4}{EI},
$$
이므로 세 점 모두 아래쪽으로 같은 양만큼 처진다.

## 검산과 남은 자료 한계

- 위쪽 양의 힘, 반시계 양의 외부모멘트를 사용해 모든 보의 평형식을 일관되게 적용했다. 수치형 직선 보 및 무차원화한 다수 기호 문제에 대해 특이함수의 정확한 다항 적분을 별도 계산 코드로 평가하고, 힘·모멘트 평형 및 각 지점의 처짐·고정단 기울기 잔차를 확인했다.
- 계산 검산 결과: 일정한 $EI$의 47개 모델 사례를 평가했고, 추가 다항 분포하중·변단면 면적 적분·목표 처짐조건을 포함해 **202개 스칼라 비교를 통과**했다. 비교한 모델의 평형·경계조건 최대 잔차는 해당 계산 단위에서 $4.55\times10^{-13}$이었다. 이는 계산식 검산이며, 원본에서 잘린 데이터까지 확인되었다는 뜻은 아니다.
- 9.12, 9.60, 9.62는 $\theta(x)=0$의 구간 내 해를 구한 후 원래 처짐식에 재대입했다. 9.122와 9.124는 목표 처짐조건에 재대입했다.
- 같은 하중·지지조건인 9.2/9.96, 9.10/9.112, 9.26/9.50, 9.38/9.110의 결과는 좌표·길이 정의를 맞추면 일치한다. 변단면 문제는 구간별 $1/(EI)$를 따로 적용했다.
- 정확한 단면 제원이 없어 최종 처짐·기울기의 단독 숫자를 정할 수 없는 문제는 각 항목에 **부록 참조 필요**를 표시했다. 9.90의 케이블 힘도 보의 $I$에 의존한다. 반면 9.92와 9.122 등은 동일한 $EI$가 소거되어 반력·하중을 수치로 확정할 수 있다.
- **판독상 별도 확인점:** 9.16의 옅은 길이는 확대 판독값 2.5 m로 계산했으며 일반식도 함께 제공했다. 9.118의 A 모멘트 수치는 사진 밖으로 잘려 미확정이며, 부호 있는 $m_A$에 대한 최종식으로 남겼다. 9.94 코너의 국부변형은 별도 치수가 없어 포함하지 않았다.
- 총 **62개** 짝수 문제를 번호별로 기록했다. 사용자 지시에 따라 커밋·푸시는 하지 않았다. 시작 시 시도한 git pull은 저장소 메타데이터 쓰기 권한 제한으로 수행되지 않았다.
