# round57 Claude 검증 — Codex 전사(codex.md) vs Claude 전사(claude.md) vs PDF 지면

방법: 두 전사의 식을 항별로 비교, 불일치 항은 PDF를 300~400dpi로 다시 렌더링해 판독 (PDF 18쪽 Eqn.2 끝, PDF 19쪽 Eqn.4·5a, PDF 20쪽 Eqn.5b·5c).

## 식 비교
| 식 | 결과 |
|---|---|
| Eqn.1, 3a, 3b, 3c, 5b, 5c, 6, Fig.1 내 K_I, ΔK(Kmax−Kmin) | 두 전사 일치, 지면과 일치 |
| Eqn.2 | **Claude 전사 오류**: Claude는 마지막 항 `T_{j-1}(k_j r_j+k_{j-1}r_{j-1})`에 닫는 소괄호를 넣었으나, 400dpi 지면은 `T_{j-1}(k_j r_j+k_{j-1}r_{j-1}]`로 소괄호 닫힘 없이 대괄호로 끝남. Codex가 맞음 → 정리본에는 지면대로 전사하고 "원문 자체 이상"으로 표기 |
| Eqn.4 | 불일치: 지면 둘째 적분 피적분 `(T−T_o)`(소문자 o 첨자). Codex는 `T_0`으로 통일 전사(원문 자체 이상 목록에도 없음). 300dpi 지면 = `T_o` → 정리본은 지면대로 `T_o`, 원문 자체 이상으로 표기 |
| Eqn.5a | 불일치 2곳: (1) 둘째 적분 하한 지면 `r_1`(Codex는 `r_i`로 통일), (2) 둘째·셋째 적분 피적분 지면 `(T−T_o)`(Codex는 `T_0`). 첫째 적분은 `T_0`. 정리본은 지면대로 전사, 원문 자체 이상으로 표기 |
| Eqn.5b | 지면: α₁ 항 분자 `r²+r_o²`, α₂ 항 분자 `r²+r_i²`. 두 전사 일치 |

## 원문 자체 이상 합집합
Eqn.2 괄호 닫힘; Eqn.4·5a `T_o`/`T_0` 혼용, 5a `r_1`; Eqn.3b 분자 `r²+r_i²` 대 Eqn.5b 분자 `r²+r_o²`·`r²+r_i²`(통일하지 않음); 기호표 H1/h2, K 이중 사용, κ 기호; μ(본문)·ν(Table 4)·NuIn(Table 2); c_sp(식)·C(Table 4); IATypeIn/IYType/IAType; RTIF-6/7 Table 번호; a/h(Table 1) 대 a/t(Table 3); "Timoshenko [7]"(참고문헌 [7]은 Edwards, [8]이 Timoshenko); §2.4 단계 (4)의 "steps 3 and 4"; 철자(temperatuare, discreet, the the, theTIFFANY, modulii, recommendatioins, desireable); "variation of µ" 중복; §2 첫 문장 끝 "..".

## 결론
식 12개(1, 2, 3a–c, 4, 5a–c, 6, K_I, ΔK) 중 불일치 3건 모두 지면 재판독으로 해소(Claude 1건 오류 정정, Codex 2건 정규화로 인한 지면 불일치). 표·본문 전사는 두 전사가 상충하는 항목 없음. 최종 HTML은 이 해소 결과를 사용하고 Codex가 HTML을 PDF와 다시 전수 대조한다.

## 추가 — Codex 2단계(codex_review.md) 반영 결과
- 반영(B01–B14): 17쪽 제목에서 등호 제거(B01); Table 2 변수 수를 코드에서 계산(48개, B02); `PhoopStrMaxO [ ]`의 `[ ]` 삭제(B03); Table 3 Notes를 원문 병합 범위대로 rowspan(PW 4, TW 2, TW 2, axial PW 4, axial TW 2, Type 1 2행, B04); 기호표 `csp` 표기(B05); 앞쪽 접힌 영어 쪽번호 표기 분리(B06); 어색한 번역 문장을 원문 영어 인용으로 교체(B07–B10, B12); σθ·접선 응력 같은 원문 밖 명칭 삭제(B11); 식 3b/5b 분자 차이를 "표기 관찰"로 분류(B13); 저작권 서술을 원문 면책 문구 인용으로 교체(B14).
- claude.md 오류 인정(C01–C06): Eqn.2 닫는 괄호(C01), Table 4 기호 K·C 대소문자(C02), 기호표 열전도도 기호 K를 κ로 혼동 서술(C03), T_o/T_0 혼용 범위에 5b 포함은 오류 — 4·5a로 한정(C04), 표 본문을 외부 파일로 넘긴 추적성 문제(C05), "표·본문 전사 충돌 없음" 포괄 판정 철회(C06). claude.md 본문은 blind 결과 보존을 위해 수정하지 않고 여기에 정오를 남긴다. 최종 HTML은 위 항목이 모두 바로잡힌 상태다.

## 추가 2 — Codex 3단계(codex_final.md) 반영
- B01~B14 전부 "반영" 확인(Codex). 새 지적 F01~F05 처리: F01 접힌 영어의 `α₁ ≠ α₂` 복원, F02 `(σ_T and σ_B)` 복원, F03 `Δp` 복원 — 모두 HTML에서 확인. F04 표기 차이는 "원문 표기 관찰"로 표현을 낮추고 철자 항목만 오타로 구분. F05 HTML 신뢰성 주석에서 AI 이름·dpi·저장소 경로 삭제(검증 이력은 이 라운드 문서에만 남김).
- 최종 HTML: J:\Desktop\XLPR\2026_10_21_B048_주기응력확대계수\XLPR_주기응력확대계수_B048.html (28페이지, 식 12개 KaTeX, 표 전사 Table 1·2·3·4·가정표·기호표·약어표·참고문헌).
- 사용자 결정 사항(미결정): 신뢰성 주석에 남긴 "독립 전사 2종 일치" 문구 유지 여부, 4단락 카드 제목의 "원문이 밝힌 …" 표기, 원문 표기 관찰 목록의 노출 방식.
