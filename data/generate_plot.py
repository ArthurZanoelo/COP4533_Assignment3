import sys
import os
import time
import matplotlib
import matplotlib.pyplot as plt

# So that it can find hvlcs properly
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from hvlcs import hvlcs, parse_input

matplotlib.use("Agg")
DATA_DIR = os.path.dirname(__file__)

labels, times = [], []
for idx in range(1, 11):
    with open(os.path.join(DATA_DIR, f"test_{idx:02d}.in")) as f:
        values, A, B = parse_input(f.read())
    start = time.perf_counter()
    for _ in range(5):
        hvlcs(A, B, values)
    times.append((time.perf_counter() - start) / 5 * 1000)
    labels.append(f"{len(A)}x{len(B)}")

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(labels, times, marker="o", color="#2563eb", linewidth=2, markersize=7)
ax.fill_between(range(len(labels)), times, alpha=0.1, color="#2563eb")
ax.set_xticks(range(len(labels)))
ax.set_xticklabels(labels, rotation=30, ha="right", fontsize=9)
ax.set_xlabel("Input Size  |A| x |B|", fontsize=11)
ax.set_ylabel("Runtime (ms)", fontsize=11)
ax.set_title("HVLCS Runtime Across 10 Test Files", fontsize=13, fontweight="bold")
ax.grid(axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()
plt.savefig(os.path.join(DATA_DIR, "..", "runtime_plot.png"), dpi=150)