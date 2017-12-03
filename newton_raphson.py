from __future__ import division

import math

from piecewise_linear import PiecewiseLinearInterpolator
from slope_interpolation import SlopeInterpolator

L_a = 5e-3
A = 1e-4
mu_0 = 4e-7 * math.pi
EPSILON = 1e-6


def newton_raphson_solve():
    """
    Solves for the flux of the magnetic circuit in Q2 by Newton-Raphson.

    :return: the solved flux and number of steps
    """
    h_interpolator = PiecewiseLinearInterpolator()
    h_prime_interpolator = SlopeInterpolator()

    flux = 0
    f_0 = update_f(flux, h_interpolator)
    f_prime = update_f_prime(flux, h_prime_interpolator)
    f = f_0
    iterations = 0
    while abs(f / f_0) >= EPSILON:
        print('Flux: {} Wb at iteration {}'.format(flux, iterations))
        flux -= f / f_prime
        f = update_f(flux, h_interpolator)
        f_prime = update_f_prime(flux, h_prime_interpolator)
        iterations += 1
    return flux, iterations


def update_f(flux, h_interpolator):
    """
    Updates the f vector to perform a Newton-Raphson step.

    :param flux: the old flux
    :param h_interpolator: the interpolation for the H curve
    :return: the new f vector
    """
    return L_a / (A * mu_0) * flux + 0.3 * h_interpolator.evaluate_flux(flux) - 8000


def update_f_prime(flux, h_prime_interpolator):
    """
    Updates the f  vector to perform a Newton-Raphson step.

    :param flux: the old flux
    :param h_prime_interpolator: the interpolation for the H curve derivative
    :return: the new f vector
    """
    return L_a / (A * mu_0) + 3000 * h_prime_interpolator.evaluate_flux(flux)
