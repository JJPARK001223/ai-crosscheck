# Round 20 Codex 블라인드 독립 검증

## 0. 검증 범위와 결론 요약

- **블라인드 준수:** `round20/claude.md`와 지정된 Claude HTML 산출물은 열지 않았다. `round20/codex_prompt.md`, `round20/PROBLEM.md`, 두 원문 논문, 표준 LEFM 관계와 ASTM 원문만 사용했다.
- **선행연구 1:** 식 (1)~(13)의 전사와 제시된 유도 경로는 대체로 원문과 일치한다. 특히 식 (3)+(4)+(5)에서 거리 $r$가 정확히 소거되어 $w_f=K^2/(2\pi E)$가 나온다.
- **선행연구 3:** 식 (1)~(4)의 표기는 원문과 일치한다. 다만 원문 식 (2)에는 응력구배의 절댓값이 빠져 있어, 식 (3)의 음의 미분을 그대로 넣으면 식 (4)는 나오지 않는다. 식 (4)는 “응력 감소율의 크기” — 즉 \(|d\sigma_e/ds|\) — 를 암묵적으로 써야만 성립한다.
- **핵심 \(2\pi\) 판정:** 선행연구 3의 식 (3)을 실제 곡선맞춤식으로 존중하면 그 논문의 $K$는 표준 Mode-I 응력확대계수 $K_I$가 아니라
  \[
  K_{\text{선3}}=\frac{K_I}{\sqrt{2\pi}}
  \]
이다. 따라서 $Y=K_{\text{선3}}^2/E=K_I^2/(2\pi E)$이며, 선행연구 1의 $w_f$와 동일하다. 평면응력에서는 $Y=w_f=G_c/(2\pi)$, 평면변형에서는 $Y=w_f=G_c/[2\pi(1-\nu^2)]$이다. **그러므로 선행연구 3의 “\(Y\)가 임계 에너지방출률과 동일하다”는 문장은 수치적 동일성 $Y=G_c$를 뜻한다면 틀리다.**
- **반복 금지 정정 7개:** ②, ④, ⑤, ⑥, ⑦은 타당하다. ③은 논문의 실제 절차와 부합한다. ①은 본인 FE 모델의 좌표축 정의가 제공되지 않아 원문만으로는 확인할 수 없다.

## 1. 선행연구 1 식 (1)~(13)

출처: Y. W. Kwon, “Revisiting Failure of Brittle Materials,” *Journal of Pressure Vessel Technology*, 143(6), 064503 (2021), DOI: 10.1115/1.4050989.

### 1.1 두 파괴 조건, 식 (1)~(3)

**판정: 원문과 일치.**

원문 식 (1)은

\[
\sigma_l\ge \sigma_f
\tag{1}
\]

이다. “국부응력이 재료 파괴강도보다 작지 않아야 한다”는 조건이다.

원문 식 (2)는 다음 구조이다.

\[
\frac{\sigma_l^2}{2E}
\left[
\frac{1}{\sigma_l}\left|\frac{d\sigma_l}{ds}\right|
\right]^{-1}
\ge w_f .
\tag{2}
\]

앞의 항은 변형에너지밀도이고, 대괄호 안은 응력으로 정규화한 응력구배이다. 단순화하면

\[
\frac{\sigma_l^3}{2E}
\left|\frac{ds}{d\sigma_l}\right|
\ge w_f ,
\tag{3}
\]

가 된다. 즉 식 (2)→(3)의 대수정리는 맞다. $s$는 국부점에서 “응력구배 절댓값이 가장 작은 방향”, 곧 제안된 파괴경로이다. $w_f$의 단위는 “힘/길이 = 에너지/면적” \((\mathrm{J/m^2})\)이다.

### 1.2 균열 Case 2, 식 (4)~(7)

**판정: 원문과 일치.**

원문은 Irwin 근접장으로

\[
\sigma_x=\frac{K}{\sqrt{2\pi r}}
\tag{4}
\]

를 쓰고, 균열 진행방향 좌표에 대해

\[
\left|\frac{d\sigma_x}{dr}\right|
=\frac{K}{2\sqrt{2\pi}\,r^{3/2}}
\tag{5}
\]

를 쓴다(원문 좌표명은 (y)로도 표기되지만 균열선단 거리라는 역할은 동일하다). 결합 결과는

