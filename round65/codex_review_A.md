# round65 Codex 독립 검토 A — 카드 1~59

검토 대상: `round65/input/b046_card.html`의 페이지 n / 118 중 n=1~59. 근거: `round65/input/b046.pdf`. `PROBLEM.md`를 읽고 수행했으며 round65의 claude*.md 및 다른 검토 결과는 읽지 않았다.

방법: PDF p.15~43(인쇄 p.3~31)을 `pdftoppm -r 150 -png`로 150dpi, 1275×1650px 이미지로 렌더링해 모든 쪽을 직접 열어 확인하고, 동일 PDF에서 `pdftotext -layout`으로 추출한 텍스트와 대조했다. 식 TeX 재전사는 하지 않았다. 이 범위에 계수표 Table 2-3~2-7 카드는 없다.

아래는 직접 확인한 불일치·누락이다. 기호 정의 내용이 맞아도 표의 ‘출처’가 정의가 없는 쪽을 가리키면 쪽번호 문제로 기록했다. 식이 있는 쪽과 설명·정의가 있는 쪽을 구분했다. 원문의 식 2-49·2-53 마지막 b_2 중복은 카드 53·57이 원문 그대로라고 명시하므로 전사 오류로 세지 않았다. 새로운 식 해석이나 원문 오류의 임의 수정은 제안하지 않는다.

[카드 1 / §2.1.1 / 쪽번호 / 현재 문장: 원문 p.3 (PDF p.15) / 원문 근거(쪽, 인용): p.4 (PDF p.16): “Fifty-three cases”; “industry consensus as well as engineering judgment.” 형상 연구 및 적정성 근거는 p.4에 있고 그림은 p.5에 있다. / 제안: 본문 출처를 p.3~5 (PDF p.15~17)로 표시하고 근거 단락에는 p.4를 붙인다.]

[카드 2 / §2.1.2 / 쪽번호 / 현재 문장: 원문 p.6 (PDF p.18) / 원문 근거(쪽, 인용): p.7 (PDF p.19): “For through-wall cracks ... a single stress value was used”; “based on engineering judgement.” / 제안: 관통균열 단락 출처 p.7 (PDF p.19)을 추가한다.]

[카드 7 / 2-4 / 쪽번호 / 현재 문장: 기호표 R_i, t 출처 p.11 / 원문 근거(쪽, 인용): p.9 (PDF p.21), 식 2-1~2-3 아래: “inner radius of pipe, m”; “pipe wall thickness, m”. p.11 where에는 a, c, R_m만 있다. / 제안: 식 자체의 p.11은 유지하고 두 정의의 출처는 p.9 (PDF p.21)로 고친다.]

[카드 9 / 2-6 / 쪽번호 / 현재 문장: 기호표 t: pipe wall thickness, m / p.11 / 원문 근거(쪽, 인용): p.9 (PDF p.21): “t = pipe wall thickness, m”. p.11의 공통 where에는 t가 없다. / 제안: t 정의 출처를 p.9 (PDF p.21)로 고친다.]

[카드 10 / 2-7 / 쪽번호 / 현재 문장: 기호표 a: crack depth, m / p.12 / 원문 근거(쪽, 인용): p.9 (PDF p.21): “a = crack depth, m”. p.12에서는 a가 식에 쓰이지만 crack depth 정의 행은 없다. / 제안: a 정의 출처를 p.9 (PDF p.21)로 고친다.]

[카드 11 / 2-8 / 쪽번호 / 현재 문장: 기호표 a: crack depth, m / p.12 / 원문 근거(쪽, 인용): p.9 (PDF p.21): “a = crack depth, m”. p.12에서는 a가 식에 쓰이지만 crack depth 정의 행은 없다. / 제안: a 정의 출처를 p.9 (PDF p.21)로 고친다.]

[카드 12 / 2-9 / 쪽번호 / 현재 문장: 기호표 t: pipe wall thickness, m / p.12 / 원문 근거(쪽, 인용): p.9 (PDF p.21): “t = pipe wall thickness, m”. p.12의 식 2-9 아래 where는 B_j와 σ(x)_B만 정의한다. / 제안: t 정의 출처를 p.9 (PDF p.21)로 고친다.]

