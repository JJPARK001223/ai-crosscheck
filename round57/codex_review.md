# round57 Codex 2단계 검증 — B048 HTML 및 Claude 전사

검증일: 2026-10-21. 대상은 사용자가 지정한 B048 PDF 한 편과 HTML 28개 카드, `claude.md`, `claude_review.md`, `codex.md`이다. HTML과 기존 보고서는 수정하지 않았다. 이 보고서의 ‘페이지’는 별도 표시가 없으면 HTML 카드 번호다. 본문 인쇄 p.1–27은 PDF p.11–37에 대응한다. 전면부에는 이 빼기 규칙을 적용하지 않는다.

**결과:** 지정한 12개 수식의 `data-tex`는 PDF 지면과 일치한다. 다만 17페이지 제목에는 원문에 없는 등호가 있다. Table 1의 38개 요구사항, 가정표 5행, 참고문헌 12개는 내용상 일치한다. Table 2는 원문과 HTML 모두 **48개 변수**이며, HTML의 ‘49개’ 설명은 개수 오류다. Table 3에는 `PhoopStrMaxO`의 배열 표시 추가와 병합 비고 범위의 소실이 있다. 기호표의 `csp` 조판, 전면부 쪽수, 일부 한국어 표현 및 원문 밖의 명명도 아래에 구분했다. 이를 HTML 무오류 판정으로 읽으면 안 된다.

## 검증 방법과 버전

- PDF 37쪽 전부를 PyMuPDF로 150dpi PNG로 렌더링하여 직접 열람했다. 식 2, 식 4·5a, 식 5b는 400dpi 부분 이미지로, Figure 1 식·반경 표기 및 기호표 `csp`는 500dpi 부분 이미지로 추가 확인했다.
- HTML은 처음부터 끝까지 읽고, 28개 `section`의 한국어 본문·표·주석·접힌 영어 원문과 12개 `data-tex`를 확인했다. PDF 텍스트와 표 추출은 누락·철자 검색의 보조 수단이며, 지면 이미지와 함께 사용했다.
- 표의 줄바꿈, 공백, 따옴표 모양, 굵기와 이탤릭의 일반적 차이는 내용 오류로 세지 않았다. 다만 아래첨자 및 배열 표시처럼 기호를 바꾸는 차이는 기록했다. 원문 자체의 이상을 수학적으로 교정하지 않았다.
- 외부 문헌·실제 TIFFANY 코드의 작동은 조사하지 않았다. ‘일치’는 이 PDF의 서술과 일치한다는 뜻이다. 한국어 표현의 적합성 판단은 검토 의견이며 원문의 과학적 결론에 대한 보충이 아니다.
- 작업 시작 `git pull`: `Already up to date.` 기존의 다른 파일 변경과 미추적 파일은 보존했다. 시작 시 스테이징된 파일은 없었다.

검증 대상 SHA-256:

| 파일 | SHA-256 |
|---|---|
| `(ML16341B048)Cyclic stress intensity factors.pdf` | `3aaf46e98c5819a86a98fc1a3e29cf64b7b6cf94ab23c8433ca91f9e34cd764a` |
| `XLPR_주기응력확대계수_B048.html` | `8bfe83ff330d9e270140f7038e8c90389b2f6a9b8be1c56bac12d59d12dc58f4` |
| `round57/claude.md` | `10601acf928c82a7d25d0af546559ef548982a372a62118df10919804a9a9c37` |
| `round57/claude_review.md` | `811f3bece217c3a656e1b16a920bf00db4f61489b5650ec3c26c00c30f018854` |
| `round57/codex.md` | `e23c59d2675c8c120b41ab79687f7c29bdbaf6a0b3f23f61ee51bcfa7d510fb6` |

## (A) 페이지별 점검 결과표

‘일치, 예외’는 지정 부분 이외의 본문·표를 대조했으나 B의 문제가 남아 있다는 뜻이다. 인용은 원문 위치를 찾기 위한 짧은 발췌다.

