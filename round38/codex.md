# Round38 PPT 수정본 독립 검사

검사일: 2026-10-16. 검사만 수행했으며 PPT·덤프·원문을 수정하지 않았다. 결과 파일은 이 문서뿐이다. Claude 결과는 열람하지 않았다.

## 자료와 판정 범위

- 이전본: `round38/ppt_old_dump.txt`, 현재본: `round38/ppt_new_dump.txt`. 각각 SLIDE 마커 90개, 91개를 직접 집계했다.
- 원문: Kyle Schmitt, EPRI, *xLPR Models Subgroup Report—Crack Growth and Coalescence*, xLPR-MSGR-CGR Version 1.0, 2016-06-29 (`J:\\Desktop\\XLPR\\2026_10_13_XLPR모델분석\\cgr_text.txt`). 이하 영어 인용은 모두 이 문서의 인쇄 쪽이다. 2021년 공개용 행정 개정이 있으나 버전·발행일을 올리지 않았다는 Revision History도 확인했다.
- PAGE n 블록을 인쇄 쪽 n−1로 읽었으며, 아래에서 사용하는 서로 다른 25쪽 모두 블록 끝의 단독 쪽 숫자와 일치함을 확인했다.
- 사용자 지시에 따라 제공된 덤프 본문을 비교했다. 줄 양끝 공백·빈 줄, 독립 슬라이드 번호, 독립 `[IMAGE]`, 독립 `[n] Reference`, 독립 `p.NN`은 구분했다. 본문 속 인용·표의 문자열은 보존하여 대조했다. 나머지 문장·제목·표 행은 대응 슬라이드에서 전부 일치했다.
- **수식·그림 등 추출되지 않은 시각 요소의 동일성 및 출처 대응은 확인 불가**다. `Text` 반복, 닫는 괄호 `)`는 실질 본문으로 보지 않았다. 제목 전용 슬라이드에서는 요청대로 **본문 없음**으로 기록하고 지시 쪽 제목·내용만 대조했다. 옆 슬라이드나 통상 수식 순서로 대응을 추측하지 않았다.

## 1. 슬라이드 수·구조 대응

현재 84~85번에 동일한 제목 전용 블록이 두 개 존재한다. 이전에는 해당 위치에 한 개뿐이다. 따라서 **내용 기준 +1은 84~85 구간**이다. 두 현재 블록이 번호를 제외하면 같아서, 원래 84번을 복제하여 앞에 넣었는지 뒤에 넣었는지는 텍스트만으로 식별 불가다. 아래는 이전84→현재84, 현재85 추가로 놓은 대표 대응이며, 이전84→현재85·현재84 추가 역시 동일하게 성립한다.

