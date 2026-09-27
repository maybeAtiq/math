import math

import sympy as sp

from problems.p05_taylor_error import lagrange_bound, taylor_poly


x = sp.symbols("x")
EXPECTED_POLY = 1 + x + x**2 / 2 + x**3 / 6 + x**4 / 24 + x**5 / 120


def test_taylor_polynomial_matches_closed_form():
    poly = taylor_poly()
    assert sp.expand(poly - EXPECTED_POLY) == 0


def test_error_is_below_lagrange_bound():
    poly = taylor_poly()
    value = float(poly.subs(x, sp.Rational(1, 2)))
    actual_error = abs(math.e**0.5 - value)
    bound = lagrange_bound(0.5, 5)

    assert actual_error < bound
    assert bound < 3.58e-05