| 페이지 | 항목 | 일치/불일치 | 원문 근거 |
|---|---|---|---|
| 1 | 문서번호, 네 사람의 성명·소속·역할·각 날짜, 개정 이력, SQA 고지와 번역 | 일치, 접힌 영어의 쪽수는 B06 | 서명쪽(PDF 3, 인쇄쪽 없음): “Author Signature”, “Reviewer Signatures”, “Approver Signatures”, “01/28/16”, “01/27/16”, “01/31/16”; 개정쪽(PDF 4): “administrative update in 2021”, “without incrementing the version number or issue date” |
| 2 | Executive Summary 모든 한국어 문단 | 의미 일치, 접힌 영어 쪽수 B06 | p.iv: “prepares inputs to xLPR related to cyclic conditions”, “fatigue crack initiation and growth calculations”, “influence functions”, “called by a pre-processor” |
| 3 | §1.1 세 문단 | 일치 | p.1: “strictly a deterministic module”; “uncertainties … primarily in the time-temperature inputs”; “providing test cases … then performing the verification and validation” |
| 4 | §1.2 목표 6개, §1.3 | 일치, 목표 2 표현은 B10 | p.1: “changes in restraint of thermal expansion stress”; p.2: “results are sorted to define maximum and minimum values” |
| 5 | §2, §2.1, §2.2 | 사실 일치. §2 반복 문단은 요약·2페이지 참조 형태 | p.3: “single or bimaterial pipe”; “Fluid properties for liquid water are temperature-dependent”; “A TIFFANY analysis must be performed for each thermal transient” |
| 6 | §2.3, §2.4의 5단계 | 일치. 원문의 단계 자기참조도 보존 | p.4: “There is no sacrifice in accuracy, other than TIFFANY’s restriction to straight sections of pipe”; “due to the stresses in steps 3 and 4” |
| 7 | Figure 1의 식, 상자·화살표·축 문구와 기호표 | 전사한 부분 일치. 그림 자체는 생략됐음을 HTML이 명시 | p.5 Figure 1: “Evaluation of Stress Intensity Factors vs. Time”, `K_I=∫₀ᵃσ(x)m(x,a)dx`; “Resulting K_a, K_c”; “Sorting for Evaluation of Maximum and Minimum K” |
| 8 | §2.4.1 한국어 본문, 가정표 5행×3열 | 일치 | pp.6–7: “No bias or uncertainty expected.”, “These differences may be small (?)”, “dissimilar elastic modulii”, “Minimal impact expected” |
| 9 | Eqn.1 전 항, 기호표, 목적·조건·수치해법 | 일치 | p.7: “governing partial differential equation”, “function of radial coordinate and time only, T(r, t)”, “thermal conductivity can be temperature-dependent” |
| 10 | Eqn.2 전 항、경계조건·차분·절점 정의·해법 | 식과 의미 일치, 해법 한국어 B07 | p.8: “This leads to equations such as”; “previous time-step”; “method of successive substitutions”. 마지막 항은 닫는 소괄호 없이 대괄호로 끝남 |
| 11 | §2.4.3 전체 번역, Figure 2 표 | 의미 일치, 어색한 직역 B08 | p.8: “same elastic constants E and μ”, “will behave more strongly like the majority material”, “constant (not zero) at any instant”; p.9: “Mat 1”, “Mat 2”, “Insulated OD” |
| 12 | Eqn.3a–c, 4의 부호·계수·적분경계·온도 첨자 | 수식 일치, 응력 명칭의 추가는 B11 | p.9: “In region 1 (inner material)”, “where”; Eqn.4 둘째 적분 `r(T−T_o)` |
| 13 | Eqn.5a–c 및 본문 인용 | 수식 일치, 응력 명칭의 추가는 B11 | p.9: “In region 2 (outer material)”; 5a 둘째 적분 하한 `r_1`; p.10: “μ is Poisson’s ratio”, “Timoshenko [7]” |
| 14 | Eqn.6, 가중평균 설명과 가정표 인용 | 일치 | p.10: “weighted average of the cross-sectional areas and elastic modulus values”; p.7: “rule-of-mixtures type of relationship”, “Minimal impact expected” |
| 15 | 균일 온도, T₀, 물성, α 제안 | 일치 | p.10: “all of the stresses are zero”, “except at the single temperature T=T₀”, “T₀ is user specified”, “instantaneous value … generally conservative” |
| 16 | Global Stresses, 압력, segment, stratification, mechanical | 일치 | pp.10–11: “non-pressure global stresses”, “zero at T₀ = 70°F”, “only deviations from these stresses”, “multiplied by a factor … (DispFactorIn)” |
| 17 | ΔK 표기, Kmax/min 정의, 균열·응력 방향 대응, 출력 | LaTeX·본문 일치, 제목 불일치 B01 | p.11: “ΔK (Kmax - Kmin)”; “axial stress … circumferential cracks”, “hoop stress … axial cracks”; “times at which Kmax occurs is not the same for all crack sizes” |
| 18 | Sorting, Uncertainty Quantification | 의미상 원문과 대응. 모호한 한국어 B09 | p.12: “results printed to files of Kmax and Kmin”; “Uncertainties in material properties are considered to be minimal, being available from the ASME Boiler and Pressure Vessel Code [9].” |
| 19 | §3.1, Table 1 RTIF-1–38의 3열 모든 칸 | 일치 | pp.13–16 “List of TIFFANY Module Requirements”; “The subroutine should be readable and modular”; “Numerical procedure to independently check the determination of maximum and minimum K values.”; “Independent numerical procedures or by examining the intermediate output” |
| 20 | §3.2–3.3 번역 전체 | 일치 | pp.16–17: “intermediate maxima and minima are not captured”, “explicit passing of variables”, “consult the Error Flag output” |
| 21 | §3.4, Table 2 변수명·자료형·설명·제한, 자료형 주석 | 48개 행 모두 일치. 49개라는 설명만 B02 | pp.18–19 “Inputs to Subroutine TIFFANY”; “TitleIn”, “T21In”, “T22In”, “CTWAxa [ ]”; “[] – Indicates an array input” |
| 22 | Table 3의 29개 출력 변수, 설명·비고, 표 아래 주석 | 대부분 일치, B03·B04 | pp.20–21 “Outputs from Subroutine TIFFANY”; “PhoopStrMaxO”; “Only for Type 1 input”; “K in this table is the excursion from normal operation” |
| 23 | Table 4의 7행×3열, 물성·입력이력 번역 | 일치 | p.21: “thermal conductivity”, “specific heat”, “thermal diffusivity”; “Values of these properties … TIFFANY STP [12]”; “expected to bound the transient input from actual plant measurements” |
| 24 | §3.5–3.6 전 문장, Figure 3 양 분기 | 사실·순서 일치, closed form 번역 B12 | pp.21–23: “closed form solutions”, “scope does not include the wrapper code”; Figure 3 “IAType = 2 or 3”, “Calculate K (CalcK23)”, “IAType = 1”, “End Timestep Iteration” |
| 25 | §4–6 전 문장 | 사실 일치, closed form 번역 B12 | pp.24–26: “No recommendatioins … at this time”, “None at this time”, “TIFFANY itself is deterministic, but there are uncertainties in the inputs” |
| 26 | 참고문헌 [1]–[12] 모든 칸 | 일치 | p.27: [5] “SAI–331–82–PA”, “8679501, Task 2”; [7] “D.K. Edwards, V.E. Denny and A.F. Mills”; [8] “S. Timoshenko and J.N. Goodier” |
| 27 | 기호표22항목·약어표17항목 모든 칸 | 내용 일치, `csp` 조판 B05 | pp.viii–ix: “csp — Specific heat”, “H1 — Inner pipe thickness”, 이탤릭 “K — Thermal conductivity”, “SI — Système International d’Unités”, “SRD — Software Requirements Document” |
| 28 | 원문 표기 차이·오타 목록 | 관찰한 글자들은 일치. 오류라는 분류가 확정되지 않은 부분 B13 | pp.4,7–10,13,19,20,24 및 p.viii의 실제 표기. 특히 p.9 “In region 1”, “In region 2”가 서로 다른 식의 문맥임 |
| 머리말·꼬리말 | 출처, 쪽수 원칙, 저작권 문구 | 본문 쪽수 대응은 일치, 저작권 범위는 B14 | 면책쪽(PDF 2, 인쇄쪽 없음): “EPRI RETAINS COPYRIGHT IN EPRI-GENERATED MATERIALS CONTAINED IN THIS PUBLICATION.” |

