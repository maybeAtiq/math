"""
Problem 04: Solving and verifying a linear system

Statement:
    A = [[4, -2, 1], [-2, 4, -2], [1, -2, 4]],  b = [11, -16, 17]
    (a) Solve Ax = b using scipy.linalg.lu_factor / lu_solve.
    (b) Verify the residual ||Ax - b|| < 1e-12.
    (c) A is symmetric; confirm its eigenvalues (numpy.linalg.eigvalsh) are real
        and positive, so A is positive definite.

Expected output:
    x = [1, -2, 3]
    eigenvalues approximately [1.6277, 3.0, 7.3723]

TODO: implement, then write tests in tests/test_p04_linear_system.py
"""

import numpy as np
from scipy.linalg import lu_factor, lu_solve


def solve_system(A, b):
    """Solve Ax = b using LU factorization and return the solution vector."""
    lu, piv = lu_factor(A)
    return lu_solve((lu, piv), b)


def is_positive_definite(A):
    """Return True when the symmetric matrix has strictly positive eigenvalues."""
    A = np.asarray(A, dtype=float)
    if A.shape[0] != A.shape[1]:
        return False
    if not np.allclose(A, A.T):
        return False
    eigvals = np.linalg.eigvalsh(A)
    return bool(np.all(eigvals > 0.0))