[카드 17 / 2-14 / 쪽번호 / 현재 문장: 유한요소해석에서는 균열이 없는 상태의 응력값을 이산 절점에서만 알고 있다. ... / 원문 p.14 (PDF p.26) / 원문 근거(쪽, 인용): p.13 (PDF p.25) 마지막 단락: “Generally, stress values at discrete nodal points are known”; “in the absence of a crack”. / 제안: 식과 d_ji 정의의 p.14는 유지하되 목적 설명 출처 p.13 (PDF p.25)을 추가한다.]

[카드 18 / §2.3.3 / 조건 / 현재 문장: Ref. [16]은 ... 두 방법이 같다는 것을 예제 계산으로 보였다. / 원문 근거(쪽, 인용): p.14 (PDF p.26): “relatively smooth and is not representative of the typical weld residual stress at DM welds”; 정확한 계산에는 “provided that a proper stress fitting approach is used [20]”라는 조건이 이어진다. / 제안: 예제 응력이 비교적 매끄럽고 전형적인 DM 용접부 잔류응력을 대표하지 않는다는 한계를 추가한다. 고비선형 응력에 대한 설명을 덧붙일 때도 적절한 응력 피팅 조건을 함께 적는다.]

[카드 18 / §2.3.3 / 조건 / 현재 문장: 원주방향 균열 [18] a/c = 0.2, R_i/t = 3, 축방향 WRS 프로파일 4개 ... 로 비교했다. / 원문 근거(쪽, 인용): p.16 (PDF p.28): “the variation of stress between discrete locations was approximated in a piece-wise cubic format”. / 제안: 이 원주방향 비교에서 UWFM은 구간별 3차 응력 보간을 사용했다고 명시한다. 앞의 축방향 비교 및 최종 채택한 선형 보간과 구분할 수 있게 해당 단락에 넣는다.]

[카드 18 / §2.3.3 / 쪽번호 / 현재 문장: 원문 p.14 (PDF p.26) / 원문 근거(쪽, 인용): p.15~16에 축방향 비교, p.18~19에 평균 차이와 표, p.19 (PDF p.31)에 “it was decided to use ... piece-wise linear interpolation of stress.” / 제안: 카드 전체 근거를 p.14~19 (PDF p.26~31)로 표시하고 채택 결정은 p.19로 특정한다.]

[카드 26 / 2-22 / 쪽번호 / 현재 문장: 기호표 k_i, b_i, x_i, a, n의 출처를 모두 p.21로 표시 / 원문 근거(쪽, 인용): p.20 (PDF p.32): “constant of piece-wise linear representation”; “coefficient of piece-wise linear representation”; “number of intervals”; “positions of discrete data points”. a의 “crack depth, m” 정의는 p.9 (PDF p.21)에 있다. / 제안: K_IMj/K_INj 관계식과 그 정의의 p.21는 유지하고, k_i·b_i·x_i·n 정의는 p.20 (PDF p.32), a 정의는 p.9 (PDF p.21)로 구분한다. 정의 내용 자체는 일치한다.]

[카드 27 / 2-23 / 쪽번호 / 현재 문장: 기호표 k_i, b_i, x_i, a, n의 출처를 모두 p.21로 표시 / 원문 근거(쪽, 인용): p.20 (PDF p.32): “constant of piece-wise linear representation”; “coefficient of piece-wise linear representation”; “number of intervals”; “positions of discrete data points”. a의 “crack depth, m” 정의는 p.9 (PDF p.21)에 있다. / 제안: K_IMj/K_INj 관계식과 그 정의의 p.21는 유지하고, k_i·b_i·x_i·n 정의는 p.20 (PDF p.32), a 정의는 p.9 (PDF p.21)로 구분한다. 정의 내용 자체는 일치한다.]

