# round57 Codex 3단계 — 수정 반영 재검증

검증일: 2026-10-21. 지정된 `codex_review.md`와 `claude_review.md` 끝의 「추가 — Codex 2단계(codex_review.md) 반영 결과」를 읽고, 수정된 HTML과 B048 PDF를 직접 대조했다. HTML 및 다른 결과 보고서는 수정하지 않았다.

**판정: B01~B14는 모두 반영됐다(반영 14, 부분 0, 미반영 0). 수정된 문단·표에서 이번 수정 때문에 새로 발생했다고 확인된 오류는 없다. 다만 전체 28개 카드 재점검에서 접힌 영어 본문의 기호 누락과 원문 밖 편집 서술 등이 남아 있다. 따라서 ‘B01~B14 반영’과 ‘HTML 전체 무오류’는 구별해야 한다.**

이 보고서의 ‘HTML 쪽’은 28개 카드의 번호다. 원문 인쇄 p.1~27은 PDF p.11~37, p.iv는 PDF p.5, p.viii~ix는 PDF p.9~10이다. PDF p.2~4는 인쇄쪽 번호 미표기다.

검증 대상:

| 파일 | SHA-256 |
|---|---|
| `J:\Desktop\XLPR\2026_10_21_B048_주기응력확대계수\XLPR_주기응력확대계수_B048.html` | `f4ce336db9f1e300c9ad2ac9479cfc6bcdc660bcc12d81a143c44336b1d96004` |
| `J:\Desktop\XLPR\xLPR참고문헌\(ML16341B048)Cyclic stress intensity factors.pdf` | `3aaf46e98c5819a86a98fc1a3e29cf64b7b6cf94ab23c8433ca91f9e34cd764a` |

검증 방법: HTML 28개 `section`의 본문·표·주석·접힌 영어를 읽고 PDF의 해당 본문과 재대조했다. PDF 텍스트 추출은 검색·문장 비교에 사용하고, 표 병합과 기호·그림 및 교체된 인용은 지면 이미지로 보완했다. 이번에 직접 렌더링해 열람한 PDF쪽은 2, 9, 11, 15, 18~22, 30~33, 36이다. 이전 단계에서 열람했다는 이유만으로 이번 직접 열람에 포함하지 않았다. 영어의 줄바꿈과 연속 공백은 지면 조판으로 보고 비교에서 제외했으며, 철자·문장부호·기호의 누락은 별도로 확인했다. 외부 문헌이나 통상 공학지식으로 원문을 보충하지 않았다.

## (A) B01~B14 반영 확인표

