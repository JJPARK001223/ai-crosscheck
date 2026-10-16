# Round 43 — xLPR 모델 평가 순서 독립 조사

작성: Codex, 2026-10-16. Blind 조사이며 Claude 결과는 읽지 않았다. 조사 대상은 `round43/txt/`의 지정된 12개 원문이다. 자동화 실행 스크립트는 실행하지 않았다. `PROBLEM.md`는 round28 내용이므로 이번 작업 범위는 `round43/prompt.txt`를 따랐다.

## 1. 핵심 판정과 근거 범위

**전체 순서는 의존성만으로 추정할 필요가 없다. 불확실성 보고서 §3.2.2, PDF 42–44쪽에 realization 초기화, CI, 시간 루프의 평가 순서가 직접 열거되어 있다.** 아래의 [원문]은 보고서에 명시된 내용, [추론]은 그 입력·출력 관계를 연결한 해석이다. 보고서의 실행 설명은 확인했지만, 실행 코드·GoldSim 모델 파일을 실행하거나 추적한 것은 아니다. 특정 배포본의 실제 함수 호출 로그는 **확인 불가**다.

12개 문서는 12개의 독립 실행 모듈과 일치하지 않는다. 지정 목록상 Models Subgroup Report는 10편(B044–B053), 나머지는 PWSCC 매개변수 개발·검증 기술보고서와 불확실성 기술보고서다. B051은 성장과 합체라는 별도 모듈을 포함하며 B052는 SCC와 피로 CI를 포함한다. C202를 B052 다음에 호출하는 별도 물리 모듈로 배열해서는 안 된다.

계산 구조의 요점은 다음과 같다.

- [원문] TIFFANY와 LEAPOR는 전처리에서 표를 만들며, Framework가 시뮬레이션 시작 시 표를 읽는다.
- [원문] realization 초기화 뒤 CI가 발생 시각·위치 배열을 만든다. 시간 루프에서는 예정 시각에 새 균열을 활성화한다.
- [원문] 루프 안에서 축방향 균열을 진행시킨 뒤 원주방향 균열을 진행시킨다. 합체는 원주방향 분기에 있다.
- [원문] 각 분기의 주요 순서는 K 계산 → 성장 → 균열 유형 갱신 → 전이 → 안정성 → COD → 누설률 → ISI다. 원주방향에서는 성장 뒤에 합체와 추가 유형 갱신이 들어간다.
- [원문] ISI의 POD/POR는 검사 시점에 계산하지만, 검사에 따른 위험 감소는 후처리에서 적용한다.

전체 순서의 직접 근거: `(ML19337C165)Source and treatment of uncertainties.txt`, PDF 42쪽, “Run initialization”; 같은 파일 PDF 43쪽, “axial crack progression (as needed)”, “Circumferential crack progression (as needed)”; PDF 44쪽, “Go to next time step; stop if rupture or end of simulation period”. 각 인용은 15단어 이하다.

## 2. 출처 목록과 읽은 절

쪽번호는 전부 추출문의 `=====PAGE n=====` 기준 **PDF 쪽**이다. 인쇄 쪽번호와 혼용하지 않는다. 저자·연도·버전은 각 보고서 서명·개정 이력에서 확인했다. 아래 자료는 NRC/EPRI 공동 xLPR 보고서이며 학술지 논문은 아니다. 다수 문서에 있는 2021년 행정 개정은 원래 발행연도와 구분한다.

