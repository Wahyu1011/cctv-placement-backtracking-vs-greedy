# CCTV Placement Optimization using Backtracking and Greedy Algorithms

## 📖 Description

This project implements and compares **Backtracking** and **Greedy** algorithms for optimizing CCTV placement in a campus parking area based on security risk points.

The objective is to determine the best CCTV positions that maximize surveillance coverage of vulnerable locations while using a limited number of cameras.

This project was developed as part of an Algorithm Design and Analysis course assignment.

---

## 🎯 Problem Statement

Campus parking areas often contain several locations with different security risk levels. Due to budget and infrastructure limitations, only a limited number of CCTV cameras can be installed.

The challenge is to determine which CCTV positions should be selected to maximize the total security coverage.

---

## 🧠 Algorithms Used

### 1. Backtracking

Backtracking evaluates every possible CCTV placement combination and selects the one with the highest total security coverage.

**Advantages**

* Produces an optimal solution.
* Explores all possible combinations.

**Disadvantages**

* Higher computational cost.
* Slower for large datasets.

### 2. Greedy

Greedy selects the CCTV position that provides the highest immediate gain at each step.

**Advantages**

* Faster execution.
* Simple implementation.

**Disadvantages**

* Does not always guarantee the optimal solution.

---

## 📊 Sample Dataset

### Security Risk Points

| Point | Risk Value |
| ----- | ---------- |
| P1    | 5          |
| P2    | 4          |
| P3    | 3          |
| P4    | 5          |
| P5    | 2          |
| P6    | 4          |
| P7    | 3          |
| P8    | 5          |

### CCTV Coverage

| CCTV | Covered Points |
| ---- | -------------- |
| C1   | P1, P2, P3     |
| C2   | P2, P4, P5     |
| C3   | P4, P6, P7     |
| C4   | P1, P5, P8     |
| C5   | P3, P6, P8     |

Maximum CCTV installed: **2 units**

---

## 📁 Project Structure

```text
cctv-placement-backtracking-vs-greedy/
│
├── src/
│   └── main.py
│
├── README.md
│
└── LICENSE
```

---

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/yourusername/cctv-placement-backtracking-vs-greedy.git
```

Move into the project directory:

```bash
cd cctv-placement-backtracking-vs-greedy
```

Run the program:

```bash
python src/main.py
```

---

## 📈 Example Output

```text
==================================================
HASIL BACKTRACKING
==================================================
CCTV Terpilih : ('C1', 'C3')
Titik Terawasi: ['P1', 'P2', 'P3', 'P4', 'P6', 'P7']
Jumlah Titik  : 6
Total Bobot   : 24

==================================================
HASIL GREEDY
==================================================
CCTV Terpilih : ['C1', 'C3']
Titik Terawasi: ['P1', 'P2', 'P3', 'P4', 'P6', 'P7']
Jumlah Titik  : 6
Total Bobot   : 24
```

---

## 📋 Comparison

| Parameter        | Backtracking | Greedy  |
| ---------------- | ------------ | ------- |
| CCTV Selected    | C1 + C3      | C1 + C3 |
| Covered Points   | 6            | 6       |
| Total Risk Score | 24           | 24      |
| Optimality       | Optimal      | Optimal |
| Computation Time | Longer       | Faster  |

---

## 📚 Related Paper

**Comparison of Backtracking and Greedy Algorithms in CCTV Placement Optimization for Campus Parking Areas Based on Security Risk Points**

This repository serves as the implementation and experimental component of the paper.

---

## 👨‍💻 Author

Wahyu Eko Setyo Pribowo

Algorithm Design and Analysis Project

2026
