# Worst Paper 상세 분석

**No.1 — Iliev, S. (2021). "A Comparison of Ethanol, Methanol, and Butanol Blending with Gasoline and
Its Effect on Engine Performance and Emissions Using Engine Simulation." *Processes*, 9(8), 1322.**

선정 근거: 기존 내용평가 8개 범주형 항목 중 "하"가 3개로 15편 중 최다. (근거: `paper_list.csv`,
`ai-crosscheck/round85/input/evaluation_data.md` No.1 항목)

원문 직접 열람: 본 PDF(14쪽) 전체 확인함(2025-11-20).

---

## 0. 기존 평가 기록과 원문 대조 중 발견한 불일치 (중요 — 반드시 Codex 재검증 필요)

`evaluation_data.md`의 Introduction 구체성 등급 근거는 "메탄올·에탄올·부탄올의 일반적 배경과 연료 물성표(Table 1)만
제시, 선행연구의 정량적 결과 인용은 거의 없음"(하)이다. 그러나 원문 3~5쪽을 직접 대조한 결과, 다음과 같은
**수치가 포함된 선행연구 인용이 실제로 존재한다**:

- "Storey et al. [39]...a reduction of PM mass emissions (between E0 and E10 it is **29%** in the stoichiometric
  mixture, and a **42%** reduction was seen in the lean mixture)"(4쪽)
- "Jung et al. [41]...reported a **25%–45%** decrease in NOx for E85"(4쪽)
- "...blends (M10 and E10) reduced HC emissions by **13%** for methanol blends and **15%** for ethanol blends,
  reduced CO emissions by **10.6%** for methanol blends and **9.8%** for ethanol blends"(5쪽, 문헌 [28])

**"거의 없음"이라는 기존 근거 문구는 원문과 완전히 일치하지는 않는다.** 다만 이 3건을 제외한 나머지
7~8건의 선행연구 인용(Liu et al., Geng et al., Agarwal et al., Vertin et al., Schifter et al., Wallner et al.
등)은 실제로 전부 "decreased/increased/slightly lower" 식의 정성적 서술만 포함하고 있어, 15편 중 가장 수치가
풍부한 No.5·No.3(20개 이상 %수치)와 비교하면 여전히 "구체성이 낮은 편"이라는 **결론 방향 자체는 원문과 부합**한다.
등급을 "하"에서 "중"으로 올려야 하는지는 round85~88에서 이미 여러 차례 교차검증을 거친 확정본을 임의로
뒤집지 않기 위해, 이번 round(round89로 예정)에서 Codex에게 동일 원문을 제시해 독립적으로 재검증을 요청한다.
**이 문서에서는 기존 등급(하)을 그대로 인용하되, 위 불일치를 명시적으로 기록해 둔다.**

---

## 1. Title / Authors

**실제 내용**: 제목 21단어, 단독저자(Simeon Iliev, 불가리아 Ruse대). ORCID·CRediT 명시 없음(Acknowledgments·
Conflicts of Interest만 있음, 13쪽).

**긍정적 요소**: 간결성 2.0/2.0 만점(21단어는 10~15단어 기준보다 길지만 CSV 평가 기준상 "부합"으로 처리),
약어 없음(1.0/1.0), 구조 명료(서술형, 0.5/0.5).

**부정적 요소**: 단독저자라 공동1저자 표기·국제공동연구 항목이 원천적으로 해당 없음(각 0.25/0.5, 0.4/1.0만
부여). ORCID 0/1.0.

**종합 평가**: 총점 7.65/10으로 15편 평균(7.59)과 비슷해, Title/Authors 측면에서는 특별히 부족하지 않다.
**즉 이 논문이 "Worst"로 선정된 이유는 서지정보 작성 관행이 아니라 전적으로 본문 내용(Abstract·Introduction)의
정량적 근거 부족 때문임을 분명히 한다.**

## 2. Abstract

**실제 내용**(1쪽, 전문 인용): "Results obtained from different fuel blends showed that when alcohol blends
were used, brake power decreased and the brake specific fuel consumption increased compared to when using
gasoline, and CO and HC concentrations decreased as the fuel blends percentage increased."

