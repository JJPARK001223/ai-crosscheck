# Round 17 — Claude Blind 조사: 연구배경 구성안

## 1. 서사 구조 (5단계)

1. **문제의식**: 취성재료는 파괴 직전까지 선형탄성이라 파괴강도 $\sigma_f$ 자체는
   명확하지만, 실제 부재의 극한하중은 $\sigma_f$만으로 정해지지 않고 형상급변(노치·홀)과
   의도치 않은 균열에 좌우된다(round6 A2). 문제는 노치 유형마다 다른 이론을 써왔다는
   점 — 균열이면 LEFM, 홀이면 다른 파괴기준.
2. **응력집중·특이장의 두 고전**: Kirsch(1898)의 원형 홀 응력집중계수 3(§B-2), Irwin
   (1957)의 균열선단 특이장 $\sigma\propto r^{-1/2}$·에너지방출률 $\mathcal G=K^2/E'$
   (§B-1). 이 둘이 "응력집중"과 "응력특이성"이라는 양 극단을 세웠다.
3. **임계거리이론/유한파괴역학(TCD/FFM) 계열의 접근과 한계**: 응력식+에너지식을
   미지수 $\Delta$(균열진전/특성거리)로 연립해서 푸는 접근 — Sapora et al.(2018, 홀
   개시), Braun et al.(2020, 피로 응력구배), Camanho et al.(2012, 복합재 open-hole).
   한계: $\Delta$가 재료상수가 아니라 매번 풀어야 하는 미지수.
4. **기존 다이론 지형의 한계**: Daniel(2007) 복합재 파괴이론 리뷰 — 19개 이론이
   단방향 라미나에서도 200~300% 예측차. Podgórski(1985) 일반 파괴기준 — 응력상태의
   파괴 여부는 판정하나 파괴 위치·경로 법칙은 별도로 주지 않음.
5. **Kwon의 수렴**: 근접장을 응력구배조건에 직접 대입해 위치변수($r$ 또는 $s$)를
   대수적으로 소거함으로써 "응력조건+구배조건" 두 줄로 위치와 경로를 동시에 얻는
   구조로 수렴(선행연구1, 2021) → 노치형상·재료 확장(PVT144 2022, Polymers 2022,
   배경 인용만) → 선행연구3(2024)의 시멘트 페이스트(§4, 본 재현 대상)·PLA(§5)·
   다중스케일 복합재(§6)로 펼침.

## 2. 슬라이드/페이지 배분 제안 (5페이지)

| 페이지 | 내용 | 수식 | 핵심 인용 |
|---|---|---|---|
| 1 | 문제의식 — 강도 단독 조건의 한계 | $\sigma_l\ge\sigma_f$ (조건①만으로는 부족) | round6 A2 |
| 2 | 응력집중의 고전 — Kirsch | $\sigma_\theta(R,\pi/2)=3\sigma_o$ | Kirsch 1898 [선1 ref.2] |
| 3 | 응력특이성의 고전 — Irwin | $\sigma_y=K/\sqrt{2\pi r}$, $\mathcal G=K^2/E'$ | Irwin 1957, *ASME JAM* 24, 361–364, DOI 10.1115/1.4011547 |
| 4 | TCD/FFM 계열과 한계 | $\Delta$를 미지수로 연립(식 없이 개념만) | Sapora 2018 *FFEMS* 41(7); Braun 2020 *FFEMS* 43(7); Camanho 2012 *Composites A* 43 |
| 5 | 기존 지형의 한계 + Kwon으로 수렴 | (수식 없음, 서술) | Daniel 2007 *Strain* 43; Podgórski 1985 *JEM* 111(2); → 선행연구1(2021)·3(2024) |

## 3. 인용 정확성 체크 (round7 대조, 오탈자 확인)

- Kirsch, G., "Die Theorie der Elastizität und die Bedürfnisse der
  Festigkeitslehre," *Z. Ver. Dtsch. Ing.* 42, 797–807 (1898). DOI 없음.
