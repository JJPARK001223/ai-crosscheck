# round43 — Claude의 codex.md 교차검증

방식: codex.md의 핵심 주장을 원문 텍스트(round43/txt)로 직접 대조. "Codex가 말했다"는 근거로 쓰지 않음.

## 원문으로 확인되어 맞는 점
- 루프 순서·원주방향만 합체: C165 PDF p.42~44 (내 claude.md와 일치).
- 입력은 realization당 1회 샘플링(일부 subunit/두께별): C165 p.44 "Each input is sampled once per realization (except for several inputs … per subunit or through the thickness)". 맞음.
- ISI 검사 효과는 시뮬레이션 후 후처리 적용: B045 PDF p.46(txt L2774) "The adjustment for inspection is performed after simulation, as a post-processing …". 맞음. ISI 루틴은 예정 검사마다 활성 균열별 호출: B045 L3857. 맞음.
- 온라인 누설감지는 ISI와 별도: C165 L9553 "Framework implements the online leakage detection independent from ISI". 맞음.
- CT 호출 조건(A/t≥0.95, θ1/θ2·a1/a2>1.05)과 현재/다음 스텝 계산(RTC-16, 21, 22): 직접 확인(B044 PDF p.46). 맞음.

## Codex가 Claude보다 잘 잡은 점 (Claude 수용)
1. C202(PWSCC initiation)는 독립 런타임 모듈이 아니라 B052 SCC 매개변수 개발·검증 보고서.
2. 호출 순서 ≠ 데이터 의존성(안정성·누설·ISI는 같은 최종 균열 배열 소비; COD→누설만 직접).
3. ISI 효과는 후처리 — Claude 초안은 루프 단계로만 적어 오해 소지.
4. CT의 피드백(현재·다음 스텝) 가능성. 세부 타이밍은 확인 불가(Fig.22 미확인).
5. 12편이 12개 순차 모듈이 아님, "as needed" 조건부 호출.

## Codex 결과의 문제/주의
- (정정됨) 처음엔 codex.md의 C165 인용("...when applying coalescence rules", p.136)이 부정확하다고 썼으나, 원문 재확인 결과 두 문장이 서로 다른 위치에 모두 있음: p.131(txt L6854) "neglected with respect to coalescence considerations", p.136(txt L7082) "neglected when applying …". Codex 인용은 오류 아님. Claude 쪽 오판이었음.
- Codex가 새로 지적한 Stability 재호출 조건 직접 확인: B050 TWCF-10*(txt L2258) TWC 성장이 θcrit의 95% 도달 시 재호출 — Claude의 호출 조건 3개는 불완전(맞음). 축방향 RACS-1* c/ccrit > 0.9 (L2765) vs RACS-10* ≥ 0.9 (L2827) 부등호 차이 확인.
- 읽기 순서 제안이 14개 항목 중 "C165 나머지 장은 마지막" 등 학습 제안일 뿐 공식 순서가 아님을 Codex 스스로 [추론]으로 표시 — 적절.
- git: Codex 당시 세션은 approval never라 .git 쓰기 불가였음. 이후 Invoke-CodexStage.ps1(--approve-for-me)로 개선됨(커밋 483ad68).

## Claude가 놓친 점
- C202를 독립 단계로 취급할 뻔함. 12편=12모듈 가정.

## 충돌
- 읽기 순서에서 B046 위치만 상이(Claude: initiation 직후, Codex: 성장 직전). 루프 순서(K→성장)에 맞는 Codex안 채택(DECISION.md 반영).

## 한계
- 양쪽 모두 Figure 3-1·Fig.22 그림 내부, 실제 실행본 호출 로그 미확인. 둘이 같은 결론이어도 본문 열거 목록 하나에 의존하므로 "보고서 기준 순서"이며 코드 검증은 아님.
