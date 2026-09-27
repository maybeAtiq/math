import numpy as np

from problems.p02_logistic_ode import closed_form, numerical


def test_closed_form_matches_known_value():
    value = closed_form(10.0)
    assert np.isclose(value, 599.8596018130347, rtol=1e-12, atol=1e-12)


def test_numerical_matches_closed_form():
    t_eval = np.linspace(0.0, 20.0, 201)
    y_num = numerical(t_eval)
    y_exact = closed_form(t_eval)
    np.testing.assert_allclose(y_num, y_exact, rtol=1e-6, atol=1e-8)
