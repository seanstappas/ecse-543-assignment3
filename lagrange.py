from polynomial import Polynomial


def lagrange_fj_constant_denominator(j, x_values):
    product = 1
    for r, x_r in enumerate(x_values):
        if r != j:
            product *= (x_values[j] - x_r)
    return product


def lagrange_fj_polynomial(j, x_values):
    result_polynomial = Polynomial([1])
    for r in range(len(x_values)):
        if r != j:
            result_polynomial *= Polynomial([-x_values[r], 1])
    return result_polynomial