### A-1. 수식 12개 항 단위 대조 기록

아래 수학 표기는 지면에서 읽은 항의 식별용 전사이며 교정식이 아니다. Eqn.2의 미닫힘도 유지한다.

| 식 / HTML 페이지 | 지면에서 항별로 확인한 내용 | 판정 |
|---|---|---|
| 1 / 9 | 좌변 `ρ c_sp ∂T/∂t`; 우변 `1/r`, `∂/∂r`, 괄호 안 `kr ∂T/∂r` | 일치, p.7 |
| 2 / 10 | 좌변 `δ²h²ρc_sp/Δt`, `(T_j−T*_j)`; 우변 `1/r_j`; 첫 항 `+T_{j+1}(k_{j+1}r_{j+1}+k_jr_j)`; 가운데 `−T_j(k_{j+1}r_{j+1}+2k_jr_j+k_{j−1}r_{j−1})`; 끝 `+T_{j−1}(k_jr_j+k_{j−1}r_{j−1}]` | 일치, p.8. Claude 초기 전사의 끝 `)`는 지면에 없음 |
| 3a / 12 | `E/(1−μ)·1/r²`; `−α₁∫[r_i→r]r(T−T₀)dr`; `+(r²−r_i²)/(r_o²−r_i²)Ω` | 일치, p.9 |
| 3b / 12 | 동일 전계수; `+α₁∫[r_i→r]r(T−T₀)dr`; `−α₁r²(T−T₀)`; `+(r²+r_i²)/(r_o²−r_i²)Ω` | 일치, p.9 |
| 3c / 12 | `E/(1−μ)`; `{2Ω/(r_o²−r_i²)−α₁(T−T₀)}` | 일치, p.9 |
| 4 / 12 | `Ω=α₁∫[r_i→r_c]r(T−T₀)dr + α₂∫[r_c→r_o]r(T−T_o)dr`; 마지막 첨자는 숫자0이 아닌 이탤릭 o | 일치, p.9 |
| 5a / 13 | `E/(1−μ)·1/r²`; 첫 항 `−α₂∫[r_c→r]r(T−T₀)dr`; 둘째 `−(r_o²−r²)/(r_o²−r_i²)α₁∫[r_1→r_c]r(T−T_o)dr`; 셋째 `+(r²−r_i²)/(r_o²−r_i²)α₂∫[r_c→r_o]r(T−T_o)dr` | 일치, p.9. 하한 `r_1`과 두 `T_o`를 보존 |
| 5b / 13 | `E/(1−μ)·1/r²`; `+α₂∫[r_c→r]r(T−T₀)dr`; `−α₂r²(T−T₀)`; `+(r²+r_o²)/(r_o²−r_i²)α₁∫[r_i→r_c]r(T−T₀)dr`; `+(r²+r_i²)/(r_o²−r_i²)α₂∫[r_c→r_o]r(T−T₀)dr` | 일치, p.10. 두 분자 순서와 모든 `T₀` 확인 |
| 5c / 13 | `E/(1−μ)`; `{2Ω/(r_o²−r_i²)−α₂(T−T₀)}` | 일치, p.10 |
| 6 / 14 | 분자 `E₁A₁+E₂A₂`; 분모 `A₁+A₂` | 일치, p.10 |
| K_I / 7 | `K_I=∫[0→a]σ(x)m(x,a)dx` | 일치, Figure 1 p.5 |
| ΔK / 17 | `ΔK (Kmax−Kmin)`、등호 없음 | `data-tex` 일치, p.11. 제목은 B01 |

