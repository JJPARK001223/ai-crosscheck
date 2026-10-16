# round43 교차검증 — Claude의 xLPR 모듈 평가 순서

작성: Codex, 2026-10-16. 검증 대상은 `round43/claude.md`, 대조 자료는 `round43/txt/`의 원문 추출문이다. 자기 정정을 위해 `round43/codex.md`도 읽었다. `DECISION.md`와 `claude_review.md`는 읽지 않았다. 아래 PDF 쪽은 추출문의 `=====PAGE n=====` 기준이며 인쇄 쪽과 구분한다. 소스 코드 실행이나 실제 DLL 호출 추적은 수행하지 않았다. 따라서 보고서에 명시된 요구사항과 특정 배포본의 실제 실행을 동일시하지 않는다.

## 1. 원문과 맞는 점

| Claude 주장 | 판정 및 직접 대조 근거 |
|---|---|
| C165 §3.2.2에 전체 평가 순서가 직접 제시됨 | **맞음.** `(ML19337C165)Source and treatment of uncertainties.txt`, PDF 42–44쪽(인쇄 21–23쪽). 42쪽은 한 입력 집합의 realization을 정의하고 초기화 및 CI를 열거하며, 43–44쪽은 시간 루프를 열거한다. 그림 자체를 읽지 않고도 본문 목록으로 순서를 확인할 수 있다. |
| TIFFANY/LEAPOR 전처리 → 텍스트 표 → 시뮬레이션 시작 시 가져오기 | **맞음.** `(ML19337C165)Source and treatment of uncertainties.txt`, PDF 41쪽. Excel 입력 스프레드시트에서 전처리 모드로 두 모듈을 실행하고 개별 텍스트 표를 Framework가 시뮬레이션 시작에 가져온다. `(ML16341B048)Cyclic stress intensity factors.txt`, PDF 26–27쪽도 입력 전처리기의 TIFFANY DLL 호출을 명시한다. |
| 초기화 → CI → 시간 루프 | **맞음.** `(ML19337C165)Source and treatment of uncertainties.txt`, PDF 42–43쪽. 초기화 하위 항목의 순서와 초기 결함 계산 → CI DLL → 기구 식별 → 달력시간 변환 → 도래시간 정렬이 일치한다. `(ML16341B052)Crack initiation.txt`, PDF 14쪽도 CI가 시간 루프 전에 발생 시각·위치 배열을 만든다고 명시한다. 다만 Claude의 DLL 명칭은 아래에서 정정한다. |
| 시스템 갱신 → 축방향 진행 → 원주방향 진행 → 다음 스텝/종료 | **맞음.** `(ML19337C165)Source and treatment of uncertainties.txt`, PDF 43–44쪽. 온도·압력·산소, 물리/화학 완화, 활성 과도 및 사이클 수, 균열 특성과 독립적인 응력 계산도 일치한다. |
| K → 성장 → 유형 갱신 → CT → 안정성 → COD → 누설률 → ISI | **주요 순서는 맞음.** `(ML19337C165)Source and treatment of uncertainties.txt`, PDF 43–44쪽. 원주방향에는 성장/유형 갱신 뒤 합체 및 추가 유형 갱신이 들어가며 축방향 목록에는 합체가 없다. 다만 원문에는 K-solution DLL 호출 뒤 별도 `perform K calculations`도 있다. |
| 환경 조건/배열 변경/최종 배열 평가로 역할 구분, COD는 배열을 바꾸지 않음 | **맞음.** `(ML19337C165)Source and treatment of uncertainties.txt`, PDF 45쪽. 원문은 COD도 배열 관련 활동 목록에 넣지만, 바로 뒤에서 COD를 제외한 모듈들이 균열 크기·위치·유형을 바꾼다고 명시한다. stability/leak rate/ISI는 균열이나 환경 민감도를 변경하지 않는다. |
| CT의 A/t ≥ 0.95 및 길이비 > 1.05 기준 | **수치와 부등호가 맞음.** `(ML16341B044)Crack transition.txt`, PDF 46쪽 RTC-16*. 활성 표면균열 및 천이균열에 관한 두 조건이 그대로 있다. θ1/θ2와 a1/a2는 각각 원주/축방향 길이비로 구분해 쓰는 것이 명확하다(RTC-17*). |
| COD의 관통/천이균열 조건 | **내용은 맞음.** `(ML16341B053)Crack opening displacement.txt`, PDF 15쪽 RCCOD-8*은 활성 이상화 또는 천이 관통균열이 있을 때 CrCOD를 호출한다고 한다. PDF 16쪽 RAxCOD-14*는 AxCOD에 대해 a/t ≥ 0.95에서 천이가 시작될 때 및 이후 모든 스텝을 명시한다. 두 요구사항의 방향별 적용 범위는 구분해야 한다. |
| ISI는 검사 시점의 활성 균열마다 계산하고 후처리에서 위험에 적용 | **맞음.** `(ML16341B045)Inservice inspection.txt`, PDF 52쪽 §3.1 및 PDF 59쪽 §3.2.2가 호출 조건을, PDF 46쪽 §2.3.2가 시뮬레이션 중 POD/POR 계산과 시뮬레이션 후 적용을 구분한다. |
| 런타임에 LEAPOR 표를 ID COA 기준으로 보간 | **맞지만 불완전함.** `(ML16341B047)Leak rate.txt`, PDF 13쪽(인쇄 2쪽). 전처리 표의 런타임 보간이 명시되어 있다. ID/OD 보정 등은 아래에 보완한다. |