| 식별자 | 파일명·출처 | 확인한 Introduction / Overview / Framework / Interfacing 절 |
|---|---|---|
| B052 | `(ML16341B052)Crack initiation.txt` — Clifford Lange, xLPR-MSGR-CI v1.0, 2016 | §1 PDF 11–12; §2.1–2.2 PDF 13–15; §3.3 PDF 49 |
| C202 | `(ML19337C202)PWSCC initiation.txt` — Kyle Schmitt·Greg Troyer, xLPR-TR-CI-SCC-Calibration v2.0, 2017 | §1.1–1.3 PDF 18–19; §1.5 PDF 22–24 |
| B049 | `(ML16341B049)Welding residual stresses.txt` — F. W. Brust·Mike Benson·John Broussard, xLPR-MSGR-WRS v1.0, 2016 | §1 PDF 16–17; §2 PDF 18–19; §6.3 PDF 94 |
| B046 | `(ML16341B046)Stress intensity factors.txt` — Russell C. Cipolla·Steven X. Xu·Do Jun Shim, xLPR-MSGR-KSol v1.0, 2016 | §1 PDF 13–14; §3.1.1 PDF 62; §3.1.2.2 PDF 66; §3.1.3.2 PDF 70–71 |
| B048 | `(ML16341B048)Cyclic stress intensity factors.txt` — David O. Harris, xLPR-MSGR-TIFF v1.0, 2016 | §1 PDF 11; §3.2–3.4 PDF 26–27; 입출력 표 계속 PDF 31; §3.5 PDF 32 |
| B044 | `(ML16341B044)Crack transition.txt` — Do Jun Shim, xLPR-MSGR-CTM v1.0, 2016 | §1 PDF 12–14; §3.1 PDF 45–46; §3.2 PDF 49 |
| B051 | `(ML16341B051)Crack growth and coalescence.txt` — Kyle Schmitt, xLPR-MSGR-CGR v1.0, 2016 | §1 PDF 18–20; §2.1 PDF 21; §3.1 PDF 69–70; §3.2.2 PDF 75–76; §5.1 PDF 104; §5.2.2 PDF 109 |
| B053 | `(ML16341B053)Crack opening displacement.txt` — Rick Olson, xLPR-MSGR-COD v1.0, 2016 | §1 PDF 15–16; §3.1–3.2 PDF 72 |
| B047 | `(ML16341B047)Leak rate.txt` — Elizabeth Kurth, xLPR-MSGR-LRM v1.1, 2016 | §1 PDF 12–13; §2・§2.1 PDF 13–14; §2.3 표 PDF 25 |
| B050 | `(ML16341B050)Crack stability.txt` — Rick Olson, xLPR-MSGR-Stability v1.0, 2016 | §1 PDF 17–18; §3.1–3.1.2 PDF 33–34 |
| B045 | `(ML16341B045)Inservice inspection.txt` — Kyle Schmitt, xLPR-MSGR-ISI v1.0, 2016 | §1 PDF 14–16; §2.3.2 PDF 46–48; §3.1 PDF 52; §3.2.2 PDF 59 |
| C165 | `(ML19337C165)Source and treatment of uncertainties.txt` — Marjorie Erickson, xLPR-TR-UNCERT v2.0, 2020 | §1 PDF 22–23; §3.1–3.3 PDF 39–47; §12.3 PDF 144; §14.1–14.2 PDF 174 |

## 3. 12편의 입력 출처와 출력 소비처

표에서 **FW**는 Computational Framework다. 화살표는 데이터 의존성을 나타낸다. 모듈들이 서로 직접 호출한다는 뜻은 아니다. FW가 입력 변환·샘플링·배열 관리·DLL 호출과 결과 전달을 담당한다.

