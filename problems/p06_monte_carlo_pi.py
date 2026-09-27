"""
Problem 06: Monte Carlo estimate of pi

Statement:
    Estimate pi by sampling N random points in the unit square and counting
    the fraction inside the quarter circle x^2 + y^2 <= 1.
    Use numpy.random.default_rng(seed) so results are reproducible.
    (a) With N = 1,000,000 and seed = 42, the estimate is within 0.01 of pi.
    (b) The same seed always returns the same estimate.
    (c) Averaged over several seeds, the error shrinks as N grows
        (roughly like 1/sqrt(N)).

TODO: implement, then write tests in tests/test_p06_monte_carlo_pi.py
"""

import numpy as np


def estimate_pi(n, seed=42):
    """Estimate pi from Monte Carlo sampling in the unit square."""
    rng = np.random.default_rng(seed)
    x = rng.random(n)
    y = rng.random(n)
    inside = x * x + y * y <= 1.0
    return 4.0 * inside.mean()
