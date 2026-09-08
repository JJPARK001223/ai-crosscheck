# Codex blind 검증 과제 (round10)

`round10/claude.md` 를 **열지 말 것**. 독립적으로 검토.

## 대상
사용자 발표 pptx `J:\Desktop\2026_09_07.pptx` (14슬라이드, Kwon 통합 파괴 기준).
- 텍스트/수식 덤프: `round10/pptx_텍스트덤프.txt`
- 수식 이미지: `round10/image{3,4,6,7,8,9,13,14,15,16}.png`
  (image3=슬4 통합기준식, image4=슬5, image6~9=슬6, image13~15=슬10 Y유도, image16=슬11 표)

## 원문 (검증 기준, 직접 확인)
- 선1: `J:\Desktop\선행연구 관련\[선행연구 1] Revisintg Failure of Brittle Materials (2021-12).pdf`
  또는 `J:\Desktop\공학\claude_code\2026_09_01_선행연구분석\images\paper1_page2.png`
- 선3: `J:\Desktop\선행연구 관련\[선행연구 3] Unified Failure Criterion ... (2024-01).pdf`
  또는 `...\2026_09_01_선행연구분석\images\paper3_page-02.png`
- round9 결론: `DECISION_round9_발표목차5장.md`

## 검증 항목 (PROBLEM.md A~F)
1. 슬라이드4 식의 계수가 `2KY` 인데 원문(선1식13·선3식2)은 `2EY` 아닌가?
2. 슬라이드11 표: 선1 w_f=K_IC²/(2πE) 와 선3 Y=K²/E 를 "같은 물리량의 다른 기호 표기"로
   제시한 것이 타당한가? (두 값의 2π 차이 / 근접장 정규화 차이 σ=K/√(2πr) vs σ=K/√s)
3. 슬라이드10: w_f=K_I²/(2πE), K_IC=√(2πE·w_f) 를 "Y(선3) 유도"로 라벨. 선3 식(3)엔 2π가
   없어 Y=K²/E 가 되는데, 슬라이드10 유도는 선1 것 아닌가? 슬라이드11과 모순되지 않나?
4. 슬라이드6 image7 "σ_e³/2E = 변형 에너지 밀도 U" — 차원 맞나? (에너지밀도 = σ²/2E)
5. 출처·식번호 인용 정확성: 선1 식(6)(7), 선3 식(4), Karihaloo 2003 (선3 ref[39]).
6. 오타·범위: Griffith/Irwin/CZM(≠CMZ)/Karihaloo 철자, 슬라이드5 "방향별 유효응력"이
   round9에서 제거한 이방성·복합재 갈래인지.
7. 그 밖에 claude가 놓쳤을 수 있는 슬라이드별 수식/논리/출처 오류.

## 독립 재유도 요구
- 선3 식(3)+도함수를 식(2)에 대입 → Y=K²/E 가 나오는지 직접 전개.
- 선1 식(4)+(5)를 식(13)에 대입 → w_f=K²/(2πE) 가 나오는지 직접 전개.
- 두 결과의 비가 정확히 2π 인지 확인.

## 출력
- `round10/codex.md` 에: 항목별 판정(동의/이견/추가), 원문 페이지·식번호 인용, 재유도 전개.
- git add/commit/push. 샌드박스로 push 실패 시 파일 저장 + "Claude가 대신 commit 요망" 한 줄.
