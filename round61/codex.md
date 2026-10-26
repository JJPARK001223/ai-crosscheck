# round61 Codex 독립 조사: C202 번호 없는 별행 수식

## 조사 범위와 확인 방법

- 원문: `round61/input/c202.pdf`, 318 PDF쪽. SHA-256: `fef69914754ec5bff529df6567b41c8e0070712406dea1abbd32bc0e1a2e5230`.
- 본문 전체인 PDF 18–190쪽(인쇄쪽 1-1–8-46)을 조사했다. PDF 191쪽부터는 9장 참고문헌이며, 이후 부록은 이 본문 집계에서 제외했다.
- `pdftotext -layout`로 추출한 본문 텍스트의 수식 후보를 확인하고, PyMuPDF 1.27.2.3으로 150dpi 렌더링한 본문 전체를 페이지별 모아보기로 훑었다. 후보와 경계 사례는 해당 쪽 전체 렌더링을 확대 확인했으며, 후보 쪽은 PyMuPDF 텍스트 추출도 대조했다. PDF쪽은 파일의 첫 장을 1로 센다.
- 같은 쪽에서 설명 문단을 사이에 두지 않고 이어지는 여러 줄의 식은 여백이 있더라도 한 묶음으로 세었다. 페이지가 바뀌면 별도 묶음으로 세었다. 식 번호가 여러 줄 전체에 붙은 경우는 전체를 제외했다. 문장에 삽입된 수식과 콜론으로 값을 나열한 글머리표는 별행 수식으로 세지 않았다.
- 상대 AI 결과, round60·round61의 `claude*.md`, 지정된 XLPR HTML은 읽지 않았다. 아래는 원문 전사이며, 모델 해석이나 교정은 하지 않았다.

## 전사

### 1. [인쇄쪽 7-11 / PDF쪽 121, 절 7.3 Direct Model 1]

\[
\begin{aligned}
t &= \Lambda_{cc}\cdot\Lambda_{wc}\cdot g(T,\sigma;Q,n)\\
g &= e^{Q/(RT)}\sigma^{-n}
\end{aligned}
\]

표기 보존: 지수의 분모는 원문 그대로 \(RT\)이다.

### 2. [인쇄쪽 7-12 / PDF쪽 122, 절 7.3 Direct Model 1, 7.3.1 직전]

앞쪽 7-11의 재기재가 이어진다. 같은 쪽의 두 식 블록을 한 묶음으로 적고 블록 사이 여백을 유지했다.

\[
\begin{aligned}
\Lambda_{cc} &= \frac{1}{A_{cc}}\\
A_{cc} &\sim \text{log-N}\left(0,\sigma_{A,cc}\right)\\[1em]
\Lambda_{wc} &= \frac{1}{A_{wc}}\\
A_{wc} &\sim \text{log-N}\left(\mu_{A,wc},\sigma_{A,wc}\right)\\
\mu_{A,wc} &= \mu_{A,N=n}\\
\sigma_{A,wc} &= \sqrt{\sigma_{A,N=n}^{2}-\sigma_{A,cc}^{2}}
\end{aligned}
\]

### 3. [인쇄쪽 7-21 / PDF쪽 131, 절 7.4 Direct Model 2, 7.4.1 직전]

\[
\begin{aligned}
t &= \Lambda_{cc}\cdot\Lambda_{wc}\cdot
g\left(T,\sigma,\sigma_{ys},\sigma_{ult},E;Q,z_1,z_2,v,w,q,a_{dm2},b_{dm2},c_{dm2},k_{dm2}\right)\\
g &= Ge^{Q/RT}\ln\left[\frac{D-z}{\dfrac{\sigma}{\sigma_{ys}}-z}\right]\\[1em]
\Lambda_{cc} &= B_{cc}\\
B_{cc} &\sim \text{log-N}\left(0,\sigma_{B,cc}\right)\\[1em]
\Lambda_{wc} &= B_{wc}\\
B_{wc} &\sim \text{log-N}\left(\mu_{B,wc},\sigma_{B,wc}\right)\\
\mu_{B,wc} &= \mu_{B,N=n}\\
\sigma_{B,wc} &= \sqrt{\sigma_{B,N=n}^{2}-\sigma_{B,cc}^{2}}
\end{aligned}
\]

표기 보존: 원식의 지수 \(Q/RT\) 및 대괄호 안의 중첩 분수는 원문 그대로이다. 다른 쪽의 식에 맞춰 기호를 보충하지 않았다.