## 2. 틀렸거나 과장되었거나 인용을 고쳐야 하는 점

1. **Stability(TWC) 호출 조건에서 성장에 따른 재호출을 누락했다.** Claude가 적은 최초 TWC/천이균열 출현, 하중 변경, 물성 변경의 세 조건 자체는 맞다. 그러나 `(ML16341B050)Crack stability.txt`, PDF 40쪽 TWCF-10*에는 네 번째로, TWC가 존재한 후 균열이 성장하여 최초 TWC_fail 호출에서 계산한 θcrit의 **95% 이상**에 도달할 때의 재호출도 있다. 세 조건만으로 전체 호출 조건을 제시하면 불완전하다. 이 요구사항은 원주 TWC_fail에 관한 것이며 모든 방향의 TWC에 일반화할 수 없다. 같은 파일 PDF 45쪽 RACS-1*/10*의 축방향 기준은 별도로 아래에 적는다.

2. **“초기화 DLL 호출(PWSCC/피로)”은 모듈 명칭 오류다.** `(ML19337C165)Source and treatment of uncertainties.txt`, PDF 42쪽은 `call crack initiation DLLs (as needed)`이다. “균열 개시 DLL 호출(필요 시)”로 고쳐야 한다. 초기화(run initialization)는 그 앞의 별도 항목이다. `(ML16341B052)Crack initiation.txt`, PDF 14쪽에서 이 DLL의 출력은 발생 시각과 위치이며, “초기 시각”보다 “개시 시각”이라고 쓰는 것이 정확하다.

3. **“스텝마다” 아래의 순서를 모든 DLL의 무조건 호출로 읽으면 과장이다.** `(ML19337C165)Source and treatment of uncertainties.txt`, PDF 42쪽은 Framework가 필요에 따라 모듈을 호출한다고 하며 PDF 43쪽은 시스템 갱신, 축방향 진행, 원주방향 진행에 각각 `as needed`를 붙인다. Claude의 도식에는 이 제한을 복원해야 한다. 같은 도식에서 생략한 `perform K calculations`도 K-solution DLL 호출 뒤의 별도 Framework 계산 항목으로 표시하면 원문에 충실하다(PDF 43쪽). 실제 스킵·재호출의 전체 구현은 **확인 불가**다.

