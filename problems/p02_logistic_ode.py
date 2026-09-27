"""
Problem 02: Logistic growth ODE, numerical vs closed form

Statement:
    Solve dP/dt = r * P * (1 - P/K) with r = 0.5, K = 1000, P(0) = 10.
    (a) Implement the closed-form solution P(t) = K / (1 + ((K - P0)/P0) * exp(-r t)).
    (b) Solve the ODE numerically with scipy.integrate.solve_ivp on t in [0, 20].
    The numerical and closed-form values must agree to a relative tolerance of 1e-6.

Expected output:
    P(10) is approximately 599.8596018130347
    P(t) approaches K = 1000 as t grows and never exceeds it.

TODO: implement both functions, then write tests in tests/test_p02_logistic_ode.py
"""

import numpy as np
from scipy.integrate import solve_ivp


def closed_form(t, r=0.5, K=1000.0, P0=10.0):
    """Return the closed-form logistic solution for scalar or array time values."""
    t_arr = np.asarray(t, dtype=float)
    return K / (1.0 + ((K - P0) / P0) * np.exp(-r * t_arr))


def numerical(t_eval, r=0.5, K=1000.0, P0=10.0):
    """Return P values at the times in t_eval using solve_ivp (use rtol=1e-10)."""
    t_eval = np.asarray(t_eval, dtype=float)

    def rhs(t, y):
        return r * y[0] * (1.0 - y[0] / K)

    sol = solve_ivp(rhs, (t_eval[0], t_eval[-1]), [P0], t_eval=t_eval, rtol=1e-10, atol=1e-12)
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol.y[0]