[카드 28 / 2-24 / 쪽번호 / 현재 문장: 기호표 k_i, b_i, x_i, a, n의 출처를 모두 p.21로 표시 / 원문 근거(쪽, 인용): p.20 (PDF p.32): “constant of piece-wise linear representation”; “coefficient of piece-wise linear representation”; “number of intervals”; “positions of discrete data points”. a의 “crack depth, m” 정의는 p.9 (PDF p.21)에 있다. / 제안: K_IMj/K_INj 관계식과 그 정의의 p.21는 유지하고, k_i·b_i·x_i·n 정의는 p.20 (PDF p.32), a 정의는 p.9 (PDF p.21)로 구분한다. 정의 내용 자체는 일치한다.]

[카드 29 / 2-25 / 쪽번호 / 현재 문장: 기호표 k_i, b_i, x_i, a, n의 출처를 모두 p.21로 표시 / 원문 근거(쪽, 인용): p.20 (PDF p.32): “constant of piece-wise linear representation”; “coefficient of piece-wise linear representation”; “number of intervals”; “positions of discrete data points”. a의 “crack depth, m” 정의는 p.9 (PDF p.21)에 있다. / 제안: K_IMj/K_INj 관계식과 그 정의의 p.21는 유지하고, k_i·b_i·x_i·n 정의는 p.20 (PDF p.32), a 정의는 p.9 (PDF p.21)로 구분한다. 정의 내용 자체는 일치한다.]

[카드 34 / 2-30 / 쪽번호 / 현재 문장: 기호표 k_i, b_i, x_i, a, n의 출처를 모두 p.22로 표시 / 원문 근거(쪽, 인용): p.20 (PDF p.32): “constant of piece-wise linear representation”; “coefficient of piece-wise linear representation”; “number of intervals”; “positions of discrete data points”. a의 “crack depth, m” 정의는 p.9 (PDF p.21)에 있다. / 제안: K_IMj/K_INj 관계식과 그 정의의 p.22는 유지하고, k_i·b_i·x_i·n 정의는 p.20 (PDF p.32), a 정의는 p.9 (PDF p.21)로 구분한다. 정의 내용 자체는 일치한다.]

[카드 35 / 2-31 / 쪽번호 / 현재 문장: 기호표 k_i, b_i, x_i, a, n의 출처를 모두 p.22로 표시 / 원문 근거(쪽, 인용): p.20 (PDF p.32): “constant of piece-wise linear representation”; “coefficient of piece-wise linear representation”; “number of intervals”; “positions of discrete data points”. a의 “crack depth, m” 정의는 p.9 (PDF p.21)에 있다. / 제안: K_IMj/K_INj 관계식과 그 정의의 p.22는 유지하고, k_i·b_i·x_i·n 정의는 p.20 (PDF p.32), a 정의는 p.9 (PDF p.21)로 구분한다. 정의 내용 자체는 일치한다.]

[카드 36 / 2-32 / 쪽번호 / 현재 문장: 기호표 k_i, b_i, x_i, a, n의 출처를 모두 p.22로 표시 / 원문 근거(쪽, 인용): p.20 (PDF p.32): “constant of piece-wise linear representation”; “coefficient of piece-wise linear representation”; “number of intervals”; “positions of discrete data points”. a의 “crack depth, m” 정의는 p.9 (PDF p.21)에 있다. / 제안: K_IMj/K_INj 관계식과 그 정의의 p.22는 유지하고, k_i·b_i·x_i·n 정의는 p.20 (PDF p.32), a 정의는 p.9 (PDF p.21)로 구분한다. 정의 내용 자체는 일치한다.]

[카드 37 / 2-33 / 쪽번호 / 현재 문장: 기호표 k_i, b_i, x_i, a, n의 출처를 모두 p.22로 표시 / 원문 근거(쪽, 인용): p.20 (PDF p.32): “constant of piece-wise linear representation”; “coefficient of piece-wise linear representation”; “number of intervals”; “positions of discrete data points”. a의 “crack depth, m” 정의는 p.9 (PDF p.21)에 있다. / 제안: K_IMj/K_INj 관계식과 그 정의의 p.22는 유지하고, k_i·b_i·x_i·n 정의는 p.20 (PDF p.32), a 정의는 p.9 (PDF p.21)로 구분한다. 정의 내용 자체는 일치한다.]