- Irwin, G.R., "Analysis of Stresses and Strains Near the End of a Crack
  Traversing a Plate," *ASME J. Appl. Mech.* 24 (Trans. 79), 361–364 (1957).
  DOI: 10.1115/1.4011547.
- Sapora, A., Torabi, A.R., Etesam, S., Cornetti, P., "Finite Fracture
  Mechanics crack initiation from a circular hole," *Fatigue Fract. Eng.
  Mater. Struct.* 41(7), 1627–1636 (2018). DOI: 10.1111/ffe.12801.
- Braun, M., Müller, A.M., Milaković, A.-S., Fricke, W., Ehlers, S.,
  "Requirements for stress gradient-based fatigue assessment of notched
  structures according to theory of critical distance," *Fatigue Fract. Eng.
  Mater. Struct.* 43(7), 1541–1554 (2020). DOI: 10.1111/ffe.13232.
- Camanho, P.P., Erçin, G.H., Catalanotti, G., Mahdi, S., Linde, P., "A
  finite fracture mechanics model for the prediction of the open-hole
  strength of composite laminates," *Composites Part A* 43, 1219–1225
  (2012). DOI: 10.1016/j.compositesa.2012.03.004.
- Daniel, I.M., "Failure of composite materials," *Strain* 43, 4–12 (2007).
  DOI: 10.1111/j.1475-1305.2007.00302.x.
- Podgórski, J., "General Failure Criterion for Isotropic Media," *J. Eng.
  Mech.* 111(2), 188–201 (1985). DOI: 10.1061/(ASCE)0733-9399(1985)111:2(188).
- (배경 각주만) Kwon, Y.W., Diaz-Colon, C., DeFisher, S., "Failure Criteria
  for Brittle Notched Specimens," *J. Press. Vessel Technol.* 144, 051506
  (2022). DOI: 10.1115/1.4053484.
- (배경 각주만) Kwon, Y.W., "Failure Prediction of Notched Composites Using
  Multiscale Approach," *Polymers* 14, 2481 (2022). DOI: 10.3390/polym14122481.

전부 round7 B-1~B-10과 문자 그대로 일치. 추가 PDF 재대조 불필요(이미 Round7에서
Claude·Codex 양쪽이 원문과 대조 완료).

## 4. 주의할 표현 (round6/7 캐벗 반영)

- "$Y\equiv G_c$" 등식 금지 — "$Y$는 임계 에너지방출률과 같은 종류의 양($Y=G_c/2\pi$,
  평면응력)"으로.
- 시멘트 페이스트(§4)는 Kirsch 홀이 아니라 Irwin형 균열 문제 — 연구배경 페이지2
  (Kirsch)와 페이지3(Irwin)을 혼동 없이 분리.
- Podgórski 한 줄 요약은 "노치·균열에 무력"이 아니라 "파괴 위치·경로의 별도 법칙을
  주지 않는다"로 완화.
- Braun(2020)은 **피로** 연구이므로 "선행연구3의 정적 취성파괴를 직접 검증한 것은
  아니고 방법론적 참고"라는 단서를 반드시 유지.
- 선행연구2(PVT144 2022)·Polymers(2022)는 배경 설명에서 "Kwon의 후속/확장 연구"로만
  언급하고, 본 세미나의 재현 대상(선행연구1·3)과 혼동되지 않게 별도 박스나 각주로
  시각적으로 분리.

## 5. 열린 판단 (사용자가 볼 것)

- 5페이지 중 Kirsch/Irwin을 각각 1페이지씩 쓸지, 한 페이지에 "두 고전" 비교표로
  합칠지는 세미나 시간 제약에 따라 사용자가 결정할 사안.
- TCD/FFM 세 논문(Sapora·Braun·Camanho)을 한 페이지에 다 넣으면 밀도가 높다 —
  필요시 Camanho(복합재 전용)를 각주로 내리고 Sapora·Braun 중심으로 압축하는 안도
  가능.
