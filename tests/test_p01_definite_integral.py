import math
import sympy as sp
from problems.p01_definite_integral import exact_integral, numerical_integral


def test_exact_matches_closed_form():
    # Integration by parts twice gives pi^2 - 4
    assert sp.simplify(exact_integral() - (sp.pi**2 - 4)) == 0


def test_numerical_matches_exact():
    value, _ = numerical_integral()
    assert math.isclose(value, float(exact_integral()), abs_tol=1e-10)


def test_quad_error_estimate_is_small():
    _, error = numerical_integral()
    assert error < 1e-10