**긍정적 요소**: 배경("air pollution...demand for alternatives")→목적("aimed to develop a gasoline engine
model to predict...")→방법(AVL Boost)→결과(위 인용문) 순서로 전개되어 구조 자체는 논리적이다.

**부정적 요소**: 결과 문장 전체에 **숫자가 단 하나도 없다.** "decreased", "increased"만으로 4개 변수(출력,
BSFC, CO, HC)의 변화를 서술해, 독자는 "얼마나" 변했는지 전혀 알 수 없다. 15편 중 Abstract에 수치가 전혀
없는 논문은 No.1과 No.11 둘뿐인데, No.11은 그나마 "프레임워크 제안"이라는 방법론 논문 특성상 결과수치가
없는 것이 상대적으로 자연스럽지만, No.1은 "성능·배출 비교"가 연구 목적인데도 비교 결과를 숫자 없이
서술한 것이어서 더 치명적이다(새로 확인한 비교 관찰).

**가점·감점 사유**: 기존 등급(구체성=하, 연관성=중)의 근거(정성적 서술, 구체 수치 없음)를 원문에서 그대로
확인했다. 숫자 점수 체계가 없으므로 기존 점수 반영 내역 없음.

**종합 평가**: 15편 중 Abstract의 정보 전달력이 가장 낮은 축에 속한다. "증가/감소"만으로는 이 연구의
실제 기여를 독자가 판단할 수 없다.

## 3. Introduction

**실제 내용**(1~5쪽): 1.1 Properties of Methanol, 1.2 Properties of Ethanol, 1.3 Properties of Butanol
3개 소단락으로 각 알코올의 물성(Table 1)과 일반적 특징을 순서대로 설명한 뒤, 말미에 "there is not enough
information about the comparison of methanol, ethanol, and n-butanol blending with gasoline and its effect
on engine performance and emissions in the same PFI SI engine and under the same conditions"(5쪽)라는
연구공백을 제시한다.

**긍정적 요소**: 연구공백 문장 자체는 명확하고 제목과 직결된다(이 점은 기존 평가에서도 "논문-Introduction
연관성=하"로 낮게 평가되었는데, 공백 문장만 보면 오히려 명확한 편이라 **이 부분도 round89 교차검증에서
재확인이 필요한 지점**이다).

**부정적 요소**: 공백 문장 앞 4쪽 분량이 "methanol/ethanol/butanol이 각각 무엇인지"에 대한 일반 화학·물성
설명(물성표, 비등점, 옥탄가 등)이 대부분을 차지하고, "3종 알코올을 동일 엔진·동일 조건에서 비교한 연구가
없다"는 핵심 공백과 직접 관련된 선행연구 비교는 상대적으로 적은 분량이다. 즉 전체 5쪽 중 공백 논증에
직접 기여하는 부분은 마지막 1개 문단 정도에 불과하다.

**종합 평가**: 연구공백 제시 자체는 존재하지만, 그에 이르는 과정이 일반 배경지식 설명에 치우쳐 있어 논증의
효율이 낮다. (0번 항목에서 밝힌 "정량적 인용 거의 없음" 근거 문구의 불일치는 round89에서 재확인 예정)

## 4. Methodology

**실제 내용**(5~7쪽): AVL BOOST 1D PFI 엔진모델(Fig.1, Table 2 라이브러리), 엔진 사양(Table 3, 보어·스트로크
86mm, 압축비 10.5), 2-zone Vibe 연소모델 지배방정식(1)~(4)을 제시. "The gasoline engine model was calibrated
and described by Iliev [49]"(5쪽)라고 명시해, **모델의 보정·검증 자체는 저자 자신의 선행연구[49]로 위임**된다.

**긍정적 요소**: 지배방정식과 엔진 사양이 구체적으로 제시되어 모델 구조 자체는 투명하다(기존 평가 "중"과
일치).

**부정적 요소**: 본 논문 내에는 시뮬레이션 결과를 검증할 실험 데이터나 보정 과정이 전혀 없다. 즉 이 논문의
핵심 결과(출력·BSFC·배출가스 전부)는 "검증된 적 없는 모델"에서 나온 수치일 가능성을 배제할 수 없고, 독자가
그 신뢰도를 판단할 근거가 본문에 없다.

**종합 평가**: 수식은 충실하지만 "이 모델이 왜 믿을 만한가"에 대한 본문 내 근거가 가장 약한 논문 중
하나다.

## 5. Results

**실제 내용**(7~12쪽): Figure 2~6(출력·BSFC·CO·HC·NOx)이 전부 막대그래프로 제시되고, 본문 설명은 "brake
power decreased with increasing ethanol", "BSFC increased with increasing alcohol content", "CO emissions
decreased...as the...percentage increased" 등 **정성적 서술로만 구성**된다. 결론(Conclusion, 12쪽)도 동일한
정성적 문장 5개의 반복이다.

**긍정적 요소**: 5개 배출·성능 지표(출력, BSFC, CO, HC, NOx)를 전 속도범위(1000~6500rpm)·전 블렌드비율
(5~85%)에 걸쳐 빠짐없이 그래프로 제시했다.

**부정적 요소**: 그래프에는 수치가 있지만 본문 어디에도 "몇 % 감소/증가"라는 구체적 비교 수치가 등장하지
않는다. 독자가 결론을 확인하려면 그래프를 직접 읽어 수치를 추정해야 한다.

**종합 평가**: 15편 중 Results 본문의 정량적 서술 밀도가 가장 낮은 축에 속하며, 이것이 Abstract의 약점과
그대로 이어진다.

## 6. 종합 — 이 논문이 Worst인 이유

Title/Authors는 평균 수준이고 Methodology의 수식·사양도 구체적이지만, **Abstract와 Results 본문 전체에
걸쳐 숫자로 뒷받침된 비교 수치가 거의 등장하지 않는다**는 점이 일관된 약점이다. 이는 "결과를 수치로 명확히
제시하라"는 과학논문작성법의 핵심 원칙(Day & Gastel, *How to Write and Publish a Scientific Paper*)과
가장 거리가 먼 사례이며, 15편 중 "하" 등급이 가장 많은 이유이기도 하다.
