# round43 — xLPR 평가(호출) 순서 및 정리 순서 결정

## 공통 (Claude·Codex 독립 결과 일치)
- 근거: (ML19337C165) Source and treatment of uncertainties §3.2.2, PDF p.42~44 (인쇄 p.21~23). 순서가 본문에 직접 열거됨.
- 전처리: TIFFANY·LEAPOR는 Excel 사전처리로 lookup table 생성 → 시작 시 Framework가 읽음(PDF p.41).
- 초기화 → Crack initiation(시간 루프 밖, 균열을 도래 시간순 정렬) → 시간 루프 → 다음 스텝, 파단/종료 시 정지.
- 루프 안: 축방향 [K-solution → 성장 → 유형갱신 → 천이 → 안정성 → COD → 누설률 → ISI], 원주방향은 성장 뒤에 합체+유형갱신 추가. 합체는 원주방향만.
- 초기 균열 길이·깊이는 CI가 아니라 Framework가 샘플링(B052 p.14).

## Codex가 추가/보정한 점 (Claude 수용)
- 12편 ≠ 12개 순차 모듈: PWSCC initiation(C202)은 B052의 SCC 초기화 매개변수 개발·검증 보고서라 독립 런타임 단계가 아님. C165는 Framework/불확실성 구조 문서.
- 목록 순서 ≠ 데이터 의존성: 안정성·누설·ISI는 같은 최종 균열 배열을 소비(COD→누설만 직접 의존). ISI의 검사 효과는 시뮬레이션 후 후처리로 적용(B045 p.46), POD/POR만 루프에서 계산.
- 천이(CT)는 성장 뒤에 나열되지만 CGR이 CT 보정계수를 쓰고 CT는 현재·다음 스텝 계산을 명시(B044 RTC-21/22) → 피드백 있음. 세부 타이밍은 확인 불가(Fig.22 그림 미확인).
- 모든 DLL이 매 스텝 무조건 호출되는 것은 아님("as needed", 호출 조건 있음).

## 충돌
- 읽기 순서: Claude는 K-solution(B046)을 initiation 다음에, Codex는 B046을 CGR 직전(6번)에 둠. 루프 순서(K → 성장)에 맞는 Codex 안을 채택.

## 최종 결정 — 정리 순서
완료: B051 Crack growth & coalescence.
남은 순서: 1) C165 §1·§3(전체 흐름) → 2) B049 WRS → 3) B048 TIFFANY → 4) B052 Crack initiation → 5) C202 PWSCC initiation(B052 보조) → 6) B046 Stress intensity factors → (B051 완료, 연결만 점검) → 7) B044 Crack transition → 8) B050 Crack stability → 9) B053 COD → 10) B047 Leak rate → 11) B045 ISI → 마지막에 C165 나머지 장.
다음 작업 착수 대상: **C165 §3(+§1)**, 이어서 **B049 WRS**.

## 한계
실제 실행본 호출 로그·GoldSim 모델·Fig 3-1 그림 자체는 미확인(본문 불릿 목록 기준). Codex는 git 권한 오류로 commit 불가.