| 문서 / 기능 | 입력 출처 | 출력 및 소비처 | 원문 근거: 파일명 + PDF 쪽 + 짧은 인용 |
|---|---|---|---|
| B049 / WRS 입력 개발 | 용접부 형상·용접 공정·열/기계 물성·경계조건 → 별도 FE 해석. FW는 결과 분포와 두께 방향 상관을 사용 | 평균 WRS 프로파일·불확실성·상관 → FW 응력 계산 → CI 표면응력과 K 계산. AxCOD에는 평균 hoop WRS도 공급 | `(ML16341B049)Welding residual stresses.txt`, PDF 16, “These profiles then feed into the stress intensity factor (K) calculation procedure”; PDF 18, “finite element modeling of the welding process”; PDF 94, “used for circumferential crack initiation and growth”. AxCOD 연결은 `(ML16341B053)Crack opening displacement.txt`, PDF 16, “through-thickness averaged hoop weld residual stress” |
| B048 / TIFFANY | 사용자 과도 이력(시간·온도·압력), 형상·물성, 사용자 최소/최대 응력 → 입력 전처리기가 TIFFANY DLL 호출 | 과도별·균열 크기별 K 변화의 최대/최소, 표면 cyclic stress, rise time, 온도 극값 → 표 → FW → 피로 CI 및 피로 CGR | `(ML16341B048)Cyclic stress intensity factors.txt`, PDF 11, “for analysis of fatigue crack initiation and growth”; PDF 26, “the input pre-processor shall call the TIFFANY DLL”; PDF 31, “A key input to TIFFANY is the time/temperature/pressure history of the transient” |
| B052 / SCC·피로 CI | FW가 구획·방향에 맞는 표면응력, 온도·수화학·시간구간·모델 매개변수 제공. WRS는 응력의 출처, TIFFANY 결과는 피로 CI의 출처 | 발생 시각·위치 → FW의 발생 배열 및 시간 루프 활성화 → 성장·합체·누설·파단. 초기 길이·깊이는 CI 출력이 아니라 FW가 별도 샘플링 | `(ML16341B052)Crack initiation.txt`, PDF 14, “return the initiation time and location”; 같은 쪽, “before entering the time-looping structure of the xLPR code”; 같은 쪽, “they do not calculate the initial crack-specific length and depth”. TIFFANY 연결은 B048 PDF 11의 위 인용 |
| C202 / PWSCC CI 매개변수 개발·검증 | 실험실 데이터·발전소 현장 데이터 및 응력·온도 등 설명변수와 그 불확실성 | PWSCC CI 세 모델의 추천 매개변수·분포·검증 결과 → B052의 SCC CI 입력을 설정하는 근거. 별도 런타임 모듈 호출은 확인되지 않음 | `(ML19337C202)PWSCC initiation.txt`, PDF 18, “Develop statistical fits for the PWSCC initiation models”; PDF 19, “the distributions assigned to model parameters, which are derived in this report”; 같은 쪽, “recommended PWSCC initiation model parameters for xLPR Version 2.0” |
| B046 / KPW·KTW | FW의 현재 균열·관 형상 및 압력·자중·열팽창·WRS에 의한 응력. 현재 균열 상태는 앞선 성장·합체·유형 갱신의 결과 | 이상화된 표면/관통균열 K → FW → CGR. 전이균열에는 FW가 CT와의 인터페이스를 처리 | `(ML16341B046)Stress intensity factors.txt`, PDF 13, “internal pressure, dead weight, thermal expansion, and weld residual stresses”; PDF 62, “the Framework feeds the calculated stress intensity factors”; 같은 쪽, “handles the interface between the K-Solutions modules and the Crack Transition module” |
| B051 / CGR | K-Solutions의 PWSCC K; TIFFANY 표의 피로 K 최소/최대·온도·rise time; CT의 K 보정계수; FW의 재료·환경·사이클 빈도·위치별 매개변수 | 균열선단 위치별 PWSCC·피로 성장률 → FW가 적분해 크기·형상·위치 갱신 → 유형 갱신·합체·전이·안정성·COD·누설·ISI | `(ML16341B051)Crack growth and coalescence.txt`, PDF 76, “stress intensity factors needed for the PWSCC CGR calculation”; 같은 쪽, “tables generated by the TIFFANY module”; PDF 70, “The sum of all CGRs is returned to the Framework for integration” |
| B051 / Coalescence | FW의 활성 원주방향 균열 배열·위치·유형·형상·관 형상·합체 매개변수. 시간 루프 목록상 성장/유형 갱신 뒤 | 합체된 균열과 흡수된 균열의 갱신 배열 → FW → 유형 갱신·CT·안정성·COD 등 및 다음 스텝 K | `(ML16341B051)Crack growth and coalescence.txt`, PDF 104, “updates the crack configuration”; 같은 쪽, “until no pair of active cracks satisfies coalescence criteria”; PDF 109, “at least each active circumferential crack” |
| B044 / CT | FW의 관 형상·ID/OD 균열 길이・방향. 개요는 하중 정보도 언급하나, PDF 49의 명시적 인수표는 형상·방향으로 구성 | ID/OD의 K 및 COD 보정계수 → FW가 이상화 K/COD에 적용 → 성장·누설 계산. CT가 성장 적분 자체를 수행하지 않음 | `(ML16341B044)Crack transition.txt`, PDF 45, “It outputs K and COD correction factors”; 같은 쪽, “for subsequent use in crack growth and leak rate”; PDF 49, “CT Module input parameters”. 이상화 해의 출처 구분은 PDF 14, “applying correction factors to the K and COD solutions for idealized TWCs” |
| B050 / Stability | FW의 현재 균열 배열·형상과 입력 데이터의 관 형상·물성·하중. 표면/관통, 축/원주별 모듈 선택 | 불안정 여부·현재값/임계값 비율 → FW의 파단 판정·기록·루프 정지 판단. 누설률을 입력으로 받아 안정성을 정하는 직렬 관계는 확인되지 않음 | `(ML16341B050)Crack stability.txt`, PDF 17, “Based on input pipe/crack geometries, pipe material properties, and loads”; 같은 쪽, “Predicted failure, yes or no”; PDF 34, “The module relies on the xLPR Framework to sample any random variables” |
| B053 / CrCOD·AxCOD | 입력 데이터의 관 형상·물성·하중 + FW의 현재 관통/전이균열 형상. AxCOD에는 평균 hoop WRS도 입력; CrCOD에는 WRS 입력 없음 | ID·중간·OD의 COD → FW에서 전이 보정과 개구 형상 처리 → COA/누설 계산 → 별도 누설감지 처리 | `(ML16341B053)Crack opening displacement.txt`, PDF 72, “They receive information on crack geometry from the Computational Framework”; 같은 쪽, “They output COD at the inner diameter, mid-thickness, and outer diameter locations”; PDF 15, “along with the TWC length, as part of the leak-rate analyses” |
| B047 / LEAPOR 및 런타임 누설 계산 | 전처리: 균열 길이·COD/개구 면적 격자, 기구별 morphology, 압력·온도 등. 런타임: FW가 현재 균열 길이·COD/COA와 운전 조건으로 표 조회 | 전처리 LEAPOR → 누설률 표. 런타임 FW 보간·ID/OD 보정·불확실성 처리 → 균열별/총 누설률 → FW 출력·누설감지. ISI의 POD 입력이 누설률인 것은 아님 | `(ML16341B047)Leak rate.txt`, PDF 13, “the LEAPOR code is run as a preprocessor”; 같은 쪽, “The Framework uses these tables during runtime”; 같은 쪽, “the Framework then applies modifications to this leak rate”; 누설감지와 ISI 구분은 `(ML19337C165)Source and treatment of uncertainties.txt`, PDF 174, “The Framework implements the online leakage detection independent from ISI” |
| B045 / ISI | FW의 검사 일정, 현재 실제 균열 크기·두께/잔여 ligament, 방향·용접/완화 configuration, POD·sizing 매개변수·보수 임계값 | POD 및 검출 조건부 POR → FW 저장 → 후처리에서 검사 고려 누설·파단 위험 계산. 루프에서 보수를 추첨해 균열을 제거하는 것으로 해석하면 안 됨 | `(ML16341B045)Inservice inspection.txt`, PDF 52, “the inspection routine that calculates POD”; 같은 쪽, “the evaluation routine that calculates POR”; PDF 59, “The ISI routines are called for each active crack at each scheduled inspection”; PDF 46, “The adjustment for inspection is performed after simulation” |
| C165 / FW 및 불확실성 구조 | 사용자 입력·분포·샘플링 선택, TIFFANY/LEAPOR 표, 개별 물리 모듈 출력 | FW가 샘플링·변환·호출·상태배열·오류·결과를 연결. 문서 자체는 전체 구조·불확실성 설명이며, 마지막에 실행하는 독립 uncertainty DLL은 확인되지 않음 | `(ML19337C165)Source and treatment of uncertainties.txt`, PDF 39, “coordinates execution of the independent, deterministic modules and passes information between modules”; PDF 41, “lookup tables are stored in individual text files”; PDF 46, “an outer loop to sample epistemic variables and an inner loop to sample aleatory variables” |

