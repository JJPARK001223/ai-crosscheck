# -*- coding: utf-8 -*-
"""
경화 시멘트 페이스트(HCP) 3점굽힘 균열시편 - Abaqus 절반대칭 모델 (재시작판)

원본: Kwon, Markoff, DeFisher (2024), Materials 17, 569, §4 Hardened Cement
      Pastes with Cracks (PMC10856633). 값의 출처는 00_모델링_스펙_출처정리.md 참조.

K 산출은 논문의 수동 곡선맞춤 대신 Abaqus 내장 Contour Integral(symmetric half-crack,
kFactor 직접출력)을 사용 - 선배 Practice.cae와 같은 계열이라 결과 비교가 쉬움.

이 환경에는 Abaqus가 없어 실제 구동 검증은 못 했습니다. 첫 실행 에러는 그대로 알려주세요.
실행: abaqus cae noGUI=01_cement_paste_3PB_model.py
"""
from abaqus import *
from abaqusConstants import *
import regionToolset
import mesh
import os

# ---------------------------------------------------------------
# 파라미터 (출처: 00_모델링_스펙_출처정리.md, 2026-09-03 확정)
# ---------------------------------------------------------------
W_MM          = 100.0        # A: 폭 (논문 원문)
H_MM          = 100.0        # B: 채택 가정값 (2026-09-03 최종 확정) - W/H=1로 3D 자유표면효과 최소화
L_MM          = 4.0 * H_MM   # A: L/H=4 (논문 원문 비율) -> 400mm
A_OVER_H_LIST = [0.10, 0.30, 0.50]  # 0.10/0.30=논문 Fig.11, 0.50=선배 Practice.cae 추가분
E_MPA         = 20800.0      # A: 20.8 GPa (논문 원문) - Practice.cae의 208000은 10배 오류이므로 미채택
NU            = 0.20         # B: 가정값 - 문헌 미기재, 시멘트 페이스트 전형값
LOAD_N        = 1000.0       # B: 기준하중(가정) - 선형탄성이므로 K는 P에 비례
ELEM_SIZE_TIP = 0.3          # A: 논문 "element length around 0.3 mm"
ELEM_SIZE_FAR = min(5.0, H_MM / 4.0)  # B: 가정값 - 원거리 조대 메쉬, H에 비례해 자동 축소
STRIP_MM      = min(5.0, 0.05 * (L_MM / 2.0))  # B: 하중 적용 스트립 폭(가정, 단순화)
N_CONTOURS    = 6            # Contour Integral 적분경로 개수

OUT_DIR = os.path.dirname(os.path.abspath(__file__))


