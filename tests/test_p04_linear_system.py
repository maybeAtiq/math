import numpy as np

from problems.p04_linear_system import is_positive_definite, solve_system


A = np.array([[4, -2, 1], [-2, 4, -2], [1, -2, 4]], dtype=float)
b = np.array([11.0, -16.0, 17.0])


def test_solve_system_matches_exact_solution():
    x = solve_system(A, b)
    np.testing.assert_allclose(x, np.array([1.0, -2.0, 3.0]), atol=1e-12)
    np.testing.assert_allclose(A @ x, b, atol=1e-12)


def test_matrix_is_positive_definite():
    assert is_positive_definite(A) is True
    eigenvalues = np.linalg.eigvalsh(A)
    np.testing.assert_allclose(eigenvalues, [1.627713, 3.0, 7.372287], rtol=1e-4, atol=1e-4)
    assert np.all(eigenvalues > 0)
