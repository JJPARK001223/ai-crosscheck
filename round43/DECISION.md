# round43 — xLPR 평가(호출) 순서 및 정리 순서 결정 (교차검증 반영 최종)

단계: ① blind(claude.md / codex.md) → ② 상호 검증(claude_review.md / codex_review.md) → ③ 본 결정. 최종 채택은 사용자.

## 공통 (Claude·Codex 독립 결과 일치, 서로의 검증에서도 유지)
- 근거: (ML19337C165) Source and treatment of uncertainties §3.2.2, PDF p.42~44 (인쇄 p.21~23). 순서가 본문에 직접 열거됨. 두 AI가 원문 대조로 재확인.
- 전처리: TIFFANY·LEAPOR는 Excel 사전처리로 lookup table 생성 → 시작 시 Framework가 읽음(PDF p.41).
- 초기화 → Crack initiation(시간 루프 밖, 균열을 도래 시간순 정렬) → 시간 루프 → 다음 스텝, 파단/종료 시 정지.
- 루프 안: 축방향 [K-solution → K 계산 → 성장 → 유형갱신 → 천이 → 안정성 → COD → 누설률 → ISI], 원주방향은 성장 뒤에 합체+유형갱신 추가. 합체는 원주방향만(C165 PDF p.131 "Axial cracks are neglected with respect to coalescence considerations").
- 초기 균열 길이·깊이는 CI가 아니라 Framework가 샘플링(B052 p.14).

## 교차검증에서 보정된 점 (확정)
1. C202(PWSCC initiation)는 독립 런타임 단계가 아니라 B052 SCC 매개변수 개발·검증 보고서. 12편 ≠ 12개 순차 모듈.
2. 목록 순서 ≠ 데이터 의존성: 안정성·누설·ISI는 같은 최종 균열 배열 소비(C165 p.45), COD→누설만 직접 의존. ISI 효과는 시뮬레이션 후 후처리(B045 p.46), POD/POR만 루프에서 계산, 온라인 누설감지는 ISI와 별개.
3. 모든 DLL이 매 스텝 무조건 호출되는 것이 아님 — 원문 "as needed". "초기화 DLL"이 아니라 "crack initiation DLL(필요 시)", "초기 시각"이 아니라 "개시 시각".
4. 호출 조건 정정(Claude 초안 불완전 → 보완):
   - 안정성: (원주 TWC) 최초 TWC/천이 출현, 하중 변경, 물성 변경 **+ 성장해 θcrit 95% 도달 시 재호출**(B050 TWCF-10*). (축방향) 활성 축방향 TWC 발생, c/ccrit > 0.9(RACS-1*) / 재호출 ≥ 0.9(RACS-10*), 활성 축 SC 존재; p/pcrit ≥ 1이면 SC→TWC 변경(RACS-9*) — 루프 목록 밖의 유형 변경이 있음.
   - COD: 원주 CrCOD는 활성 이상화/천이 관통균열(RCCOD-8*), 축 AxCOD는 a/t≥0.95 이후 모든 스텝(RAxCOD-14*) — 방향별로 구분.
   - CT: A/t ≥ 0.95 또는 θ1/θ2·a1/a2 > 1.05(RTC-16*); 호출 후 현재·다음 스텝 계산(RTC-21*/22*) → 성장·누설에 보정계수 피드백 가능. 저장·갱신 시점은 확인 불가.
5. 누설률은 ID 표 보간 + ID/OD 평균 보정·불확실성 처리(B047 p.13, C165 p.81·144), 성장은 "CGR 함수(성장률 합산) vs Framework 시간 적분" 분리, 합체는 모듈 내부 반복(B051 p.104).
6. 쪽 표기는 PDF 쪽(=인쇄 쪽+11 정도, 파일마다 다름)과 인쇄 쪽을 구분해 적을 것(예: B047 PDF 13 = 인쇄 2).

## 충돌·정정 기록
- 읽기 순서에서 B046 위치만 상이(Claude: initiation 직후, Codex: 성장 직전) → 루프 순서(K→성장)에 맞는 Codex안 채택.
- Claude가 처음 "Codex 인용 부정확"이라 지적한 것은 Claude 오판 — C165에는 p.131 "with respect to…"와 p.136 "when applying…" 두 문장이 모두 있음(원문 재확인). Codex 인용 정상.
- Codex 자기정정: C165 §14.1은 PDF 173, §14.2는 174.

## 최종 결정 — 정리 순서 (학습 제안이며 공식 DLL 순서 아님)
완료: B051 Crack growth & coalescence.
남은 순서: 1) C165 §1·§3(전체 흐름) → 2) B049 WRS → 3) B048 TIFFANY → 4) B052 Crack initiation → 5) C202 PWSCC initiation(B052 보조) → 6) B046 Stress intensity factors → (B051 완료, 연결 점검만) → 7) B044 Crack transition → 8) B050 Crack stability → 9) B053 COD → 10) B047 Leak rate → 11) B045 ISI → 마지막에 C165 나머지 장.
다음 착수: **C165 §3(+§1)**, 이어서 **B049 WRS**.

## 한계
실제 실행본 호출 로그·GoldSim 모델·C165 Fig 3-1·B044 Fig 22 그림 내부는 양쪽 모두 미확인(본문 열거 목록 기준). 두 AI가 같은 결론이어도 하나의 원문 목록에 의존하므로 코드 수준 검증은 아님.

## Git 상태
Codex 교차검증은 `Invoke-CodexStage.ps1`(--approve-for-me, approval on-request) 실행. codex_review.md는 작성됐으나 Codex 단계에서 커밋되지 않아 Claude가 지정 파일만 커밋.