## 4. 시뮬레이션 1회와 시간 루프의 평가 순서

### 4.1 전처리와 확률 샘플링의 위치

1. **[원문] 해석 준비/전처리:** 입력 Excel에서 TIFFANY와 LEAPOR를 구동하여 과도 파라미터 표와 누설률 표를 생성한다. FW는 시뮬레이션 시작 시 이를 불러온다. 이는 매 시간 스텝에서 TIFFANY 열전도 해석과 LEAPOR 유동 해석을 재실행한다는 뜻이 아니다.
   - `(ML19337C165)Source and treatment of uncertainties.txt`, PDF 41, “they are run from the Excel Inputs Spreadsheet”; 같은 쪽, “preprocessing mode to produce transient parameter and leak rate look-up tables”.
2. **[원문] 확률 구조:** 바깥 epistemic 샘플링 루프와 안쪽 aleatory 샘플링 루프가 있다. 다음의 deterministic realization은 주어진 한 입력 집합으로 계산한다. 이 확률 루프와 운전시간 스텝 루프를 혼동하지 않는다.
   - `(ML19337C165)Source and treatment of uncertainties.txt`, PDF 46, “an outer loop to sample epistemic variables and an inner loop to sample aleatory variables”; PDF 42, “a single realization using a single set of inputs”.