### A-2. 표 전수 대조 범위

1. **Table 1:** RTIF-1–8(p.13), 9–17(p.14), 18–29(p.15), 30–38(p.16)의 Requirement / Short Description / Acceptance Criteria를 각 행별로 확인했다. RTIF-11–14의 `(a/c,a/h,θ)`, 15–18의 `(c,θ)`, 19–22의 `(a/c,a/h)`, 23–24의 `(c)`를 포함하여 일치한다. RTIF-27에 `(θ)`가 없고 RTIF-28–30·35에 있는 차이도 보존됐다. RTIF-6/7의 표번호와 RTIF-5의 `[8]`은 원문 그대로이며 임의로 고치지 않는다.
2. **Table 2:** p.18에 30행, p.19에 18행, 합계 48행이다. TitleIn부터 T21In까지 30행, T22In부터 CTWAxa까지 18행을 대조했다. 자료형은 **Character 1 / Integer 9 / Real (8) 38**이다. Integer는 IATypeIn, IUnitsIn, IPrintIn, NHist, NumSegsIn, NAOCIn, NAOTIn, NCTWCircIn, NCTWAxIn이다. 변수 행 수는 표 헤더를 제외했다. 60자 제한, NHist의 10000, 개수 제한 100, IAType/IYType의 조건, 배열 표시가 있는 **7행**(TimeA, FlTempA, PrA, AOCa, AOTa, CTWCirca, CTWAxa)까지 확인했다.
3. **Table 3:** Circumferential 14행(8개 K, PaxStrMaxO, AllAxStrMaxO/MinO, TimeMax/MinAllAxialO, RiseTimeAxStrO), Axial 이후15행(6개 K, PhoopStrMaxO, AllHoopStrMaxO/MinO, TimeMax/MinAllHoopO, RiseTimeHpStrO, TempMaxO/MinO, Ierror), 합계29행이다. 설명의 maximum/minimum, deepest/surface, 차원, 배열순서, ID, RGTS, Pr, membrane/bending, 오류범위 `101-120,123-128,131-144 or 0`를 대조했다. B03·B04 이외 내용상 차이 없음.
4. **Table 4:** `thermal conductivity / K / W/(m-°K)`, `specific heat / C / J/(kg-°K)`, `Density / ρ / kg/m³`, `thermal diffusivity / κ / m²/s`, `Young’s modulus / E / MPa`, `Poisson’s ratio / ν / --`, `coeff of thermal exp / α / °C⁻¹`의 21개 칸 확인. 일치.
5. **가정표:** 5행의 가정·기술적 근거·예상 영향 15칸, 특히 phase transformation, radiation/convection, DMWs, `(?)`, `modulii`, `variation of µ` 반복을 확인했다. 일치.
6. **기호표·약어표:** 각각22행·17행의 기호/약어와 정의를 대조했다. `csp` 조판만 B05. `H1/h2`, 두 `K`, σT/σB, μ, SI, SRD 정의의 원문 표기를 보존했다.
7. **참고문헌:** [1]–[12]의 문서코드·제목·버전, 저자·출판사·연도·계약번호까지 대조했다. 일치. 본문의 “Timoshenko [7]”를 [8]로 바꾸지 않은 것은 전사 오류가 아니다.

