# Round18 — 참고문헌 9편 번역 검증 요청 (Codex)

Claude가 아래 9개 참고문헌(round7 읽기자료 B-1,3~10)을 원문 PDF를 보고 한국어 HTML로 번역/요약했습니다.
당신(Codex)의 역할은 **Claude의 번역 결과를 원문 PDF와 대조해 블라인드로 검증**하는 것입니다 — Claude의
`round18/claude.md`는 먼저 읽지 말고, 아래 파일 쌍을 직접 대조한 뒤 결과를 작성하세요.

## 검증 대상 (HTML ↔ 원본 PDF)
1. `J:\Desktop\선행연구 관련\참고문헌_번역\B1_Irwin1957_번역.html` ↔ `J:\Desktop\선행연구 관련\Irwin_1957_Analysis_of_Stresses_and_Strains.pdf`
2. `J:\Desktop\선행연구 관련\참고문헌_번역\B3_Sapora2018_번역.html` ↔ `J:\Desktop\선행연구 관련\Fatigue Fract Eng Mat Struct - 2018 - Sapora - Finite Fracture Mechanics crack initiation from a circular hole.pdf`
3. `J:\Desktop\선행연구 관련\참고문헌_번역\B4_Han2015_번역.html` ↔ `J:\Desktop\선행연구 관련\1-s2.0-S0013794415000661-main.pdf`
4. `J:\Desktop\선행연구 관련\참고문헌_번역\B5_Braun2020_번역.html` ↔ `J:\Desktop\선행연구 관련\Fatigue Fract Eng Mat Struct - 2020 - Braun - Requirements for stress gradient‐based fatigue assessment of notched.pdf`
5. `J:\Desktop\선행연구 관련\참고문헌_번역\B6_Camanho2012_번역.html` ↔ `J:\Desktop\선행연구 관련\1-s2.0-S1359835X12000978-main.pdf`
6. `J:\Desktop\선행연구 관련\참고문헌_번역\B7_Daniel2007_번역.html` ↔ `J:\Desktop\선행연구 관련\Strain - 2007 - Daniel - Failure of Composite Materials.pdf`
7. `J:\Desktop\선행연구 관련\참고문헌_번역\B8_Podgorski1985_번역.html` ↔ `J:\Desktop\선행연구 관련\podgórski-1985-general-failure-criterion-for-isotropic-media.pdf` (파일명에 비ASCII 문자가 있어 쉘에서 열기 어려우면 폴더를 ls로 확인 후 정확한 이름으로 cp 하거나 glob 사용)
8. `J:\Desktop\선행연구 관련\참고문헌_번역\B9_Kwon_PVT144_2022_번역.html` ↔ `J:\Desktop\선행연구 관련\pvt_144_05_051506.pdf`
9. `J:\Desktop\선행연구 관련\참고문헌_번역\B10_Kwon_Polymers2022_번역.html` ↔ `J:\Desktop\선행연구 관련\polymers-14-02481.pdf`

## 참고 — 이 HTML들의 성격
B1,3,4,6,7,8은 저작권(비오픈액세스) 때문에 **"요약번역"**(Abstract 번역 + 핵심 수식 + 절별 요약, 전문
축자번역 아님, 원본 그림 이미지 미포함)입니다. B5,B9,B10은 오픈액세스/퍼블릭도메인이라 더 완전한
번역이지만 이것도 원본 그림 이미지는 포함하지 않았습니다(텍스트로 설명). **"전문 번역이 아니라서
불완전하다"는 지적은 하지 마세요** — 그것은 의도된 설계입니다. 대신 아래 항목만 점검하세요.

## 점검 항목 (파일별로)
1. **서지정보 정확성**: 저자/저널명/권/호/페이지/DOI/연도가 원문 표지와 일치하는가?
2. **핵심 수식의 정확성**: HTML에 포함된 수식(LaTeX)이 원문의 해당 수식과 수학적으로 일치하는가? 특히
   Irwin의 $K$-$\mathcal{G}$ 관계, B-9의 Eq.(1)(2)(3)(4)(5), B-6/B-3의 FFM 개념식(이들은 Claude가
   "2단 조판 때문에 정확한 계수 확인 어려움"이라고 스스로 caveat을 달았으니, 그 caveat이 적절한지도
   평가).
3. **요약 내용의 사실 정합성**: 각 절의 한국어 요약이 원문의 핵심 주장·수치(%, 오차율 등)를 왜곡하지
   않았는가?
4. **본 프로젝트 고유 사실과의 모순 여부**: 이미 확정된 사실 — Irwin 식에 $\sqrt{\pi}$ 계수 없음
   ($K_I=\sqrt{\mathcal{G}E'}$), B-9/B-10은 "선행연구 2"로 부르지 않음 — 과 모순되는 서술이 있는가?

## 작업 방법
- `pdftotext -layout`로 각 PDF의 텍스트를 빠르게 추출해 대조하세요(스캔본인 B-1은 `pdftoppm`으로 이미지
  렌더 후 직접 보세요).
- 발견한 오류·누락·caveat 적절성 평가를 파일별로 정리해 `round18/codex.md`에 작성하세요(마크다운, 간결하게).
- 이 저장소는 당신의 샌드박스에서 git 커밋 권한이 없을 수 있습니다 — `round18/codex.md` 파일만 작성하면
  됩니다(커밋은 Claude가 대신 수행합니다).
- Claude의 다른 분석(연구배경.html, round6/7 등)을 재검증하지 마세요 — 이번 라운드는 오직 이 9개 번역
  파일의 원문 대조 검증입니다.
