# ai-crosscheck

Claude Code + Codex 교차검증 협업 워크스페이스. 한 PC · 개인 GitHub · 배심원2/판사 모델.

## 자동 모드 — 한 번 실행 (권장)

```powershell
cd "J:\Desktop\공학\ai-crosscheck"
.\orchestrate.ps1 "이번에 풀 문제"
```

스크립트가 알아서: `PROBLEM.md` 기록 → 두 AI **blind 병렬** 독립 조사 → 서로 교차검증
→ `DECISION.md` 초안 → 화면에 출력. 매 단계 git commit/push 도 자동.
마지막에 `DECISION.md` 의 **`## 내 최종 결정`** 만 내가 채우면 끝.

- 이전 라운드 내용은 `rounds/<시각>/` 로 자동 보관 후 새 라운드 시작.
- git(pull/commit/push)은 스크립트가, 파일 작성은 각 AI(`claude -p` / `codex exec`)가 담당.
- 전제: `claude`, `codex` 둘 다 PATH에 있고 로그인 완료. PowerShell 5.1 이상.

## 수동 모드 — 쓰는 순서 (매번)

1. **문제 적기** — `PROBLEM.md`에 이번에 풀 문제를 쓴다. 특정 답으로 유도하지 말 것.
2. **두 AI에게 각각 (서로 안 보게)**
   - Claude 창: `PROBLEM.md 읽고 독립 조사해서 round1/claude.md 에 정리해줘. Codex 결과는 보지 마.`
   - Codex 창: `PROBLEM.md 읽고 독립 조사해서 round1/codex.md 에 정리해줘. Claude 결과는 보지 마.`
3. **커밋** — 각 AI에게 "커밋하고 푸시해줘".
4. **교차검증** — Claude: `round1/codex.md 읽고 더 맞는 점/틀린 점/내가 놓친 점 찾아줘.` Codex도 똑같이(claude.md 검증).
5. **최종 결정** — 내가 `DECISION.md`에: 공통 의견 / 충돌(제일 중요) / 내 최종 결정+이유.

## 두 마디만 기억

- "커밋해줘" = 지금까지 작업을 GitHub에 올려 (유의미한 결과마다)
- "풀 해줘" = 상대가 올린 최신 작업을 받아와 (다른 AI 작업 이어받기 전)

## 규칙 파일

- `CLAUDE.md` — Claude가 자동으로 읽는 작업 규칙
- `AGENTS.md` — Codex가 자동으로 읽는 작업 규칙

## 하면 안 되는 것

- 처음부터 한 AI 답을 다른 AI에게 보여주기 (앵커링)
- 비번·API키·개인정보를 파일이나 커밋에 넣기
- 둘 다 같은 결론이라고 무조건 안심 (실제 실행으로 확인)
- AI 말을 근거로 삼기 (근거 = 코드·실행결과·데이터)

라운드가 늘면 `round2/`, `round3/` … 폴더를 같은 방식으로 만든다.