| 이전 슬라이드 | 현재 슬라이드 | 내용 기준 결과 |
|---:|---:|---|
| 1 | 1 | 본문 동일 |
| 2 | 2 | 본문 동일 |
| 3 | 3 | 본문 동일 |
| 4 | 4 | 본문 동일 |
| 5 | 5 | 본문 동일 |
| 6 | 6 | 본문 동일 |
| 7 | 7 | 본문 동일 |
| 8 | 8 | 본문 동일 |
| 9 | 9 | 본문 동일 |
| 10 | 10 | 본문 동일 |
| 11 | 11 | 본문 동일 |
| 12 | 12 | 본문 동일 |
| 13 | 13 | 본문 동일 |
| 14 | 14 | 본문 동일 |
| 15 | 15 | 본문 동일 |
| 16 | 16 | 본문 동일 |
| 17 | 17 | 본문 동일 |
| 18 | 18 | 본문 동일 |
| 19 | 19 | 본문 동일 |
| 20 | 20 | 본문 동일 |
| 21 | 21 | 본문 동일 |
| 22 | 22 | 본문 동일 |
| 23 | 23 | 본문 동일 |
| 24 | 24 | 본문 동일 |
| 25 | 25 | 본문 동일 |
| 26 | 26 | 본문 동일 |
| 27 | 27 | 본문 동일 |
| 28 | 28 | 본문 동일 |
| 29 | 29 | 본문 동일 |
| 30 | 30 | 본문 동일 |
| 31 | 31 | 본문 동일 |
| 32 | 32 | 본문 동일 |
| 33 | 33 | 본문 동일 |
| 34 | 34 | 본문 동일 |
| 35 | 35 | 본문 동일 |
| 36 | 36 | 본문 동일 |
| 37 | 37 | 본문 동일 |
| 38 | 38 | 본문 동일 |
| 39 | 39 | 본문 동일 |
| 40 | 40 | 본문 동일 |
| 41 | 41 | 본문 동일 |
| 42 | 42 | 본문 동일 |
| 43 | 43 | 본문 동일 |
| 44 | 44 | 본문 동일 |
| 45 | 45 | 본문 동일 |
| 46 | 46 | 본문 동일 |
| 47 | 47 | 본문 동일 |
| 48 | 48 | 본문 동일 |
| 49 | 49 | 본문 동일 |
| 50 | 50 | 본문 동일 |
| 51 | 51 | 본문 동일 |
| 52 | 52 | 본문 동일 |
| 53 | 53 | 본문 동일 |
| 54 | 54 | 본문 동일 |
| 55 | 55 | 본문 동일 |
| 56 | 56 | 본문 동일 |
| 57 | 57 | 본문 동일 |
| 58 | 58 | 본문 동일 |
| 59 | 59 | 본문 동일 |
| 60 | 60 | 본문 동일 |
| 61 | 61 | 본문 동일 |
| 62 | 62 | 본문 동일 |
| 63 | 63 | 본문 동일 |
| 64 | 64 | 본문 동일 |
| 65 | 65 | 본문 동일 |
| 66 | 66 | 본문 동일 |
| 67 | 67 | 본문 동일 |
| 68 | 68 | 본문 동일 |
| 69 | 69 | 본문 동일 |
| 70 | 70 | 본문 동일 |
| 71 | 71 | 본문 동일 |
| 72 | 72 | 본문 동일 |
| 73 | 73 | 본문 동일 |
| 74 | 74 | 본문 동일 |
| 75 | 75 | 본문 동일 |
| 76 | 76 | 본문 동일 |
| 77 | 77 | 본문 동일 |
| 78 | 78 | 본문 동일 |
| 79 | 79 | 본문 동일 |
| 80 | 80 | 본문 동일 |
| 81 | 81 | 본문 동일 |
| 82 | 82 | 본문 동일 |
| 83 | 83 | 본문 동일 |
| 84 | 84 | 제목 전용 블록 대응은 84/85 사이 식별 불가 |
| 없음 | 85 (대표 대응) | 제목 전용 블록 한 장 증가; 현재84와 실질 텍스트 동일 |
| 85 | 86 | 본문 동일; 번호 +1 |
| 86 | 87 | 본문 동일; 번호 +1 |
| 87 | 88 | 본문 동일; 번호 +1 |
| 88 | 89 | 본문 동일; 번호 +1 |
| 89 | 90 | 본문 동일; 번호 +1 |
| 90 | 91 | 본문 동일; 번호 +1 |

별도 내용의 삭제·이동은 추출 텍스트에서 검출되지 않았다. 이것은 이미지·수식·내부 슬라이드 ID의 삭제·이동이 없었다는 증명이 아니다.

## 2. 문장·제목·표의 추가·삭제·변경