\[
w_f=\frac{K^2}{2\pi E},
\tag{6}
\]

이고 임계상태에서

\[
K_{IC}=\sqrt{2\pi E w_f}.
\tag{7}
\]

이다. 모두 원문과 정확히 일치한다.

### 1.3 원공 Case 3, 식 (8)~(13)

**판정: 원문과 일치.**

원문 식 (8)~(10)은 무한판 원공의 Kirsch 해 \((\sigma_r,\sigma_\theta,\tau_{r\theta})\)이다. 특히

\[
\sigma_\theta
=\frac{\sigma_0}{2}
\left[
1+\frac{R^2}{r^2}
-\left(1+3\frac{R^4}{r^4}\right)\cos 2\theta
\right].
\tag{9}
\]

\(r=R,\theta=\pi/2\)이면 \(\cos\pi=-1\)이므로

\[
\sigma_\theta(R,\pi/2)=3\sigma_0.
\]

또한

\[
\left.
\frac{\partial \sigma_\theta}{\partial r}
\right|_{\theta=\pi/2}
=\frac{\sigma_0}{2}
\left(-\frac{2R^2}{r^3}-\frac{12R^4}{r^5}\right),
\]

이므로 원공 가장자리에서는

\[
\left|
\left.\frac{\partial \sigma_\theta}{\partial r}
\right|_{r=R,\theta=\pi/2}
\right|
=\frac{7\sigma_0}{R}.
\tag{11}
\]

따라서 Case 3의 동시 판정식은 원문 그대로

\[
\sigma_\theta(R,\pi/2)\ge \sigma_f
\tag{12}
\]

및

\[
\frac{\{\sigma_\theta(R,\pi/2)\}^3}
{2E\left|\left.\partial\sigma_\theta/\partial r\right|_{R,\pi/2}\right|}
\ge w_f
\tag{13}
\]

이다. 원문은 \(\sigma_0\ge\sigma_f/3\)이면 식 (12)가 만족되고, 이후 식 (13)이 지배할 수 있다고 설명한다.

## 2. 선행연구 1 식 (6)의 독립 재대수검산

**판정: 유도 맞음. (r)은 정확히 소거됨.**

임계상태에서 식 (3)을 등호로 두고 (s=r)로 놓는다.

\[
\sigma=\frac{K}{\sqrt{2\pi r}},\qquad
\left|\frac{d\sigma}{dr}\right|
=\frac{K}{2\sqrt{2\pi}r^{3/2}},
\]

따라서

\[
\left|\frac{dr}{d\sigma}\right|
=\frac{2\sqrt{2\pi}r^{3/2}}{K}.
\]

이를 식 (3)의 좌변에 대입하면

\[
\begin{aligned}
w_f
&=\frac{1}{2E}
\left(\frac{K}{\sqrt{2\pi r}}\right)^3
\left(\frac{2\sqrt{2\pi}r^{3/2}}{K}\right)\\
&=\frac{1}{2E}
\frac{K^3}{(2\pi)^{3/2}r^{3/2}}
\frac{2(2\pi)^{1/2}r^{3/2}}{K}\\
&=\frac{K^2}{2\pi E}.
\end{aligned}
\]

\(r^{3/2}\)와 \(K\)가 소거되며 계수도 정확히 \(1/(2\pi)\)가 남는다. 이 결과는 단순 차원검사가 아니라 직접 대수검산으로 확인된다.

## 3. 선행연구 3 식 (1)~(4)

출처: Y. W. Kwon, E. K. Markoff, and S. DeFisher, “Unified Failure Criterion Based on Stress and Stress Gradient Conditions,” *Materials*, 17(3), 569 (2024), DOI: 10.3390/ma17030569.

### 3.1 원문 전사

**판정: 제시된 네 식은 원문과 일치. 단, 식 (2)에 중요한 부호 문제가 있음.**

원문은

\[
\sigma_e\ge\sigma_f,
\tag{1}
\]

\[
\sigma_e\ge
\left(2EY\frac{d\sigma_e}{ds}\right)^{1/3},
\tag{2}
\]

\[
\sigma_e=\frac{K}{\sqrt{s}},
\tag{3}
\]

\[
Y=\frac{K^2}{E}
\tag{4}
\]

