# round102 — round101 지적사항 수정 확인

## 배경

round101(`round101/codex.md`)에서 Codex가 `paper_review_presentation_revised.html`에서 다음 오류·개선
사항을 발견했다. Claude가 전부 수정해 `round102/input/paper_review_presentation_revised.html`에 반영했다.
이번 round102는 수정이 제대로 됐는지만 좁게 재확인한다(15개 항목 전체를 처음부터 다시 훑지 않아도 됨).

## 수정한 항목 (round101 지적 → 조치)

1. **18장 CRediT 점수 오류**: "ORCID·CRediT 모두 명시 없음(각 0점)"이 원본 CSV(CRediT=1.0/1.5)와 불일치
   → ③에 CRediT 점수 1.0/1.5 설명 추가, ④에 CRediT 1.0/1.5를 우수한 점으로 이동, ⑤는 ORCID만 남김,
   ⑥에 9개 항목 합산 산식(7.55=2.0+1.5+1.0+0.5+0.3+0.25+0+1.0+1.0) 명시.
2. **18장 "파키스탄 3개 기관" 오류**: 실제로는 파키스탄 2개 대학(Capital University of Science and
   Technology, National University of Sciences and Technology) + 미국 1개 대학(Ohio State University) →
   본문 수정.
3. **22~23장 Results의 0.03초 누락**: Fig.6(9쪽)의 초기조건 과도현상 수렴시간 0.03초를 ③④에 추가하고,
   ⑤⑥⑦⑧에서 "고장 발생 이후의 검출 지연·잔류오차"와 "초기 과도현상 수렴시간"을 구분. Fig.5(상태추정)·
   Fig.6(추정오차) 그림 번호도 구분해 표기. 23장의 "수치로 전달하지 않는다"는 포괄 표현을 "제한적으로만
   수치로 전달한다"로 완화.
4. **9·15장 Best Abstract 수치의 조건 누락**: "BSFC 9.70% 감소" 등에 "G90M10 블렌드·100% 부하·G100 대비"
   조건을 명시. 9장 "가장 정확하게 전달하는 논문"을 "Abstract의 5요소 구성이 가장 완결된 논문"으로 완화
   (IMRaD 완결성과 수치 정확성은 별개임을 명시).
5. **11장 Abstract 연관성 축 누락**: ①②에 연관성(상) 설명 추가.
6. **13·14장 "재현 가능"/"표 우선" 단정 완화**: "동일 조건으로 재현 가능한 수준" → "재현에 필요한 조건을
   비교적 상세히 제공"으로, "표를 우선해야 한다"는 사실 진술이 아니라 "평가자 판단"임을 명시.
7. **20장 Introduction "문헌 14건/수치 0건" 과장**: "14개 문헌" → "선행연구 [1]~[14]", "구체적 성능 결과
   수치로 소개되지 않는다"로 한정(고조파 차수 같은 기술적 수치는 존재함을 ③에 추가).
8. **21장 Methodology 페이지 범위 오류**: "2~8쪽"→"2~9쪽"(식71 포함), Appendix 위치를 "10~11쪽"으로 명시.
9. **3장 "가솔린 엔진 15편" 표현**: No.13·14·15(디젤·수소)와 모순되므로 "가솔린 엔진 관련 SCI(E) 논문
   15편(디젤·수소 엔진 3편 포함)"으로 수정.
10. **17장 AI 합의와 사용자 결정 혼동**: "Claude와 Codex가 독립 검토한 뒤 채택을 확정했다"를 "Claude×Codex가
    독립 검토해 수학적 타당성을 확인했고 사용자가 최종 채택했다"로 수정.
11. **전체화면 기능 버그**: CSS가 `body:fullscreen`을 선택하지만 JS는 `document.documentElement`(html)에
    requestFullscreen을 호출해 선택자가 맞지 않음 → CSS를 `:root:fullscreen`으로 수정. requestFullscreen/
    exitFullscreen의 Promise에 `.catch()` 추가.
12. **스크롤·잘림 우려(소스 추론으로만 지적됨)**: Claude가 Chrome으로 1568×772, 1366×768 두 해상도에서
    24장 중 표 3장·8-part 10장(가장 긴 Worst Methodology 포함)을 직접 렌더링해 스크롤·잘림이 없음을
    확인했다(스크린샷 근거는 이번 보고서에 첨부하지 않으나 직접 조작·확인함).

## 검증 요청

위 12개 수정이 실제로 `round102/input/paper_review_presentation_revised.html`에 정확히 반영됐는지만
좁게 확인하라. 추가로 새로운 오류를 발견하면 함께 적어도 좋다. No.5·No.11 PDF의 해당 페이지를 다시 열어
대조할 것(특히 2번·3번·8번 항목).

## 결과 파일

`round102/codex.md`에 작성. 끝나면 `round102/codex.md`만 git add/commit/push 하고 원격 반영까지 확인하라.
