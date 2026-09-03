# -*- coding: utf-8 -*-
"""
01_cement_paste_3PB_model.py 가 생성한 ODB에서 Contour Integral의 K1(모드I 응력확대계수)
history output을 읽어 CSV로 저장한다. 첫 1~2개 적분경로(contour)는 균열끝단에 너무 가까워
부정확할 수 있어 제외하고, 나머지 경로의 평균을 대표값으로 삼는다(표준적인 관례).

이 환경에는 Abaqus가 없어 실제 odb로 검증하지 못했습니다.
실행: abaqus python 02_read_K.py
"""
from odbAccess import openOdb
import os
import csv

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
A_OVER_H_LIST = [0.10, 0.30, 0.50]   # 01_cement_paste_3PB_model.py 와 동일하게 유지
SKIP_FIRST_N_CONTOURS = 1             # 균열끝단에 가장 가까운 경로 제외


def read_K1(a_over_h):
    tag = 'aH%03d' % int(round(a_over_h * 100))
    odb_path = os.path.join(OUT_DIR, 'Job_' + tag + '.odb')
    if not os.path.exists(odb_path):
        print('없음: %s (먼저 01_cement_paste_3PB_model.py 실행 필요)' % odb_path)
        return None

    odb = openOdb(path=odb_path, readOnly=True)
    step = odb.steps[odb.steps.keys()[-1]]

    k1_values = []
    for region_name in step.historyRegions.keys():
        region = step.historyRegions[region_name]
        if 'K1' in region.historyOutputs.keys():
            data = region.historyOutputs['K1'].data
            if len(data) > 0:
                k1_values.append(data[-1][1])   # 마지막 증분값

    odb.close()

    if len(k1_values) == 0:
        print('a/H=%.2f : K1 history output을 못 찾음 - HistoryOutputRequest 설정 확인 필요' % a_over_h)
        return None

    used = k1_values[SKIP_FIRST_N_CONTOURS:] if len(k1_values) > SKIP_FIRST_N_CONTOURS else k1_values
    k_avg = sum(used) / len(used)
    print('a/H=%.2f : 전체 %d개 경로 K1=%s -> 평균(앞 %d개 제외)=%.4f MPa*sqrt(mm)' % (
        a_over_h, len(k1_values), ['%.4f' % v for v in k1_values],
        SKIP_FIRST_N_CONTOURS, k_avg))
    return {'a_over_h': a_over_h, 'n_contours': len(k1_values),
            'k1_all': k1_values, 'k1_avg': k_avg}


if __name__ == '__main__':
    rows = []
    for ah in A_OVER_H_LIST:
        r = read_K1(ah)
        if r:
            rows.append(r)

    csv_path = os.path.join(OUT_DIR, 'K_results.csv')
    with open(csv_path, 'wb') as f:
        w = csv.writer(f)
        w.writerow(['a_over_H', 'n_contours', 'K1_avg_MPa_sqrt_mm', 'K1_all_contours'])
        for r in rows:
            w.writerow([r['a_over_h'], r['n_contours'], r['k1_avg'],
                        ';'.join('%.4f' % v for v in r['k1_all'])])
    print('저장: %s' % csv_path)
    print('※ 논문 Fig.10/11의 이론값·실험값(또는 선배 Practice.cae 결과)과 이 K값을 비교해 검증할 것.')
