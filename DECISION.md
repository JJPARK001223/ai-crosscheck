# Round 25 — 최종 결정: Abstract 분석표 "저널 가이드라인 부합여부" 검증

## 결론 요약

사용자 지적이 맞았다. 이전 Abstract 분석표는 11개 서로 다른 저널에
**"약 150~250단어"라는 단일 추정치**를 일괄 적용했고, 이는 각 저널의
실제 가이드라인을 전수 확인한 것이 아니었다.

Claude·Codex 교차검증 결과:
- **1차 출처(저널/출판사 공식 페이지)로 직접 확인된 저널은 11개 중 2개뿐**이다.
- 나머지 9개 저널은 Elsevier·MDPI·ACS 등 출판사 사이트가 자동화 접근을
  차단(HTTP 403)해 공식 수치를 확인하지 못했다. 2차 출처(요약 블로그 등)
  일부 숫자가 있었지만 신뢰도가 낮아 공식 사실로 채택하지 않았다.
- **부수적으로, Claude가 수동으로 옮겨 적은 Abstract 원문 중 2편(No.3, No.5)에서
  실제 문장이 누락/병합된 전사 오류가 발견되어 단어수가 수정되었다.** 이는
  Codex가 PDF에서 기계적으로 직접 추출·대조한 결과로 교차검증이 실제로
  오류를 잡아낸 사례다.

## 공통 (Claude·Codex 둘 다 동일하게 확인한 것)
- No.1(Processes, 231), No.4(Energy/baffles, 195), No.6(ACS Omega, 171),
  No.10(Fuel/Kaya, 204), No.12(Topics in Catalysis, 220) — Abstract
  단어수가 양쪽 계산에서 완전히 일치.
- 11개 저널 중 **Elsevier·MDPI·ACS 공식 페이지는 이 환경에서 자동화 접근이
  막혀 있다**는 사실 — Claude는 WebFetch 403으로, Codex는 네트워크 자체가
  차단된 것으로 각자 독립 확인.
- 저널별 숫자를 "확실하다"고 말할 수 있는 근거가 없으면 숫자를 적지 않고
  "확인 불가"로 남긴다는 원칙에 양쪽 다 동의.

## 충돌 / 차이 (중요)

| 항목 | Claude 1차 판정 | Codex 독립 재계산 | 채택 | 사유 |
|---|---|---|---|---|
| No.3(Fuel, Sarıkoç) 단어수 | 380 | 404 | **404 (Codex)** | Claude가 손으로 옮겨 적을 때 "The combustion characteristics improved after the addition of hydrogen and methanol, which also considerably affected the engine performance and emission characteristics." 한 문장을 통째로 누락. PDF 원문 재대조로 404가 맞음을 직접 확인(wc -w로 재검증) |
| No.5(Fuel, Özker&Çelebi) 단어수 | 252 | 290 | **290 (Codex)** | Claude가 "is provided by G90M10 fuel, followed by G90M5N5 and G90T5N5 fuel mixtures, respectively. It is determined that the G90T5N5 fuel mixture provides the highest reduction in HC and CO emissions compared to G100" 구간을 통째로 생략하고 두 문장을 하나로 압축. PDF 원문 재대조로 290이 맞음을 직접 확인 |
| No.2, 7, 8, 9, 11, 13, 15 단어수 | ±1~10 소폭 차이 | Codex가 대체로 소폭 더 높음 | **Codex 값 채택** | 주로 "56.8 %"처럼 숫자와 %사이 공백이 있는 경우 %를 별도 단어로 셀지 여부의 토큰화 관례 차이. 기계적 추출(Codex)이 수작업 전사(Claude)보다 체계적으로 신뢰도가 높다고 판단 |
| No.14(Combustion and Flame) 단어수 | 388(Novelty and significance 소제목 단락 포함) | 303(그 단락 제외) | **두 값 모두 기록, "Abstract 본문만"은 303** | 이건 오류가 아니라 "Abstract의 범위를 어디까지로 볼 것인가"의 정의 차이. 저널 지면상 Abstract 바로 아래 볼드체 소제목으로 별도 단락이 붙은 구조이므로, 공식 Abstract 분량 규정과 비교할 때는 303(본문만)을 기준으로 삼는 것이 타당 |
| ASME(JEGTP) 250단어 | 1차 출처로 확인(asme.org) | "250단어 이하로 기억"하나 "추측(불확실)"로 표시 | **Claude 조사 채택(1차 출처 있음)** | Codex는 웹 접근이 없어 학습기억에 의존했고 스스로도 불확실하다고 명시. Claude는 asme.org 공식 페이지 원문("An abstract (250 words maximum) should open the paper or brief.")을 직접 인용 |
| Springer Nature 350단어 | 1차 출처로 확인(support.springernature.com) | "150~250단어로 기억"(회상, 미검증) | **Claude 조사 채택(1차 출처 있음)** | 동일한 이유. Codex의 회상치(150~250)는 Claude가 확인한 공식 FAQ 수치(350)와 다르며, Codex 스스로 "현행 공식 페이지 미확인"이라고 단서를 달았다 |