| 범주 | 직접 비교 결과 | 원문 근거 판정 |
|---|---|---|
| 대응된 90장 본문·제목·표 | 공백·추출 표식·페이지/슬라이드 번호를 구분하면 모두 동일. 인용할 새 본문 문장·삭제 문장·변경 문장 없음 | 신규 ADDED-CLAIM 없음. 기존 내용 전체의 정확성을 보증하는 판정은 아님 |
| 현재84~85 구간의 +1장 | 추가 블록 전체 실질 텍스트: “RECOMMENDATIONS FOR FUTURE WORK”, “p.119”. 번호를 빼면 두 블록 동일 | 새 기술 주장 없음. p.119에는 향후 권고 §6.2.2~6.2.4와 식6-1·6-2가 있으나 어느 것을 표시하려는지는 확인 불가 |
| 자리표시자 삭제 | 이전 77장에 존재하던 `[n] Reference`가 현재 3장(71, 89, 90)에만 남음. 대응 기준 74개 삭제 | 단순히 모든 자리표시자가 쪽 번호로 치환된 것은 아님 |
| 독립 쪽 표기 추가 | 현재6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,47,49,51,53,55,59,61,63,84,85에 총30개. 6·8은 이전 자리표시자 없이 새 표기 추가 | 각 표기의 검증 한계는 아래 표 참조 |
| 슬라이드 번호 | 이전85~89의 번호가 현재86~90으로 +1; 마지막 감사 슬라이드에는 독립 번호 텍스트 없음 | 구조 변경에 따른 번호 갱신 |
| 추출 차이 | 이전의 독립 `[IMAGE]`와 줄바꿈·공백 차이 | 이미지가 삭제됐다고 판정하지 않음 |

## 3. 현재의 모든 p.NN 표기 검증: 제목 전용 30장

다음 30장 모두 **본문 없음**. 현재6~63의 표시 제목은 CRACK GROWTH MODELS 또는 CRACK GROWTH RATE MODELS이고, 84·85는 RECOMMENDATIONS FOR FUTURE WORK이다. 원문의 모델·모듈·향후 권고 분야와 넓은 수준에서 일치하지만, 구체적인 식·내용이 빠져 있어 **해당 쪽이 그 슬라이드의 정확한 출처인지 확인 불가**다. 아래 식 번호는 원문 해당 쪽에 존재한다는 관찰값이며 슬라이드 식 번호 판정이 아니다. 틀린 쪽이라고 단정하거나 대체 쪽을 제안할 근거도 없다.