## (B) 불일치·오역·원문 밖 명명·영어 유지 후보

확신도 ‘높음’은 지면에서 글자·범위·추가 여부를 확인했다는 뜻이다. ‘중간’은 문장 표현에 관한 판단이며 의미 오류를 확정한 것이 아니다. 아래 수정안은 보고서상 제안일 뿐 HTML에는 반영하지 않았다.

| ID·구분 | 페이지 | 현재 | 원문(영어 인용 + 인쇄쪽) | 수정안 | 확신도 |
|---|---|---|---|---|---|
| B01·수식 추가 | 17 제목 | `ΔK = K_max − K_min` | p.11: “ΔK (Kmax - Kmin)”; 절 제목은 “Stress Intensity Factors”. 지면에 등호 없음 | 제목에서도 `ΔK (K_max − K_min)`로 유지. 수식 카드 자체는 유지 | 높음 |
| B02·개수 오류 | 21 주석 | “변수 49개 전부” | pp.18–19: “Inputs to Subroutine TIFFANY”; “TitleIn”–“T21In”30행, “T22In”–“CTWAxa [ ]”18행 | “변수48개 전부”. **49번째 변수가 누락된 것으로 판단하지 않는다** | 높음 |
| B03·배열 표시 추가 | 22 Table 3 | `PhoopStrMaxO [ ]` | p.21 해당 변수칸은 “PhoopStrMaxO”, 설명 “Maximum pressure stress change (hoop)”. 그 변수칸에 `[ ]` 없음 | 변수명 뒤 `[ ]` 삭제 | 높음 |
| B04·병합 비고 범위 손실 | 22 Table 3 | PW/TW와 “Only for Type 1 input”을 첫 행에만 넣고 나머지 행의 비고를 빈 칸으로 둠. 별도 주석은 일부 묶음 표시였다고만 설명 | p.20 “PW Cracks”는 KCircDeepMxO–KCircSurfMnO 4행, “TW Cracks”는 KCircTWMxMO–MnMO 2행 및 MxBO–MnBO 2행; axial PW4행·TW2행도 병합. p.21 “Only for Type 1 input”은 TempMaxO와 TempMinO **두 행**에 걸친 셀 | 원문 병합 범위를 `rowspan`으로 보존하거나 각 해당 행에 비고를 반복. 특히 TempMinO에도 Type1 조건이 적용되는 표 구조를 보존 | 높음 |
| B05·기호 조판 정규화 | 27 기호표 | `c<sub>sp</sub>` | p.viii: “csp — Specific heat”. 지면에서 c·s·p가 같은 기준선에 있고 하첨자가 아님. 반면 Eqn.1(p.7)은 c의 하첨자 sp | 기호표는 지면처럼 `csp`로 표시. 식의 `c_{sp}`는 그대로 | 높음 |
| B06·전면부 쪽수 | 1·2 접힌 영어 | PDF2·3·4·5 모두 “원문 인쇄 p.i~x” | 면책 “DISCLAIMER”(PDF2), 서명쪽 “Author Signature”(PDF3), “Revision History”(PDF4)는 인쇄쪽 번호가 보이지 않음. “EXECUTIVE SUMMARY”(PDF5) 하단은 **iv** | 앞 세 항목은 “인쇄쪽 미표기, PDF p.2/3/4”; Summary는 “인쇄 p.iv, PDF p.5”. 본문의 PDF쪽−10 규칙과 분리 | 높음 |
| B07·영어 유지 후보 | 10 풀이 방법 | “successive substitutions(연속 대입)법” | p.8: “These equations are readily and efficiently solved by the method of successive substitutions.” | 원문의 영어 문장 그대로 유지. ‘연속 대입’이라는 어색한 대응어를 굳이 붙이지 않음 | 중간(표현) |
| B08·기계적 직역 | 11 취급 방식 | “이중금속 재료의 비율이 비교적 작은 이중금속 구조는 다수 재료처럼 더 강하게 거동한다” | p.8: “Therefore, bimetallic structures with a relatively small ratio of bimetallic material, will behave more strongly like the majority material.” | 이 영어 문장 그대로 사용. 한국어의 ‘더 강하게’는 ‘like’와 결합한 표현을 강도 증가처럼 읽게 하고 ‘다수 재료’도 불명료함. 원문 자체의 ratio 표현을 추측해 보충하지 않음 | 중간~높음(번역 표현) |
| B09·모호한 문장 영어 유지 | 18 불확실성 | “재료 물성의 불확실성은 …[9]에서 구할 수 있어 미미한 것으로 본다” | p.12: “Uncertainties in material properties are considered to be minimal, being available from the ASME Boiler and Pressure Vessel Code [9].” | 원문 영어 그대로 사용. `being available`의 대상을 재료 물성 또는 불확실성으로 단정해 다시 설명하지 않음. 현재 문장을 확정 오역으로 세지는 않음 | 중간(명료성) |
| B10·구문의 의미 보존 | 4 목표2 | “열팽창 구속 응력의 변화” | p.1: “changes in restraint of thermal expansion stress” | 이 구절은 영어 그대로 유지. 원문은 `changes in restraint`로 되어 있는데 현재 한국어는 응력의 변화에 초점을 옮겨 읽힐 수 있음 | 중간(구문) |
| B11·원문에 없는 명시적 기호 명명 | 12·13 목적·조건 | “반경·접선(θ)·축 방향 응력”, “반경·접선·축 방향 응력” | p.9 원문은 “In region 1 (inner material)” / “In region 2 (outer material)” 다음에 σr·σθ·σz 식을 제시. p.8에는 “radial stress”, “axial strain”이 있고 기호표 p.viii의 θ는 “Angular location”이지만, σθ를 ‘접선 응력’이라고 명시한 정의 문장은 없음 | 엄격한 원문 한정 규칙에 맞춰 “In region 1 (inner material)” / “In region 2 (outer material)”와 수식 기호 그대로 사용. 물리적 명칭의 옳고 그름을 주장하는 지적은 아님 | 높음(명시적 정의 부재) |
| B12·영어 유지 후보 | 24·25 | “닫힌 형태 해”, “닫힌 형태의 온도·응력 해” | p.22: “closed form solutions for transient temperature fields”, “closed form solutions”; p.26: “closed form temperature and stress solutions” | 해당 표현 또는 해당 문장을 원문 영어로 유지. ‘닫힌 형태 해’는 기계적인 직역으로 읽힘 | 중간(표현) |
| B13·원문 오류라는 분류의 근거 부족 | 28 목록3 | 식3b·5b의 분자 차이를 “원문 자체의 표기 불일치와 오타 모음”에 포함 | p.9 “In region 1 (inner material)”의 3b는 `(r²+r_i²)Ω`; p.9–10 “In region 2 (outer material)”의 5b는 α₁항 `r²+r_o²`, α₂항 `r²+r_i²`. 원문은 이를 오타라고 쓰지 않음 | 식은 그대로 두되 해당 항목은 ‘지면 표기 관찰’로 표시. 서로 다른 영역 식의 분자가 다르다는 관찰만으로 오타·오류로 확정하지 않음 | 높음(표기 관찰), 오류 여부 확인 불가 |
| B14·원문보다 넓은 저작권 서술 | 꼬리말 | “원문 저작권은 EPRI에 있습니다” | 면책쪽(PDF2, 인쇄쪽 없음): “EPRI RETAINS COPYRIGHT IN EPRI-GENERATED MATERIALS CONTAINED IN THIS PUBLICATION.” | 이 영어 문장을 그대로 유지. 원문은 EPRI가 생성한 자료의 저작권 보유로 범위를 한정함 | 높음(인용 범위) |

