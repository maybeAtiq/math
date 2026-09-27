import math

from scipy.optimize import brentq

from problems.p03_newton_root import newton


def f(x):
    return x**3 - 2 * x - 5


def df(x):
    return 3 * x**2 - 2


def test_newton_converges_to_expected_root():
    root, iterates = newton(f, df, 2.0)

    assert math.isclose(root, brentq(f, 2.0, 3.0), rel_tol=1e-12, abs_tol=1e-12)
    assert len(iterates) < 10
    assert iterates[0] == 2.0
    assert abs(iterates[-1] - root) < 1e-12


def test_newton_iterates_shrink_quadratically():
    _, iterates = newton(f, df, 2.0)
    root = iterates[-1]
    errors = [abs(x - root) for x in iterates]
    positive_errors = [e for e in errors if e > 0]

    assert len(positive_errors) >= 2
    assert positive_errors[-1] < positive_errors[-2] < positive_errors[0]
    assert errors[-1] < 1e-12