| 현재 슬라이드 | 표기 | 본문 판정·쪽 대응 | 지시 쪽의 실제 제목/계속 내용 | 영어 원문 근거 및 그 쪽 식 |
|---:|---|---|---|---|
| 6 | p.21 | 본문 없음; 분야만 일치, 정확한 대응 확인 불가 | 2.2.1 Alloy 600 / 2.2.1.1 Mathematical Description | “The Alloy 600 PWSCC CGR model, based on MRP-55 [2]”; 식 2-1 |
| 8 | p.27 | 본문 없음; 분야만 일치, 정확한 대응 확인 불가 | 2.2.2.1 Mathematical Description | “The Alloys 82/182/132 PWSCC CGR model, based on MRP-115”; 식 2-2 |
| 10 | p.33 | 본문 없음; 분야만 일치, 정확한 대응 확인 불가 | 2.2.3.1 Mathematical Description | “a hydrogen effect scaling term is added”; 식 2-3~2-5 |
| 12 | p.33 | 본문 없음; 분야만 일치, 정확한 대응 확인 불가 | 2.2.3.1 Mathematical Description | “f = hydrogen factor”; 식 2-3~2-5 |
| 14 | p.33 | 본문 없음; 분야만 일치, 정확한 대응 확인 불가 | 2.2.3.1 Mathematical Description | “The difference in ECP between the Ni/NiO transition”; 식 2-3~2-5 |
| 16 | p.34 | 본문 없음; 분야만 일치, 정확한 대응 확인 불가 | 2.2.3.2 Model Development 및 앞 절 계속 | “The concentration of dissolved hydrogen corresponding to the potential Ni/NiO transition is temperature dependent”; 식 2-6, 2-7 |
| 18 | p.38 | 본문 없음; 분야만 일치, 정확한 대응 확인 불가 | 2.2.4.2 Other SCC-Resistant Materials / 2.3 Fatigue Model Development | “a general material model of the form shown in [Eqn. 2-8] is included in xLPR”; 식 2-8 |
| 20 | p.39 | 본문 없음; 분야만 일치, 정확한 대응 확인 불가 | 2.3.1 General Considerations | “Stress intensity factor range: Cyclic loading is readily characterized”; 식 2-9, 2-10 |
| 22 | p.39 | 본문 없음; 분야만 일치, 정확한 대응 확인 불가 | 2.3.1 General Considerations | “Load ratio: The load ratio calculation is also based on ASME Section XI Appendix A guidance”; 식 2-9, 2-10 |
| 24 | p.40 | 본문 없음; 분야만 일치, 정확한 대응 확인 불가 | 2.3.1 계속; 새 절 제목 없음 | “This model form is based on ASME Code Case N-643-2 [23]”; 식 2-11, 2-12 |
| 26 | p.40 | 본문 없음; 분야만 일치, 정확한 대응 확인 불가 | 2.3.1 계속; 새 절 제목 없음 | “A least squares linear fit to the data of Figure 2-10”; 식 2-11, 2-12 |
| 28 | p.42 | 본문 없음; 분야만 일치, 정확한 대응 확인 불가 | 2.3.2 Nickel-Based Alloys / 2.3.2.1 Mathematical Description | “Fatigue CGRs for nickel-based alloys are calculated as follows”; 식 2-13, 2-14 |
| 30 | p.42 | 본문 없음; 분야만 일치, 정확한 대응 확인 불가 | 2.3.2 Nickel-Based Alloys / 2.3.2.1 Mathematical Description | “Fatigue CGRs for nickel-based alloys are calculated as follows”; 식 2-13, 2-14 |
| 32 | p.43 | 본문 없음; 분야만 일치, 정확한 대응 확인 불가 | 2.3.2.2 Model Development 및 앞 절 계속 | “The alloy factor defines any systematic difference in fatigue behavior”; 식 2-15~2-17 |
| 34 | p.43 | 본문 없음; 분야만 일치, 정확한 대응 확인 불가 | 2.3.2.2 Model Development | “the load ratio effect was expressed as given in [Eqn. 2-16]”; 식 2-15~2-17 |
| 36 | p.44 | 본문 없음; 분야만 일치, 정확한 대응 확인 불가 | 2.3.2.3 Treatment of Uncertainty 및 모델 개발 계속 | “the temperature effect was re-estimated for Alloy 690”; 식 2-18 |
| 38 | p.48 | 본문 없음; 분야만 일치, 정확한 대응 확인 불가 | 2.3.3.1 Mathematical Description / 2.3.3.2 Model Development | “Fatigue CGRs for austenitic SS are calculated as follows”; 식 2-19 |
| 40 | p.49 | 본문 없음; 분야만 일치, 정확한 대응 확인 불가 | 2.3.3.3 Treatment of Uncertainty 및 모델 개발 계속 | “The load ratio effect model given in [Eqn. 2-21]”; 식 2-20~2-22 |
| 42 | p.49 | 본문 없음; 분야만 일치, 정확한 대응 확인 불가 | 2.3.3 모델 개발 계속 | “Loading rise time effect: Fatigue CGRs in austenitic SS increased”; 식 2-20~2-22 |
| 44 | p.49 | 본문 없음; 분야만 일치, 정확한 대응 확인 불가 | 2.3.3 모델 개발 계속 | “Alloy effect: The alloy factor has two purposes”; 식 2-20~2-22 |
| 47 | p.52 | 본문 없음; 분야만 일치, 정확한 대응 확인 불가 | 2.3.4 Ferritic Steels / 2.3.4.1 Mathematical Description | “This section presents the fatigue CGR model for general ferritic steels in PWR environments”; 식 2-23 |
| 49 | p.54 | 본문 없음; 분야만 일치, 정확한 대응 확인 불가 | 2.3.4 모델 개발 계속; 새 절 제목 없음 | “defines the following “critical velocity” that must be achieved before EAC can engage”; 식 2-24 |
| 51 | p.55 | 본문 없음; 분야만 일치, 정확한 대응 확인 불가 | 2.3.4 모델 개발 계속; 새 절 제목 없음 | “the TCF curve is regained for stress intensity factor ranges above that specified below”; 식 2-25 |
| 53 | p.56 | 본문 없음; 분야만 일치, 정확한 대응 확인 불가 | 2.3.4 모델 개발 계속; 새 절 제목 없음 | “This transition is modeled to occur at a stress intensity factor range threshold”; 식 2-26, 2-27 |
| 55 | p.56 | 본문 없음; 분야만 일치, 정확한 대응 확인 불가 | 2.3.4 모델 개발 계속; 새 절 제목 없음 | “The environmental factor is the following function of loading rise time and load ratio”; 식 2-26, 2-27 |
| 59 | p.72 | 본문 없음; 분야만 일치, 정확한 대응 확인 불가 | 3.2.1.3 CGR Calculation | “calculate PWSCC CGR for all materials besides the custom material”; 식 3-1, 3-2 |
| 61 | p.72 | 본문 없음; 분야만 일치, 정확한 대응 확인 불가 | 3.2.1.3 CGR Calculation | “For custom materials (Material Group 10)”; 식 3-1, 3-2 |
| 63 | p.73 | 본문 없음; 분야만 일치, 정확한 대응 확인 불가 | 3.2.1.3 계속 / 3.2.1.4 Post-CGR Calculation | “all variables with the subscript cstm are user-defined custom CGR model parameters”; 식 3-3 |
| 84 | p.119 | 본문 없음; 분야만 일치, 정확한 대응 확인 불가 | 6.2.2 Enhancements to Probabilistic Model for Nickel-Based Alloys / 6.2.3 / 6.2.4 | “The material groupings for the SS alloy effect were changed to”; 식 6-1, 6-2 |
| 85 | p.119 | 본문 없음; 분야만 일치, 정확한 대응 확인 불가 | 6.2.2 Enhancements to Probabilistic Model for Nickel-Based Alloys / 6.2.3 / 6.2.4 | “log-normal distribution with a median of 4.4x10-7”; 식 6-1, 6-2 |