확정된 수치·기호 오류와 중간 확신도의 영어 유지 후보를 같은 성격의 오류로 합산하지 않는다. 위에 들지 않은 한국어 문장에서 별도의 확정적 의미 반전이나 외부 과학적 설명의 삽입은 발견하지 못했다. 검증 과정·AI 이름·dpi·파일 경로를 적은 ‘신뢰성’ 주석은 B048 원문 인용이 아니라 편집 이력이다. 그 사실은 이 보고서의 작업 기록으로는 확인할 수 있으나 원문 자체에서 인용 근거를 붙일 수 없으므로, 과학 내용의 근거로 사용하지 않는다.

## (C) claude.md 오류·누락 및 claude_review.md 재검증

Claude 보고서의 핵심 사실(독립 모듈, 결정론적 성격, 열전도·탄성론·영향함수, 균열 방향별 응력 사용, 불확실성, 시험 범위, 각 절의 위치)은 원문과 일치했다. 다음은 구체적인 예외다.

| ID | 위치·현재 서술 | PDF 지면 근거(영어 + 인쇄쪽) | 판정 및 필요한 조치 |
|---|---|---|---|
| C01 | §1 Eqn.2 마지막에 `...r_{j-1})\right]` | p.8 “This leads to equations such as”; Eqn.2 지면 끝 `+T_{j−1}(k_jr_j+k_{j−1}r_{j−1}]` | 닫는 소괄호를 추가한 전사 오류. `claude_review.md`는 오류를 인정하고 HTML은 이미 바로잡았으나 `claude.md`의 해당 행에는 그대로 남아 있음 |
| C02 | §3 Table4를 `k W/(m·°K), c J/(kg·°K)`로 요약 | p.21 “thermal conductivity” 기호 **K**, “specific heat” 기호 **C** | 대소문자 전사 오류. 소문자 k·c로 정규화하지 말 것. HTML의 K·C는 맞음 |
| C03 | §3 Nomenclature의 열전도도 기호를 `κ`로 먼저 적고 뒤에서 “지면 기호 K”라고 설명; §5도 “κ 기호 K” | p.viii “Thermal conductivity” 앞의 기호는 이탤릭 대문자 **K**. p.21 “thermal diffusivity”의 기호는 **κ** | 혼동을 유발하는 전사. 기호표 행은 `K`로만 전사하고 Table4의 diffusivity κ와 구별할 것. HTML의 K는 맞음 |
| C04 | §5 “Eqn.4·5a·5b 일부 항에 T_o와 T_0 혼용” | p.9 Eqn.4·5a에는 T_o가 보임. p.10 Eqn.5b의 피적분함수·비적분항은 전부 **T₀**; 주변 문장 “In the above equations, μ is Poisson’s ratio.” | 혼용 범위에 5b를 포함한 것은 지면과 다름. 4·5a로 한정. HTML과 `claude_review.md`는 5b를 같은 방식으로 잘못 바꾸지는 않았음 |
| C05 | §3 Table1 ‘전체’를 외부 `scratchpad/b048/b048_text.txt`로 넘기고 요약만 적음. Table2/3도 변수별 행과 전체 칸을 보고서에 싣지 않음 | pp.13–16 “List of TIFFANY Module Requirements”의38행 및 Acceptance Criteria; pp.18–19 “Inputs to Subroutine TIFFANY”48행; pp.20–21 “Outputs from Subroutine TIFFANY”29행 | 사실 오기와 구별되는 **전사 누락·추적성 문제**. 해당 상대경로는 이 저장소에서 확인되지 않음. 따라서 `claude.md` 자체를 모든 칸이 실린 완전 전사본이라고 볼 수 없음. 이번 검증은 HTML과 PDF를 직접 대조함 |
| C06 | `claude_review.md` 결론 “표·본문 전사는 두 전사가 상충하는 항목 없음” | p.21 Table4 K·C와 p.viii 기호표 K는 C02·C03의 실제 반례 | 이 포괄 판정은 철회·한정 필요. 수식 재판독 결과가 옳다는 것과 모든 표 전사가 충돌 없다는 것은 별개임 |

