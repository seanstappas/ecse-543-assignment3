from __future__ import division

from piecewise_linear import PiecewiseLinearInterpolator

EPSILON = 1e-6


def successive_substitution_solve():
    h_interpolator = PiecewiseLinearInterpolator()

    flux = 1e-8
    f_0 = update_f(flux, h_interpolator)
    f = f_0
    iterations = 0
    while abs(f / f_0) >= EPSILON:
        print('Flux: {} Wb at iteration {}'.format(flux, iterations))
        flux -= f
        f = update_f(flux, h_interpolator)
        iterations += 1
    return flux, iterations


def update_f(flux, h_interpolator):
    return 3.979e7 * flux + 0.3 * h_interpolator.evaluate_flux(flux) - 8000
