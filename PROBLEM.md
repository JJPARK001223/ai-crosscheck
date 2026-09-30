# 문제 (Round 12)

## 배경
사용자(재료공학/파괴역학 석사생)가 두 편의 선행연구 논문을 한국어로 완역해 달라고 요청함.

- 선행연구 1: Kwon, Y.W., "Revisiting Failure of Brittle Materials," J. Pressure Vessel
  Technol. 143(6), 064503 (2021). **미국 정부 저작물로 저작권 보호 대상 아님**(원문 하단에
  명시: "This material is declared a work of the U.S. Government and is not subject to
  copyright protection in the United States.")
- 선행연구 3: Kwon, Y.W.; Markoff, E.K.; DeFisher, S., "Unified Failure Criterion Based on
  Stress and Stress Gradient Conditions," Materials 17(3), 569 (2024).
  **CC BY 4.0 오픈액세스**(원문에 라이선스 명시 확인됨). 출처 표시 조건 하에 번역·재배포 허용.

Claude가 두 논문 전체를 한국어로 완역하여 아래 HTML 파일로 작성 완료함:
- `J:\Desktop\공학\claude_code\2026_09_30_선행연구_번역\선행연구1_Kwon2021_번역.html`
- `J:\Desktop\공학\claude_code\2026_09_30_선행연구_번역\선행연구3_Kwon2024_번역.html`

원문 PDF:
- `J:\Desktop\선행연구 관련\[선행연구 1] Revisintg Failure of Brittle Materials (2021-12).pdf`
- `J:\Desktop\선행연구 관련\[선행연구 3] Unified Failure Criterion Based on Stress ans Stress Gradient Conditions (2024-01).pdf`

번역 방침(사용자와 합의됨): 그림은 원본 이미지를 넣지 않고 "Fig. N" 형태로 위치만 표시함
(사용자가 원본 PDF에서 직접 확인). 수식은 원문과 동일하게 LaTeX/MathJax로 재현함.

## 조사 요청 (Codex, blind 아님 — 이미 작성된 번역본 검토)
위 두 HTML 파일을 원문 PDF와 대조하여 다음을 검토할 것:

1. **완결성**: 원문의 모든 절(섹션)과 문단이 빠짐없이 번역되었는지. 원문에는 있는데 번역본에서
   누락된 문단이나 절이 있는지.
2. **기술적 정확성**: 파괴역학·재료공학 전문용어 번역이 정확한지(예: stress gradient=응력구배,
   failure strength=파괴강도, effective stress=등가응력, critical energy release rate=임계
   에너지 해방률 등). 오역으로 인해 원문의 의미가 달라진 부분이 있는지.
3. **수식 정확성**: 번역본에 재현된 수식 (1)~(13)(선행연구 1), (1)~(9)(선행연구 3)이 원문
   수식과 일치하는지. 특히 선행연구 3의 식 (8), (9)는 원문 PDF의 폰트 인코딩이 깨져 있어
   Claude가 미시역학적으로 타당한 구조로 재구성했다고 번역본에 명시해 두었는데, 원문 PDF를
   직접 보고 실제 형태와 일치하는지, 혹은 명백히 다른 형태라면 무엇이 맞는지 확인할 것.
4. **참고문헌 정확성**: 두 논문의 References 목록(저자/연도/저널/권/페이지)이 원문과 일치하는지.
5. **저작권 판단 검증**: 위에 기재한 "미국 정부 저작물"(선행연구 1) 및 "CC BY 4.0"(선행연구 3)
   근거가 각 PDF 원문에 실제로 명시되어 있는지 원문에서 직접 재확인할 것 (이 판단에 따라 전체
   번역 작업의 저작권 적법성이 결정되므로 반드시 원문 문구를 직접 확인).

## 원하는 결과물
- 위 다섯 관점에서 **문제가 있는 부분만** 구체적으로 지적 (해당 문단/수식 인용 + 원문과의 차이 +
  수정 제안).
- 문제 없는 항목은 "문제 없음"으로 짧게 확인.
- 특히 4번(저작권 판단)은 반드시 원문에서 직접 문구를 찾아 인용하여 확인할 것 — 확인되지 않으면
  "확인 불가"라고 명시.
- 새로운 번역이나 재작성 금지. 이미 작성된 두 HTML 파일과 원문 PDF의 대조 검토만 수행.

결과를 `round12/codex.md`에 한국어로 작성. 완료 후 `git add round12/codex.md` →
`git commit -m "round12: Codex 번역 검증"` → `git push origin main`. `AGENTS.md` 규칙을 따른다.