[카드 38 / 2-34 / 쪽번호 / 현재 문장: 기호표 Q: flaw shape parameter ... (식 2-8) / p.22 / 원문 근거(쪽, 인용): p.12 (PDF p.24), 식 2-8 아래: “Q = flaw shape parameter, = 1 + 1.464(a/c)^1.65”. p.22에는 Q 정의 행이 없다. / 제안: G_0, G_1의 p.22는 유지하고 Q 정의 출처는 p.12 (PDF p.24)로 고친다.]

[카드 40 / 2-36 / 쪽번호 / 현재 문장: 기호표 G_0, G_1: standardized influence coefficients / p.23; Q 정의 / p.23 / 원문 근거(쪽, 인용): p.22 (PDF p.34): “two standardized influence coefficients, G_0 and G_1”. Q의 “flaw shape parameter” 및 형상비 관계는 p.12 (PDF p.24), 식 2-8 아래에 있다. / 제안: 계수식의 p.23은 유지하되 표준화 영향계수 정의 출처는 p.22 (PDF p.34), Q 정의 출처는 p.12 (PDF p.24)로 고친다.]

[카드 41 / 2-37 / 쪽번호 / 현재 문장: 기호표 G_0, G_1: standardized influence coefficients / p.23; Q 정의 / p.23 / 원문 근거(쪽, 인용): p.22 (PDF p.34): “two standardized influence coefficients, G_0 and G_1”. Q의 “flaw shape parameter” 및 형상비 관계는 p.12 (PDF p.24), 식 2-8 아래에 있다. / 제안: 계수식의 p.23은 유지하되 표준화 영향계수 정의 출처는 p.22 (PDF p.34), Q 정의 출처는 p.12 (PDF p.24)로 고친다.]

[카드 42 / 2-38 / 쪽번호 / 현재 문장: 기호표 G_0, G_1: standardized influence coefficients / p.23; Q 정의 / p.23 / 원문 근거(쪽, 인용): p.22 (PDF p.34): “two standardized influence coefficients, G_0 and G_1”. Q의 “flaw shape parameter” 및 형상비 관계는 p.12 (PDF p.24), 식 2-8 아래에 있다. / 제안: 계수식의 p.23은 유지하되 표준화 영향계수 정의 출처는 p.22 (PDF p.34), Q 정의 출처는 p.12 (PDF p.24)로 고친다.]

[카드 43 / 2-39 / 쪽번호 / 현재 문장: 기호표 G_0, G_1: standardized influence coefficients / p.23; Q 정의 / p.23 / 원문 근거(쪽, 인용): p.22 (PDF p.34): “two standardized influence coefficients, G_0 and G_1”. Q의 “flaw shape parameter” 및 형상비 관계는 p.12 (PDF p.24), 식 2-8 아래에 있다. / 제안: 계수식의 p.23은 유지하되 표준화 영향계수 정의 출처는 p.22 (PDF p.34), Q 정의 출처는 p.12 (PDF p.24)로 고친다.]

[카드 44 / 2-40 / 쪽번호 / 현재 문장: 목적·조건·풀이 방법·주의 전체에 별도 출처 없이 원문 p.24 (PDF p.36); 기호표 정의 출처도 p.24 / 원문 근거(쪽, 인용): p.23 (PDF p.35), §2.4.1.5: “The tabular data in API 579-1/ASME FFS-1 [6] were used”; “mainly based on engineering judgment”; “The interpolation is performed based on t/R_i [22].” a, c, t 정의는 p.9 (PDF p.21), 일반 영향계수 G_j 정의는 p.12 (PDF p.24)에 있다. / 제안: 식·평가 위치의 p.24 (PDF p.36)는 맞으므로 유지한다. 공통 목적·피팅 범위·보간·오차·외삽 주의에는 p.23 (PDF p.35)을 추가하고, 기호표 a·c·t는 p.9, G_0·G_1은 p.12 또는 구체적 설명 p.23을 출처로 표시한다. 공통 설명의 내용은 원문과 일치한다.]