## 3-계속. 본문이 있는 8장의 개별 표기 검증

같은 쪽 번호가 한 장에 반복되어도 각 사용 위치를 구분했다. ‘맞음’은 인용 쪽에 해당 근거가 있다는 뜻이며 문장 전체를 무조건 승인한다는 뜻이 아니다.

| 현재 슬라이드·위치 | 현재 표기 | 판정 / 올바른 쪽 | 영어 원문 근거 (Schmitt, EPRI, 2016) |
|---|---|---|---|
| 66 관통균열 길이 의존성 미구현 | p.94 | 맞음: p.94 | “this dependency is not implemented in the coalescence module for xLPR Version 2.0” |
| 67 표면+표면 두 규칙·0.5·ASME | p.94 | 맞음: p.94 | “Two conventions have been selected”; “the best-fit scaling factor is half (0.5)” |
| 67 표면+표면 불확실성·삼각분포 | p.98 | 맞음: p.98 | “a triangular distribution is recommended with extremes at 0.0 and 0.75 and a mode at 0.5” |
| 67 관통+관통 ligament collapse·사용자 값·0~20 in | p.94 | 맞음: p.94 | “the common physical driver of coalescence is ligament collapse”; “distances between 0 and 20 inches are possible” |
| 67 관통+관통 길이관계 | p.98 | 맞음: p.98 | “the coalescence distance has a roughly one-to-one relationship with crack length” |
| 67 표면+관통 기본값0 | p.94 | 맞음: p.94 | “the coalescence distance is set to zero by default” |
| 68 균열 유형 규칙의 물리적·논리적 근거 | p.94 | 맞음: p.94 | “These transitioning rules were developed based on physical expectations and logical considerations” |
| 68 OD길이·누설 연속성 | p.95 | 맞음: p.95 | “This convention is consistent with physical expectations and should result in acceptable leakage continuity” |
| 68 최대 깊이·re-entrant sector | p.95 | 맞음: p.95 | “the maximum depth is recommended”; “until the coalesced crack regains a roughly symmetric shape” |
| 70 분포된 합체거리·모델오차 | p.98 | **쪽은 맞음. 본문에 기존 의미 반전 오류가 있음**: “반영할 수 없음”은 원문과 반대. 올바른 근거도 p.98 | “This uncertainty may reflect variability in the complex processes that lead to coalescence as well as model error” |
| 70 표면균열 비·삼각분포 | p.98 | 맞음: p.98 | “between zero (i.e., no crack interaction) and roughly 0.75, with a best-estimate of 0.5” |
| 70 관통균열 길이관계·결정론적 실행 | p.98 | 맞음: p.98 본문 및 각주35 | “may be assumed to be deterministic for individual program runs and then varied for the purpose of sensitivity studies” |
| 70 그 밖의 convention·최대 깊이 변경 | p.98~99 | **범위가 맞음**. deterministic/논리적 근거는98, 최대 깊이 규칙 민감도 문장 끝은99 | p.98: “The other coalescence modeling conventions are fully deterministic”; p.99: “this convention may be varied for individual program runs” |
| 71 개요 | p.99 | 맞음: p.99 §4.2.3 | “Through application of published research, the coalescence modeling conventions were generally validated” |
| 71 표면균열 K 증대 | p.99 | 맞음: p.99 첫 bullet | “the onset of the intensification of stress intensity factor for surface cracks is well-predicted using a coalescence distance” |
| 71 관통균열 positive 거리 | p.99 | 맞음: p.99 두 번째 bullet. 각주36은 연구가 동일 길이 두 결함을 가정했음을 명시 | “low likelihood of rapid tearing leading to ligament collapse until the ligament between two cracks is less than the length of the cracks” |
| 72 두 표면균열 최대 깊이 | p.99 | 맞음: p.99 세 번째 bullet | “This rapid growth is predicted with higher order analytical modeling and has been observed experimentally” |
| 72 합체 후 균열 유형·표면+관통 자료 부재 | p.99 | 맞음: p.99 네 번째 bullet 및 각주37 | “transitioning rules”; “there is not experimental data involving the coalescence of a surface crack and a through-wall crack” |
| 72 적용 범위 행 | p.99 | 쪽은 맞음. **범위 설명이 충분하지 않음**: 표는 “실험 결과와 상위 수준 모델링으로 대체로 검증됨”이라고만 적어 실제 적용 범위를 쓰지 않음 | “This module validation applies for the full range of crack and component geometries expected within xLPR Version 2.0” |
| 75 입력 제공 | p.103 | 맞음: p.103 §5.1 | “the Framework provides information about the crack configuration, component geometry, and coalescence model parameters via inputs” |
| 79 range of verification와 validation 구분 | p.109 | 맞음: p.109 §5.3 | “This range is different from the range over which model validation was performed” |