### 4. [인쇄쪽 7-27 / PDF쪽 137, 절 7.5 Weibull Model, 7.5.1 직전]

\[
\begin{aligned}
t &= \Lambda_{cc}\cdot g\left(T,\sigma,N;Q,n,T_{ref},\sigma_{ref}\right)\\
g &= \exp\left[\frac{Q}{R}\left(\frac{1}{T}-\frac{1}{T_{ref}}\right)\right]
\left(\frac{\sigma}{\sigma_{ref}}\right)^{-n}N^{1/\beta_{cc}}\\[1em]
\Lambda_{cc} &\sim W\left(\beta_{cc},c_{cc}\right)\\
F_W\left(t;\beta_{cc},c_{cc}\right)
&= 1-\exp\left[-t^{\beta_{cc}}\exp\left(c_{cc}\right)\right]
\end{aligned}
\]

표기 보존: \(R\)에 첨자가 없고 마지막 행의 좌변은 \(F_W\)이다. 모두 원문 그대로이며, \(R_{gas}\)나 \(F_{\Lambda_{cc}}\)로 바꾸지 않았다.

### 5. [인쇄쪽 8-35 / PDF쪽 179, 절 8.4.2.1 Direct Model 1]

번호 있는 식 [8-4] 아래의 `where` 다음에 별행으로 놓인 기호 정의이다. [8-4] 자체는 제외하고, 번호 없이 별행으로 놓인 아래 정의만 포함했다.

\[
\Phi^{-1}=\text{inverse standard normal cumulative distribution function}
\]

## 제외 및 경계 사례

그림·표 영역 제외 쪽(PDF쪽): 그림 영역은 20, 24–25, 59–60, 64, 66, 70, 76, 80, 84, 86, 88–89, 96, 98, 110, 123, 125–130, 132, 134–137, 139–144, 147–148, 151, 154–163, 165–167, 169, 171–173, 177, 182–184, 187–189; 표 영역은 27, 32–36, 39–40, 53–57, 61–62, 69–70, 73, 83, 87–88, 112–116, 174–175에서 제외했다(표의 다음 쪽 계속 부분 포함; 해당 쪽의 표·그림 밖 본문은 별도 조사).

- 특히 PDF 66쪽 Figure 4-3의 응력 합산식, 80쪽 Figure 5-1의 모델식, 84쪽 Figure 5-2의 회귀식, 96쪽 Figure 6-1의 수식·기호는 그림 내부이므로 제외했다. 그래프의 수식형 범례도 그림 내부로 취급했다.
- PDF 102쪽(6-8)의 최적화식과 로그우도식은 설명 문단 없이 이어지며 [6-12]를 공유하는 묶음이다. 공분산과 Fisher 정보 식도 [6-13] 묶음이다. 첫 줄 옆에 번호가 없다는 이유로 이들을 분리 집계하지 않았다. 같은 원칙으로 1장·6장의 다른 번호 있는 여러 줄 식도 제외했다.
- PDF 108쪽(6-14)의 정규분포 표기는 `e.g.,`와 `For a more` 사이의 문장 내 수식이다. 추출 텍스트에서는 위로 분리되어 보이지만 렌더링상 문장에 삽입되어 있어 제외했다.
- PDF 122쪽 이후 여러 쪽에 있는 초모수 추정값 글머리표는 `기호: 값` 형식의 본문 목록이므로 제외했다.
- PDF 179쪽의 정의는 설명 문장 중간에 삽입되지 않고 `where` 다음의 독립된 행으로 놓였으므로 포함했다. 다섯 묶음 중 하나가 수치 모델식이 아니라 이 기호 정의라는 점을 명시한다.

## 판독 상태와 집계

- 사실: 위 다섯 묶음은 본문 내 독립된 행에 놓여 있으며 대괄호 식 번호가 없다.
- 집계상의 판단: 동일 쪽의 연속된 재기재 블록은 하나로 합쳤고, 별행 기호 정의도 포함했다. 이 기준을 적용한 결과이다.
- 확인 불가: 최종 전사에 판독 불명확으로 남은 기호는 없다. 이상으로 보일 수 있는 표기를 다른 식과 맞추어 교정하지 않았으며 위에 '원문 그대로'로 표시했다.

번호 없는 별행 수식 묶음 총 5개

해당 PDF쪽 목록: 121, 122, 131, 137, 179.