[카드 45 / 2-41 / 쪽번호 / 현재 문장: 목적·조건·풀이 방법·주의 전체에 별도 출처 없이 원문 p.24 (PDF p.36); 기호표 정의 출처도 p.24 / 원문 근거(쪽, 인용): p.23 (PDF p.35), §2.4.1.5: “The tabular data in API 579-1/ASME FFS-1 [6] were used”; “mainly based on engineering judgment”; “The interpolation is performed based on t/R_i [22].” a, c, t 정의는 p.9 (PDF p.21), 일반 영향계수 G_j 정의는 p.12 (PDF p.24)에 있다. / 제안: 식·평가 위치의 p.24 (PDF p.36)는 맞으므로 유지한다. 공통 목적·피팅 범위·보간·오차·외삽 주의에는 p.23 (PDF p.35)을 추가하고, 기호표 a·c·t는 p.9, G_0·G_1은 p.12 또는 구체적 설명 p.23을 출처로 표시한다. 공통 설명의 내용은 원문과 일치한다.]

[카드 46 / 2-42 / 쪽번호 / 현재 문장: 목적·조건·풀이 방법·주의 전체에 별도 출처 없이 원문 p.25 (PDF p.37); 기호표 정의 출처도 p.25 / 원문 근거(쪽, 인용): p.23 (PDF p.35), §2.4.1.5: “The tabular data in API 579-1/ASME FFS-1 [6] were used”; “mainly based on engineering judgment”; “The interpolation is performed based on t/R_i [22].” a, c, t 정의는 p.9 (PDF p.21), 일반 영향계수 G_j 정의는 p.12 (PDF p.24)에 있다. / 제안: 식·평가 위치의 p.25 (PDF p.37)는 맞으므로 유지한다. 공통 목적·피팅 범위·보간·오차·외삽 주의에는 p.23 (PDF p.35)을 추가하고, 기호표 a·c·t는 p.9, G_0·G_1은 p.12 또는 구체적 설명 p.23을 출처로 표시한다. 공통 설명의 내용은 원문과 일치한다.]

[카드 47 / 2-43 / 쪽번호 / 현재 문장: 목적·조건·풀이 방법·주의 전체에 별도 출처 없이 원문 p.25 (PDF p.37); 기호표 정의 출처도 p.25 / 원문 근거(쪽, 인용): p.23 (PDF p.35), §2.4.1.5: “The tabular data in API 579-1/ASME FFS-1 [6] were used”; “mainly based on engineering judgment”; “The interpolation is performed based on t/R_i [22].” a, c, t 정의는 p.9 (PDF p.21), 일반 영향계수 G_j 정의는 p.12 (PDF p.24)에 있다. / 제안: 식·평가 위치의 p.25 (PDF p.37)는 맞으므로 유지한다. 공통 목적·피팅 범위·보간·오차·외삽 주의에는 p.23 (PDF p.35)을 추가하고, 기호표 a·c·t는 p.9, G_0·G_1은 p.12 또는 구체적 설명 p.23을 출처로 표시한다. 공통 설명의 내용은 원문과 일치한다.]

[카드 48 / 2-44 / 쪽번호 / 현재 문장: 목적·조건·풀이 방법·주의 전체에 별도 출처 없이 원문 p.26 (PDF p.38); 기호표 정의 출처도 p.26 / 원문 근거(쪽, 인용): p.23 (PDF p.35), §2.4.1.5: “The tabular data in API 579-1/ASME FFS-1 [6] were used”; “mainly based on engineering judgment”; “The interpolation is performed based on t/R_i [22].” a, c, t 정의는 p.9 (PDF p.21), 일반 영향계수 G_j 정의는 p.12 (PDF p.24)에 있다. / 제안: 식·평가 위치의 p.26 (PDF p.38)는 맞으므로 유지한다. 공통 목적·피팅 범위·보간·오차·외삽 주의에는 p.23 (PDF p.35)을 추가하고, 기호표 a·c·t는 p.9, G_0·G_1은 p.12 또는 구체적 설명 p.23을 출처로 표시한다. 공통 설명의 내용은 원문과 일치한다.]