def build_and_run(a_over_h):
    H, L, W = H_MM, L_MM, W_MM
    Lh = L / 2.0
    a = a_over_h * H
    strip_x0 = Lh - STRIP_MM

    tag = 'aH%03d' % int(round(a_over_h * 100))
    model_name = 'HCP_' + tag
    mdb.Model(name=model_name, modelType=STANDARD_EXPLICIT)
    m = mdb.models[model_name]

    # --- 1. 단면 스케치(X:0~Lh, Y:0~H) 후 폭(W) 방향 압출 ---
    sk = m.ConstrainedSketch(name='profile', sheetSize=2.0 * max(L, H))
    sk.rectangle(point1=(0.0, 0.0), point2=(Lh, H))
    prt = m.Part(name='Half3PB', dimensionality=THREE_D, type=DEFORMABLE_BODY)
    prt.BaseSolidExtrude(sketch=sk, depth=W)
    del sk

    # --- 2. 파티션: (a) 균열깊이 a 높이에서 수평 분할, (b) 하중 스트립 시작점에서 수직 분할 ---
    dp_a = prt.DatumPlaneByPrincipalPlane(principalPlane=XZPLANE, offset=a)
    prt.PartitionCellByDatumPlane(datumPlane=prt.datums[dp_a.id], cells=prt.cells)

    dp_strip = prt.DatumPlaneByPrincipalPlane(principalPlane=YZPLANE, offset=strip_x0)
    prt.PartitionCellByDatumPlane(datumPlane=prt.datums[dp_strip.id], cells=prt.cells)

    # --- 3. 재료/단면 (E=20.8GPa 논문값, nu=0.2 가정값) ---
    m.Material(name='HCP').Elastic(table=((E_MPA, NU),))
    m.HomogeneousSolidSection(name='Sec-1', material='HCP', thickness=None)
    prt.SectionAssignment(region=(prt.cells,), sectionName='Sec-1')

    # --- 4. 메쉬: 균열끝단 근처 조밀(0.3mm), 사면체 자유메쉬(견고성 우선) ---
    # ponytail: hex+quarter-point 특이요소 대신 tet 자유메쉬 채택. 정확도 부족하면 hex로 교체.
    prt.setMeshControls(regions=prt.cells, elemShape=TET, technique=FREE)
    prt.setElementType(regions=(prt.cells,), elemTypes=(
        mesh.ElemType(elemCode=C3D10, elemLibrary=STANDARD),))
    tipEdges = prt.edges.getByBoundingBox(
        xMin=Lh - 1e-3, xMax=Lh + 1e-3, yMin=a - 1e-3, yMax=a + 1e-3,
        zMin=-1e-3, zMax=W + 1e-3)
    if len(tipEdges) > 0:
        prt.seedEdgeBySize(edges=tipEdges, size=ELEM_SIZE_TIP, constraint=FIXED)
    prt.seedPart(size=ELEM_SIZE_FAR, deviationFactor=0.1, minSizeFactor=0.1)
    prt.generateMesh()

    # --- 5. 조립 ---
    asm = m.rootAssembly
    inst = asm.Instance(name='Half3PB-1', part=prt, dependent=ON)

    # --- 6. 해석 스텝 ---
    m.StaticStep(name='Load', previous='Initial', nlgeom=OFF)

    # --- 7. 경계조건 ---
    # (a) 대칭면(X=Lh) 중 균열 위쪽(Y>=a)만 대칭BC(U1=0). 균열면(Y<a)은 구속 없음(=자유면)
    symFaces = inst.faces.getByBoundingBox(
        xMin=Lh - 1e-3, xMax=Lh + 1e-3, yMin=a - 1e-6, yMax=H + 1e-3,
        zMin=-1e-3, zMax=W + 1e-3)
    m.XsymmBC(name='Symmetry', createStepName='Initial',
              region=regionToolset.Region(faces=symFaces))

    # (b) 하단 지지(롤러): X=0 끝단, Y=0 바닥 모서리에서 U2=0
    supportEdges = inst.edges.getByBoundingBox(
        xMin=-1e-3, xMax=1e-3, yMin=-1e-3, yMax=1e-3, zMin=-1e-3, zMax=W + 1e-3)
    m.DisplacementBC(name='Support-Roller', createStepName='Initial',
                      region=regionToolset.Region(edges=supportEdges), u2=0.0)

    # (c) 강체이동 방지: 지지모서리 폭중앙 한 점에서 U3=0
    centerVerts = inst.vertices.getByBoundingBox(
        xMin=-1e-3, xMax=1e-3, yMin=-1e-3, yMax=1e-3,
        zMin=W / 2.0 - 1e-3, zMax=W / 2.0 + 1e-3)
    if len(centerVerts) > 0:
        m.DisplacementBC(name='Support-AntiRigid', createStepName='Initial',
                          region=regionToolset.Region(vertices=centerVerts), u3=0.0)

    # --- 8. 하중: 대칭면쪽 상단 스트립 면에 압력(=절반하중/스트립면적) ---
    loadFaces = inst.faces.getByBoundingBox(
        xMin=strip_x0 - 1e-3, xMax=Lh + 1e-3, yMin=H - 1e-3, yMax=H + 1e-3,
        zMin=-1e-3, zMax=W + 1e-3)
    pressure = (LOAD_N / 2.0) / (STRIP_MM * W)   # 절반모델이므로 총하중의 절반만 적용
    m.Pressure(name='Load-P', createStepName='Load',
               region=regionToolset.Region(side1Faces=loadFaces), magnitude=pressure)

    # --- 9. 균열 정의 (Contour Integral, 대칭 half-crack) ---
    # 균열끝단(crack front/tip) = 대칭면 위 Y=a 에서 폭(Z) 전체를 가로지르는 모서리
    crackEdges = inst.edges.getByBoundingBox(
        xMin=Lh - 1e-3, xMax=Lh + 1e-3, yMin=a - 1e-3, yMax=a + 1e-3,
        zMin=-1e-3, zMax=W + 1e-3)
    crackRegion = regionToolset.Region(edges=crackEdges)
    crack_name = 'Crack-' + tag
    asm.engineeringFeatures.ContourIntegral(
        name=crack_name,
        symmetric=True,
        crackFront=crackRegion,
        crackTip=crackRegion,
        extensionDirectionMethod=CRACK_NORMAL,
        crackNormal=(1.0, 0.0, 0.0),   # 균열면(X=Lh)의 법선 = 개구(모드I) 방향
        crackFrontIsClosed=False)

    m.HistoryOutputRequest(name='H-K', createStepName='Load',
                            contourIntegral=crack_name, contours=N_CONTOURS,
                            kFactor=ON, frequency=LAST_INCREMENT)

    # --- 10. Job 생성/제출 ---
    job_name = 'Job_' + tag
    mdb.Job(name=job_name, model=model_name, description=(
        'HCP 3PB half-model, a/H=%.2f (Kwon et al. 2024 Sec.4.2 reproduction)'
        % a_over_h))
    mdb.jobs[job_name].submit(consistencyChecking=OFF)
    mdb.jobs[job_name].waitForCompletion()

    odb_path = os.path.join(OUT_DIR, job_name + '.odb')
    print('완료: a/H=%.2f -> %s (상태: %s)' % (
        a_over_h, odb_path, mdb.jobs[job_name].status))
    return odb_path


if __name__ == '__main__':
    results = []
    for ah in A_OVER_H_LIST:
        try:
            results.append((ah, build_and_run(ah)))
        except Exception as e:
            print('!!! a/H=%.2f 실패: %s' % (ah, str(e)))
    print('=== 생성된 ODB 목록 ===')
    for ah, path in results:
        print('a/H=%.2f : %s' % (ah, path))
