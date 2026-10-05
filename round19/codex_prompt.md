## Codex에게 보내는 검증 지시 (round19)

다음 6개 HTML 번역 파일이 round18의 "요약번역"에서 "전섹션 요약번역"으로 확장되었다.
각 파일과 해당 원본 PDF를 블라인드로 대조해 `round19/codex.md`에 검증 결과를 작성하라.
(이 파일은 ai-crosscheck 리포 밖에 있다 — 아래 경로 그대로 열어서 확인할 것.)

1. `J:\Desktop\선행연구 관련\참고문헌_번역\B1_Irwin1957_번역.html`
   ← `J:\Desktop\선행연구 관련\Irwin_1957_Analysis_of_Stresses_and_Strains.pdf`
2. `J:\Desktop\선행연구 관련\참고문헌_번역\B3_Sapora2018_번역.html`
   ← `J:\Desktop\선행연구 관련\Fatigue Fract Eng Mat Struct - 2018 - Sapora - Finite Fracture Mechanics crack initiation from a circular hole.pdf`
3. `J:\Desktop\선행연구 관련\참고문헌_번역\B4_Han2015_번역.html`
   ← `J:\Desktop\선행연구 관련\1-s2.0-S0013794415000661-main.pdf`
4. `J:\Desktop\선행연구 관련\참고문헌_번역\B6_Camanho2012_번역.html`
   ← `J:\Desktop\선행연구 관련\1-s2.0-S1359835X12000978-main.pdf`
5. `J:\Desktop\선행연구 관련\참고문헌_번역\B7_Daniel2007_번역.html`
   ← `J:\Desktop\선행연구 관련\Strain - 2007 - Daniel - Failure of Composite Materials.pdf`
6. `J:\Desktop\선행연구 관련\참고문헌_번역\B8_Podgorski1985_번역.html`
   ← `J:\Desktop\선행연구 관련\podgórski-1985-general-failure-criterion-for-isotropic-media.pdf`

### 점검 항목 (각 파일마다)
① **섹션 커버리지**: 원문의 주요 섹션(서론/문제의식, 이론·방법론, 핵심 결과식, 실험 또는 사례,
   결과·결론)중 번역본에서 완전히 빠진 것이 있는가? (초록만 있고 본문 전개가 없다든지)
② **사실 정확성**: 수식·수치·그림 설명 중 원문과 어긋나는 것이 있는가? 특히 다음은 이미
   round18에서 정정된 사항이니 재발 여부만 확인: B1(1페이지 사진이 Irwin 자신의 그림이 아니라
   앞 논문 것), B6(미지수 기호는 $a$가 아니라 $l$이며 파괴방향을 "찾아내는" 모델이 아님),
   B3(결합 FFM 식은 Eq.8/9이며 Eq.1/2는 점응력법 단독), B4(J-적분 경로안정성은 특이요소
   사용시에만 전 경로 안정).
③ **분량 적정성**: 번역본이 "응축된 요약"의 범위를 넘어 원문을 거의 그대로 옮기는 수준(축자번역)
   으로 과도하게 길어지지는 않았는가? (참고: 각 파일은 원문 4~14쪽 대비 Korean 텍스트 1.5~2.5KB
   수준으로 설계되었다.)
④ 선행연구 1·3과의 관계 서술이 기존 교차검증 결론(round6/7/16/17/18)과 모순되지 않는가?

파일별로 "통과" 또는 "수정 필요(구체적 위치·내용)"로 명확히 판정할 것. claude.md는 보지 말고
블라인드로 수행할 것.