[카드 49 / 2-45 / 쪽번호 / 현재 문장: 목적·조건·풀이 방법·주의 전체에 별도 출처 없이 원문 p.26 (PDF p.38); 기호표 정의 출처도 p.26 / 원문 근거(쪽, 인용): p.23 (PDF p.35), §2.4.1.5: “The tabular data in API 579-1/ASME FFS-1 [6] were used”; “mainly based on engineering judgment”; “The interpolation is performed based on t/R_i [22].” a, c, t 정의는 p.9 (PDF p.21), 일반 영향계수 G_j 정의는 p.12 (PDF p.24)에 있다. / 제안: 식·평가 위치의 p.26 (PDF p.38)는 맞으므로 유지한다. 공통 목적·피팅 범위·보간·오차·외삽 주의에는 p.23 (PDF p.35)을 추가하고, 기호표 a·c·t는 p.9, G_0·G_1은 p.12 또는 구체적 설명 p.23을 출처로 표시한다. 공통 설명의 내용은 원문과 일치한다.]

[카드 50 / 2-46 / 쪽번호 / 현재 문장: 목적·조건·풀이 방법·주의 전체에 별도 출처 없이 원문 p.27 (PDF p.39); 기호표 정의 출처도 p.27 / 원문 근거(쪽, 인용): p.23 (PDF p.35), §2.4.1.5: “The tabular data in API 579-1/ASME FFS-1 [6] were used”; “mainly based on engineering judgment”; “The interpolation is performed based on t/R_i [22].” a, c, t 정의는 p.9 (PDF p.21), 일반 영향계수 G_j 정의는 p.12 (PDF p.24)에 있다. / 제안: 식·평가 위치의 p.27 (PDF p.39)는 맞으므로 유지한다. 공통 목적·피팅 범위·보간·오차·외삽 주의에는 p.23 (PDF p.35)을 추가하고, 기호표 a·c·t는 p.9, G_0·G_1은 p.12 또는 구체적 설명 p.23을 출처로 표시한다. 공통 설명의 내용은 원문과 일치한다.]

[카드 51 / 2-47 / 쪽번호 / 현재 문장: 목적·조건·풀이 방법·주의 전체에 별도 출처 없이 원문 p.27 (PDF p.39); 기호표 정의 출처도 p.27 / 원문 근거(쪽, 인용): p.23 (PDF p.35), §2.4.1.5: “The tabular data in API 579-1/ASME FFS-1 [6] were used”; “mainly based on engineering judgment”; “The interpolation is performed based on t/R_i [22].” a, c, t 정의는 p.9 (PDF p.21), 일반 영향계수 G_j 정의는 p.12 (PDF p.24)에 있다. / 제안: 식·평가 위치의 p.27 (PDF p.39)는 맞으므로 유지한다. 공통 목적·피팅 범위·보간·오차·외삽 주의에는 p.23 (PDF p.35)을 추가하고, 기호표 a·c·t는 p.9, G_0·G_1은 p.12 또는 구체적 설명 p.23을 출처로 표시한다. 공통 설명의 내용은 원문과 일치한다.]

[카드 52 / 2-48 / 쪽번호 / 현재 문장: 목적·조건·풀이 방법·주의 전체에 별도 출처 없이 원문 p.28 (PDF p.40); 기호표 정의 출처도 p.28 / 원문 근거(쪽, 인용): p.23 (PDF p.35), §2.4.1.5: “The tabular data in API 579-1/ASME FFS-1 [6] were used”; “mainly based on engineering judgment”; “The interpolation is performed based on t/R_i [22].” a, c, t 정의는 p.9 (PDF p.21), 일반 영향계수 G_j 정의는 p.12 (PDF p.24)에 있다. / 제안: 식·평가 위치의 p.28 (PDF p.40)는 맞으므로 유지한다. 공통 목적·피팅 범위·보간·오차·외삽 주의에는 p.23 (PDF p.35)을 추가하고, 기호표 a·c·t는 p.9, G_0·G_1은 p.12 또는 구체적 설명 p.23을 출처로 표시한다. 공통 설명의 내용은 원문과 일치한다.]

