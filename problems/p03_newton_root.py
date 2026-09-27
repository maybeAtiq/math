"""
Problem 03: Newton's method with a convergence check

Statement:
    Find the real root of f(x) = x^3 - 2x - 5 (Wallis's classic equation).
    (a) Implement Newton's method yourself (no SciPy), starting from x0 = 2,
        stopping when |x_{n+1} - x_n| < 1e-14 or after 50 iterations.
        Return the root and the list of iterates.
    (b) Verify the answer against scipy.optimize.brentq on the bracket [2, 3].
    (c) Show quadratic convergence: the error roughly squares each step.

Expected output:
    Root is approximately 2.094551481542327, reached in fewer than 10 iterations.

TODO: implement, then write tests in tests/test_p03_newton_root.py
"""


def newton(f, df, x0, tol=1e-14, max_iter=50):
    """Apply Newton's method to find a root of f, returning (root, iterates)."""
    x = float(x0)
    iterates = [x]

    for _ in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(dfx) < 1e-30:
            break
        x_next = x - fx / dfx
        iterates.append(x_next)
        if abs(x_next - x) < tol:
            x = x_next
            break
        x = x_next

    return x, iterates