| ID | HTML 쪽 | 판정 | 현재 HTML 및 원문 대조 근거 |
|---|---|---|---|
| B01 | 17 | 반영 | 제목은 `2.4.5 Stress Intensity Factors`이며 등호가 없다. `data-tex`도 `\Delta K\ \left(K_{\max}-K_{\min}\right)`다. 원문 인쇄 p.11의 `ΔK (Kmax - Kmin)`와 대응한다. |
| B02 | 21 | 반영 | 주석은 ‘변수 48개 전부’. 실제 표의 변수 행도 48개(TitleIn~T21In 30개, T22In~CTWAxa 18개)다. 원문 pp.18~19와 일치한다. 보고서의 ‘코드에서 계산’이라는 과거 수정 방법은 현재 HTML에 동적 계산 코드가 있다는 뜻으로 해석하지 않았다. |
| B03 | 22 | 반영 | 변수칸은 `PhoopStrMaxO`이며 `[ ]`가 없다. p.21 지면과 일치한다. 비고의 `PrA [ ]`는 별도 입력 변수의 표기이므로 삭제 대상이 아니다. |
| B04 | 22 | 반영 | Notes의 `rowspan`은 순서대로 4, 2, 2, 4, 2, 2다. 병합 중간 행에는 불필요한 빈 Notes 셀이 없어 열이 밀리지 않는다. 아래 범위표와 PDF pp.20~21의 실제 가로 경계선을 대조했다. |
| B05 | 27 | 반영 | 기호표는 같은 기준선의 `csp`이며 하첨자 태그가 없다. p.viii 지면과 일치한다. 식의 `c_{sp}`는 그대로여서 기호표와 식의 조판 차이를 보존했다. |
| B06 | 1~2 | 반영 | 접힌 영어에서 PDF p.2/3/4는 각각 ‘인쇄쪽 번호 미표기’, Summary는 ‘원문 인쇄 p.iv (PDF p.5)’다. 본문 p.1=PDF p.11 규칙을 전면부에 적용하지 않았다. |
| B07 | 10 | 반영 | ‘연속 대입’ 번역이 삭제되고 `These equations are readily and efficiently solved by the method of successive substitutions.`를 그대로 인용했다. 인쇄 p.8 지면의 문장과 일치한다. |
| B08 | 11 | 반영 | 강도 증가로 읽힐 수 있었던 한국어 대신 `Therefore, bimetallic structures with a relatively small ratio of bimetallic material, will behave more strongly like the majority material.`를 인용한다. 이어지는 `In addition, the variation of E and µ ... diffusivity.`도 p.8 원문과 일치한다. 원문의 µ 반복을 추정 교정하지 않았다. |
| B09 | 18 | 반영 | `Uncertainties in material properties are considered to be minimal, being available from the ASME Boiler and Pressure Vessel Code [9].`가 p.12와 글자·문장부호까지 일치한다. `being available`의 대상을 새로 단정하는 한국어는 없다. |
| B10 | 4 | 반영 | 목표 2의 구절은 `including: cyclic stress at inner surface of the pipe; rise time of transient, and changes in restraint of thermal expansion stress.`로 p.1과 일치한다. 세미콜론·쉼표·마침표 및 `changes in restraint`를 보존했다. |
| B11 | 12~13 | 반영 | 목적·조건은 `In region 1 (inner material)` / `In region 2 (outer material)`와 σ_r·σ_θ·σ_z 기호로 기술된다. ‘접선(θ) 응력’이라는 별도 명명은 삭제됐다. p.9의 두 영역 문구 및 수식과 대응한다. |
| B12 | 24~25 | 반영 | ‘닫힌 형태’ 번역이 없다. 24쪽의 `closed form solutions for transient temperature fields`는 p.22의 연속 구절, 25쪽의 `comparisons with closed form temperature and stress solutions, as well as finite element computations [10]`는 p.26의 연속 구절과 일치한다. 주변 검증 범위·wrapper 제외·통합 시험 문단도 pp.21~22와 대응한다. |
| B13 | 28 항목 3 | 반영 | 식 3b/5b의 분자 차이에 ‘표기 관찰, 오류 여부는 원문에 없음’을 명시했다. 식의 분자 자체를 통일하지 않았다. 이 특정 항목의 수정은 완료됐지만 다른 항목의 포괄적인 ‘이상/오타’ 분류는 B절 F04처럼 별도 잔여 사항이다. |
| B14 | 꼬리말 | 반영 | `EPRI RETAINS COPYRIGHT IN EPRI-GENERATED MATERIALS CONTAINED IN THIS PUBLICATION.`를 인용한다. PDF p.2 지면의 대문자·하이픈·마침표와 일치하고, ‘원문 저작권은 EPRI에 있다’는 범위 확대 문장은 없다. |

### Table 3 병합 범위 직접 확인

| Notes | HTML 시작 변수 | 마지막 변수 | rowspan | 원문 |
|---|---|---|---|---|
| PW Cracks | KCircDeepMxO | KCircSurfMnO | 4 | 인쇄 p.20, PDF p.30 |
| TW Cracks | KCircTWMxMO | KCircTWMnMO | 2 | 같은 쪽 |
| TW Cracks | KCircTWMxBO | KCircTWMnBO | 2 | 같은 쪽 |
| PW Cracks | KAxDeepMxO | KAxSurfMnO | 4 | 같은 쪽 |
| TW Cracks | KAxTWMxO | KAxTWMnO | 2 | 같은 쪽 |
| Only for Type 1 input | TempMaxO | TempMinO | 2 | 인쇄 p.21, PDF p.31 |

TempMinO까지 조건이 걸리고 Ierror에는 걸리지 않는다. PW/TW 조건이 뒤의 응력 출력까지 번지지 않는다. 수정된 Table 3의 29개 변수명·설명·비고를 다시 대조했으며 병합으로 인한 내용 변경이나 행 누락은 발견하지 못했다.

### 28쪽 재점검 범위와 쪽번호

