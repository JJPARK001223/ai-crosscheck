# -*- coding: utf-8 -*-
"""
LEFM(선형탄성파괴역학) 초보자용 시각화.
근거: [선행연구 1] Kwon, "Revisiting Failure of Brittle Materials", JPVT 143(6) 064503 (2021)
      [선행연구 3] Kwon et al., "Unified Failure Criterion...", Materials 17, 569 (2024)

사용 식(전부 위 2개 파일 본문에서 인용):
  - [선행연구 1] Eq.(4): sigma_x = K / sqrt(2*pi*r)          (균열선단 응력장, Irwin 1957)
  - [선행연구 1] Eq.(5): |d sigma_x / dy| = K / (2*sqrt(2*pi)*y**1.5)
  - [선행연구 1] Eq.(7): K_Ic = sqrt(2*pi*E*w_f)
  - [선행연구 3] Eq.(4): Y = K**2 / E  (= 임계 에너지방출률)

주: 라벨은 폰트 문제 회피를 위해 영어로 둠. 실행: python lefm_viz.py
"""
import sys, os

# --- 전역규칙 16: 라이브러리 / 경로 / 인코딩 확인 ---
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
try:
    import numpy as np
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
except ImportError as e:
    sys.exit(f"[중단] 필요한 라이브러리 없음: {e}  ->  pip install numpy matplotlib")

OUTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figs")
os.makedirs(OUTDIR, exist_ok=True)

# --- 예시 수치 (개념 설명용 임의값) ---
K   = 1.0e6          # 응력확대계수 [Pa*sqrt(m)]  (예시)
E   = 3.0e9          # 탄성계수 [Pa]  (예: PMMA 급)
sig_f = 7.0e7        # 파손강도 sigma_f [Pa]  (예시)

# =========================================================
# Fig A : 균열선단 응력 특이성  sigma = K / sqrt(2*pi*r)
# =========================================================
r = np.linspace(1e-6, 5e-3, 800)          # 균열선단으로부터 거리 [m]
sig = K / np.sqrt(2 * np.pi * r)

fig, ax = plt.subplots(figsize=(6, 4.2))
ax.plot(r * 1e3, sig / 1e6, lw=2, label=r"$\sigma = K/\sqrt{2\pi r}$  (Ref.1 Eq.4)")
ax.axhline(sig_f / 1e6, color="crimson", ls="--", lw=1.5,
           label=r"failure strength $\sigma_f$")
ax.set_xlabel("distance from crack tip  r  [mm]")
ax.set_ylabel("stress  [MPa]")
ax.set_ylim(0, 5 * sig_f / 1e6)
ax.set_title("Fig A. Crack-tip stress singularity  (r -> 0  =>  sigma -> infinity)")
ax.legend(fontsize=8)
ax.text(2.0, 4.3 * sig_f / 1e6,
        "strength criterion sigma>=sigma_f is ALWAYS met near tip\n=> cannot predict failure load  => need K",
        fontsize=7.5, color="dimgray")
fig.tight_layout(); fig.savefig(os.path.join(OUTDIR, "figA_singularity.png"), dpi=150)

# =========================================================
# Fig B : 같은 곡선 log-log  (기울기 -1/2)
# =========================================================
fig, ax = plt.subplots(figsize=(6, 4.2))
ax.loglog(r * 1e3, sig / 1e6, lw=2)
ax.set_xlabel("r  [mm]  (log)")
ax.set_ylabel("stress  [MPa]  (log)")
ax.set_title("Fig B. Same field on log-log : slope = -1/2  (the '1/sqrt(r)' singularity)")
ax.grid(True, which="both", ls=":", alpha=0.5)
fig.tight_layout(); fig.savefig(os.path.join(OUTDIR, "figB_loglog.png"), dpi=150)

