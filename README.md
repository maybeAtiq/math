# Math Coding Problems

A collection of well-defined mathematical coding problems, each with a verified
Python solution and unit tests. Every problem checks its answer in at least one
independent way: a symbolic result against a numerical one, a hand-written
algorithm against a library routine, or a result against a proven error bound.

**Tools:** Python, NumPy, SciPy, SymPy, pytest

## Problems

| # | Problem | Topic | Verified by |
|---|---------|-------|-------------|
| 01 | Definite integral of x² sin(x) | Calculus | SymPy exact result vs SciPy `quad` |
| 02 | Logistic growth ODE | Differential equations | `solve_ivp` vs closed-form solution |
| 03 | Newton's method on x³ − 2x − 5 | Root finding | Hand-written Newton vs `brentq`, convergence order |
| 04 | 3×3 linear system | Linear algebra | LU solve, residual norm, eigenvalue check |
| 05 | Taylor polynomial of eˣ | Series / analysis | Actual error vs Lagrange remainder bound |
| 06 | Monte Carlo estimate of π | Probability | Tolerance, reproducibility, error vs N |

Each file in `problems/` contains the problem statement, the expected output,
and the solution. Tests live in `tests/`.

## Run it

```bash
pip install -r requirements.txt
pytest -v
```
