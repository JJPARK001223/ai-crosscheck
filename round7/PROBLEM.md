# Round 7 — 선행연구 1·3 참고문헌 + 윤석준 세미나자료 한국어 읽기자료(PDF) 검증

## 목적
사용자가 이동 중 읽을 **한국어 전용 읽기자료 PDF**를 만든다.
- 대상 = `J:\Desktop\선행연구 관련\` 폴더의 PDF 논문들. 이 논문들은 **선행연구 1·3의 참고문헌**이다.
- 이름에 "윤석준"이 들어간 자료 2건은 참고문헌이 아니라 **방향이 비슷한 발표(세미나) 자료** → **별도 챕터**로 다룬다.
- 나머지 논문은 **논문별로 챕터 하나씩** 나눠 하나의 PDF에 담는다.
- 원문(영문)·스캔 없이 한국어 본문 + 시각화(inline SVG).
- 대상 독자 = 재료공학·파괴역학 석사과정 본인. "읽고 이해"용.

## 대상 파일 (블라인드로 Claude가 직접 읽어 정리, 새 번역 아님)
선행연구 1 참고문헌 3건:
- Irwin, G.R. 1957, "Analysis of Stresses and Strains Near the End of a Crack Traversing a Plate," ASME J. Appl. Mech. 24, 361–364.  → `Irwin_1957_Analysis_of_Stresses_and_Strains.pdf` (뒤에 C.B. Ling, "Stresses in a Perforated Strip" 스캔 2쪽 첨부)
- Kirsch, G. 1898 (원 PDF 없음 — 선1[2], 개념만)
- Sapora, A.; Torabi, A.R.; Etesam, S.; Cornetti, P. 2018, "Finite Fracture Mechanics Crack Initiation From a Circular Hole," FFEMS 41(7), 1627–1636. → `Fatigue Fract...2018 - Sapora...circular hole.pdf` (선1[3], 선3[21])

선행연구 3 참고문헌 (핵심):
- Podgórski, J. 1985, "General Failure Criterion for Isotropic Media," J. Eng. Mech. 111(2), 188–201. → `podgórski-1985-...pdf` (선3[2])
- Daniel, I.M. 2007, "Failure of composite materials," Strain 43, 4–12. → `Strain - 2007 - Daniel...pdf` (선3[8])
- Irwin 1957 (선3[9], 위와 동일)
- Han, Q.; Wang, Y.; Yin, Y.; Wang, D. 2015, "Determination of stress intensity factor for mode I fatigue crack based on finite element analysis," Eng. Fract. Mech. 138, 118–126. → `1-s2.0-S0013794415000661-main.pdf` (선3[14])
- Braun, M.; Müller, A.M.; Milaković, A.-S.; Fricke, W.; Ehlers, S. 2020, "Requirements for stress gradient-based fatigue assessment of notched structures according to theory of critical distance," FFEMS 43(7), 1541–1554. → `Fatigue Fract...2020 - Braun...notched.pdf` (선3[22])
- Camanho, P.P.; Erçin, G.H.; Catalanotti, G.; Mahdi, S.; Linde, P. 2012, "A finite fracture mechanics model for the prediction of the open-hole strength of composite laminates," Compos. Part A 43, 1219–1225. → `1-s2.0-S1359835X12000978-main.pdf` (선3[24])
- Kwon, Y.W.; Diaz-Colon, C.; DeFisher, S. 2022, "Failure Criteria for Brittle Notched Specimens," J. Press. Vessel Technol. 144, 051506. → `pvt_144_05_051506.pdf` (선3[35] — 사실상 "선행연구 2")
- Kwon, Y.W. 2022, "Failure Prediction of Notched Composites Using Multiscale Approach," Polymers 14, 2481. → `polymers-14-02481.pdf` (선3[36] — 선3 §6의 직접 선행)

윤석준 세미나 자료 (별도 챕터):
- `20240122_윤석준_Displacement-controlled stress intensity factor solution 진행상황.pdf/pptx`
- `20250912_윤석준_[Speciment level] Compact tension test #3.pdf`