[카드 53 / 2-49 / 쪽번호 / 현재 문장: 목적·조건·풀이 방법·주의 전체에 별도 출처 없이 원문 p.28 (PDF p.40); 기호표 정의 출처도 p.28 / 원문 근거(쪽, 인용): p.23 (PDF p.35), §2.4.1.5: “The tabular data in API 579-1/ASME FFS-1 [6] were used”; “mainly based on engineering judgment”; “The interpolation is performed based on t/R_i [22].” a, c, t 정의는 p.9 (PDF p.21), 일반 영향계수 G_j 정의는 p.12 (PDF p.24)에 있다. / 제안: 식·평가 위치의 p.28 (PDF p.40)는 맞으므로 유지한다. 공통 목적·피팅 범위·보간·오차·외삽 주의에는 p.23 (PDF p.35)을 추가하고, 기호표 a·c·t는 p.9, G_0·G_1은 p.12 또는 구체적 설명 p.23을 출처로 표시한다. 공통 설명의 내용은 원문과 일치한다.]

[카드 54 / 2-50 / 쪽번호 / 현재 문장: 목적·조건·풀이 방법·주의 전체에 별도 출처 없이 원문 p.29 (PDF p.41); 기호표 정의 출처도 p.29 / 원문 근거(쪽, 인용): p.23 (PDF p.35), §2.4.1.5: “The tabular data in API 579-1/ASME FFS-1 [6] were used”; “mainly based on engineering judgment”; “The interpolation is performed based on t/R_i [22].” a, c, t 정의는 p.9 (PDF p.21), 일반 영향계수 G_j 정의는 p.12 (PDF p.24)에 있다. / 제안: 식·평가 위치의 p.29 (PDF p.41)는 맞으므로 유지한다. 공통 목적·피팅 범위·보간·오차·외삽 주의에는 p.23 (PDF p.35)을 추가하고, 기호표 a·c·t는 p.9, G_0·G_1은 p.12 또는 구체적 설명 p.23을 출처로 표시한다. 공통 설명의 내용은 원문과 일치한다.]

[카드 55 / 2-51 / 쪽번호 / 현재 문장: 목적·조건·풀이 방법·주의 전체에 별도 출처 없이 원문 p.29 (PDF p.41); 기호표 정의 출처도 p.29 / 원문 근거(쪽, 인용): p.23 (PDF p.35), §2.4.1.5: “The tabular data in API 579-1/ASME FFS-1 [6] were used”; “mainly based on engineering judgment”; “The interpolation is performed based on t/R_i [22].” a, c, t 정의는 p.9 (PDF p.21), 일반 영향계수 G_j 정의는 p.12 (PDF p.24)에 있다. / 제안: 식·평가 위치의 p.29 (PDF p.41)는 맞으므로 유지한다. 공통 목적·피팅 범위·보간·오차·외삽 주의에는 p.23 (PDF p.35)을 추가하고, 기호표 a·c·t는 p.9, G_0·G_1은 p.12 또는 구체적 설명 p.23을 출처로 표시한다. 공통 설명의 내용은 원문과 일치한다.]