3. **[원문] 입력 공유:** 기본적으로 입력은 realization당 한 번 샘플링하며 공간 변동을 나타내는 일부 입력은 subunit/두께 위치별로 독립 샘플링한다. 동일 샘플 값은 필요한 여러 모듈에 공통으로 전달한다. 모듈 호출마다 재샘플링하는 구조로 설명해서는 안 된다. 세부 샘플링 빈도는 각 입력의 정의를 따른다.
   - `(ML19337C165)Source and treatment of uncertainties.txt`, PDF 44, “Each input is sampled once per realization”; 같은 쪽, “the same input value is used for all modules”.

### 4.2 한 realization의 초기화 — 시간 루프 밖

다음 순서는 C165 PDF 42쪽의 열거 순서를 따른 **[원문]**이다. 다만 이 항목들을 모두 별도 DLL로 해석할 근거는 없다.

1. 공간·시간 이산화.
2. 형상 계산.
3. 재료 물성 계산.
4. 공간 변동 처리.
5. 응력 계산.
6. 하중 한계 계산.
7. 이산 시간구간 구성.
8. 균열 속성 초기화.
9. DLL을 위한 추가 입력 처리.
10. 초기 결함 계산.
11. 필요한 CI DLL 호출.
12. 균열 발생 기구(PWSCC/피로) 식별.
13. 발생 시각을 calendar time으로 변환.
14. 발생 시각 순으로 균열 정렬.

근거: `(ML19337C165)Source and treatment of uncertainties.txt`, PDF 42, “space and time discretization”, “additional input processing for DLLs”, “convert initiation times to calendar time”, “order cracks by arrival time”.

**[원문] CI의 시간구간 처리는 메인 시간 루프와 별개다.** FW는 응력·온도·수화학·완화 조건이 달라지는 구간을 먼저 구성하고 CI에 제공한다. CI는 각 subunit·방향·기구의 발생 시각/위치를 계산한다. 따라서 시간 의존 조건을 반영한다고 해서 CI DLL을 메인 시간 루프 매 스텝마다 호출하는 것은 아니다.

근거: `(ML16341B052)Crack initiation.txt`, PDF 14, “before entering the time-looping structure of the xLPR code”; PDF 15, “Incremental damage is calculated for each discrete time interval”. 같은 PDF 15쪽은 CI 도식의 looping/routing이 명시적 요구사항은 아니라고 제한한다: “the looping and routing suggested in Figures 4 and 5 are not explicitly required”.

**[원문] 초기 길이·깊이는 FW가 사용자 분포에서 샘플링한다.** CI가 초기 치수까지 출력한다는 설명은 틀리다. `(ML16341B052)Crack initiation.txt`, PDF 14, “These crack properties are sampled directly by the xLPR computational Framework”.

### 4.3 메인 시간 스텝 루프 — 직접 명시된 순서

아래 전체는 **[원문]**이며 C165 §3.2.2 PDF 43–44쪽의 항목 순서를 옮겼다. 원문은 각 분기를 “as needed”로 제한하므로 모든 스텝에서 모든 DLL을 무조건 호출한다고 해석하지 않는다.

```text
현재 시간 스텝
  시스템 속성·조건 갱신(필요 시)
    정상 운전 온도·압력·산소 농도
    물리적/화학적 완화
    활성 과도와 사이클 수
    균열 속성에 의존하지 않는 응력 계산

  축방향 균열 진행(필요 시)
    새 축방향 균열 활성화
    K-solution DLL 호출
    K 계산
    crack growth DLL 호출
    균열 유형 갱신
    crack transition DLL 호출
    안정성 평가
      crack stability DLL 호출
      crack stability call reduction 계산
    COD DLL 호출
    누설률 계산
    ISI DLL 호출(검사 일정 조건)

  원주방향 균열 진행(필요 시)
    새 원주방향 균열 활성화
    K-solution DLL 호출
    K 계산
    crack growth DLL 호출
    균열 유형 갱신
    coalescence DLL 호출
    균열 유형 갱신
    crack transition DLL 호출
    안정성 평가
      crack stability DLL 호출
      crack stability call reduction 계산
    COD DLL 호출
    누설률 계산
    ISI DLL 호출(검사 일정 조건)

  다음 시간 스텝으로 진행
  파단 또는 해석기간 종료 시 중지
```