로 적는다. 여기서 식 (2)의 (s)는 파괴경로이고, 균열 예시의 식 (3)에서는 “균열선단에서 측정하여 균열 방향을 따르는 좌표”라고 명시한다. 식 (4) 직후에는 (Y)가 파괴역학의 임계 에너지방출률과 동등하다고 서술한다.

### 3.2 원문 식 (2)의 절댓값 누락

**판정: 원문 내부의 수학적 불일치.**

식 (3)을 미분하면

\[
\frac{d\sigma_e}{ds}=-\frac{K}{2s^{3/2}}<0.
\]

원문 식 (2)에 이를 부호 그대로 넣으면 (E>0,Y>0)일 때 세제곱근 안이 음수가 되어 식 (4)의 양의 (Y)를 얻을 수 없다. 반면 선행연구 1처럼 구배의 크기를 쓰면

\[
\sigma_e^3=2EY\left|\frac{d\sigma_e}{ds}\right|
=2EY\frac{K}{2s^{3/2}},
\]

\[
\frac{K^3}{s^{3/2}}=EY\frac{K}{s^{3/2}}
\quad\Rightarrow\quad
Y=\frac{K^2}{E}.
\]

즉 식 (4)는 **식 (2)를 \(\left|d\sigma_e/ds\right|\) 또는 \(-d\sigma_e/ds\)로 읽을 때만** 성립한다. 문서에서 이 절댓값을 복원하지 않고 “그대로 대입해 식 (4)가 나온다”고 쓰면 불완전하다.

## 4. 핵심 쟁점: \(K\), \(Y\), \(w_f\), \(G_c\)의 관계

### 4.1 표준 LEFM와 선행연구 3 식 (3)의 비교

**판정: 선행연구 3의 \(K\)는 식의 작동 방식상 표준 \(K_I\)가 아니라 \(K_I/\sqrt{2\pi}\)이다.**

표준 Mode-I 균열선단 응력의 선도항은 균열 전방선 \((\theta=0)\)에서

\[
\sigma_{\text{opening}}(r,0)
=\frac{K_I}{\sqrt{2\pi r}}+O(r^0).
\]

선행연구 3은 \(s\)를 실제 균열선단으로부터 균열 방향을 따라 잰 거리로 정의하고, §4에서 FE 응력-거리 자료를 식 (3) \(\sigma_e=K/\sqrt{s}\)에 직접 곡선맞춤하여 \(K\)를 구한다. 따라서 같은 물리 응력장과 같은 거리 좌표를 맞춘 계수는 필연적으로

\[
K_{\text{선3, fit}}=\frac{K_I}{\sqrt{2\pi}}
\]

이다. 저자들이 이를 문장상 “stress intensity factor (K)”라고 부르지만, 표준 정규화의 (K_I)와 수치가 같은 상수는 아니다.

반대로 \(K_{\text{선3}}=K_I\)라고 강제로 해석하면 식 (3) 자체가 표준 Irwin 장보다 \(\sqrt{2\pi}\)만큼 큰 응력을 예측한다. 즉 “식 (3)이 맞다”와 “그 \(K\)가 표준 \(K_I\)와 같다”를 동시에 유지할 수 없다. 실제 §4의 곡선맞춤 절차 때문에 전자의 해석, 곧 재정규화된 계수로 보는 것이 타당하다.

### 4.2 \(Y\)와 \(G_c\)의 최종 판정

표준 LEFM는