| HTML 쪽 | 대조한 원문 | 재점검 결과 |
|---|---|---|
| 1, 2 | PDF pp.1~4; 인쇄 p.iv | 문서 정보·개정 내용·요약 및 수정된 전면부 쪽수 확인. 추가 오류 발견 없음. |
| 3, 4 | 인쇄 pp.1~2 | 역할·목표 6개·모델 설명 및 B10 확인. 추가 오류 발견 없음. |
| 5, 6 | 인쇄 pp.3~4 | 모델 설명·개발·선정 근거·5단계 확인. 원문의 `steps 3 and 4`는 유지돼 있다. |
| 7, 8 | 인쇄 pp.5~7 | Figure 1 전사와 가정표 5행 확인. 그림 곡선 자체를 생략했다는 표시가 있다. 새로운 과학적 해석 삽입은 발견하지 못했다. |
| 9, 10, 11 | 인쇄 pp.7~9 | 열전도·차분 설명, B07~B08, Figure 2 확인. 신뢰성 주석 문제는 F05. |
| 12, 13, 14 | 인쇄 pp.9~10 | 영역별 식 설명·B11·가중평균 확인. T_o/r_1 등 기존 관찰을 임의 교정하지 않았다. |
| 15, 16, 17 | 인쇄 pp.10~11 | 균일 온도·기준 온도·다른 하중·K 설명·B01 확인. 접힌 영어 누락은 F01~F03. |
| 18 | 인쇄 p.12 | 정렬·불확실성 및 B09 확인. 추가 오류 발견 없음. |
| 19, 20 | 인쇄 pp.13~17 | 요구사항 38행·한계·통합 요구 확인. 원문의 표번호와 RTIF-27의 배열 표기 차이를 유지했다. |
| 21, 22, 23 | 인쇄 pp.17~21 | 입력 48개·출력 29개·물성표 7행 및 B02~B04 확인. 새로운 숫자·조건 오류 발견 없음. |
| 24, 25 | 인쇄 pp.21~26 | V&V·Figure 3 양 분기·권고·교훈·요약 및 B12 확인. 추가 오류 발견 없음. |
| 26, 27 | 인쇄 p.27; pp.viii~ix | 참고문헌 12개·기호 22개·약어 17개 및 B05 확인. 새 쪽번호 오류 발견 없음. |
| 28, 머리말·꼬리말 | 위 원문 위치 및 PDF p.2 | B13~B14 확인. 원문 밖 분류·이력의 잔여 사항은 F04~F05. |

‘추가 오류 발견 없음’은 해당 범위를 재검토했다는 결과이며 무오류의 증명은 아니다. 이번 전면부 수정 후 본문/전면부의 새로운 쪽번호 오류는 발견하지 못했다.

## (B) 새로 확인한 잔여 문제

아래는 이번 재검토에서 구체화한 잔여 사항이다. B07~B10·B12·B14의 새 인용문 자체의 철자 오류와 구별한다. F05의 편집 이력은 2단계에서도 원문 밖 내용으로 언급했으며 새 발견으로 중복 집계하지 않는다. 수정 전 HTML 전체 사본을 이번 입력으로 확보하지 않았으므로 F01~F04의 발생 시점을 이번 수정 전후로 확정하지 않는다.

| ID·문제 | 페이지 | 현재 | 원문 | 수정안 | 확신도 |
|---|---|---|---|---|---|
| F01·영어 본문 조건의 기호 누락 | HTML 15·16의 접힌 영어, 원문 인쇄 p.10/PDF p.20 | `However if` 다음에 `α ≠`만 남고 이어서 `, a uniform temperature ...`가 나온다. α의 두 하첨자와 우변 α가 소실됐다. 펼친 본문 인용·한국어는 맞다. | 지면은 `However if α₁ ≠ α₂, a uniform temperature produces stresses except at the single temperature T=T₀.` | 접힌 영어에도 `α₁ ≠ α₂`를 그대로 복원한다. 독립된 식 행을 생략한다는 안내와 달리 문장 안 조건이 손상된 경우다. 원문 자체 오류로 표시하지 않는다. | 높음 |
| F02·영어 본문 응력 기호 및 닫는 괄호 누락 | HTML 15·16의 접힌 영어, 원문 인쇄 p.10/PDF p.20 | `A tension stress and a bending stress are input to TIFFANY (` 다음에 `and`만 있고 곧바로 `along with the temperature ...`로 이어진다. | 지면은 `to TIFFANY (σ_T and σ_B) along with the temperature at which these values are applicable`다. | 문장 속 `(σ_T and σ_B)`를 괄호까지 복원한다. 한국어 본문 16쪽의 σ_T·σ_B는 유지한다. | 높음 |
| F03·영어 본문 Δp의 p 누락 | HTML 16·17의 접힌 영어, 원문 인쇄 p.11/PDF p.21 | `the deviation from the normal operating pressure is specified as` 다음이 `Δ ) and the effects ...`로 되어 있다. | 지면은 `specified as Δp ) and the effects on stress are computed by TIFFANY.`이며 기호표 p.viii도 Δp를 싣는다. | Δ를 Δp로 복원한다. 펼친 한국어 본문 16쪽의 Δp는 맞다. | 높음 |
| F04·표기 관찰에 남은 포괄적 오류 분류 | HTML 22·23·28의 ‘원문 자체 이상’, 특히 28 항목 5·8과 전체 제목 | K 이중 사용, μ/ν/NuIn, c_sp/C, a/h와 a/t 등을 ‘이상’, ‘표기 불일치와 오타’ 아래에 둔다. 항목 3만 ‘오류 여부는 원문에 없음’이라고 제한했다. | p.viii는 두 K를 실제로 서로 다른 정의로 싣고, p.21은 ν·C, p.19는 NuIn, pp.14~15와 p.20은 각각 a/h·a/t를 쓴다. 그러나 B048은 이 차이들이 오타라는 판정을 싣지 않는다. | 지면에서 확인되는 차이는 ‘원문 표기 관찰’로 기술하고, 저자가 오류라고 확정하지 않은 항목을 일괄 오류로 단정하지 않는다. 식·기호를 고치자는 제안이 아니다. | 높음(표기·분류의 존재); 실제 오류 여부는 확인 불가 |
| F05·B048 밖 검증 이력의 본문 잔존 | HTML 9·10·12·13·14·17의 신뢰성 주석, 28의 목록 출처 주석 | `Claude·Codex 독립 전사 일치`, `400dpi`, `300dpi`, `round57/claude_review.md`, ‘Claude 전사와 Codex 전사의 합집합’ 등이 들어 있다. 머리말은 ‘이 페이지의 내용은 모두 위 보고서 한 편에서 가져왔다’고 한다. | 대응하는 B048 pp.7~11 및 나머지 원문에는 이 AI 이름·dpi·저장소 검증 이력이 없다. 원문 출처를 붙일 수 없는 제작 과정 기록이다. | ‘B048 원문 내용만’ 기준을 적용한다면 제작 이력은 검토 보고서로 옮기고 HTML의 해당 주석에서는 제거한다. p.28의 실제 표기 관찰과 원문 쪽수는 보존한다. | 높음(원문 밖 서술); 과거 작업의 실제 수행 여부는 확인 불가 |

