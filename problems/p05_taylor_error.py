"""
Problem 05: Taylor polynomial and its error bound

Statement:
    (a) Use sympy.series to get the degree-5 Taylor polynomial of e^x about x = 0.
    (b) Evaluate it at x = 0.5 and compute the actual error |e^0.5 - T5(0.5)|.
    (c) Check the error is below the Lagrange remainder bound
        e^0.5 * 0.5^6 / 6!  (approximately 3.578e-05).

Expected output:
    T5(x) = 1 + x + x^2/2 + x^3/6 + x^4/24 + x^5/120
    actual error < 3.578e-05

TODO: implement, then write tests in tests/test_p05_taylor_error.py
"""

import math

import sympy as sp


def taylor_poly(degree=5):
    """Return the Taylor polynomial of exp(x) as a SymPy expression."""
    x = sp.symbols("x")
    return sp.series(sp.exp(x), x, 0, degree + 1).removeO()


def lagrange_bound(x=0.5, degree=5):
    """Return the Lagrange remainder bound for the degree-5 Maclaurin polynomial."""
    return math.exp(abs(x)) * abs(x) ** (degree + 1) / math.factorial(degree + 1)