68번의 인용이 직접 붙지 않은 중심·면적 규칙도 p.95에 있다: “The center of the new crack is set to the center of the arc”; “the area of the coalesced crack is equivalent to the sum of the areas of the original two cracks”. 66번의 거리 분포·epistemic 권고는 p.94 한 쪽만으로 다 덮이지 않고 p.98에 있다: “It is recommended that these uncertainties be designated as epistemic”. 따라서 66번 본문의 국소 p.94는 맞지만 슬라이드 전체 출처를 한 쪽으로 대표하려면 불충분하다. 어느 인용도 붙지 않은 다른 슬라이드 전체의 주장을 이 검사에서 포괄 검증한 것은 아니다.

## 4. 인용 형식·기존 인용 유지와 내용상 주의점

| 항목 | 관찰 결과 | 판단 |
|---|---|---|
| 인용 표기가 있는 장 수 | p.NN을 가진 현재 슬라이드는 정확히38장으로 요청 목록과 일치 | 누락된 대상 슬라이드 없음 |
| 독립 쪽 표기 vs 본문·표 속 표기 | 앞의 제목 전용30장은 독립 표기; 66,67,68,70,71,72,75,79의8장은 문장 괄호 또는 표의 쪽 열 | 위치·양식은 통일되어 있지 않으나 사용 위치별로 구별 가능 |
| 한 장 여러 인쇄 쪽 | 67:94·98, 68:94·95, 70:98·98~99 | 서로 다른 주장에 서로 다른 쪽이 필요하므로 복수 쪽 자체는 오류 아님 |
| 쪽 범위 | 70의 “p.98~99”만 범위 표기 | 실제 문장이 쪽을 넘어가므로 타당. 다른 곳은 단일 쪽으로 표기 |
| 66~72의 기존 인용 | 66의1개, 67의5개, 68의3개, 70의4개, 71의3개, 72의3개가 이전본과 동일. 69는 p.NN 표기 없음 | 기존 쪽 숫자·문장·표 내용 유지. 세부 판정은 위19개 행 참조 |
| 남은 자리표시자 | 71,89,90의 “[n] Reference” | 쪽 표기 전면 치환은 완료되지 않음. 71은 본문 표에 p.99가 이미 있음 |
| 현재84·85 반복 | 제목과 p.119가 동일 | 텍스트상 반복. 본문·수식 차이는 덤프만으로 확인 불가 |
| 기존 오류: 70 “분포된 합체거리” | 원문 may reflect를 “반영할 수 없음”으로 기재 | **명확한 의미 반전**. 수정 권고: “이 불확실성은 … 변동성과 모델 오차를 반영할 수 있음”. 신규 추가 오류가 아니라 양 덤프에 존재하던 오류 |
| 기존 불명확성: 72 “적용 범위” | 범위 대신 검증됐다는 요약만 기재 | p.99의 마지막 문장대로 “xLPR Version 2.0에서 예상되는 균열·부품 형상의 전체 범위”를 명시해야 원문과 정확히 대응함 |
| 기존 표기의 한계: 66 | p.94는 길이 의존성 미구현 문장 바로 뒤에 붙음 | 이 국소 인용은 정확함. 거리 불확실성·epistemic 문장의 근거는 p.98 추가가 필요 |
| 75·79 기존 국소 인용 | p.103, p.109가 대응 이전75·79에서도 동일 | 국소 문장에 대한 쪽은 맞음. 슬라이드 다른 문장 전체까지 같은 쪽에 있다고 확대 해석하면 안 됨 |

