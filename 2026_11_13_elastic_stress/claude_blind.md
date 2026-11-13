**판정: 미해결(unresolved).** Kamaya (2009)는 Eq.(5)의 σ를 정의하지 않습니다. 후보 4개(외면 M·Ro/I, 평균반경 M/(πRm²t), 내면 M·Ri/I, 기준응력 σy·M/ML)는 모두 논문 본문만으로는 확정되지 않았습니다.

**확인된 사실** (paper.txt와 원본 PDF 5쪽 확인)
- Eq.(5) `K(ae)=f1σ√(πae)`는 paper.txt 110행(PDF p.2, 쪽번호 1116)에 있습니다. 바로 아래 문장은 "f1 is a constant depending on the geometrical condition and ae is the crack depth modified…"이며, σ에 대한 설명은 없습니다.
- Table 1은 "Parameter f1 for stress intensity factors"라는 제목뿐입니다 (PDF p.5, 쪽번호 1119). 응력 정의는 캡션과 각주 어디에도 없습니다.
- Fig. 4의 범례는 `f1 = K_I/(σ√(πa))`입니다. 여기서도 σ는 정의되지 않습니다.
- §3.2(paper.txt 234행 부근)는 "elastic FEA was performed and the constant f1 was calculated from Eq. (5) from obtained SIF"라고만 씁니다. SIF를 어떤 하중으로 어떤 σ로 나눴는지는 적혀 있지 않습니다.
- 본문에서 σ가 붙은 것은 σy(항복강도), σo(정규화 응력), σf(유동응력)뿐입니다. 굽힘 공칭응력은 어디에도 정의되지 않습니다.
- 정의된 굽힘 관련 양은 ML(Eq.7)과 Rm, t, Ri, θ뿐입니다. ML은 `2σy·Rm²·t·(2 sinβ − (a/t) sinθ)` 형태이며 σ의 정의가 아닙니다.

**Chapter5 Eq.(9)로 충분한가: 충분하지 않습니다.**
- 본문 583–584행은 "almost identical to Eq. (6) when … K(a) is replaced with f1σ(πa)^0.5"라고만 말합니다. 이는 Eq.(5)를 다시 쓴 것일 뿐 σ를 새로 정의하지 않으므로 순환 서술입니다.
- Eq.(9)와 Eq.(11)에서 σ는 f1 안에 흡수된 채 M/ML만 남습니다. 그래서 σ를 정의하는 근거가 되지 못합니다.

**추측** (확정 아님)
- 굽힘 SIF 정규화에서 공칭 굽힘응력을 쓰는 것이 관례이므로 σ는 M에 비례하는 공칭 굽힘응력일 가능성이 있습니다.
- 그러나 외면/평균반경/내면 중 어느 것인지는 본문에서 가릴 수 없습니다.
- FE 결과나 목표값과의 일치로 역추정한 정의는 근거로 인정하지 않았고, 위 판단에도 쓰지 않았습니다.

**다음 검증 단계** (파라미터 조정이나 FEA 실행 없이)
1. 인용 문헌 (15) Kamaya & Machida, 일본기계학회논문집 Vol.75 (2009) pp.333–342를 확인합니다. 본문 187행이 "J-integral estimation scheme"의 근거로 이 논문을 인용하므로, 같은 체계의 응력 정의가 거기 있을 수 있습니다.
2. 비교 대상인 Ref. (6) EPRI NP-6301의 균일깊이 표면균열 SIF 식과 Ref. (16) Chapuliot, CEA-R-5900의 공칭응력 정의를 확인합니다. 두 문헌은 Fig. 4에서 직접 비교됩니다.
3. 가능하면 저자(kamaya@inss.co.jp)에게 σ 정의를 문의합니다.

이번에는 웹 공식 출처를 조회하지 않았고, 위 내용은 로컬 paper.txt와 PDF 5쪽만 근거로 합니다. PDF 나머지 쪽은 paper.txt 텍스트로만 대조했습니다.