4. **“루프 순서 = 학습 순서”는 원문 사실이 아니라 학습 제안이다.** `(ML19337C165)Source and treatment of uncertainties.txt`, PDF 41–43쪽에서 TIFFANY는 전처리, CI는 메인 시간 루프 이전, K 이후 성장 등은 루프 내부다. 학습 계획 전체가 루프 순서와 같다는 등식은 성립하지 않는다. 원주방향의 주요 루프 순서를 따르는 학습 제안이라고 범위를 한정하면 된다. 원문이 유일한 권장 학습 순서를 제시했는지는 **확인 불가**다.

5. **Leak rate “B047 p.2”는 PDF 쪽으로 읽으면 틀리다.** 해당 내용은 `(ML16341B047)Leak rate.txt`, **PDF 13쪽, 인쇄 2쪽**이다. Claude는 다른 곳에서 PDF 쪽을 사용하므로 표기 체계를 통일해야 한다. COD의 RCCOD-8*/RAxCOD-14*에는 각각 PDF 15/16쪽, ISI §3.1에는 PDF 52쪽을 덧붙여야 한다. 모듈 역할의 직접 목록은 C165 PDF 45쪽이며 PDF 44쪽은 정보 전달·샘플링 설명이다.

6. **COD 조건 두 문장을 방향 공통의 하나의 규칙처럼 묶으면 적용 범위가 흐려진다.** `(ML16341B053)Crack opening displacement.txt`, PDF 15–16쪽. RCCOD-8*은 원주 CrCOD, RAxCOD-14*는 축 AxCOD 요구사항이다. Claude가 인용한 내용 자체는 맞으나 방향별로 분리해서 표기해야 한다.

## 3. Claude가 놓친 점

- **축방향 안정성의 별도 호출 기준과 SC→TWC 변경.** `(ML16341B050)Crack stability.txt`, PDF 45쪽 RACS-1*은 활성 축방향 TWC 발생, TWC의 c/ccrit > 0.9, 활성 축방향 SC의 존재를 다룬다. RACS-10*은 최초 호출 이후 재호출을 c/ccrit **≥ 0.9**로 적는다. 두 요구사항의 엄격/비엄격 부등호 차이를 임의로 통일하면 안 된다. 실제 경계값 처리는 **확인 불가**다. RACS-9*은 p/pcrit ≥ 1에서 축방향 SC를 TWC로 바꾸고 TWC 길이를 SC 길이로 설정하도록 한다. 따라서 일반적인 시간 루프 목록만으로 모든 유형 변경이 안정성 평가 전에 끝난다고 단정할 수 없다.

- **CT 출력은 단순히 다음 상자 하나로만 흐르지 않는다.** `(ML16341B044)Crack transition.txt`, PDF 45쪽은 ID/OD의 K·COD 보정계수가 성장 및 누설 계산에 사용된다고 명시한다. PDF 46쪽 RTC-21*/22*는 호출 후 현재 스텝 및 다음 스텝의 Framework 계산을 각각 요구한다. `(ML16341B051)Crack growth and coalescence.txt`, PDF 76쪽도 천이균열 형상에 맞추는 K scaling을 명시한다. 루프 목록에서 CT가 성장 뒤에 있다는 이유만으로 성장에 CT 보정이 없다고 결론낼 수 없다. 계수 저장·갱신 시점과 최초 천이 스텝의 재평가 여부는 제공 텍스트만으로 **확인 불가**다.

- **누설 계산은 ID 표 보간으로 끝나지 않는다.** `(ML16341B047)Leak rate.txt`, PDF 13쪽은 ID/OD 개구 면적 차이와 균열 morphology 불확실성에 따른 보정을 설명한다. `(ML19337C165)Source and treatment of uncertainties.txt`, PDF 81쪽은 Regime 1에서 ID와 OD 치수로 구한 누설률을 평균하는 보정, 저누설률의 불확실성 처리, 표 생성 전에 정한 압력·온도 범위를 벗어난 예측의 정확성을 보장하지 못한다는 제한을 명시한다. `(ML19337C165)Source and treatment of uncertainties.txt`, PDF 144쪽은 Framework가 중심선 COD와 가정한 균열 개구 형상으로 COA를 만든다고 설명한다.