\[
G_c=\frac{K_{Ic}^2}{E'},\qquad
E'=\begin{cases}
E & \text{평면응력},\\
E/(1-\nu^2) & \text{평면변형}
\end{cases}
\]

이다. 그러므로 선행연구 3 식 (4)은

\[
Y=\frac{K_{\text{선3}}^2}{E}
=\frac{K_{Ic}^2}{2\pi E}.
\]

결국

\[
\boxed{Y=w_f=\frac{G_c}{2\pi}}
\qquad\text{(평면응력)}
\]

및

\[
\boxed{Y=w_f=\frac{G_c}{2\pi(1-\nu^2)}}
\qquad\text{(평면변형, 식의 (E)가 Young률일 때)}
\]

이다.

**최종 판정:** 선행연구 1과 3의 물리량 \(w_f\), \(Y\) 사이에는 모순이 없고 둘은 같은 정규화된 파괴 파라미터이다. 그러나 표준 임계 에너지방출률 \(G_c\)와는 계수 차이가 있다. 선행연구 3의 “equivalent to the critical energy release rate”는 “같은 차원을 갖고 \(G_c\)에 비례한다”는 느슨한 뜻으로만 허용된다. **수치적 등식 \(Y=G_c\)은 틀리며 평면응력에서 정확한 식은 \(Y=G_c/(2\pi)\)이다.**

근거: G. R. Irwin, “Analysis of Stresses and Strains Near the End of a Crack Traversing a Plate,” *Journal of Applied Mechanics*, 24, 361–364 (1957); R. G. Munro, S. W. Freiman, and T. L. Baker, *Fracture Toughness Data for Brittle Materials*, NISTIR 6153 (1998), 특히 (K_{Ic}^2=G_cE')와 (E') 정의.

## 5. 선행연구 3 §4 경화 시멘트 페이스트

### 5.1 모델링 및 역산→곡선맞춤→예측

**판정: 원문과 일치.**

원문의 실제 절차는 다음과 같다.

1. 시편은 \(L\times H\times W\)의 3PB 관통균열 블록이고, 모두 \(W=100\ \mathrm{mm}\), \(L/H=4\), \(E=20.8\ \mathrm{GPa}\)이다.
2. 먼저 대칭 반모델 하나를 3D solid 요소(약 0.3 mm 균일 요소)로 해석하고, 균열선을 따라 폭 방향 응력분포가 거의 같음을 확인했다.
3. 계산시간 절감을 위해 이후 파괴하중 예측은 약 10,000개의 4절점 사각형 요소를 쓴 2D 해석으로 수행했다.
4. \(Y\)가 알려지지 않았으므로 \(a/H=0.1,\ H=100\ \mathrm{mm}\) 시험결과 하나를 사용해 \(Y\)를 역산했다.
5. 각 주어진 하중에 대한 FE 균열선단 응력을 식 (3)에 곡선맞춤하여 \(K_{\text{선3}}\)를 얻었다.
6. 동일한 (Y)와 식 (4)을 나머지 시편에 적용하여 파괴하중을 예측했다.

따라서 “한 시험값으로 (Y) 역산 → FE 응력장 곡선맞춤으로 (K) 산정 → 같은 (Y)로 나머지 파괴하중 예측”이라는 요약은 정확하다. 다만 계산 구현상 각 하중의 (K) 곡선맞춤이 (Y) 역산에도 먼저 필요하므로, 이를 완전히 시간순으로 분리된 세 단계라고 이해하면 안 된다.

### 5.2 이상치 및 해석 케이스 수

**판정: 원문과 일치.**

- 원문은 \(a/H=0.3,\ H=100\ \mathrm{mm}\)인 한 시편만 예측과 시험의 차이가 크다고 명시하고, 추가 시편 정보가 없어 원인을 더 조사하지 못했다고 쓴다.
- Fig. 11은 \(H=0.05\ \mathrm{m}\)와 \(0.10\ \mathrm{m}\), 각 세 균열비의 총 6개 2D 예측/시험 비교를 보여준다.
- §4.2는 3D 모델을 먼저 하나 제시해 2D화 가능성을 점검한 뒤 실제 예측은 2D로 수행했다고 서술한다. 그러므로 “3D 세 케이스”가 아니라 **대표 3D 한 케이스 + 2D 여섯 케이스**라는 정정이 원문에 부합한다.

## 6. “반복 금지 정정” 7개 항목 판정

### ① \(\sigma_{yy}\)가 아니라 \(\sigma_{xx}\) (본인 FE 모델 맥락)

**판정: 확인불가.**

두 원문만으로 본인 FE 모델의 전역 \(x,y\)축 정의를 알 수 없다. 선행연구 1은 균열에 수직이고 하중과 평행한 응력을 \(\sigma_x\)라고 부르며, 선행연구 3은 성분명 대신 \(\sigma_e\) 및 최대정규응력을 쓴다. 응력성분 첨자는 좌표 정의에 종속되므로, 본인 모델에서 하중/개구 방향이 실제 \(x\)축이라는 모델 도면 또는 경계조건이 있어야 \(\sigma_{xx}\)로 확정할 수 있다. **따라서 원문 근거만으로 이 정정을 사실이라고 단정하면 안 된다.**

### ② \(K H^{3/2}/P\)가 아니라 \(K_I W\sqrt H/P\)

**판정: 조건부로 사실에 부합.**

3PB SE(B) 시편에서 두께(폭)를 (W), 높이(깊이)를 (H), 하중을 (P)라 하면

\[
K_I=\frac{P}{W\sqrt H}\,F(a/H,L/H)
\quad\Rightarrow\quad
\frac{K_IW\sqrt H}{P}=F.
\]

따라서 일반적인 무차원화는 \(K_IW\sqrt H/P\)이다. \(KH^{3/2}/P\)는 \(W=H\)인 정사각 단면일 때만 위 식과 같거나, \(P/W\)를 단위폭당 하중으로 새로 정의했을 때만 정당화된다. 선행연구 3은 \(W=100\ \mathrm{mm}\)로 고정하고 \(H\)를 바꾸므로 \(W=H\)를 일반식으로 가정할 수 없다.

### ③ 3D 3케이스가 아니라 2D 6케이스 + 대표 3D 1케이스

**판정: 원문과 일치.**

§4.2와 Fig. 11의 절차가 이를 직접 지지한다. 3D는 폭 방향 균일성 확인용 대표 모델이고, 파괴하중 비교는 2D 여섯 조합이다.

### ④ \(Y=G_c\)는 틀림(평면응력에서 \(2\pi\) 차이)

**판정: 사실에 부합.**

선행연구 3 식 (3)의 곡선맞춤 계수 정의를 따르면 \(Y=G_c/(2\pi)\)이다. 평면변형에서는 \(Y=G_c/[2\pi(1-\nu^2)]\)이다. 단, 논문 저자 자신의 문장은 \(Y\)와 임계 에너지방출률이 “동등”하다고 쓰므로, 이 정정은 **논문 문장 자체의 계수 오류를 지적하는 것**이다.

### ⑤ ASTM D5045로 \(W/H=1\) 정당화 금지

**판정: 사실에 부합.**

ASTM D5045-14(2022)는 플라스틱의 평면변형 (K_{Ic}), (G_{Ic}) 측정을 위한 SENB/CT 시험법이다. 표준 SENB 형상은 표준의 기호로 시편 깊이 (W_{ASTM}=2B), 즉 두께/깊이 (B/W_{ASTM}=0.5), (0.45<a/W_{ASTM}<0.55)를 규정한다. 이는 경화 시멘트 페이스트 논문의 폭 (W)와 높이 (H)를 같게 두라는 근거가 아니며, 재료 범위도 플라스틱이다. 따라서 ASTM D5045로 이 논문의 (W/H=1)을 일반적으로 정당화해서는 안 된다.

출처: ASTM International, ASTM D5045-14(2022), *Standard Test Methods for Plane-Strain Fracture Toughness and Strain Energy Release Rate of Plastic Materials*.

### ⑥ 코너특이성으로 폭비 정당화 금지

**판정: 사실에 부합.**

선행연구 3이 2D화를 정당화한 근거는 코너특이성이 아니라, 대표 3D 해석에서 균열선을 따른 응력분포가 폭을 가로질러 거의 같았다는 직접 비교이다. 자유표면과 균열전면이 만나는 점의 3D corner/free-surface singularity는 오히려 국부 3D 효과이며, 임의의 (W/H)가 충분하다는 보편적 폭비 기준을 제공하지 않는다. 따라서 코너특이성 자체로 (W/H=1)을 정당화하는 것은 논리적으로도 원문상으로도 근거가 없다.

### ⑦ 무한판 Griffith의 \(-a^2\) 곡선을 유한 3PB에 그대로 적용 금지

**판정: 사실에 부합.**

Griffith의 무한판 중앙균열 해에서 고정 원격응력하의 탄성에너지 변화가 (a^2)에 비례하는 것은 그 형상과 하중조건의 결과이다. 유한 3PB SE(B)에서는

\[
K_I=\frac{P}{W\sqrt H}F(a/H,L/H),
\qquad
G=\frac{K_I^2}{E'},
\]

처럼 유한형상 함수 (F), 지점간 거리, 두께 및 하중/변위 제어가 개입한다. 따라서 무한판의 (-a^2) 에너지 곡선을 유한 3PB에 계수와 경계조건 수정 없이 그대로 옮길 수 없다.

근거: A. A. Griffith, “The Phenomena of Rupture and Flow in Solids,” *Philosophical Transactions of the Royal Society A*, 221, 163–198 (1921); B. L. Karihaloo, H. M. Abdalla, and Q. Z. Xiao, “Size effect in concrete beams,” *Engineering Fracture Mechanics*, 70, 979–993 (2003); ASTM E399-24, SE(B) 유한형상 규정.

## 7. 최종 판정표

| 검증 항목 | 판정 | 핵심 근거/주의점 |
|---|---|---|
| 선1 식 (1)~(3) | 원문과 일치 | 식 (2)의 절댓값을 포함해야 함 |
| 선1 식 (4)~(7) | 원문과 일치 | 직접 대수검산에서 \(r\) 소거, \(1/(2\pi)\) 확인 |
| 선1 Kirsch 식 (8)~(11) | 원문과 일치 | \(3\sigma_0\), \(7\sigma_0/R\) 직접 미분 확인 |
| 선1 Case 3 식 (12),(13) | 원문과 일치 | 두 조건을 동시에 만족 |
| 선3 식 (1)~(4) 표기 | 원문과 일치 | 단, 식 (2)에 절댓값 누락 |
| 선3 식 (2)→(4) 유도 | 조건부 일치 | “구배 크기”를 암묵적으로 써야 성립 |
| 선3 \(K\)와 표준 \(K_I\) | 불일치 | \(K_{\text{선3}}=K_I/\sqrt{2\pi}\) |
| 선3 문장 \(Y=G_c\) | 불일치 | 평면응력에서 \(Y=G_c/(2\pi)\) |
| 선3 §4 절차 | 원문과 일치 | 한 시험값으로 \(Y\) 보정, FE 곡선맞춤, 나머지 예측 |
| \(a/H=0.3,H=100\) 유일 이상치 | 원문과 일치 | 저자도 추가 정보 부재를 명시 |
| 정정 ① 응력성분 | 확인불가 | 본인 FE 좌표축 정의 필요 |
| 정정 ② 무차원화 | 조건부 일치 | \(K_IW\sqrt H/P\)가 일반식; \(W=H\) 때만 두 식 동일 |
| 정정 ③ 2D/3D 케이스 | 원문과 일치 | 2D 6 + 대표 3D 1 |
| 정정 ④ \(Y\ne G_c\) | 일치 | 정확히 \(2\pi\) 및 평면변형 보정 차이 |
| 정정 ⑤ ASTM D5045 | 일치 | 플라스틱 표준이며 오히려 \(B/W_{ASTM}=0.5\) |
| 정정 ⑥ 코너특이성 | 일치 | 원문의 근거는 폭 방향 응력분포 직접 비교 |
| 정정 ⑦ Griffith 곡선 | 일치 | 유한 3PB 형상함수와 경계조건 필요 |

## 8. 참고문헌

1. Kwon, Y. W., “Revisiting Failure of Brittle Materials,” *Journal of Pressure Vessel Technology*, 143(6), 064503 (2021). DOI: 10.1115/1.4050989.
2. Kwon, Y. W., Markoff, E. K., and DeFisher, S., “Unified Failure Criterion Based on Stress and Stress Gradient Conditions,” *Materials*, 17(3), 569 (2024). DOI: 10.3390/ma17030569.
3. Irwin, G. R., “Analysis of Stresses and Strains Near the End of a Crack Traversing a Plate,” *Journal of Applied Mechanics*, 24, 361–364 (1957).
4. Munro, R. G., Freiman, S. W., and Baker, T. L., *Fracture Toughness Data for Brittle Materials*, NISTIR 6153, National Institute of Standards and Technology (1998).
5. Griffith, A. A., “The Phenomena of Rupture and Flow in Solids,” *Philosophical Transactions of the Royal Society A*, 221, 163–198 (1921).
6. Karihaloo, B. L., Abdalla, H. M., and Xiao, Q. Z., “Size effect in concrete beams,” *Engineering Fracture Mechanics*, 70, 979–993 (2003).
7. ASTM International, ASTM D5045-14(2022), *Standard Test Methods for Plane-Strain Fracture Toughness and Strain Energy Release Rate of Plastic Materials* (2022).
8. ASTM International, ASTM E399-24, *Standard Test Method for Linear-Elastic Plane-Strain Fracture Toughness of Metallic Materials* (2024).
