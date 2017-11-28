from __future__ import division

A = 1e-4
EPSILON = 1e-6


def newton_raphson_solve():
    flux = 0
    f_0 = update_f(flux)
    f_prime = update_f_prime(flux)
    f = f_0
    while (f / f_0) >= EPSILON:
        flux = flux - f / f_prime
        f = update_f(flux)
        f_prime = update_f_prime(flux)


def update_f(flux):
    return 3.979e7 * flux + 0.3 * get_H(flux) - 8000


def update_f_prime(flux):
    return 3.979e7 + 0.3 * get_H_prime(flux)


def get_H(flux):
    B = flux / A
    return piecewise_linear_HB(B)


def get_H_prime(flux):
    pass


def piecewise_linear_HB(B):
    pass