- **CI 출력과 초기 균열 치수의 담당이 다르다.** `(ML16341B052)Crack initiation.txt`, PDF 14쪽에서 CI는 발생 시각·위치를 반환하고 초기 길이·깊이는 Framework가 사용자 분포에서 샘플링한다. Framework는 운전조건·잔류응력·두께·수화학 변화에 맞는 구간을 CI 호출 전에 구성한다. 따라서 루프 밖 CI 계산과 루프 안 새 균열 활성화는 서로 다른 작업이다.

- **성장률 계산과 시간 적분의 담당이 다르다.** `(ML16341B051)Crack growth and coalescence.txt`, PDF 70쪽. 활성 과도 성분마다 피로 성장률 함수를 호출하고 PWSCC/피로 성장률의 합을 Framework에 반환한다. 시간 및 균열선단 위치에 관한 적분·배열 관리는 Framework가 담당한다. “성장 DLL”이라는 상자 하나로 이 구분을 생략했다.

- **합체 DLL 내부에는 반복 절차가 있다.** `(ML16341B051)Crack growth and coalescence.txt`, PDF 104쪽. 활성 균열 쌍을 검사하여 합체 균열과 흡수 균열의 속성을 갱신하고, 조건을 만족하는 쌍이 없을 때까지 반복한다. 축방향 합체가 목록에 없는 이유도 원문으로 확인된다. `(ML19337C165)Source and treatment of uncertainties.txt`, PDF 131쪽은 합체 범위를 동일 평면의 원주균열로 제한하고 축/원주 상호작용을 가정하지 않는다고 명시한다. 이는 실제 균열의 일반 물리 법칙이 아니라 모델 가정이다.

- **메인 시간 루프 바깥의 확률 샘플링 구조.** `(ML19337C165)Source and treatment of uncertainties.txt`, PDF 46쪽은 바깥 epistemic/안쪽 aleatory 루프를 명시한다. PDF 44–45쪽은 입력의 realization당 샘플링과 공간 변동을 위한 예외, 필요한 여러 모듈 사이의 동일 입력값 공유를 설명한다. 모듈 호출 순서와 매 호출 재샘플링을 혼동하면 안 된다. 세부 빈도 예로 `(ML16341B045)Inservice inspection.txt`, PDF 59쪽은 ISI 매개변수의 용접형태·균열방향·완화상태 configuration별 샘플링을 요구한다.

- **ISI는 누설감지와 별개이며, 검사 시점에는 완화 시점도 포함된다.** `(ML19337C165)Source and treatment of uncertainties.txt`, PDF 174쪽은 온라인 누설감지를 Framework가 ISI와 독립적으로 구현한다고 한다. `(ML16341B045)Inservice inspection.txt`, PDF 46쪽은 완화 시점에 기존 검사 일정과 겹치지 않아도 검사를 배정하고 완화 후 configuration 매개변수를 적용한다고 명시한다. PDF 48쪽은 검사 미고려 위험에 부품이 아직 보수되지 않았을 확률을 곱하여 위험을 조정한다.

## 4. 내 codex.md의 자기 점검 및 정정

1. **요청에 제시된 C165 인용 문제는 두 위치를 구분해야 한다.** 내 §4.3의 “Axial cracks are neglected when applying coalescence rules”는 `(ML19337C165)Source and treatment of uncertainties.txt`, **PDF 136쪽(인쇄 115쪽)** 가정 표에 실제로 존재한다. 따라서 해당 쪽을 지정한 기존 인용을 오인용이라고 철회할 근거는 없다. 반면 같은 파일 **PDF 131쪽(인쇄 110쪽), §10.3**의 문장은 “Axial cracks are neglected with respect to coalescence considerations.”이다. 사용자가 지적한 문구도 원문과 맞는다. 두 문장을 서로 다른 위치의 문구로 병기하며, 131쪽 문장을 인용할 때 136쪽 문구로 대체해서는 안 된다.

