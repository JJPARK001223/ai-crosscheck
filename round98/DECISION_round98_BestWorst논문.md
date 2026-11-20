# round98 — Best/Worst 논문 선정·상세분석 교차검증 결정 기록

## 절차

1. Claude가 15편 전체 인벤토리, 평가기준 정리, Best(No.5)/Worst(No.1) 선정, 두 논문 PDF 원문 전체를
   직접 열람해 Title/Abstract/Introduction/Methodology/Results/Conclusion 상세분석·비교분석·근거행렬을
   작성(`claude_analysis/`), round98/input/에 복사해 commit·push(`87dc143`).
2. Codex가 동일 PROBLEM.md로 두 PDF 원문을 독립적으로 직접 열어 6개 항목을 블라인드 검증, `codex.md` 작성·
   commit·push(`0f53970`).
3. Claude가 `claude_review.md`에서 codex.md를 재검증(블라인드 아님, 자신이 가진 원문 이미지로 직접 재확인).
4. Codex의 지적사항을 반영해 `claude_analysis/*.md`, `evidence_matrix.csv`, `paper_list.csv`,
   `html_presentation/paper_review_presentation.html`을 수정.

## 결과

- **15편 집계·Best(No.5)/Worst(No.1) 선정**: Codex가 Python으로 120개 등급을 독립 재집계해 전부 일치
  확인. 선정 논리(동점 해소에 Abstract IMRaD 완결성 사용, "하" 개수로 Worst 판정)도 타당하다고 확인.
  **선정 결과와 등급 자체는 변경하지 않았다.**
- **연료·엔진 종류 배제 원칙**: 지정 자료 범위에서 준수 확인(No.13·14·15 디젤·수소 엔진도 동일 기준
  적용, 점수·선정에 차별 없음).
- **No.1 Introduction 근거 문구 수정(핵심 쟁점)**: "선행연구 정량적 인용 거의 없음"이 부정확함을 Claude·
  Codex 모두 확인. Codex의 정밀 재집계(정량 서술 4대목, 참고문헌 5개[27,28,39,41,44], 결과 수치 8개)를
  채택해 근거 문구를 수정했다. **등급(하)은 round85~88 확정본을 유지하고 바꾸지 않았다** — 이번 수정은
  근거 문구의 정확도 문제이지 등급 재심이 아니다.
- **원문 인용 정확도 수정**: No.1 엔진을 "단일실린더"로 오인한 오류(실제 4기통·2000cc, Table 3) 수정,
  No.5 Introduction 인용구의 부정확한 직접인용 수정, No.5가 3종 첨가제를 "동시에" 시험한 것처럼 읽히는
  표현을 "저자는 공백을 제시했으나 실제 시험배합에는 3종 동시조합이 없음"으로 명확화, No.1 Introduction
  수치인용 출처 오기([28]→[44]) 수정, evidence_matrix.csv의 No.1 CRediT 점수 오류(0→1.0, 원본 CSV
  점수열 기준) 수정 등 10여 건.
- **원문(No.5) 자체의 내적 결함 반영**: 저울 정밀도(본문 0.1g vs Table4 0.01g), Table 6·8·10 일부 값과
  본문 서술 불일치는 **원문 저자의 오류**이며 Claude 분석 과정의 오류가 아님을 확인해, "본문-표가 항상
  일치한다"는 과신성 표현을 삭제하고 이 내적 결함을 분석에 추가했다.
- **척도 비교 방법**: 숫자점수(Title/Authors)와 범주형 등급(Abstract~Results)을 합산하지 않는다는 판단에
  Codex도 동의. Title/Authors 평균 수치 오류(7.59→7.55)도 수정.
- **번역체**: 지정 금지표현은 발견되지 않았으나, "전부/전혀/가장/오직/거의 없음" 같은 범위 단정 표현을
  전반적으로 완화했다.

## 결론

Codex가 지적한 사항 전부(반박 없음)를 수용해 `claude_analysis/` 4개 문서, `evidence_matrix.csv`,
`paper_list.csv`(Abstract_연관성 열 추가), HTML 발표자료를 수정했다. Best(No.5)/Worst(No.1) 선정 결과와
15편의 상/중/하 등급은 변경되지 않았으며, 바뀐 것은 상세분석의 근거 문구·인용 정확도뿐이다.

## 최종 승인 상태

**CONDITIONAL** — Claude가 Codex의 전체 지적사항을 반영해 1차 수정을 완료했으나(이 기록 작성 시점),
수정본에 대한 Codex의 재확인(2차 검증)은 아직 수행하지 않았다. 사용자가 즉시 결과를 받기를 원하면
현재 상태로 제공하고, 완전한 승인(APPROVED)을 원하면 round99로 Codex 재확인을 한 번 더 진행할 수 있다.

## 사용자 결정

(사용자가 이 섹션에 최종 결정을 기록)