## 참고 (기존 확정 지식 — round1~6)
- 선1 두 조건: ① σ_e ≥ σ_f, ② 응력구배조건. 둘 다(AND).
- 응력구배조건에 균열 근접장 대입 → r 소거 → w_f = Y = K_IC²/(2πE) = 재료상수.
- 2π 이슈: 선3 식(3) σ_e = K/√s 는 2π 없음. K_선3 = K_I/√(2π). 파괴개시 임계상태에서 Y = G_c/(2π)(평면응력). 문헌 G_c 직접대입 금지. 1점 보정+동일계열 예측이면 정규화 상수 상쇄.
- 선3 §4 시멘트 페이스트 6케이스 = 재현 과업(round4·5), 실험 원출처 Karihaloo 2003.
- 읽기자료 산출물 = `claude_code\2026_09_04_선행연구1_3_한국어읽기자료\`.

## Claude 산출물 (검증 대상)
`round7/읽기자료_참고문헌_윤석준.html` — 검토 후 PDF로 변환.

## Codex 검증 항목 (1~8)

1. **논문 식별 정확성** — 각 챕터가 실제로 그 논문을 다루는가? 저자·연도·저널·제목·DOI/권/페이지가 원 PDF와 일치하는가? 선1/선3 참고문헌 번호 매핑([1][3][9][14][21][22][24][35][36] 등)이 맞는가?

2. **내용 충실도** — 각 챕터 본문이 원 PDF의 초록·방법·핵심식·결론과 의미상 일치하는가? 왜곡·과장·창작·중대한 누락이 있는가? (특히 수치·조건·인과관계)

3. **수식 정확성** — 옮긴 식이 원문과 일치하는가?
   - Irwin 1957: 근접장 σ_x, σ_y ∝ (KG/π)^{1/2} 형태, G↔K, 평면변형시 E→E/(1-ν²).
   - Sapora: 식(2) Δ=½(K_Ic/σ_u)²=½l_ch, 식(3) LM, 식(5) 에너지, 식(7) QFM, 식(8)(9) coupled FFM, 식(10) σ_y(x)=σ/2(2+R²/x²+3R⁴/x⁴), 식(11) K_I(a)=σ√(πa)F(s), 식(13) F(s).
   - Han: 식(1)(2) 변위외삽, 식(3)(4) 응력외삽 K_I=σ_{y,θ=0}√(2πr), 식(5)(6) quarter-point, 식(7)(8) J적분 K_I=√(JE).
   - Camanho: 식(1) 평균응력+에너지 연립, 식(6) K_I=σ^∞F_h F_w√(πa), 식(14) η_N=2R/l.
   - Podgórski: 식(13) A_0+A_1τ_0+A_2τ_0²=0, Heigh-Westergaard, shape function.
   - Kwon 2022(PVT144): 식(1) σ_max≥σ_fail, 식(2) (σ³/2E)|dσ/ds|⁻¹≥κ_fail, 식(3) Kirsch, 식(4) |∂σ/∂r(R)|=7/R, 식(5) σ∝R^{-1/3}.
   - Kwon 2022(Polymers): 식(11)(12)(13) κ_fail=K_Ic²/(2πE)=G_c/(2π), 식(14) 섬유, 식(15) 기지 매콜리, 식(16) 계면, 식(17) Kirsch, 식(19) 7σ_o/a.
   - Braun: 식(1) K_f=1+(K_t-1)/(1+a/r), 식(2) N=N_R(Δσ_eff/Δσ_R)^{-k}, 식(3) PM, 식(4) L=(1/π)(ΔK_th/Δσ_0)², 식(5) LM.
   - 윤석준: K^Fixed = K^Free 를 (N_I-N_II),(M_I-M_II)로; C(T) σ_l≥σ_fail, σ_l≥(2E|dσ_l/ds|w_f)^{1/3}.

4. **시각화 정확성** — 각 SVG 그림이 물리적으로 맞는가? (Irwin G↔K, Kirsch 1-2cos2θ, coupled FFM 두 조건, TCD 분류, Han 4방법, Camanho 평균화 구간, Podgórski 편차평면 단면, 다중스케일 루프, 윤석준 중첩분해, C(T) 메시 비수렴)

5. **선1·선3와의 연결 정확성** — 각 문헌이 선1/선3에서 하는 역할 설명이 맞는가? (예: Sapora가 선1 Case4 실험데이터 출처, Han이 선3 K 추출 방법론, Kwon2022 Polymers가 선3 §6의 직접 선행, PVT144가 사실상 선행연구2)

6. **윤석준 자료 취급** — 참고문헌이 아니라 "방향이 비슷한 발표자료"임이 본문에 명확한가? 별도 챕터로 분리했는가? 미완성·진행중 연구임(수렴 안 됨 등)을 정확히 전달하는가?

7. **round1~6 정합성** — 서술이 선행 DECISION과 충돌하지 않는가? (특히 2π, w_f=재료상수, FE 방법)

8. **읽기자료 완성도** — 한국어 자연스러움, 논리 흐름, 그림·본문 대응, 챕터 간 균형. 빠진 필수 내용.

## 결과물
`round7/codex.md` — 항목별 판정(정확/부분 정정 필요/틀림/확인 불가) + 근거 + 구체적 수정 지점(챕터·문단).
