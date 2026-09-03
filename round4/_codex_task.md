# Codex 작업 지시 (Round 4, blind)

[CROSSCHECK_WORKER] `round4/PROBLEM.md`, `round4/FE재현계획.html`,
`round4/01_current.py`, `round4/02_current.py` 를 읽고 독립 분석한다.

## 하지 말 것
- `round4/claude.md` 를 열지 말 것 (blind).

## 할 일
`round4/PROBLEM.md` 의 검증 항목 1~6 을 각각 독립 판정한다:
**정확 / 부분적 정정 필요 / 틀림 / 확인 불가** + 근거.

특히:
- **항목 1**: `01_current.py` 의 `engineeringFeatures.ContourIntegral(...)` 호출
  (`symmetric=True`, `crackNormal=(1.0,0.0,0.0)`, `extensionDirectionMethod=CRACK_NORMAL`,
  `crackFront`/`crackTip` 동일 edge) 이 이 형상(균열면 X=L/2, 성장 +Y, 전선 Z축)에
  대해 맞는가. **Abaqus 2020/2021 Scripting Reference** 로 `crackNormal` 의 의미
  (균열면 법선 vs 확장방향), 인자 형식(단일 벡터 vs 두 점), `symmetric=True` 의 K
  정규화(절반 여부)를 확인. 문서 접근 불가 시 "확인 불가" 명시.
- **항목 3**: 강체이동 구속(대칭면 부분 U1=0 + X=0&Y=0 모서리 U2=0 + 1점 U3=0)이
  충분한가. Z=W/2 대칭(1/4 모델)이 더 나은가.
- **항목 4**: 무차원 형상계수 $K/(P\,H^{-3/2})$ 표기가 맞는가 (차원·지수 부호 점검).
  $H$=50·100 을 같은 축에서 비교할 올바른 무차원 SIF 형태 제시.
- **항목 5**: 논문 재현이면 6케이스 K 추출을 2D(4절점)로 할지 3D로 할지.
  현행 `01_current.py` 는 3D only 인데 논문 본체 방법(2D 곡선맞춤)과 맞는가.

## 결과물
`round4/codex.md` 에 한국어로:
- 항목별 판정표 + 근거(조회한 문서·범위 명시)
- 계획서·스크립트에서 구체적으로 고칠 것 (파일·줄 단위)
- FE 재현에 빠진 필수 절차/식

완료 후: `rm -f .git/index.lock; git add round4/codex.md;
git commit -m "round4: Codex blind 분석 (FE 재현 계획)"; git push origin main`.
근거 없는 주장 금지. 모르면 "확인 불가".