근거: `(ML19337C165)Source and treatment of uncertainties.txt`, PDF 43, “call K-solution DLLs”, “perform K calculations”, “call crack growth DLL”, “update crack type”, “call coalescence DLL”, “call crack transition DLL”, “call crack stability DLLs”, “perform crack stability call reduction calculations”, “call COD DLL”; PDF 44, “Perform leak rate calculations”, “call ISI DLL”.

**[원문] 성장 DLL 호출 내부에도 중첩 구조가 있다.** FW가 활성 균열별·균열선단의 대표 위치별로 입력을 선정하여 CGR을 평가하고 시간 적분한다. CGR 내부 피로 함수는 활성 과도 성분마다 호출되며 PWSCC 및 피로 성장률을 합산하여 FW에 반환한다. FW의 적분·치수 갱신과 CGR 함수의 성장률 계산은 구분해야 한다.

근거: `(ML16341B051)Crack growth and coalescence.txt`, PDF 69, “varying stress intensity factor on the advancing crack front”; PDF 70, “The fatigue CGR function is called once for each active transient component”; 같은 쪽, “The sum of all CGRs is returned to the Framework for integration”.

**[원문] 합체는 한 번의 단순 쌍 비교로 끝나지 않는다.** 모듈 안에서 활성 균열 쌍을 반복 검사하고 합체 후 배열을 갱신하며 더 이상 합체 조건을 만족하는 쌍이 없을 때 반환한다. 축방향 합체를 원주방향과 대칭으로 추가해서는 안 된다.

근거: `(ML16341B051)Crack growth and coalescence.txt`, PDF 104, “The iterative procedure continues until no pair of active cracks satisfies coalescence criteria”; `(ML19337C165)Source and treatment of uncertainties.txt`, PDF 136, “Axial cracks are neglected when applying coalescence rules”.

### 4.4 호출 순서와 데이터 의존성의 차이 — CT 피드백

위 순서에 CT가 성장 뒤에 있다고 해서 **현재 성장 계산에 전이 보정을 사용하지 않는다**고 결론내릴 수 없다.

- **[원문]** CGR에 필요한 PWSCC K는 K-Solutions가 계산하고, 피로 K 등은 TIFFANY 표에서 가져오며, 전이균열에는 CT의 scaling factor를 적용한다. `(ML16341B051)Crack growth and coalescence.txt`, PDF 76, “The Transitioning Crack module calculates scaling factors”; 같은 쪽, “appropriate for the transitioning crack shape”.
- **[원문]** CT 호출 조건은 활성 SC의 `A/t ≥ 0.95`, 또는 전이균열의 `θ1/θ2` 혹은 `a1/a2 > 1.05`다. `(ML16341B044)Crack transition.txt`, PDF 46, “Any active surface crack where A/t ≥0.95”; 같은 쪽, “Any transitioning crack where θ1/θ2 or a1/a2 >1.05”.
- **[원문]** CT 인터페이스에는 호출 후 현재 스텝 계산뿐 아니라 다음 스텝 계산도 명시되어 있다. `(ML16341B044)Crack transition.txt`, PDF 46, “at the current time step after”; 같은 쪽, “at the next time step after”.
- **[추론]** 따라서 계산은 매 스텝마다 시작 상태로 되돌아가는 단방향 사슬이 아니다. FW가 유지하는 균열 상태와 전이 보정 정보가 이후 계산 및 다음 스텝의 K/CGR 입력으로 이어지는 피드백을 포함한다. CT를 CGR 앞 또는 뒤 한 자리에만 두는 데이터 흐름도는 이 상태 전달을 생략한다.
- **확인 불가:** CT 계수의 정확한 변수명·저장 시점·캐시 갱신과 최초 전이 시의 동일 스텝 재평가 여부. B044 PDF 47–48의 Fig.22 도형 내부는 제공 텍스트에서 추출되지 않아, 그 그림을 근거로 세부 분기를 확정할 수 없다. Framework 코드/SDD 또는 해당 그림의 직접 시각 확인이 필요하다. 본 조사에서는 추측하여 채우지 않았다.

### 4.5 안정성·COD·누설·ISI는 같은 균열 배열을 소비하는 평가 단계

