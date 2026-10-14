# Round 28 Claude (blind) output

XLPR 균열성장 수식집
XLPR 균열 성장·합체 수식 정리
EPRI, xLPR Models Subgroup Report — Crack Growth and Coalescence, xLPR-MSGR-CGR Ver.1.0 (저자 K. Schmitt, 2016.06.29) 한 편의 내용만 사용. 쪽수는 원문 인쇄 쪽번호이며 PDF 뷰어 쪽번호는 +1입니다. 번역본 PDF는 만든 적이 없어서 원문(영문)만 근거로 했습니다.
5초 요약
균열이 얼마나 빨리 자라는가는 두 가지 식을 더해서 구합니다. ① PWSCC(물 환경 응력부식, 정하중, 시간 기준 m/s) ② 피로(반복하중, 한 사이클당 m/cycle). 어떤 식을 쓸지는 재료 코드(1~10)가 정합니다. 두 균열이 가까워지면 합체 규칙으로 하나로 합칩니다.
0. 어느 재료에 어떤 식을 쓰나 (원문 Table 3-1, §3.2.1.3)
코드 | 재료 | PWSCC (시간 기준) | 피로 (사이클 기준) | 
1 | Alloy 600 | 식 3-1 (= 식 2-1 값). 수소 효과 끔(P=1) | Ni계 식 2-13/2-14 | 
2 | Alloy 182 / 132 | 식 3-1. 수소 효과 끔 = 식 2-2 값, 켬 = 식 2-3 값 | Ni계 식 2-13/2-14 (용접부 f=2.0) | 
3 | Alloy 82 | 식 3-1, 개선계수 IF = 2.6 (Alloy 82에서만 확정될 때) | Ni계 (용접부 f=2.0) | 
4 | Alloy 690 | 합의된 모델 없음, 값 미제공 (α=0이면 끔) | Ni계 (f=1) | 
5 | Alloy 52 / 152 | 합의된 모델 없음, 값 미제공 | Ni계 (용접부 f=2.0) | 
6 · 7 · 8 | 304 또는 316L / 316 / 304L·304LE 스테인리스와 용접부 | 정상 PWR에서 SCC 민감하지 않다고 보아 모델 없음 | 오스테나이트 식 2-19 | 
9 | 페라이트강(CS/LAS), 용접부, 모재 HAZ | SCC 모델 없음 | 페라이트 식 2-23 (TCF / EAC 분기) | 
10 | 사용자 정의 재료 | 식 3-2 (수소·IF 없음) | 식 3-3 | 
메커니즘 플래그 Imechanism: 1 = PWSCC+피로 합산(기본), 2 = PWSCC만, 3 = 피로만. 최종 성장률 = PWSCC 성장률 + 활성 천이(transient)별 피로 성장률의 합입니다(p.62, p.73).
2-12-22-3~2-72-8
2-9~2-122-13~2-182-19~2-222-23~2-27
§2.43-1~3-3§4 합체6-1·6-2하첨자 사전파라미터 표
1. PWSCC 성장 모델 (원문 §2.2)
PWSCC식 2-1 · Alloy 600 균열 성장 속도
p.21 · §2.2.1.1
K가 문턱값을 넘으면, 온도가 높고 K가 클수록 균열이 빨리 자란다. 문턱 이하면 0.
[EQ] \dot a=\begin{cases}\exp\!\left[-\dfrac{Q_g}{R_{gas}}\left(\dfrac1T-\dfrac1{T_{ref}}\right)\right]\alpha\,f_{heat}\,f_{wh}\,(K-K_{th})^{\beta}&K>K_{th}\\[6pt]0&K\le K_{th}\end{cases}
기호 | 의미 | 하첨자 읽는 법 | 
ȧ | 균열 성장 속도 (CGR), m/s | a 위의 점 = 시간미분 da/dt | 
Qg | 균열 성장의 열활성화 에너지, kJ/mol | g = growth(균열 성장) | 
Rgas | 기체상수 | gas = 기체 | 
T, Tref | 균열 위치의 절대온도, 기준 절대온도(325°C) | ref = reference(기준) | 
α | 전체 크기를 맞추는 상수 (m/s)/(MPa√m)β | - | 
fheat | 같은 용해 로트(heat)에서 만든 시편 전체에 공통인 민감도 보정 | heat = 용해 로트 (heat-to-heat 변동) | 
fwh | 같은 heat 안에서 시편마다 다른 변동 | wh = within-heat | 
K, Kth | 균열선단 응력확대계수(Mode I), 그 문턱값, MPa√m | th = threshold | 
β | K에 대한 거듭제곱 지수 | - | 
왜 이 식을 쓰나
MRP-55에서 국제 전문가 패널이 합의한 형태. K 의존성은 Scott 식에서, 온도 의존성은 열활성화 과정의 아레니우스 식에서 가져옴.
158개 실험실 측정(26개 heat)으로 보정. 결정론적 75번째 백분위 곡선은 ASME Sec. XI 비의무부록 C, O에 채택됨.
언제 쓰나
두꺼운 벽의 단조(wrought) Alloy 600에서 PWSCC가 진행 중일 때.
검증 범위: K 10~80 MPa√m, 280~350°C. 근거 데이터는 K ≥ 약 15 MPa√m라서 낮은 K에서는 주의.
대표 값
Qg = 130 kJ/mol (정규분포, 표준편차 5) · Tref = 325°C
α = 1.34E-12 (중앙값 기준; 결정론 75% 값은 2.67E-12) · β = 1.16 · Kth = 9
fheat: 대수정규, 중앙값 1, 5%=0.19, 95%=5.32 (epistemic)
fwh: 대수정규, 중앙값 1, 5%=0.39, 95%=2.55 (aleatory)
Alloy 600의 수소 효과 모델은 이 보고서가 제시하지 않음(수소 효과가 82/182/132보다 작고 우선순위가 낮다고 서술). 아연 첨가 효과도 데이터가 엇갈려 성장식에는 넣지 않음(균열 발생 모델에만 반영).
PWSCC식 2-2 · Alloy 82/182/132 (수소 효과 제외)
p.27 · §2.2.2.1
식 2-1과 같은 틀인데, 용접부라서 “용접 로트·용접 내 위치·합금·방향” 보정이 붙는다.
[EQ] \dot a=\begin{cases}\exp\!\left[-\dfrac{Q_g}{R_{gas}}\left(\dfrac1T-\dfrac1{T_{ref}}\right)\right]\alpha\,f_{weld}\,f_{ww}\,f_{alloy}\,f_{orient}\,(K-K_{th})^{\beta}&K>K_{th}\\[6pt]0&K\le K_{th}\end{cases}
기호 | 의미 | 하첨자 읽는 법 | 
fweld | 용접마다 공통인 보정(용접봉 로트, 용접 시공 차이) | weld = 개별 용접부 (weld-to-weld 변동) | 
fww | 한 용접 안에서 위치별 변동 | ww = within-weld | 
falloy | 합금 보정. Alloy 82는 Cr이 높아 덜 민감 | alloy = 합금 종류 | 
forient | 균열 방향 보정 (덴드라이트와 평행 / 수직) | orient = orientation | 
그 외 | 식 2-1과 동일 (Qg, Rgas, T, Tref, α, K, Kth, β) |  | 
왜 이 식을 쓰나
MRP-115(2004). MRP-55의 K 거듭제곱 항과 아레니우스 항을 그대로 채택, 77개 측정(19개 시험 용접)으로 보정.
데이터가 부족해 0이 아닌 K 문턱값은 넣지 않음.
언제 쓰나
Alloy 82/182/132 용접금속(J-groove, 이종금속 맞대기 용접)의 PWSCC, 수소 효과를 고려하지 않을 때.
falloy = 1 (182/132), 0.385 (Alloy 82, 개선계수 2.6). Alloy 82에만 쓰는 경우는 PWSCC가 Alloy 82 안에만 있다고 확인될 때뿐.
forient: 평행 1, 수직 0.5. 실제로는 덴드라이트 방향을 모르므로 모델에서 쓰지 않음.
대표 값
Qg = 130 kJ/mol (표준편차 20) · α = 9.82E-13 · β = 1.6 · Kth = 0
fweld: 대수정규, 5%=0.38, 95%=2.64 (epistemic)
fww: 대수정규, 5%=0.45, 95%=2.20 (aleatory)
결정론 75% α = 1.5E-12
PWSCC식 2-3 ~ 2-7 · 용존수소 효과를 넣은 Alloy 82/182/132
p.33–34 · §2.2.3.1
식 2-2에 수소 보정 fH2를 곱한다. 수소 농도가 Ni/NiO 전이점에 가까울수록 성장이 가장 빠르고, 양쪽으로 멀어질수록 느려진다.
[EQ] \dot a=f_{H_2}\left(\exp\!\left[-\dfrac{Q_g}{R_{gas}}\left(\dfrac1T-\dfrac1{T_{ref}}\right)\right]\alpha f_{weld}f_{ww}f_{alloy}f_{orient}(K-K_{th})^{\beta}\right)
[EQ] f_{H_2}=\frac1P+\frac{P-1}{P}\exp\!\left[-0.5\left(\frac{\Delta ECP_{Ni/NiO}}{c}\right)^{2}\right]
[EQ] \Delta ECP_{Ni/NiO}=29.58\,[\mathrm{mV}]\cdot\frac{T}{298.15\,[\mathrm K]}\,\log\frac{[H_2]}{[H_2]_{Ni/NiO}}
[EQ] [H_2]_{Ni/NiO}=10^{(0.0111\,T-2.59)}
[EQ] CGR=CGR_{max}\left[\frac1P+\frac{P-1}{P}\exp\!\left[-0.5\left(\frac{\Delta ECP_{Ni/NiO}}{c}\right)^{2}\right]\right]
기호 | 의미 | 하첨자 읽는 법 | 
fH2 | 수소 보정 계수 (Ni/NiO 전이점에서 1, 멀면 1/P) | H2 = 수소 | 
ΔECPNi/NiO | 현재 수소 농도에서의 전기화학 부식전위(ECP)와 Ni/NiO 전이 전위의 차, mV | Ni/NiO = 니켈 금속과 산화니켈의 평형 전이 | 
P | peak-to-valley 비. 전이점 성장속도 ÷ 전이점에서 멀리 떨어진 곳의 성장속도 | - | 
c | peak width, mV. ΔECP = c일 때 (최댓값−점근값) 차이의 약 40% 감소 | - | 
[H2] | 1차수 용존수소 농도, cc(STP)/kg | - | 
[H2]Ni/NiO | 그 온도에서 Ni/NiO 전이에 해당하는 수소 농도 | Ni/NiO = 위와 같음 | 
T | 식 2-5는 절대온도(K), 식 2-6은 섭씨(모듈 식 3-1에서 TC로 구분) | C = Celsius | 
왜 이 식을 쓰나
PWSCC 성장이 Ni/NiO 전이에서 멀어지면 줄어드는 현상을 반영. 수소 농도를 높여 PWSCC를 완화하는 방안의 연구가 가능.
MRP-263/MRP-307에서 개발. 가우스형 ECP 의존성.
수소 효과를 빼면 활성화 에너지에 ECP 변화분이 섞여 들어감(“겉보기 활성화 에너지”).
언제 쓰나
82/182/132에서 수소 농도 변화를 반영할 때. 이때 Qg는 “실제 활성화 에너지” 104 kJ/mol을 사용.
검증 범위: K 10~80, 280~350°C, 수소 약 1~60 cc/kg (ECP −50~+50 mV).
파라미터는 Alloy 182/132 데이터 기반. Alloy 82는 피크 위치 어긋남이 있어 추가 시험 필요.
대표 값
Qg = 104 kJ/mol (표준편차 20) · α = 2.01E-12 · β = 1.6 · Kth = 0
P: 이동 대수정규(P−1이 대수정규), 중앙값 92.8, 5%=1.0, 95%=8462
c: 정규분포, 평균 18.2 mV, 표준편차 5.5 mV (P와 상관계수 0.714)
fweld 5%=0.45, 95%=2.24 · fww 5%=0.54, 95%=1.85
P(peak-to-valley 비)는 독립 데이터로 검증하지 못했다고 원문에 명시되어 있음(p.37).
PWSCC식 2-8 · 그 밖의 재료용 일반 SCC 식
p.38 · §2.2.4.2
모델이 없는 재료에 사용자가 직접 값을 넣어 쓰는 빈 틀.
[EQ] \dot a=\begin{cases}\alpha\,f_{comp}\,f_{flaw}\,(K-K_{th})^{\beta}\exp\!\left[-\dfrac{Q_g}{R_{gas}}\left(\dfrac1T-\dfrac1{T_{ref}}\right)\right]&K>K_{th}\\[6pt]0&K\le K_{th}\end{cases}
기호 | 의미 | 하첨자 읽는 법 | 
fcomp | 부품(재료 그룹)마다 다른 변동 | comp = component-to-component | 
fflaw | 한 부품 안에서 결함 위치마다 다른 변동 | flaw = flaw-to-flaw (within-component) | 
언제 쓰나
오스테나이트 스테인리스, 페라이트강은 정상 PWR 환경에서 SCC에 민감하지 않다고 보아 이 보고서는 모델을 만들지 않음. 필요하면 이 틀에 값을 넣음.
fcomp, fflaw는 식 2-3의 fweld, fww에 대응(p.72).
2. 피로 성장 모델 (원문 §2.3)
피로 공통식 2-9 ~ 2-12 · ΔK, 하중비 R, 피로 문턱값 ΔKth
p.39–40 · §2.3.1
한 사이클의 K 폭(ΔK)과 최소/최대 비(R)를 정하고, 그 아래에서는 피로로 안 자라는 문턱값을 둔다. 세 재료군(Ni계, 오스테나이트, 페라이트)이 같은 문턱 식을 공유합니다.
[EQ] \Delta K=\begin{cases}K_{max}-K_{min}&K_{max}>0\\0&K_{max}\le0\end{cases}
[EQ] R=\begin{cases}K_{min}/K_{max}&K_{min}>0\\0&K_{min}\le0\end{cases}
[EQ] \Delta K_{th}=C_{Kth}\cdot5.5\cdot(1-0.8R)\quad[\mathrm{MPa\sqrt m}]
[EQ] \Delta K_{th}=7.0\cdot(1-0.693R)\quad(R\ge0.10,\ 28\ \text{points})
기호 | 의미 | 하첨자 읽는 법 | 
Kmax, Kmin | 한 사이클의 최대, 최소 응력확대계수 | max / min | 
ΔK | 응력확대계수 범위. 압축-압축 사이클은 0이라 성장 없음. 대부분 압축이어도 인장 구간이 있으면 성장 가능 | Δ = 범위 | 
R | 하중비 | - | 
ΔKth | 피로 성장이 무시되는 ΔK 문턱값 | th = threshold | 
CKth | 문턱값 척도 상수. 1이면 ASME Code Case N-643-2 곡선(보수적으로 낮음) | Kth = ΔK threshold용 상수 | 
왜 이 식을 쓰나
식 2-9, 2-10은 ASME Sec. XI Appendix A(경수로 환경) 규정을 따름.
식 2-11은 N-643-2 형태. 식 2-12 자료로 보면 N-643-2는 낮은 R에서 약 30%, 높은 R에서 2배 낮게 예측해서 CKth로 보정.
언제 쓰나
모든 피로 계산 전 단계. Ni계, 오스테나이트, 페라이트 모두 이 한 식을 사용(Ni계는 데이터가 적어 같은 식을 선택).
공칭 온도는 사이클의 평균(플래그 1), 최소(2), 최대(3) 중 사용자 선택.
대표 값
CKth: 대수정규, 중앙값 1.27, 5%=1.01, 95%=1.60 (log-σ 0.139)
상한 절단 +3σ = 중앙값의 1.517배 (= 1.927)
보수적으로 쓰려면 중앙값 1.0. 시뮬레이션당 1회 샘플링, epistemic.
피로 · Ni계식 2-13 ~ 2-18 · Alloy 600/690 및 용접금속
p.42–44 · §2.3.2
공기 중 피로 속도에 “환경이 얼마나 더 빠르게 만드는가” 항을 더한다. 환경 영향은 하중 상승 시간이 길수록 커진다.
[EQ] \frac{da}{dN}=\left.\frac{da}{dN}\right|_{air}+A_{env}\left(\left.\frac{da}{dN}\right|_{air}\right)^{n_{env}}\tau_r^{\,1-n_{env}}
[EQ] \left.\frac{da}{dN}\right|_{air}=C_{Ni}\,f_{alloy}\,F_T\,F_R\,(\Delta K)^{n_{Ni}}
[EQ] f_{alloy}=\begin{cases}1&\text{Alloy 600, 690}\\f_{Ni,weld}&\text{Alloy 182/132/82, 152/52}\end{cases}
[EQ] F_R=(1-b\,R)^{-p}
[EQ] F_T=4.835\times10^{-14}+(1.622\times10^{-16})T-(1.490\times10^{-18})T^2+(4.355\times10^{-21})T^3
[EQ] F_T=5.423\times10^{-14}+(1.830\times10^{-16})T-(1.725\times10^{-18})T^2+(5.490\times10^{-21})T^3
기호 | 의미 | 하첨자 읽는 법 | 
da/dN | 환경을 포함한 사이클당 성장량, m/cycle | N = 사이클 수 | 
(da/dN)air | 공기 중 사이클당 성장량 | air = 공기 중 | 
Aenv, nenv | 환경 계수, 환경 지수 | env = environment(환경) | 
τr | 천이 성분의 하중 상승 시간, s | r = rise (상승) | 
CNi, nNi | Ni계 척도 상수, Paris 지수 | Ni = 니켈계 합금 | 
falloy, fNi,weld | 합금 보정(용접부 계수) | weld = 용접금속 | 
FR, FT | 하중비 효과, 온도 효과 | R = 하중비, T = 온도 | 
b, p | 하중비 효과의 계수와 지수 | - | 
왜 이 식을 쓰나
NUREG/CR-6721의 방대한 데이터(공기, 모의 PWR 환경)를 그대로 표현. Paris 거듭법칙 + 하중비 + 온도 + 합금.
환경 효과는 공기 중 속도가 작을 때(약 1E-9 m/s 미만) 더 크게 나타남.
용접부(Alloy 182)는 공기 중에서 Alloy 600의 약 2배 → f=2.0.
언제 쓰나
재료 코드 1~5, 피로 메커니즘이 켜졌을 때.
FT는 Alloy 600과 82/182/132에 식 2-17, Alloy 690과 52/152에 식 2-18.
Alloy 690은 약 60개 시험이라 Paris 지수와 하중비 효과는 재추정하지 못하고 온도 효과만 다시 구함. 690 계열에서는 환경 증폭이 관찰되지 않았다는 제한된 데이터가 있음.
대표 값
nNi = 4.1 (측정 범위 3.5~5.5) · b = 0.82 · p = 2.2 · fNi,weld = 2.0
CNi: 대수정규, 중앙값 1, 5%=0.51, 95%=1.96 (log-σ 0.408)
Aenv 중앙값 4.4E-7 (m/cyc-s)1−0.33, log-μ −14.6, log-σ 1.2
nenv = 0.33 (NUREG/CR-6721), MHI 데이터 검증에서 0.25가 더 맞음 → 입력 0.25~0.33 균일분포
식 2-17, 2-18의 T 단위는 해당 식 주변에 명시되어 있지 않습니다(원문 확인 필요). 원문 본문은 시험 온도 범위를 °C로 서술합니다.
피로 · 오스테나이트식 2-19 ~ 2-22 · 304 / 304L / 316 / 316L 스테인리스
p.48–49 · §2.3.3
Paris 식에 온도·하중비·상승시간·합금 4개 보정을 곱한다. 공기와 환경을 따로 나누지 않고 모두 한 식에 합쳤다.
[EQ] \frac{da}{dN}=C_{SS}\cdot f_{alloy}\cdot F_\tau\cdot F_R\cdot F_T\cdot(\Delta K)^{n_{SS}}
[EQ] F_T=e^{-2516/T}\max\{1.0,\;3.39\times10^{5}\,e^{-0.0301\,T}\}\quad(T\ \text{in K})
[EQ] F_R=\begin{cases}\begin{cases}1&R\le0.7\\1+1.5(R-0.7)&R>0.7\end{cases}&\text{304L, 304LE, 316L}\\[8pt]1+e^{8.02(R-0.748)}&\text{304 or 316}\end{cases}
[EQ] F_\tau=\tau_r^{\,0.3},\qquad\tau_{r,limit}=\begin{cases}1&\tau_r2000\end{cases}
원문은 위처럼 Fτ = τr0.3과 τr,limit 정의를 따로 적었습니다. 본문 설명("1초와 2000초로 절단")에 따라 실제 계산에는 절단된 τr,limit을 넣는 것으로 읽힙니다.
기호 | 의미 | 하첨자 읽는 법 | 
CSS, nSS | 척도 상수, Paris 지수 (n = 2.25) | SS = stainless steel | 
falloy | 합금 계수 (단위 [m/cyc-s0.3]/[MPa√m]2.25). 전체 크기를 실험에 맞추고 합금을 구분 | alloy | 
Fτ | 하중 상승 시간 효과 (지수 0.3) | τ = 하중 상승 시간(rise time) | 
FR, FT | 하중비 효과, 온도 효과 | R, T | 
τr,limit | 1초~2000초로 잘라낸 상승 시간 | limit = 제한(절단)값 | 
왜 이 식을 쓰나
ASME Code Case N-809(작성 중) 해석 기반. Mills의 방대한 시험 데이터(635점)와 일치.
온도: 약 150~325°C에서 온도가 오르면 속도 증가, 약 90~150°C에서는 오히려 온도가 내려가면 증가(원인 미규명) → max 항.
하중비: 탄소 함량이 높은 304/316은 R>0.5부터 크게 증가, 저탄소(304L/316L)는 완만.
언제 쓰나
재료 코드 6, 7, 8(스테인리스와 용접금속)에서 피로가 켜졌을 때, 탈기수(DO ≲ 2 ppb) 환경.
시험 범위: 실온~371°C, 상승시간 1~30,000 s, R 0.1~0.95.
316NG, 316LN, 주조재(CF8, CF8M, CF3, CF3M)도 검증됨.
대표 값
falloy: 304L·304LE = 1.39E-8, 304·316L = 9.10E-9, 316 = 7.28E-9
CSS: 대수정규, 중앙값 1, 5%=0.5, 95%=2.0 (log-σ 0.42)
NUREG/CR-2189 모델과 비교: xLPR이 같거나 더 높게 예측(보수적).
식 2-21은 316L을 저탄소 그룹에, falloy(2-3-3절)는 316L을 304와 같은 값에 묶어 원문 표기가 서로 다릅니다. 원문 그대로 옮겼습니다. 개정 사항은 §6.2.1(식 6-1) 참고.
피로 · 페라이트식 2-23 ~ 2-27 · 탄소강, 저합금강 (TCF / EAC 분기)
p.52–56 · §2.3.4
식은 하나인데 계수 3개(Cenv, nfer, nR)를 상황에 따라 바꾼다. 상황 = 황 함량, 균열 속도, 하중 상승 시간, ΔK 크기.
[EQ] \frac{da}{dN}=C_{env}\left[\frac{\Delta K}{(2.88-R)^{n_R}}\right]^{n_{fer}}
[EQ] V_{trans}=\begin{cases}5.1\times10^{-7}\ \mathrm{mm/s}&a\le2.5\ \mathrm{mm}\\5.1\times10^{-7}\ \mathrm{mm/s}\cdot(2.5\ \mathrm{mm}/a)&a>2.5\ \mathrm{mm}\end{cases}
[EQ] \Delta K_c=\left(\frac{C_{upper}}{C_1}\right)^{2.122}\theta^{0.326}\,(2.88-R)
[EQ] \Delta K_b=C_{K_b}\cdot\theta^{0.326}\cdot(2.88-R)^{2.69}
[EQ] C_{upper}=C_{EAC}\cdot(\Delta K_b)^{2.122}\,(2.88-R)^{-5.702}
기호 | 의미 | 하첨자 읽는 법 | 
Cenv | 환경 계수. 상황에 따라 C1/C2/C3/Cupper 중 하나 | env = 환경 | 
nfer, nR | Paris 지수, 황 의존 하중비 지수 | fer = ferritic | 
C1 / C2 / C3 | TCF 환경계수 / 중간 황 EAC / 높은 황 EAC | 1·2·3 = 레짐 번호 (표 2-1) | 
CEAC, Cupper | 높은 황 EAC의 계수 / 상부 천이 구간의 계수 | upper = 상부 천이 | 
Vtrans | EAC로 넘어가기 위한 임계 균열 속도 | trans = transition | 
ΔKb, ΔKc | EAC→TCF 복귀가 시작되는 ΔK, 완전히 TCF로 복귀하는 ΔK | b = 시작점, c = 복귀 완료점 | 
CKb | ΔKb 척도 상수 | Kb = ΔKb용 상수 | 
θ, S, a | 하중 상승 시간(앞 절의 τr과 같은 양), 황 함량(%wt), 균열 깊이 | - | 
레짐 (원문 표 2-1) | Cenv | nfer | nR | 
공기 | 7.87E-11 | 3.07 | 1 | 
TCF (진성 부식피로) | 2.76E-10 | 3.07 | 1 | 
EAC, 중간 황(0.004~0.013%) | 1.17E-9 | 3.07 | 1 | 
EAC, 높은 황(>0.013%) | 1.42E-7 | 3.07 | 2.166 | 
높은 황 EAC의 상부 천이 (ΔKb ~ ΔKc) | 식 2-27 | 0.948 | 1 | 
TCF로 가는 조건 (하나라도 해당)
황 < 0.004%wt
PWSCC+피로 성장 속도 합 < Vtrans
Vtrans보다 빠르게 자란 누적 길이 < 0.33 mm (연속일 필요 없음)
황 < 0.013%이고 상승 시간 ≤ 1 s (EAC 유지 불가)
ΔK ≥ ΔKc (아주 공격적인 하중이면 TCF 곡선으로 복귀)
EAC로 가는 조건
위 조건에 하나도 해당하지 않으면 EAC.
중간 황 → C2 (1.17E-9), 높은 황 → C3 (1.42E-7, nR = 2.166).
높은 황에서 ΔKb < ΔK < ΔKc이면 Cupper, n = 0.948 (선형 천이).
EAC는 시간이력에 의존해 모듈이 균열 끝점마다 상태를 기억함.
왜 이 식을 쓰나 · 대표 값
ASME Code Case N-643-2와 일치. 온도 효과는 넣지 않고 불확실성에 흡수.
C1 (TCF): 대수정규, 로그평균 −22.01, log-σ 0.467. 공기의 약 3.5배.
C2: 로그평균 −20.6, log-σ 0.88 · C3: 로그평균 −15.8, log-σ 0.88 (둘 다 하한은 샘플된 C1)
CKb: 중앙값 0.498, 5%=0.35, 95%=0.70
식 2-25의 지수 2.122는 원문 표기를 그대로 옮긴 것입니다. 식 2-27로 두 곡선의 교차점을 직접 풀어 보면 지수가 1/2.122가 되는 것으로 보여, 원문 오기인지는 확인하지 못했습니다(제 추정이며 검증 전). 계산에 쓰실 때는 원문과 구현 코드를 확인하세요.
3. 시간 적분과 균열 모양 (원문 §2.4)
공통시간 적분 규칙과 합산
p.61–62 · §2.4.1
매 시간 스텝마다 “지금 상태”로 성장률을 구하고 그만큼 자란 것으로 갱신한다. 번호가 붙은 식은 없고 서술만 있습니다.
[EQ] a(t+\Delta t)=a(t)+\dot a_{net}\,\Delta t,\qquad \dot a_{net}=\dot a_{PWSCC}+\sum_{i=1}^{N_{TS}}\dot a_{fat,i},\qquad \dot a_{fat,i}=\frac{da}{dN}\Big|_i\cdot\frac{N_{cyc,i}}{\Delta t}
기호 | 의미 | 하첨자 읽는 법 | 
Δt | 시간 스텝 길이 (공칭 1 유효전출력개월) | - | 
NTS | 활성 천이 성분의 수 (1~20) | TS = transient(s) | 
Ncyc | 이번 스텝 동안의 천이 성분별 사이클 수 | cyc = cycles | 
이렇게 하는 이유
PWSCC 식은 K가 균열 모양과 크기의 비선형 함수라 비선형 상미분방정식. 명시적 고정 스텝 전진 오일러법으로 푼다.
몬테카를로 시뮬레이션에서는 고정밀 적분이 결정론 해석만큼 중요하지 않다고 서술.
PWSCC와 피로는 서로 독립이라 가정하고 단순 합산(ASME Sec. XI 지침과 일치).
균열 모양 3종과 계산 위치
표면균열: 대칭 반타원, 깊이 < 두께. 가장 깊은 점과 표면 끝 2점에서 성장 계산.
천이 관통균열: 대칭 사다리꼴(깊이 = 두께, OD 길이 < ID 길이). ID 끝 2점 + OD 끝 2점.
이상화 관통균열: ID와 OD 길이가 같음.
특수 규칙
이종금속 용접에서 표면 끝이 모재에 닿거나 인레이/온레이로 표면 쪽 성장이 막히면, 가장 깊은 점의 K를 계산할 때 (반길이/깊이)를 최소 1로 제한.
4. 모듈에서 실제로 쓰는 식 (원문 §3.2.1.3)
PWSCC식 3-1 · 모든 재료 공통 PWSCC 식 (수소·개선계수 포함)
p.72 · §3.2.1.3
식 2-1, 2-2, 2-3을 한 식으로 합친 구현용 식. 재료마다 “값”만 바꾼다.
[EQ] \dot a_{PWSCC}=\begin{cases}\dfrac1{IF}\,\alpha f_{comp}f_{flaw}\,e^{-\frac{Q_g}{R_{gas}}\left(\frac1T-\frac1{T_{ref}}\right)}(K-K_{th})^{\beta}\left[\dfrac1P+\dfrac{P-1}{P}\exp\!\left(-0.5\left(\dfrac{\Delta ECP_{Ni/NiO}}{c}\right)^{2}\right)\right]&K>K_{th}\\[10pt]0&K\le K_{th}\end{cases}
[EQ] \Delta ECP_{Ni/NiO}=29.58\,\frac{T}{298.15}\log_{10}\!\left(\frac{[H_2]}{10^{(0.0111\,T_C-2.59)}}\right),\qquad T=T_C+273.15,\quad T_{ref}=T_{ref,C}+273.15
기호 | 의미 | 하첨자 읽는 법 | 
IF | 개선계수. PWSCC 성장을 1/IF로 줄임 (예: Alloy 82는 2.6) | IF = improvement factor | 
fcomp, fflaw | 식 2-3의 fweld, fww에 해당 (샘플 빈도: heat별 / 하위 구간(subunit)별) | comp = 부품 간, flaw = 결함 간 | 
TC, Tref,C | 섭씨 입력 온도와 기준온도 | C = Celsius | 
언제 쓰나
재료 코드 1~9에서 PWSCC가 켜졌을 때(커스텀 10 제외). 식 2-1(Alloy 600), 2-2(82/182/132 수소 없음), 2-3(수소 있음)을 모두 이 식에서 값만 바꿔 재현.
수소 효과 끄기: P = 1. 개선 효과 끄기: IF = 1. PWSCC 끄기: 메커니즘 플래그 3 또는 α = 0.
값 설정 요령
falloy·forient 대신 IF로 합금 보정을 넣는다.
Alloy 600: P = 1, IF = 1. Alloy 82/182/132: 수소 없음 쓰려면 P = 1.
모듈 내부에서는 수소 보정을 이 한 식에서 바로 계산.
PWSCC · 사용자식 3-2 · 커스텀 재료 PWSCC
p.72
식 3-1에서 수소와 개선계수를 뺀 형태.
[EQ] \dot a_{PWSCC}=\begin{cases}\alpha f_{comp}f_{flaw}\,e^{-\frac{Q_g}{R_{gas}}\left(\frac1T-\frac1{T_{ref}}\right)}(K-K_{th})^{\beta}&K>K_{th}\\0&K\le K_{th}\end{cases}
재료 코드 10에서만 사용. 사용자가 α, β 등을 직접 입력.
피로 · 사용자식 3-3 · 커스텀 재료 피로
p.73
사용자가 정한 5개 파라미터로 Paris형 피로 식을 만든다.
[EQ] \frac{da}{dN}=C_{cstm}\,\tau_R^{\,p_{cstm}}\left(\frac{\Delta K}{(1-a_{cstm}R)^{b_{cstm}}}\right)^{m_{cstm}}
기호 | 의미 | 하첨자 읽는 법 | 
Ccstm | 전체 척도 상수 (불확실성을 분포로 넣을 수 있음) | cstm = custom(사용자 정의) | 
pcstm | 상승 시간 지수 |  | 
acstm, bcstm | 하중비 상수와 하중비 지수 | (식 속의 a는 균열 깊이가 아니라 상수) | 
mcstm | Paris 지수 |  | 
Ni계·스테인리스·페라이트 모델이 맞지 않는 재료에서만 사용.
5. 균열 합체 모델 (원문 §4)
합체수식 없는 규칙 모음: 언제 합치고, 합친 뒤 모양은?
p.92–99 · §4.1–4.2
두 균열 사이의 가장 짧은 ID 쪽 연결부(ligament)가 “합체 거리”보다 짧아지면 두 균열을 한 균열로 바꾼다. 두 개씩 짝지어(pairwise) 적용합니다.
짝 | 합체 거리 (언제 합치나) | 물리적 이유 | 
표면 + 표면 | (1) 사용자 지정 절대거리, 또는 (2) 최대 깊이 × 계수 (권장). 계수 0~0.75, 최적 0.5 → 삼각분포(최소 0, 최빈 0.5, 최대 0.75) | 균열 간섭으로 K가 증폭. ASME Sec. XI IWA-3000도 최대 깊이의 1/2 미만 간격은 합쳐서 평가하도록 요구 | 
관통 + 관통 | 사용자 지정값. 가능한 범위 0~20 in, 균열 길이와 거의 1:1로 잡는 것이 해석 결과와 맞음 | 사이 ligament의 소성 붕괴 | 
표면 + 관통 | 기본 0 | ASME 규정도 없고 진짜 ligament도 없음 | 
합친 뒤 속성 | 규칙 | 
균열 종류 | 표면+표면 → 표면 · 천이+천이 → 천이 · 이상화 관통+이상화 관통 → 이상화 관통 · 종류가 다르면 → 천이 관통 | 
깊이 | 관통이 하나라도 있으면 두께. 표면+표면은 최소/최대/평균 중 선택, 최대 깊이 권장(재진입 구간의 K 증폭 때문) | 
중심 | 두 균열의 ID 길이를 감싸는 호의 중심 | 
OD 길이 | 두 균열의 OD 길이를 감싸는 호의 길이. 표면+표면이면 0, 표면+관통이면 그 관통균열의 OD 길이 | 
ID 길이 | 같은 종류 둘은 ID 길이를 감싸는 호의 길이. 표면+관통은 합친 균열의 면적 = 원래 두 균열 면적의 합이 되도록 설정(안정성 예측의 연속성) | 
이 모델의 전제
규칙 기반(역학 계산 대체). 1~3 mm 이상의 이미 성장 중인 큰 균열만 대상이며, 미세균열(micro-fissure) 합체는 범위 밖.
모든 원주방향 균열은 같은 평면(coplanar)이라고 가정.
축방향 균열은 합체 계산에서 제외. 원주 구간마다 의미 있는 축방향 균열은 최대 1개.
검증 데이터는 평판 형상. 반경이 작은 부품은 곡률의 영향이 불확실.
모듈 플래그 (§5)
Coalescence Direction flag, Surface Crack Coalescence Distance Rule flag(1 = 절대거리, 2 = 최대 깊이 비율), Depth Rule flag를 입력으로 받음.
6. 향후 개정 식 (원문 §6.2)
개정 예정식 6-1, 6-2 · 오스테나이트 합금 계수 개정 / Ni계 환경계수 산포
p.119 · §6.2.1–6.2.2
실제 모듈이 쓰는 값이 아니라, 모듈 구현 후 바뀐 Code Case N-809와 향후 개선안.
[EQ] f_{alloy}=\begin{cases}9.10\times10^{-9}&304,\ 316\\1.39\times10^{-8}&304L,\ 316L,\ 304LE\end{cases}
[EQ] \text{log-}\sigma=\begin{cases}0&CGR_{air}>10^{-8}\\-2.4-0.3\log_{10}(CGR_{air})&10^{-12}
식 6-1: 합금 그룹을 304·316과 304L·316L·304LE 두 개로 바꾸고, 식 2-22의 상승 시간 상한 2000 s를 없앰.
식 6-2: Aenv의 산포(log-σ)를 공기 중 성장 속도에 따라 변하게 하는 개선안. xLPR 2.0에서는 구현 불가라 고정값 1.2를 사용.
부록 A. 하첨자 사전 (알파벳 순, 원문 Nomenclature p.xi–xiii 기준)
하첨자 | 풀어 쓴 말 | 쓰이는 기호 | 
air | 공기 중 | (da/dN)air | 
alloy | 합금 종류 | falloy | 
b, c (ΔK) | EAC→TCF 복귀 시작점 / 복귀 완료점 | ΔKb, ΔKc | 
C (온도) | 섭씨 | TC, Tref,C | 
comp | component-to-component, 부품 간 변동 | fcomp | 
cstm | custom, 사용자 정의 재료 | C, p, a, b, mcstm | 
cyc | 사이클 | Ncyc | 
EAC | 환경 보조 균열(environmentally assisted cracking), 속도가 크게 증가한 레짐 | CEAC | 
env | 환경 | Aenv, nenv, Cenv | 
fer | 페라이트강 | nfer | 
flaw | 결함 간 변동 (부품 내) | fflaw | 
g | (균열) 성장 (growth) | Qg | 
gas | 기체 | Rgas | 
H2 | 수소 | fH2, [H2] | 
heat | 용해 로트 (heat-to-heat) | fheat | 
Kth, Kb | ΔK 문턱값용 상수, ΔKb용 상수 | CKth, CKb | 
limit | 절단(제한)값 | τr,limit | 
max, min | 사이클의 최대, 최소 | Kmax, Kmin, CGRmax | 
Ni | 니켈계 합금 | CNi, nNi | 
Ni/NiO | 니켈 금속 / 산화니켈 평형 전이 | ΔECPNi/NiO, [H2]Ni/NiO | 
orient | 균열 방향 | forient | 
r | rise, 하중 상승 | τr | 
R | 하중비 (효과 · 지수) | FR, nR | 
ref | 기준값 | Tref | 
SS | 스테인리스강 | CSS, nSS | 
T, τ | 온도 효과, 상승 시간 효과 | FT, Fτ | 
TCF | 진성 부식피로(true corrosion fatigue), 환경 영향이 작은 레짐 | C1 | 
th | 문턱값 | Kth, ΔKth | 
tip, material, mechanism, Temp | 균열 끝점 번호 / 재료 그룹 / 메커니즘 플래그 / 공칭 온도 플래그 (모듈 입력용 지수 I) | Itip, Imaterial, Imechanism, ITemp | 
trans | 천이 (EAC 진입 임계 속도) | Vtrans | 
TS | 천이 성분 (transient) | NTS | 
upper | 상부 천이 구간 | Cupper | 
weld / ww | 용접 간 / 용접 내 변동 | fweld, fww | 
wh | within-heat, 같은 heat 안 변동 | fwh | 
부록 B. 권장 파라미터 표 (원문 Table 3-4, 3-5 요약)
PWSCC 입력 | Alloy 600 | 82/182/132 수소 없음 | 82/182/132 수소 있음 | 
기준 온도 Tref (°C) | 325 | 325 | 325 | 
α (m/s)/(MPa√m)β | 1.34E-12 | 9.82E-13 | 2.01E-12 | 
β | 1.16 | 1.6 | 1.6 | 
Kth (MPa√m) | 9 | 0 | 0 | 
fcomp 대수정규 σ / 절단 | 1.0160 / 0.143~5.32 | 0.5892 / 0.313~2.64 | 0.4895 / 0.44~2.24 | 
fflaw 대수정규 σ / 절단 | 0.5695 / 0.208~3.68 | 0.4807 / 0.309~3.24 | 0.3742 / 0.335~2.04 | 
Qg 평균, 표준편차 (kJ/mol) | 130, 5 | 130, 20 | 104, 20 | 
P (P−1의 log μ, σ) | 1 (끔) | 1 (끔) | 4.52, 2.75 | 
c (mV) | 사용 안 함 | 사용 안 함 | 평균 18.2, 표준편차 5.5 | 
IF | 1 | 1 (182/132), 2.6 (82) | 1 (182/132), 2.6 (82) | 
피로 입력 | 값 | 분포 (epistemic) | 
ΔKth 척도 CKth | log-μ 0.239 | 대수정규, log-σ 0.139, 상한 1.927 | 
Ni계 척도 CNi | log-μ 0.0 | 대수정규, log-σ 0.408 | 
Ni계 Paris 지수 / 용접계수 | 4.1 / 2.0 | 결정값 | 
Ni계 환경계수 Aenv | log-μ −14.6 | 대수정규, log-σ 1.2 | 
Ni계 환경지수 nenv | 0.25 ~ 0.33 | 균일분포 | 
SS 척도 CSS / Paris 지수 | log-μ 0.0 / 2.25 | 대수정규 log-σ 0.420 / 결정값 | 
페라이트 C1 (TCF) | log-μ −22.01 | 대수정규, log-σ 0.467 | 
페라이트 C2 (중간 황 EAC) | log-μ −20.6 | 대수정규, log-σ 0.88, 하한 = 샘플된 C1 | 
페라이트 C3 (높은 황 EAC) | log-μ −15.8 | 대수정규, log-σ 0.88, 하한 = 샘플된 C1 | 
페라이트 CKb | log-μ −0.697 | 대수정규, log-σ 0.210 (중앙값 0.498) | 
부록 C. 적용 범위와 제약 (원문 §2.5, §3)
PWSCC 검증 범위K 10~80 MPa√m
온도 280~350°C
ECP −50~+50 mV (수소 약 1~60 cc/kg)
범위 밖 외삽은 근거를 붙여서만.
피로 검증 범위ΔK 0~60 MPa√m, R 0~1
상승 시간 0.1~7200 s
온도 160~315°C
황 0~0.02%
모델에 없는 것Mode II, III, 면외 균열 성장
냉간가공도, 이방성(방향) 직접 항
용접 경계·희석 영역 전용 모델
PWSCC와 피로의 상승작용(독립 가정)
오류 코드 (모듈)101~144: 입력 범위 밖 → 실행 종료
201, 202: PWSCC/피로 성장률이 음수나 NaN → 종료
203: ΔKb < ΔKth → 계산은 하되 경고
301~305: 사용자가 일부 열화 모드를 껐음 → 기록만
출처: K. Schmitt, xLPR Models Subgroup Report — Crack Growth and Coalescence, xLPR-MSGR-CGR Version 1.0, EPRI / U.S. NRC (ADAMS ML16341B051), 2016. 문서 안 값과 수식은 위 보고서 한 편에서만 가져왔고 설명 문장은 새로 썼습니다. 원문의 저작권은 EPRI에 있습니다.
검증: 수식은 PDF 쪽 이미지와 직접 대조했습니다. 다만 식 2-25의 지수는 원문 표기를 그대로 두었고 위 카드에 표시했습니다. Codex 교차검증 결과는 아래에 별도 표기합니다.
Codex 교차검증: Codex 실행 환경(Windows 샌드박스)이 명령 실행을 못 해서, 원문 추출 텍스트와 제 수식 전사 34개를 프롬프트에 담아 Codex가 대조하게 했습니다(원본 PDF를 Codex가 직접 보지는 못함). 결과: 34개 중 불일치 2건(식 2-3 좌변 첨자, 식 6-2 log-σ 표기)과 표기 불확실 일부를 지적받아 모두 반영했습니다. 나머지는 원문 텍스트와 일치. 식 2-25 지수 의문은 Codex가 지적하지 않았고 제 추정이라 그대로 표시해 둡니다.