2. **샘플링 일반론의 단정은 한정해야 한다.** 내 §4.1의 “모듈 호출마다 재샘플링하는 구조로 설명해서는 안 된다”는 공통 입력의 일관성에 관한 설명으로 한정한다. `(ML19337C165)Source and treatment of uncertainties.txt`, PDF 44쪽의 일반 설명과 함께 `(ML16341B045)Inservice inspection.txt`, PDF 59쪽의 configuration별 샘플링 등 각 입력의 규칙을 확인해야 한다. 내 문서에 세부 빈도는 입력 정의를 따른다는 단서를 이미 넣었지만, 예외 사례를 함께 적어야 더 정확하다.

3. **균열 유형 갱신은 안정성 전 단계에만 있는 것이 아니다.** 내 §4.3의 도식 자체는 `(ML19337C165)Source and treatment of uncertainties.txt`, PDF 43쪽을 충실히 옮겼다. 다만 `(ML16341B050)Crack stability.txt`, PDF 45쪽 RACS-9*에 따른 축방향 SC→TWC 변경도 별도 주석으로 추가해야 한다. 도식이 구현의 모든 유형 변경을 열거한 것으로 읽히면 불완전하다.

4. **출처 목록의 C165 §14.1 위치를 정밀하게 고친다.** 내 표의 “§14.1–14.2 PDF 174”는 관련 내용이 이어지는 쪽은 맞으나, §14.1 시작은 `(ML19337C165)Source and treatment of uncertainties.txt`, **PDF 173쪽**, §14.2 시작은 PDF 174쪽이다. “§14.1–14.2 PDF 173–174”로 정정한다.

5. **내 blind 보고서의 Git 실패 기록은 당시 세션의 기록이다.** 이는 원문에 대한 학술 판단이 아니다. 이번 검토 세션에서는 승인 요청을 사용한 `git pull`이 성공했다. 기존 blind 보고서 자체는 이번 수정 허용 대상이 아니므로 변경하지 않고, 자기 점검은 이 검토 파일에만 기록한다.

## 5. 출처 및 검증 한계

위 모든 근거는 NRC/EPRI xLPR 기술보고서이며 학술지 논문이 아니다. 사용한 보고서의 저자·연도·식별자는 다음과 같다. 각 판단의 파일명과 PDF 쪽은 위에 개별 표기했다.

- Marjorie Erickson, *Sources and Treatment of Uncertainties*, xLPR-TR-UNCERT v2.0, 2020, ML19337C165.
- Do Jun Shim, *Crack Transition*, xLPR-MSGR-CTM v1.0, 2016, ML16341B044.
- Kyle Schmitt, *Inservice Inspection*, xLPR-MSGR-ISI v1.0, 2016, ML16341B045.
- Elizabeth Kurth, *Leak Rate*, xLPR-MSGR-LRM v1.1, 2016, ML16341B047.
- David O. Harris, *Cyclic Stress Intensity Factors*, xLPR-MSGR-TIFF v1.0, 2016, ML16341B048.
- Rick Olson, *Crack Stability*, xLPR-MSGR-Stability v1.0, 2016, ML16341B050.
- Kyle Schmitt, *Crack Growth and Coalescence*, xLPR-MSGR-CGR v1.0, 2016, ML16341B051.
- Clifford Lange, *Crack Initiation*, xLPR-MSGR-CI v1.0, 2016, ML16341B052.
- Rick Olson, *Crack Opening Displacement*, xLPR-MSGR-COD v1.0, 2016, ML16341B053.

C165 Figure 3-1과 CT Figure 22의 그림 자체는 이번 텍스트 대조에서 확인하지 않았다. 실제 배포본의 호출 로그, CT 계수 캐시 및 모든 예외 분기의 구현은 확인 불가다. 이 보고서는 교차검증 결과이며 최종 종합 결정은 작성하지 않는다.
