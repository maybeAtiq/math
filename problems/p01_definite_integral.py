"""
Problem 01: Definite integral, exact vs numerical

Statement:
    Compute I = integral from 0 to pi of x^2 * sin(x) dx.
    (a) Return the exact value symbolically using SymPy.
    (b) Return a numerical approximation using scipy.integrate.quad.
    The two answers must agree to within 1e-10.

Expected output:
    Exact value: pi^2 - 4  (approximately 5.869604401089358)
"""
import numpy as np
import sympy as sp
from scipy.integrate import quad


def exact_integral():
    """Return the exact value of the integral as a SymPy expression."""
    x = sp.symbols("x")
    return sp.integrate(x**2 * sp.sin(x), (x, 0, sp.pi))


def numerical_integral():
    """Return (value, estimated_error) from scipy.integrate.quad."""
    value, error = quad(lambda x: x**2 * np.sin(x), 0, np.pi)
    return value, error