### C-1. Claude가 맞게 지적한 Codex 전사 오류

`claude_review.md`의 다음 지적은 이번에 별도로 렌더링한 지면으로 재확인했다. 내 이전 결과도 기준으로 삼아 자동 방어하지 않는다.

- **Eqn.4(p.9):** `codex.md`는 둘째 적분을 `T_0`로 정규화했다. 지면은 `T_o`다. Claude 지적이 맞고 HTML은 지면대로다.
- **Eqn.5a(p.9):** `codex.md`는 둘째 적분 하한을 `r_i`, 둘째·셋째 적분을 `T_0`로 전사했다. 지면은 각각 `r_1`, `T_o`, `T_o`다. Claude 지적이 맞고 HTML은 지면대로다.
- **Eqn.2(p.8):** Codex의 닫는 소괄호 부재 관찰은 맞았다. 다만 이것이 Codex 전사 전체의 정확성을 보증하지는 않는다.
- **Eqn.5b(p.10):** α₁항 분자 `r²+r_o²`, α₂항 분자 `r²+r_i²`라는 양쪽 전사는 지면과 일치한다. 이를 통일하거나 교정할 근거는 이번 작업에 없다.

이 단계를 위해 기존 독립 결과를 덮어쓰지 않고, 오류 기록을 여기 남긴다.

