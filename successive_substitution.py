from __future__ import division

import math

from piecewise_linear import PiecewiseLinearInterpolator
from piecewise_linear_inverse import PiecewiseLinearInterpolatorInverse

L_a = 5e-3
A = 1e-4
mu_0 = 4e-7 * math.pi
EPSILON = 1e-6


def successive_substitution_solve():
    h_interpolator = PiecewiseLinearInterpolator()
    b_interpolator = PiecewiseLinearInterpolatorInverse()

    flux = 1e-6
    f_0 = update_f(flux, h_interpolator)
    f = f_0
    iterations = 0
    while abs(f / f_0) >= EPSILON:
        print('Flux: {} Wb at iteration {}'.format(flux, iterations))
        flux = update_flux4(flux, b_interpolator)
        f = update_f(flux, h_interpolator)
        iterations += 1
    return flux, iterations


def update_f(flux, h_interpolator):
    return L_a / (A * mu_0) * flux + 0.3 * h_interpolator.evaluate_flux(flux) - 8000


def update_flux(flux, h_interpolator):
    return (8000 - 0.3 * h_interpolator.evaluate_flux(flux)) / (L_a / (A * mu_0))


def update_flux2(flux, h_interpolator):
    return 8000 / ((L_a / (A * mu_0)) + 0.3 * h_interpolator.evaluate_flux(flux) / flux)


def update_flux3(flux, h_interpolator):
    return 0.3 * h_interpolator.evaluate_flux(flux) / (8000 / flux - (L_a / (A * mu_0)))


def update_flux4(flux, b_interpolator):
    return A * b_interpolator.evaluate_h((8000 - (L_a / (A * mu_0)) * flux) / 0.3)