## 최종 판정표 (저널 가이드라인 부합여부 — 재작성)

| No | 저널 | Abstract 단어수(최종 채택값) | 해당 저널 공식 기준 | 판정 |
|---|---|---|---|---|
| 1 | Processes (MDPI) | 231 | 확인 불가 (1차 출처 403 차단) | **판정 보류** |
| 2 | Case Studies in Thermal Engineering (Elsevier) | 244 | 확인 불가 | **판정 보류** |
| 3 | Fuel (Elsevier) | **404** (380→정정) | 확인 불가 | **판정 보류** (단, 11개 논문 중 가장 긴 Abstract) |
| 4 | Energy (Elsevier) | 195 | 확인 불가 | **판정 보류** |
| 5 | Fuel (Elsevier) | **290** (252→정정) | 확인 불가 | **판정 보류** |
| 6 | ACS Omega (ACS) | 171 | 확인 불가(2차 출처 상충: "제한없음" vs "150~250단어") | **판정 보류** |
| 7 | International Journal of Engine Research (SAGE) | 246 | 확인 불가 | **판정 보류** |
| 8 | Energy (Elsevier) | 184 | 확인 불가 | **판정 보류** |
| 9 | Journal of the Energy Institute (Elsevier) | 245 | 확인 불가 | **판정 보류** |
| 10 | Fuel (Elsevier) | 204 | 확인 불가 | **판정 보류** |
| 11 | Journal of Engineering for Gas Turbines and Power (ASME) | 210 | **250단어 이내 (1차 출처 확인)** | **부합** |
| 12 | Topics in Catalysis (Springer) | 220 | **350단어 이내 (Springer Nature 공통정책, 1차 출처 확인)** | **부합** |
| 13 | Energy (Elsevier) | 223 | 확인 불가 | **판정 보류** |
| 14 | Combustion and Flame (Elsevier) | 303(본문)/388(Novelty 포함) | 확인 불가 | **판정 보류** |
| 15 | Applied Thermal Engineering (Elsevier) | 191 | 확인 불가 | **판정 보류** |

**결론: 15편 중 2편(No.11, No.12)만 "해당 저널의 실제 공식 기준"으로
부합여부를 판정할 수 있다. 나머지 13편은 공식 1차 출처를 확인하지
못했으므로 "판정 보류"로 표기하며, 임의 추정치를 적용하지 않는다.**

## 왜 9개 저널을 더 못 찾았나 (한계 설명)
- Elsevier(sciencedirect.com, elsevier.com)·MDPI(mdpi.com)·ACS(pubs.acs.org,
  publish.acs.org)는 자동화 크롤러를 차단하는 봇 방지 정책을 쓰고 있어,
  이 세션의 WebFetch로는 HTTP 403 또는 빈 JS 페이지만 반환됨.
  web.archive.org도 이 세션에서는 자체적으로 차단됨.
- SAGE(journals.sagepub.com)는 저널 코드 매핑을 찾지 못해 접근 자체를
  시도하지 못함.
- 사람이 직접 브라우저로 로그인 후 열람하거나, 해당 저널에 투고 경험이
  있는 연구실 선배에게 PDF 공식 가이드 문서를 받는 방법이 더 정확할 수
  있음 — 필요하면 사용자가 직접 열람 요청.
