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