# =========================================================
# Fig C : 응력구배  |d sigma_x / dy| = K / (2*sqrt(2*pi)*y**1.5)
# =========================================================
y = np.linspace(5e-5, 5e-3, 800)
grad = K / (2 * np.sqrt(2 * np.pi) * y ** 1.5)

fig, ax = plt.subplots(figsize=(6, 4.2))
ax.plot(y * 1e3, grad / 1e9, lw=2, color="teal")
ax.set_xlabel("y  [mm]  (along crack-growth direction)")
ax.set_ylabel(r"$|d\sigma_x/dy|$  [GPa/m]")
ax.set_title("Fig C. Stress gradient near crack tip  (Ref.1 Eq.5)")
fig.tight_layout(); fig.savefig(os.path.join(OUTDIR, "figC_gradient.png"), dpi=150)

# =========================================================
# Fig D : 개념 모식도 (중심균열 무한판) + K vs K_Ic 판정
# =========================================================
fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))

# (좌) 중심균열 판 스케치  -- [선행연구1] Fig.2 대응
axL = axes[0]
axL.add_patch(plt.Rectangle((0, 0), 4, 6, fill=False, lw=1.5))
axL.plot([1.2, 2.8], [3, 3], "k-", lw=3)            # 균열 2a
axL.annotate("", xy=(1.2, 3), xytext=(2.8, 3),
             arrowprops=dict(arrowstyle="<->", color="k"))
axL.text(2.0, 3.25, "2a", ha="center", fontsize=10)
for x in np.linspace(0.4, 3.6, 6):                  # 인장 하중 화살표
    axL.annotate("", xy=(x, 6.9), xytext=(x, 6.1),
                 arrowprops=dict(arrowstyle="->", color="steelblue"))
    axL.annotate("", xy=(x, -0.9), xytext=(x, -0.1),
                 arrowprops=dict(arrowstyle="->", color="steelblue"))
axL.text(2, 7.4, r"remote tension $\sigma$", ha="center", color="steelblue")
axL.set_xlim(-1, 5); axL.set_ylim(-1.5, 8); axL.axis("off")
axL.set_title("Fig D-1. Center crack in a plate under tension\n"
              r"$K$ grows with applied $\sigma$ and crack size $a$", fontsize=9)

# (우) K vs K_Ic 판정 막대
axR = axes[1]
w_f = sig_f ** 3 / (2 * E) * 1e-4          # 예시 임계값 (개념용)
K_Ic = np.sqrt(2 * np.pi * E * w_f)        # [선행연구1] Eq.7
Ks = np.array([0.4, 0.7, 1.0]) * K_Ic
labels = ["low load", "mid load", "at failure"]
colors = ["#8ecae6", "#8ecae6", "#e63946"]
axR.bar(labels, Ks / 1e6, color=colors)
axR.axhline(K_Ic / 1e6, color="k", ls="--", lw=1.5)
axR.text(2.05, K_Ic / 1e6, r"  $K_{Ic}$ (fracture toughness)", va="center", fontsize=9)
axR.set_ylabel(r"stress intensity factor $K$  [MPa$\sqrt{m}$]")
axR.set_title(r"Fig D-2. Failure when  $K = K_{Ic}$" "\n"
              r"(energy view: $K^2/E \geq$ critical, Ref.3 Eq.4)", fontsize=9)

fig.tight_layout(); fig.savefig(os.path.join(OUTDIR, "figD_concept.png"), dpi=150)

print("저장 완료:", OUTDIR)
for f in sorted(os.listdir(OUTDIR)):
    print("  -", f)

# --- ponytail: 최소 self-check (식이 안 깨졌는지) ---
assert np.isclose(K / np.sqrt(2 * np.pi * 1.0), K / np.sqrt(2 * np.pi))
assert K_Ic > 0 and np.isfinite(K_Ic)
assert sig[0] > sig_f > sig[-1], "선단 근처 응력은 sigma_f를 크게 넘고, 멀리서는 아래로 내려가야 함"
print("self-check OK")