## 요약

| 질문 | 결론 |
|---|---|
| 90→91 구조 | 제목 전용 블록이84~85 구간에 한 장 증가. 구체적으로 어느 복제본이 추가됐는지는 텍스트로 식별 불가. 이후85~90의 이전 내용은 현재86~91에 대응 |
| 새 본문 주장 | 없음. 대응 본문·제목·표는 같고 기술 문장 ADDED-CLAIM은 검출되지 않음. 이미지·수식은 확인 불가 |
| 모든38장 인용 | 본문 있는8장의21개 인용 위치는 해당 인쇄 쪽에 근거가 있음. 본문 없는30장은 분야 제목만 대조했고 정확한 출처 대응은 확인 불가 |
| 문제점 | 70번 기존 의미 반전, 72번 범위 설명 불충분, 66번 전체 내용을 덮으려면 p.98 보충 필요. 자리표시자3개 남음 |
| 파일·Git | PPT와 입력 파일은 무수정. 시작 git pull은 “cannot open '.git/FETCH_HEAD': Permission denied”로 실패. 결과 파일만 대상으로 git add를 시도했으나 “Unable to create 'J:/Desktop/공학/ai-crosscheck/.git/index.lock': Permission denied”로 실패했다. 따라서 커밋·푸시는 미완료이며 로컬 결과 파일만 작성됨 |

__DONE__