새로 확정한 한국어 의미 반전이나 수정 과정에서 추가된 과학적 해석은 발견하지 못했다. F01~F03은 접힌 ‘원문 영어’ 영역의 전사 결손이며 해당 펼친 본문의 번역·수식이 틀렸다는 뜻은 아니다. 독립된 수식 행의 의도적 생략 자체는 이 문제 건수에 포함하지 않았다.

## (C) 확인 불가

| 항목 | 확인한 사실 | 확인 불가 범위·이유 |
|---|---|---|
| 원문 식의 수학적 정답·저자의 의도 | Eqn.2 괄호, Eqn.4·5a의 T_o, Eqn.5a의 r_1, Eqn.3b/5b 분자 등 지면 표기는 보존돼 있다. | B048에 저자의 정오 설명이 없다. r_1→r_i, T_o→T_0 등 추정 교정은 하지 않는다. |
| 표기 차이가 실제 오류인지 | F04의 기호·이름·배열 표기는 PDF에 존재한다. | 차이가 있다는 관찰만으로 서로 다른 문맥의 기호가 모두 오류라고 판정할 수 없다. 특히 Table 3의 t가 어떤 뜻으로 의도됐는지 기호표의 Time만으로 확정하지 않는다. |
| 잔여 결손의 발생 시점 | 현재 HTML에는 F01~F03이 있다. 수정된 인용과 rowspan에는 같은 결손이 없다. | 수정 전 HTML 전체 사본 대신 2단계 보고서와 해시만 있어 이번 수정으로 생겼다고 단정할 수 없다. |
| AI/dpi 과거 작업 이력 | HTML에 그러한 이력 문구가 남아 있다. | 그 문구가 과거 실제 작업을 얼마나 정확히 설명하는지 B048로 입증할 수 없다. 이번 직접 검증 기록과 구별한다. |
| 브라우저 화면·인쇄·CDN 로딩 | HTML 소스의 표 셀 수·rowspan 및 수식 데이터와 원문 대응을 확인했다. | 이번 단계에서 실제 브라우저·인쇄 렌더링을 실행하지 않았다. 내용 검증 결과를 화면 품질 보증으로 확대하지 않는다. |
| 외부 보고서·코드의 실제 정확성 | B048이 열거한 시험·모듈·참고문헌의 서술과 목록을 대조했다. | 사용자 범위가 B048 한 편이므로 STP/MVR/실제 코드의 성능이나 보수성은 별도 검증하지 않았다. |

작업 시작 `git pull`은 `Already up to date.`였고 시작 시 스테이징된 파일은 없었다. 기존 다른 파일의 변경은 보존했다. Git 인계 대상은 이 파일 `round57/codex_final.md` 하나뿐이다. 커밋 SHA와 원격 반영 여부는 커밋·push 후 별도로 확인해 사용자에게 보고한다. 최종 결정 문서는 작성하지 않았다.
