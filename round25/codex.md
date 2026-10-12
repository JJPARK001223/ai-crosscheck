# Round 25 - Codex blind 독립 검증

## 범위와 방법

- blind 원칙에 따라 `PROBLEM.md`와 대상 PDF 15개만 확인했다. `round25/claude.md`는 열어보지 않았다.
- 각 PDF에 대해 지정된 Poppler `pdftotext.exe`로 1페이지만 추출했다. 2단 편집에서 왼쪽의 `Keywords`, `Article history`, 본문 열이 섞이는 것을 막기 위해 `-bbox-layout`의 좌표로 Abstract 본문 블록을 식별한 뒤 해당 사각형을 다시 `pdftotext.exe -f 1 -l 1 -x ... -y ... -W ... -H ...`로 추출했다.
- `Abstract` 제목은 제외하고, `Keywords` 또는 `1. Introduction` 직전까지를 대상으로 삼았다. 공백(`\s+`)으로 토큰을 나눴으며 숫자와 기호도 독립 토큰이면 단어 수에 포함했다.
- 출처: 아래 각 PDF의 1페이지 원문(논문 자체가 1차 자료). 외부 웹 자료는 사용하지 않았다.

## 작업 1: PDF Abstract 단어 수 독립 재계산

| 번호 | 파일명 | Abstract 단어 수 |
|---:|---|---:|
| 1 | A Comparison of Ethanol, Methanol, and Butanol Blending with Gasoline and Its Effect on Engine Performance and Emissions Using Engine Simulation.pdf | 231 |
| 2 | An approach to estimate CCV (cycle-to-cycle variation) of effective energy output of thermal engine.pdf | 244 |
| 3 | Effect of engine parameters on the mixture distribution, performance and emission characteristics of a gasoline direct injection engine with bafflesA numerical analysis.pdf | 195 |
| 4 | Effect of H2 addition to methanol-gasoline blend on an SI engine at various lambda values and engine loads.pdf | 404 |
| 5 | Effect of the use of methanol, toluene and nitromethane mixtures as fuel additives in a gasoline engine on engine performance and exhaust emissions.pdf | 290 |
| 6 | Effects of Piston Shape on the Performance of a Gasoline Direct Injection Engine.pdf | 171 |
| 7 | Effects of turbocharger rotational inertia on engine and turbine performance in a turbocharged gasoline direct injection engine under transient and steady conditions.pdf | 246 |
| 8 | Enhancing engine power and torque and reducing exhaust emissions of blended fuels derived from gasoline-propanol-nano particles.pdf | 184 |
| 9 | Evaluation of gasoline-phthalocyanines fuel blends in terms of engine performance and emissions in gasoline engines.pdf | 245 |
| 10 | Exergoeconomic analysis of a DI diesel engine fueled with diesel biodiesel (B5) emulsions containing aqueous nano cerium oxide.pdf | 223 |
| 11 | Experimental comparative study on combustion, performance and emissions characteristics of ethanol-gasoline blends in a two stroke uniflow gasoline engine.pdf | 204 |
| 12 | Model-Based Unified Framework for Detection and Mitigation of Cyclic Torque Imbalance in a Gasoline Engine.pdf | 210 |
| 13 | Modelling thermodiffusive instabilities in hydrogen flames and their impact on the combustion process in a direct-injection hydrogen engine.pdf | 303 |
| 14 | Novel fuel injection strategies for PCCI operation of a heavy-duty turbocharged diesel engine.pdf | 191 |
| 15 | The Impact of Thermochemical Exhaust Energy Recovery Using Ethanol-Gasoline Blend on Gasoline Direct Injection Engine Performance.pdf | 220 |

### 추출 보정 및 경계 판단

