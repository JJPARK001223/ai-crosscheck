# round43 — Claude blind 조사: xLPR 모듈 평가 순서

근거 핵심: (ML19337C165) Source and treatment of uncertainties, 3.2.2절 Deterministic Model, PDF p.42~44 (인쇄 p.21~23). "general flow … Figure 3-1 and is outlined below" [원문].

## 1회 realization 안의 순서 [원문, C165 PDF p.42~44]
0. 사전(preprocessing): TIFFANY(→ 과도하중 K·온도·상승시간 표), LEAPOR(→ 누설률 표)는 Excel 사전처리기로 돌려 lookup table 텍스트 파일로 만들고 시뮬레이션 시작 때 Framework가 읽음 (C165 PDF p.41; Leak rate B047 p.2 / TIFFANY B048 요약).
1. Run initialization: 공간·시간 분할, 기하, 재료 물성, 공간 변동성, 응력 계산(용접잔류응력 포함), 하중 한계, 이산 시간 구간, 균열 속성 초기화, DLL용 추가 입력 처리.
2. Crack initiation (시간 루프 진입 전): 초기 결함 계산 → 초기화 DLL 호출(PWSCC/피로) → 기구 판별 → 초기 시각을 달력 시간으로 → 균열을 도래 시간순으로 정렬. (Crack initiation B052 PDF p.14: "before entering the time-looping structure")
3. Time loop (스텝마다)
   - 시스템 상태 갱신(운전 온도·압력·산소, 완화(mitigation), 활성 과도하중·사이클 수, 균열과 무관한 응력)
   - **축방향 균열**: 새 균열 개시 → K-solution DLL → 균열성장 DLL → 균열 유형 갱신 → crack transition DLL → 안정성(stability) DLL(+호출 감축 계산) → COD DLL → 누설률 계산 → ISI DLL
   - **원주방향 균열**: 새 균열 개시 → K-solution → 균열성장 → 유형 갱신 → **합체(coalescence) DLL** → 유형 갱신 → crack transition → 안정성 → COD → 누설률 → ISI
   - 다음 스텝으로; 파단 또는 종료시간이면 정지.
(주의: 축방향에는 합체 단계가 목록에 없음 — 원문 목록 그대로.)

## 모듈 역할 구분 [원문, C165 PDF p.44~45]
- 환경 조건 모듈: K 입력 변환, TIFFANY, mitigation
- 균열 배열을 바꾸는 모듈: initiation, mitigation, growth, coalescence, transition, (COD는 배열 안 바꿈)
- 최종 균열 배열을 평가하는 모듈: stability, leak rate, ISI

## 모듈별 호출 조건 [원문]
- Crack transition: surface crack A/t ≥ 0.95 또는 transitioning crack θ1/θ2 or a1/a2 > 1.05 (B044 RTC-16, PDF p.46)
- COD: 활성 이상화/천이 관통균열이 있을 때(B053 RCCOD-8), 천이 시작 a/t≥0.95 이후 모든 스텝(RAxCOD-14)
- Stability(TWC): 처음 TWC/천이균열 출현, 하중 변경, 물성 변경(완화) 때(B050)
- ISI: 예정된 검사 시점에 활성 균열마다 호출; POD·POR는 사후처리에서 조건부 위험도 계산(B045 PDF 3.1절)
- 누설률: LEAPOR 표를 런타임에 보간(ID COA 기준) (B047)

## 읽기·정리 순서 제안 (루프 순서 = 학습 순서)
이미 완료: Crack growth and coalescence.
1) Source and treatment of uncertainties §3 (Framework 전체 흐름·샘플링) → 2) Welding residual stresses(응력 입력) + Cyclic SIF/TIFFANY → 3) Crack initiation + PWSCC initiation → 4) Stress intensity factors (K-solution) → [Crack growth·coalescence 완료] → 5) Crack transition → 6) Crack stability → 7) COD → 8) Leak rate → 9) ISI.
(루프 안 순서 K→성장→합체→천이→안정성→COD→누설→ISI 와 일치)

## 한계
- 보고서의 Figure 3-1 그림 자체는 텍스트 추출로 못 봄(목록은 본문 불릿).
- 각 모듈 내부 수식 정합성은 이번 조사 범위 밖.
