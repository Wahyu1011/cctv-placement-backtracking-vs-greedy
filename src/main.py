```python
from itertools import combinations
import time

# ==========================
# DATA TITIK RAWAN
# ==========================

risk_points = {
    "P1": 5,
    "P2": 4,
    "P3": 3,
    "P4": 5,
    "P5": 2,
    "P6": 4,
    "P7": 3,
    "P8": 5
}

# Posisi CCTV dan cakupannya
cctv_positions = {
    "C1": {"P1", "P2", "P3"},
    "C2": {"P2", "P4", "P5"},
    "C3": {"P4", "P6", "P7"},
    "C4": {"P1", "P5", "P8"},
    "C5": {"P3", "P6", "P8"}
}

MAX_CCTV = 2


# ==========================
# FUNGSI MENGHITUNG BOBOT
# ==========================

def calculate_score(covered_points):
    return sum(risk_points[p] for p in covered_points)


# ==========================
# BACKTRACKING
# ==========================

def backtracking():
    best_score = -1
    best_combination = None
    best_covered = set()

    cctv_list = list(cctv_positions.keys())

    for combo in combinations(cctv_list, MAX_CCTV):
        covered = set()

        for cctv in combo:
            covered.update(cctv_positions[cctv])

        score = calculate_score(covered)

        if score > best_score:
            best_score = score
            best_combination = combo
            best_covered = covered

    return best_combination, best_covered, best_score


# ==========================
# GREEDY
# ==========================

def greedy():
    selected = []
    covered = set()

    available = set(cctv_positions.keys())

    while len(selected) < MAX_CCTV:

        best_cctv = None
        best_gain = -1

        for cctv in available:

            new_points = cctv_positions[cctv] - covered
            gain = calculate_score(new_points)

            if gain > best_gain:
                best_gain = gain
                best_cctv = cctv

        selected.append(best_cctv)
        covered.update(cctv_positions[best_cctv])
        available.remove(best_cctv)

    score = calculate_score(covered)

    return selected, covered, score


# ==========================
# EKSEKUSI DAN PERBANDINGAN
# ==========================

start = time.perf_counter()
bt_combo, bt_covered, bt_score = backtracking()
bt_time = time.perf_counter() - start

start = time.perf_counter()
gr_combo, gr_covered, gr_score = greedy()
gr_time = time.perf_counter() - start

print("=" * 50)
print("HASIL BACKTRACKING")
print("=" * 50)
print("CCTV Terpilih :", bt_combo)
print("Titik Terawasi:", sorted(bt_covered))
print("Jumlah Titik  :", len(bt_covered))
print("Total Bobot   :", bt_score)
print("Waktu         : %.8f detik" % bt_time)

print()

print("=" * 50)
print("HASIL GREEDY")
print("=" * 50)
print("CCTV Terpilih :", gr_combo)
print("Titik Terawasi:", sorted(gr_covered))
print("Jumlah Titik  :", len(gr_covered))
print("Total Bobot   :", gr_score)
print("Waktu         : %.8f detik" % gr_time)

print()

print("=" * 50)
print("PERBANDINGAN")
print("=" * 50)

if bt_score > gr_score:
    print("Backtracking menghasilkan solusi lebih baik.")
elif bt_score < gr_score:
    print("Greedy menghasilkan solusi lebih baik.")
else:
    print("Kedua algoritma menghasilkan solusi yang sama.")

if bt_time > gr_time:
    print("Greedy lebih cepat.")
else:
    print("Backtracking lebih cepat.")
```