**[원문]** C165 PDF 45는 stability/leak rate/ISI가 최종 균열 배열을 사용하며 균열이나 환경적 민감도를 변경하지 않는다고 설명한다. 따라서 위 실행 목록이 `안정성 → COD → 누설 → ISI`여도, 모든 단계가 바로 앞 단계 출력만을 유일한 입력으로 받는 것은 아니다.

근거: `(ML19337C165)Source and treatment of uncertainties.txt`, PDF 45, “These modules do not modify the cracks or environmental susceptibility to cracking”.

- **[원문] COD → 누설**은 직접적인 데이터 의존성이 있다. FW가 centerline COD와 가정한 개구 형상을 결합하여 COA를 만들고 표에서 누설률을 보간한다. `(ML19337C165)Source and treatment of uncertainties.txt`, PDF 144, “provides the crack opening area”; 같은 쪽, “used to interpolate a leak rate from look-up tables”.
- **[원문] 안정성**은 균열 형상·물성·하중에 따른 임계값/현재값 비교를 수행한다. 안정성 출력이 COD의 필수 수치 입력이라는 근거는 확인되지 않았다. B050 PDF 17과 B053 PDF 72의 입력 설명을 구분해 사용한다.
- **[원문] ISI**는 현재 실제 균열 크기를 평가한다. 루프에서 각 검사 시점의 POD/POR를 계산·저장하되, UT 검사 효과는 시뮬레이션 후 적용한다. `(ML16341B045)Inservice inspection.txt`, PDF 46, “they are not applied”; 같은 쪽, “as a post-processing function of the xLPR Framework”.
- **[원문] ISI 후처리**는 검사 미고려 위험에 부품이 아직 보수되지 않았을 확률을 곱해 검사 고려 위험을 계산한다. `(ML16341B045)Inservice inspection.txt`, PDF 48, “the probability that component repair has not yet occurred”. 온라인 누설감지는 ISI와 별도로 FW가 구현한다(C165 PDF 174).

**[추론]** 그러므로 학습용 데이터 흐름은 `갱신된 균열 배열 → {안정성, COD→누설, ISI}`처럼 소비처를 분기해 표시하고, 옆에 실제 평가 목록의 순서를 별도로 적는 것이 정확하다.

## 5. 권장 읽기·정리 순서

아래 순서는 **[추론: 학습 제안]**이며 공식 DLL 호출 순서라고 주장하지 않는다. 초기화와 전처리의 입력을 먼저 이해하고, 발생→전파→판정으로 이동한다. 전체 구조를 먼저 잡는 데 C165 §3을 사용하고, 불확실성 세부 장은 각 모델을 읽은 뒤 대응해서 읽는다.

| 읽기 순번 | 보고서 | 정리할 질문과 이유 |
|---|---|---|
| 1 | **C165 Sources and Treatment of Uncertainties — 우선 §1·§3만** | FW·전처리·두 확률 샘플링 루프·realization·메인 시간 루프를 구분한다. PDF 42–44의 공식 평가 순서를 전체 목차로 삼는다. 나머지 장은 각 모델과 병행하고 마지막에 다시 검토한다. |
| 2 | **B049 Welding Residual Stresses** | CI/K의 상류 입력인 WRS 프로파일·두께 방향 상관·샘플링을 이해한다. FE 해석 개발 과정과 xLPR 런타임을 구분한다. |
| 3 | **B048 Cyclic Stress Intensity Factors** | TIFFANY 전처리와 lookup table 구조, 피로 CI/CGR에 공급하는 응력·K·rise time을 정리한다. 내부 K 해석을 위한 B046은 뒤에서 연결한다. |
| 4 | **B052 Crack Initiation** | subunit·방향·기구, 시간구간별 누적 손상, 루프 밖 발생 시각 배열과 루프 안 활성화를 정리한다. |
| 5 | **C202 PWSCC Initiation** | 바로 앞 CI의 세 PWSCC 모델을 무엇으로 보정했는지, 추천 매개변수·분포와 검증의 의미를 정리한다. 독립 런타임 단계로 번호를 붙이지 않는다. |
| 6 | **B046 Stress Intensity Factors** | 현재 균열 형상·응력 → KPW/KTW → 성장의 연결을 정리한다. B048의 과도 K와 정상/지속하중 K를 구분한다. |
| 7 | **B051 Crack Growth and Coalescence — 완료** | 새로 전면 정리하지 않고 기존 결과의 인터페이스만 점검한다: K·TIFFANY→CGR→FW 적분→합체, 원주방향 한정, 유형 갱신과 CT 연결. |
| 8 | **B044 Crack Transition** | SC/TRC/TWC 기준, ID/OD 비대칭, 이상화 K/COD에 대한 보정계수 및 다음 스텝 피드백을 정리한다. |
| 9 | **B050 Crack Stability** | 원문 평가 순서에서 CT 뒤, COD 앞이다. 표면/관통·축/원주별 파단 판정과 FW의 call reduction을 구분한다. |
| 10 | **B053 Crack Opening Displacement** | 갱신된 균열 형상과 하중·물성에서 ID/OD COD가 어떻게 나오는지, CT 보정과 COA 변환을 연결한다. |
| 11 | **B047 Leak Rate** | LEAPOR 전처리와 런타임 FW의 표 보간·보정·불확실성 적용을 분리하여 정리한다. |
| 12 | **B045 Inservice Inspection** | 검사 시점 계산(POD/POR)과 해석 후 위험 가중을 분리한다. 누설감지와 UT 검사는 별도다. |

