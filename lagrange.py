from __future__ import division

from polynomial import Polynomial


def lagrange_interpolation(x_values, y_values):
    n = len(x_values)
    result_polynomial = Polynomial([])
    for j in range(n):
        result_polynomial += lagrange_lj_polynomial(j, x_values).scalar_multiply(y_values[j])
    return result_polynomial


def lagrange_lj_polynomial(j, x_values):
    fj_x = lagrange_fj_polynomial(j, x_values)
    fj_xj = lagrange_fj_constant_denominator(j, x_values)
    return fj_x.scalar_multiply(1 / fj_xj)


def lagrange_fj_polynomial(j, x_values):
    result_polynomial = Polynomial([1])
    for r in range(len(x_values)):
        if r != j:
            result_polynomial *= Polynomial([-x_values[r], 1])
    return result_polynomial


def lagrange_fj_constant_denominator(j, x_values):
    product = 1
    for r, x_r in enumerate(x_values):
        if r != j:
            product *= (x_values[j] - x_r)
    return product
