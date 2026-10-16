# round46 — Claude 독립 감사 (blind, Codex 결과 미열람)

## 방법
`html_cards.txt` 카드와 PDF 추출 텍스트(`round43/txt`)를 쪽 단위로 대조. 서론~§3.6(PDF 16–59), §3.7 규칙 문장(PDF 60–78 일부), §4–§6(PDF 79–100), §8–§9, 부록 A(136–149), 부록 C(168–180) 서술을 직접 읽고 비교했다. 입력표(표 7~34)·참고문헌·부록 B 도상 수치·Table 35/36 수치는 이번 감사 대상이 아니다(이전 round 검증). 부록 A 150–155, 부록 C 181–187 서술은 이번 라운드에서 재대조하지 못했다.

## 총평
HTML 서술은 대부분 원문 사실과 맞지만, 원문 문장을 전보체로 줄여 문장 성분·한정어가 빠지거나 어색해진 곳이 많다. 뜻을 바꾸는 오류는 소수다.

## 뜻이 틀린 곳 (원문 확인)
|카드|HTML 문장|원문 PDF/인쇄|원문 영어|정확한 번역|분류|
|---|---|---|---|---|---|
|p10|"플랜트당 SG 노즐 DMW 2개(고온관 inlet, 크로스오버관 outlet)"|29/14|"there are two nozzle-to-safe end DMWs on each SG, one on the hot leg (inlet) and one on the crossover leg (outlet)"|각 SG에 노즐–safe end DMW가 2개(고온관 inlet 1, 크로스오버관 outlet 1)|오역(플랜트당 ≠ SG당)|
|p32|"(이 결과는 압력용기 안전·surge line 예이나 고온관 크기에 적용 가정)"|67/52|"This result was for pressurizer safety and surge line examples but is assumed to apply for hot leg size."|이 결과는 가압기(pressurizer) 안전밸브 관련 배관과 surge line 예에서 나온 것이나 고온관 크기에도 적용된다고 가정|오역(pressurizer ≠ 압력용기)|
|p15|"나머지는 Subversion·xLPR 웹포털에 보관"|41/26|"These are currently available on Subversion and will be made available from the xLPR web portal"|현재 Subversion에서 이용 가능하고 xLPR 웹포털에서도 제공될 예정|시제 오류(예정을 현재로)|
|p6|축대칭: "비드 전체를 한 번에 적층"|18–19/3–4|"forces each modeled weld pass to be deposited at once" (Table 4: "weld bead deposited at once")|각 모델 용접 패스를 (원주 전체에) 한 번에 적층하도록 강제|부정확(패스 단위)|

## 압축·어색·해석 표시 필요
|카드|HTML 문장|원문|권고|
|---|---|---|---|
|p21|"FSWOL, OWOL, 두 가지는 WOR 범주. MSIP, inlay."|60/45 "FSWOL and OWOL which are grouped in the WOR category, MSIP, and inlay"|"FSWOL과 OWOL은 WOR(weld overlay repair) 범주로 묶이고, 그 외 MSIP, inlay"로 정정|
|p55|"이상치를 통계적 관행으로 가중해 영향 감소"|81/66 "For these cases, which were rare, the WRS distributions were weighted ... using standard statistical practices"|"드물었던" 한정 누락 — 원문 인용 추가|
|p54|"극한응력 기반 변동 추정이 훨씬 안정적"|80/65 "much better behaved ... possibly since yield stress values ... might be affected by work hardening in the tensile specimens"|"훨씬 더 잘 거동(안정적)"이며 원문이 든 이유(시편 가공경화 가능성, 'possibly')가 빠짐|
|p10|"대표 치수는 Figure 5, Figure 7"|31/16 "A sketch with representative dimensions ... is shown in Figure 5"|Figure 7은 모델 형상 그림 — 대표 치수는 Figure 5|
|p43|"inlay는 ... 일반화가 틀리는 대표 사례입니다"|—|원문 문장이 아니라 Claude의 해설 — "해설(원문 아님)" 표시|
|식 F29–F55 카드|"왜 이 식을 쓰나/적용 방법" 반복 문단|60/45|원문은 "rules ... applied directly to the WRS 26-point datasets", "estimated based on literature solutions"만 말함. 문단 구성은 Claude의 풀이임을 표시|
|전 카드|전보체 요약 문장 다수|—|카드마다 원문 영어 전문을 접어서 병기하고 요약임을 표시(조치 방식)|

## 정확하다고 확인한 것(대표)
§2.1 가정 목록, shakedown 3단계, 설계검증 5항목과 Table 1(29→31 in), §3.3–3.5 결과 서술, VC Summer OI/IO, §4 Table 4, §5 가중 철학, §6.1 제약 6개와 기각 이유, Cholesky 설명, §6.2.2, §6.3–6.4, 부록 A 용접 순서·입열·재료 절차·풀림 보정, 부록 C C.1–C.4 서술.

## 미점검
부록 A 150–155, 부록 C 181–187 서술(식 카드 외), §3.7 그림별 규칙 문장 전부(이전 라운드 지면 대조), 이전에 별도 검증된 표.