이후 **C165의 모델별 불확실성 장을 재검토**하여 모듈별 입력 분포와 상관, 공통 입력의 재사용, 오차·편향의 전달을 연결한다. 이는 13번째 독립 모델이 아니라 첫 번째 문서의 나머지를 읽는 것이다.

특히 **B051이 이미 완료됐다는 사실은 실행 순서상 B051이 첫 단계라는 뜻이 아니다.** 다음 새 정리는 위 표의 미완료 상류 문서부터 진행하고, B051은 연결 확인에 사용하면 된다.

## 6. 확인 불가·해석 한계

1. **특정 실행본의 실제 호출 로그:** 제공된 것은 보고서 텍스트다. 소스 코드/GoldSim 파일/실행 추적 자료를 사용하지 않았으므로 보고서와 현재 실행본의 일치 여부는 확인 불가다.
2. **모든 세부 조건과 재호출:** C165 목록은 전체 평가 순서다. 실제 무균열 스킵, error branch, call reduction의 전체 알고리즘, 이벤트 경계에서의 재계산 횟수는 이 조사로 확정하지 않는다. “필요 시”를 보존한다.
3. **CT의 정확한 스텝 간 저장·적용 타이밍:** 현재/다음 스텝 관련 요구사항과 CGR 의존성은 확인했으나 Fig.22 내부 및 FW 실행 구현은 확인 불가다. 모순을 해소하기 위해 가상의 추가 호출을 넣지 않았다.
4. **WRS 런타임 DLL:** WRS 보고서는 FE 기반 입력 프로파일·불확실성 개발을 기술한다. 매 realization 또는 매 스텝에 용접 FE를 다시 돌리는 WRS DLL은 확인되지 않았다.
5. **C202 및 C165의 독립 물리 DLL:** 문서는 각각 매개변수 보정과 전체 불확실성/FW 구조의 근거다. 12편을 12개 순차 DLL로 대응시킬 근거는 확인되지 않았다.
6. **원문 오기/도식 제한:** B045 일부 상호참조가 “Section 0”으로 추출된다. 실제 해당 내용은 §3에 있다. B044 PDF 47–48 및 B046 PDF 63의 도형 내부는 텍스트가 거의 없어 그림 전체를 읽었다고 주장하지 않는다. 전체 순서 판정에는 C165 PDF 42–44의 본문 목록을 사용했다.

## 7. Git 인계 상태

시작 시 `git pull`을 실행했으나 `error: cannot open '.git/FETCH_HEAD': Permission denied`로 실패했다. 현재 세션의 승인 정책은 `never`이며 권한 승인 요청이 지원되지 않는다. 상위 도구 지침은 `sandbox_permissions` 제공도 금지하므로, 프로젝트 지침의 승인 요청 재실행은 수행할 수 없다. 일반 실행을 반복하거나 샌드박스를 해제하지 않았다.

결과 파일은 `round43/codex.md` 하나만 작성했다. `.git` 쓰기가 제한된 현재 환경에서 커밋·푸시 및 원격 반영 확인은 **미완료**다. 커밋 ID는 없음. 다른 작업의 수정·삭제·미추적 파일은 포함하지 않았다. Claude/상위 실행 환경에서 이 파일만 add/commit/push하는 인계가 필요하다.