[카드 56 / 2-52 / 쪽번호 / 현재 문장: 목적·조건·풀이 방법·주의 전체에 별도 출처 없이 원문 p.30 (PDF p.42); 기호표 정의 출처도 p.30 / 원문 근거(쪽, 인용): p.23 (PDF p.35), §2.4.1.5: “The tabular data in API 579-1/ASME FFS-1 [6] were used”; “mainly based on engineering judgment”; “The interpolation is performed based on t/R_i [22].” a, c, t 정의는 p.9 (PDF p.21), 일반 영향계수 G_j 정의는 p.12 (PDF p.24)에 있다. / 제안: 식·평가 위치의 p.30 (PDF p.42)는 맞으므로 유지한다. 공통 목적·피팅 범위·보간·오차·외삽 주의에는 p.23 (PDF p.35)을 추가하고, 기호표 a·c·t는 p.9, G_0·G_1은 p.12 또는 구체적 설명 p.23을 출처로 표시한다. 공통 설명의 내용은 원문과 일치한다.]

[카드 57 / 2-53 / 쪽번호 / 현재 문장: 목적·조건·풀이 방법·주의 전체에 별도 출처 없이 원문 p.30 (PDF p.42); 기호표 정의 출처도 p.30 / 원문 근거(쪽, 인용): p.23 (PDF p.35), §2.4.1.5: “The tabular data in API 579-1/ASME FFS-1 [6] were used”; “mainly based on engineering judgment”; “The interpolation is performed based on t/R_i [22].” a, c, t 정의는 p.9 (PDF p.21), 일반 영향계수 G_j 정의는 p.12 (PDF p.24)에 있다. / 제안: 식·평가 위치의 p.30 (PDF p.42)는 맞으므로 유지한다. 공통 목적·피팅 범위·보간·오차·외삽 주의에는 p.23 (PDF p.35)을 추가하고, 기호표 a·c·t는 p.9, G_0·G_1은 p.12 또는 구체적 설명 p.23을 출처로 표시한다. 공통 설명의 내용은 원문과 일치한다.]

[카드 58 / 2-54 / 쪽번호 / 현재 문장: 목적·조건·풀이 방법·주의 전체에 별도 출처 없이 원문 p.31 (PDF p.43); 기호표 정의 출처도 p.31 / 원문 근거(쪽, 인용): p.23 (PDF p.35), §2.4.1.5: “The tabular data in API 579-1/ASME FFS-1 [6] were used”; “mainly based on engineering judgment”; “The interpolation is performed based on t/R_i [22].” a, c, t 정의는 p.9 (PDF p.21), 일반 영향계수 G_j 정의는 p.12 (PDF p.24)에 있다. / 제안: 식·평가 위치의 p.31 (PDF p.43)는 맞으므로 유지한다. 공통 목적·피팅 범위·보간·오차·외삽 주의에는 p.23 (PDF p.35)을 추가하고, 기호표 a·c·t는 p.9, G_0·G_1은 p.12 또는 구체적 설명 p.23을 출처로 표시한다. 공통 설명의 내용은 원문과 일치한다.]

[카드 59 / 2-55 / 쪽번호 / 현재 문장: 목적·조건·풀이 방법·주의 전체에 별도 출처 없이 원문 p.31 (PDF p.43); 기호표 정의 출처도 p.31 / 원문 근거(쪽, 인용): p.23 (PDF p.35), §2.4.1.5: “The tabular data in API 579-1/ASME FFS-1 [6] were used”; “mainly based on engineering judgment”; “The interpolation is performed based on t/R_i [22].” a, c, t 정의는 p.9 (PDF p.21), 일반 영향계수 G_j 정의는 p.12 (PDF p.24)에 있다. / 제안: 식·평가 위치의 p.31 (PDF p.43)는 맞으므로 유지한다. 공통 목적·피팅 범위·보간·오차·외삽 주의에는 p.23 (PDF p.35)을 추가하고, 기호표 a·c·t는 p.9, G_0·G_1은 p.12 또는 구체적 설명 p.23을 출처로 표시한다. 공통 설명의 내용은 원문과 일치한다.]

이상 없음

3, 4, 5, 6, 8, 13, 14, 15, 16, 19, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 39

집계 기준: 대괄호 항목 1개를 문제 1건으로 계산했다. 문제 있는 카드는 38장이고 카드 18은 3건이다. ‘이상 없음’은 이번 지정 범위와 항목에서 추가 불일치를 찾지 못했다는 뜻이다.

문제 40건, 이상 없음 21장
