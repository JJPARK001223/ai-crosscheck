# round85 — 가솔린 엔진 SCI 논문 15편 4섹션 평가 종합 보고서 (사용자 결정 기록)

## 절차 요약
1. 기존 확정 60개 논문-섹션 평가(15편×4섹션, 각 2기준=총 120개 등급)를 `round85/input/evaluation_data.md`로 고정.
2. Claude·Codex가 서로의 결과를 보지 않고 독립 작성(`claude.md`, `codex.md`) — 등급·분포 집계가 완전히 일치함을 확인(사실 보존 CONFIRMED).
3. 상호 검증(`claude_review.md`가 codex.md 검증, `codex_review.md`가 claude.md 검증) — Codex가 claude.md에서 사실 오류 6건을 발견, Claude가 재대조 후 전부 수용.
4. Claude가 Codex 단독/Claude 단독/공통 의견 3챕터로 종합해 세미나 양식 HTML 보고서 작성.

## 결과물
- `J:\Desktop\과학논문작성법 과제\SCI논문15편_교차검증_종합보고서.html` (세미나 양식 PPT 포맷 적용)
- Claude.ai Artifact: https://claude.ai/artifact/EAYHVnAvYnYd36jXNpEoYH

## 커밋
- codex.md: commit cd65033
- claude.md, claude_review.md, input/, PROBLEM.md: commit f0c7279
- codex_review.md: Codex stage B 커밋 (round85/codex_stage_B.log 참조)

## 수정된 사실 오류 (Claude → Codex 발견 → Claude 수용)
1. "No.2가 4섹션 전체 연관성 상의 유일한 사례" → No.3·5·8·13·15도 동일. 유일성 주장 삭제.
2. "No.13·14·15 중 No.13 Methodology만 중" → No.14 Abstract(하/중) 예외 누락.
3. Introduction "중/하 4편" 집계 → 구체성/연관성 두 축을 섞어 집계, No.12 누락.
4. No.1 Methodology·Results "중" 판정 근거를 하나로 합침 → 섹션별로 다른 근거(선행연구 위임 vs 정성적 서술).
5. Abstract "하" 7편을 "수치 없음"으로 일괄 요약 → No.6·10에는 설정값 수치 존재, "결과 비교수치 부족"으로 한정 필요.
6. "60개 평가항목(15편×4섹션×2기준)" 산술 불일치(15×4×2=120) → "60개 조합×2기준=120개 등급"으로 정정.

## 확인 불가로 재분류된 해석(등급은 바꾸지 않음)
- Abstract 저평가 원인=요약문 서술 관습
- Methodology·Results 연관성 전부 상=SCI(E) 심사 통과 효과
- No.9=신소재라서 알코올 문헌으로 대체 인용
- No.11="시뮬레이션 전용 연구의 구조적 약점"(→ "부족·제한적"으로 완화)

## 사용자 결정
(사용자 확인 후 기재)
