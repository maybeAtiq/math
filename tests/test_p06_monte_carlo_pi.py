import math

from problems.p06_monte_carlo_pi import estimate_pi


def test_estimate_is_close_to_pi_for_large_sample():
    estimate = estimate_pi(1_000_000, seed=42)
    assert abs(estimate - math.pi) < 0.01


def test_same_seed_is_reproducible_and_larger_n_is_more_accurate():
    estimate_a = estimate_pi(200_000, seed=123)
    estimate_b = estimate_pi(200_000, seed=123)
    assert estimate_a == estimate_b

    small = estimate_pi(10_000, seed=123)
    large = estimate_pi(100_000, seed=123)
    assert abs(large - math.pi) < abs(small - math.pi)