1. **2단 편집 혼입 제거:** 파일 2~5, 8~11, 13은 왼쪽 `ARTICLE INFO/Keywords/Article history`와 오른쪽 Abstract가 같은 행에 배치되어 있었다. 좌표 기반으로 오른쪽 Abstract 블록만 재추출했다. 파일 1의 왼쪽 citation 영역과 파일 4의 오른쪽 Introduction 첫 문장 혼입도 같은 방식으로 제거했다.
2. **줄 끝 분철 복원:** PDF 조판상의 soft hyphen/행바꿈 때문에 둘로 추출된 단어를 원래 한 단어로 합쳤다. 확인된 사례는 파일 2의 `char­acteristic`, 파일 4의 `performed`, `combustion`, 파일 5의 `followed`, 파일 9의 `temperature`, `consumption`, 파일 13의 `instabilities`, `homogeneous`, `combustion`이다. 이 복원은 각 사례마다 토큰 수를 1개 줄인다.
3. **첨자·특수기호:** `H₂`, `CO₂`, `Al₂O₃` 등은 추출 결과의 `H2`, `CO2`, `Al2O3`처럼 한 토큰으로 세었다. `λ`는 보존하여 한 토큰으로 세었다. 원문/추출문에서 숫자와 `%` 사이에 실제 공백이 있는 경우(예: `9.70 %`)에는 지시대로 `%`도 별도 토큰으로 포함했다.
4. **저작권·서지정보 제거:** Abstract 블록 끝에 붙은 `© ... Elsevier Ltd. All rights reserved.`와 `[DOI: ...]`는 Abstract 본문이 아니므로 제외했다. `Article history`도 제외했다.
5. **파일 13의 별도 진술 제외:** Abstract 문단 다음에는 굵은 별도 소제목 `Novelty and significance`와 별도 진술이 있고, 그 뒤에 `1. Introduction`이 나온다. 이는 Abstract 본문이 아닌 별도 섹션이므로 단어 수 303에는 포함하지 않았다. 기계적으로 그 별도 진술까지 포함하면 값이 달라지므로, 이 파일은 이 경계 판단을 반드시 함께 제시해야 한다.

## 작업 2: 11개 저널의 공식 Abstract 단어 수 제한 - 사전학습 기억만 사용

### 해석상 주의

아래는 **웹이나 현행 공식 페이지를 확인한 결과가 아니다.** 2026-10-12 현재 지침인지 확인할 수 없으므로, 사전학습 기억이 비교적 분명한 경우에도 `회상(현행 미검증)`으로 표시했다. 숫자가 떠오르지만 저널별 공식 규정인지 확신할 수 없는 것은 `추측(불확실)`, 숫자 자체가 확실하지 않은 것은 `모름`으로 적었다. 따라서 이 표의 숫자를 현행 공식 사실로 인용해서는 안 된다.

| 저널 | 회상 결과 | 구분 및 판단 근거 |
|---|---:|---|
| Processes (MDPI) | 최대 약 200단어 | **회상(현행 미검증, 비교적 확실):** MDPI 원고 지침의 “약 200 words maximum” 문구를 기억한다. 다만 공식 페이지를 이번 작업에서 재확인하지 못했다. |
| Case Studies in Thermal Engineering (Elsevier) | 250단어 이하로 기억 | **추측(불확실):** Elsevier 계열의 저널별 Guide for Authors 문구였는지, 일반 템플릿 기억인지 구분할 수 없다. |
| Fuel (Elsevier) | 250단어 이하로 기억 | **회상(현행 미검증):** concise and factual abstract와 250단어 상한을 기억하지만 현행 공식 페이지 미확인이다. |
| Energy (Elsevier) | 250단어 이하로 기억 | **회상(현행 미검증):** 250단어 상한으로 기억하지만 현행 공식 페이지 미확인이다. |
| ACS Omega (ACS) | 모름 | ACS 저널의 250단어 또는 300단어 규정 기억이 서로 섞여 있어 이 저널의 공식 숫자를 특정할 수 없다. |
| International Journal of Engine Research (SAGE) | 약 150단어로 기억 | **추측(불확실):** SAGE 공통/타 저널 지침과 혼동 가능성이 커 공식 제한이라고 단정할 수 없다. |
| Journal of the Energy Institute (Elsevier) | 모름 | 저널 고유의 공식 숫자를 신뢰성 있게 회상하지 못한다. |
| Journal of Engineering for Gas Turbines and Power (ASME) | 250단어 이하로 기억 | **추측(불확실):** ASME 공통 투고 형식의 기억일 가능성이 있으며 저널 고유·현행 규정인지 확인하지 못했다. |
| Topics in Catalysis (Springer) | 150~250단어로 기억 | **회상(현행 미검증):** Springer 저널 지침의 범위로 기억하지만 이 저널의 현행 공식 페이지를 확인하지 못했다. |
| Combustion and Flame (Elsevier) | 모름 | Abstract와 별도 `Novelty and significance` 진술의 각 제한을 혼동할 가능성이 있어 숫자를 제시하지 않는다. |
| Applied Thermal Engineering (Elsevier) | 250단어 이하로 기억 | **회상(현행 미검증):** 250단어 상한을 기억하지만 현행 공식 페이지 미확인이다. |

### 작업 2의 결론

네트워크가 차단된 상태에서 공식 지침을 직접 열람하지 못했으므로, 작업 2에는 **현행 공식 제한으로 확정할 수 있는 항목이 없다.** 위 숫자는 오직 기억의 상태를 투명하게 남긴 것이며, 최종 판정에는 각 저널의 현행 공식 Guide for Authors를 별도로 확인해야 한다.
