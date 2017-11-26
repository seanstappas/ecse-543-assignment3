from __future__ import division


def one_point_gauss_legendre(n, func):
    integral = 0
    for i in range(n):
        integral += func((i + 0.5) / n)
    return integral / n


def one_point_gauss_legendre_arbitrary_widths(widths, func):
    integral = 0
    width_sum = 0
    for h in widths:
        integral += h * func(width_sum + h / 2)
        width_sum += h
    return integral


def convert_relative_widths_to_widths(relative_widths):
    sum_relative_widths = sum(relative_widths)
    return [r / sum_relative_widths for r in relative_widths]