## (D) 확인 불가 항목과 이유

| 항목 | 확인 가능한 사실 / 원문 근거 | 확인 불가 이유·처리 |
|---|---|---|
| 원문 자체 수식의 수학적 정답·작성자의 의도 | p.8 Eqn.2 괄호, p.9 Eqn.4·5a의 첨자, p.10 Eqn.5b 분자를 지면에서 확인 | 원문이 해당 글자를 정오표로 해명하지 않는다. `r_1`을 `r_i`, `T_o`를 `T_0`로 고치는 등 추정 교정 금지 |
| 식3b/5b 분자의 차이가 오류인지 | p.9 “In region 1 (inner material)” / “In region 2 (outer material)” | 서로 다른 식의 글자가 다름은 사실이나 그것이 오류라는 결론은 원문에 없음. B13처럼 관찰과 오류 판정을 구별 |
| σθ·σz·m(x,a) 등 별도 명칭·해석 | p.5 “Influence Functions”; p.viii “Angular location”; p.9 각 식 | 통상적 공학지식으로 보충하지 않음. 명시적 정의가 없는 기호의 해석은 이번 원문 전사 기준으로 확인 불가 |
| Table3의 a/t에 있는 t의 의도 | p.20 `[a/t,a/c,…]`; p.viii “t — Time”; pp.14–15는 a/h | 지면 표기 차이만 확인. t를 벽두께라고 교정·정의할 근거 없음 |
| 인용문헌·모듈 코드·시험의 실제 적합성 | p.22 “compared with finite element calculations”; p.27 참고문헌 목록 | B048에 그렇게 적혀 있다는 사실만 확인. SRD/STP/STRR/MVR·코드는 입력 범위 밖이므로 실제 정확도·보수성·요구 충족 여부 판정하지 않음 |
| HTML의 AI/dpi 작업 이력 | 각 카드 ‘신뢰성’ 주석은 B048 자체의 문장이 아님 | 현재 입력만으로 과거 각 AI가 정말 그 dpi로 판독했는지는 입증 불가. 이번 보고서의 직접 판독 결과와 구별 |
| claude.md가 참조한 별도 전사 파일 | §3의 `scratchpad/b048/b048_text.txt` | 저장소의 해당 상대경로가 확인되지 않음. 그 파일의 모든 칸을 전사했는지라는 주장까지 검증하지 못함. HTML의 표는 직접 검증 완료 |
| 브라우저별 실제 표시·수식 렌더러 로딩·인쇄 레이아웃 | 이번에 검증한 것은 HTML의 내용·LaTeX와 PDF 지면의 대응 | 브라우저에서 CDN 로딩이나 화면/인쇄의 잘림·스크롤을 시험한 것은 아님. 내용 일치와 표시 품질을 동일시하지 않음 |

확인 불가 항목을 임의로 ‘일치’ 또는 ‘오류’로 확정하지 않았다. 사용자 결정 기록인 DECISION.md는 작성·수정하지 않았다.
