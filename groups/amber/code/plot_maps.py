#!/usr/bin/env python3
"""Final embedding maps: t-SNE (full 384-d) and UMAP, topic-labeled + CAV gradient."""
import os, csv, json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, Normalize
from matplotlib.cm import ScalarMappable

BASE = os.path.dirname(os.path.abspath(__file__))
W = os.path.join(BASE, "work")
SURFACE = "#fcfcfb"; INK = "#0b0b0b"; INK2 = "#52514e"; MUTED = "#898781"
S2 = "#eb6834"
SEQ = ["#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95", "#0d366b"]

idx = list(csv.DictReader(open(os.path.join(W, "embedding_index.csv"))))
scores = {(int(r["year"]), int(r["id"])): float(r["score"])
          for r in csv.DictReader(open(os.path.join(W, "embedding_scores.csv")))}
proj = np.array([scores[(int(r["year"]), int(r["id"]))] for r in idx])
TAU = 0.2022
en = proj > TAU
clus = np.load(os.path.join(W, "clusters.npy"))
NAMES = {0: "Law & Civil Rights", 1: "Trade & Energy", 2: "Cold War & Diplomacy",
         3: "War & Terrorism", 4: "Jobs & Inflation", 5: "Legislative Agenda",
         6: "Education & Schools", 7: "American Ideals", 8: "Hero Stories & Guests",
         9: "Infrastructure & Conservation", 10: "Healthcare & Social Security",
         11: "Calls to Action", 12: "Ceremony & Salutations", 13: "Budget & Taxes"}

maps = [("t-SNE", np.load(os.path.join(W, "tsne_full.npy"))),
        ("UMAP", np.load(os.path.join(W, "umap_full.npy")))]

def nudge(labels, min_dx, min_dy):
    """Push apart label positions that would overlap (data units)."""
    pos = {k: [x, y] for k, (x, y) in labels.items()}
    for _ in range(60):
        moved = False
        ks = list(pos)
        for i in range(len(ks)):
            for j in range(i + 1, len(ks)):
                a, b = pos[ks[i]], pos[ks[j]]
                if abs(a[0] - b[0]) < min_dx and abs(a[1] - b[1]) < min_dy:
                    s = 1 if a[1] >= b[1] else -1
                    a[1] += s * min_dy * 0.35; b[1] -= s * min_dy * 0.35
                    moved = True
        if not moved:
            break
    return pos

plt.rcParams.update({"font.family": "sans-serif",
                     "font.sans-serif": ["Helvetica Neue", "Arial", "DejaVu Sans"],
                     "text.color": INK, "axes.titlecolor": INK2})

fig, axes = plt.subplots(2, 2, figsize=(15.5, 15.6))
fig.patch.set_facecolor(SURFACE)
fig.subplots_adjust(left=0.03, right=0.985, top=0.90, bottom=0.075, hspace=0.12, wspace=0.06)
cmap = LinearSegmentedColormap.from_list("seqblue", SEQ)
norm = Normalize(vmin=np.percentile(proj, 1), vmax=np.percentile(proj, 99.5))

for row, (mname, XY) in enumerate(maps):
    axA, axB = axes[row]
    xlim = np.percentile(XY[:, 0], [0.2, 99.8]); ylim = np.percentile(XY[:, 1], [0.2, 99.8])
    padx = 0.06 * (xlim[1] - xlim[0]); pady = 0.06 * (ylim[1] - ylim[0])
    for ax in (axA, axB):
        ax.set_facecolor(SURFACE); ax.set_xticks([]); ax.set_yticks([])
        for s in ax.spines.values(): s.set_visible(False)
        ax.set_xlim(xlim[0] - padx, xlim[1] + padx); ax.set_ylim(ylim[0] - pady, ylim[1] + pady)
        ax.set_aspect("equal")

    axA.scatter(XY[~en, 0], XY[~en, 1], s=2.4, c=MUTED, alpha=0.16, lw=0, rasterized=True)
    axA.scatter(XY[en, 0], XY[en, 1], s=7, c=S2, alpha=0.85, lw=0)
    cents = {k: (np.median(XY[clus == k, 0]), np.median(XY[clus == k, 1])) for k in NAMES}
    span_x = xlim[1] - xlim[0]
    placed = nudge(cents, min_dx=0.30 * span_x, min_dy=0.055 * (ylim[1] - ylim[0]))
    for k, (cx, cy) in placed.items():
        w = "bold" if k == 1 else "normal"
        col = "#b34a1d" if k == 1 else INK2
        axA.text(cx, cy, NAMES[k], fontsize=9.5, fontweight=w, color=col,
                 ha="center", va="center", zorder=5,
                 bbox=dict(facecolor=SURFACE, edgecolor="#e1e0d9", lw=0.6,
                           alpha=0.9, boxstyle="round,pad=0.28"))
    axA.set_title(f"{mname} — topic regions; energy sentences in orange",
                  fontsize=11.5, loc="left", pad=10)

    o = np.argsort(proj)
    axB.scatter(XY[o, 0], XY[o, 1], s=3.2, c=proj[o], cmap=cmap, norm=norm,
                alpha=0.55, lw=0, rasterized=True)
    axB.set_title(f"{mname} — colored by projection on the energy axis",
                  fontsize=11.5, loc="left", pad=10)

cax = fig.add_axes([0.55, 0.052, 0.4, 0.012])
cb = fig.colorbar(ScalarMappable(norm=norm, cmap=cmap), cax=cax, orientation="horizontal")
cb.outline.set_visible(False)
cb.ax.tick_params(color=MUTED, labelcolor=MUTED, labelsize=9)
cb.set_label("projection on the energy axis (CAV) — above τ = 0.20 counts as energy",
             color=INK2, fontsize=10)

fig.text(0.03, 0.965, "The energy axis in embedding space — 20,813 SOTU sentences, 1946–2020",
         fontsize=16, fontweight="bold")
fig.text(0.03, 0.945, "MiniLM sentence embeddings, projected directly from 384-d (no PCA), cosine metric; "
                      "topic regions from KMeans (k = 14), named by an agent from samples;",
         fontsize=10, color=INK2)
fig.text(0.03, 0.930, "energy axis = logistic-regression concept activation vector trained on agent sentence labels "
                      "(held-out accuracy 0.92)", fontsize=10, color=INK2)
fig.text(0.03, 0.028, "Group amber · SODAS retreat exercise", fontsize=8.5, color=MUTED)
fig.savefig(os.path.join(W, "energy_maps.png"), dpi=170, facecolor=SURFACE)
print("wrote work/energy_maps.png")
