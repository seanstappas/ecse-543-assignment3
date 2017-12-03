from __future__ import division


def one_point_gauss_legendre(n, func):
    """
    Approximates the integral of the given function from 0 to 1 with one-point Gauss-Legendre integration.

    :param n: the number of segments
    :param func: the function to integrate
    :return: the approximate integral
    """
    integral = 0
    for i in range(n):
        integral += func((i + 0.5) / n)
    return integral / n


def one_point_gauss_legendre_arbitrary_widths(widths, func):
    """
    Approximates the integral of the given function from 0 to 1 with one-point Gauss-Legendre integration with
    arbitrary widths.

    :param widths: the widths of the intervals
    :param func: the function to integrate
    :return: the approximate integral
    """
    integral = 0
    width_sum = 0
    for h in widths:
        integral += h * func(width_sum + h / 2)
        width_sum += h
    return integral


def convert_relative_widths_to_widths(relative_widths):
    """
    Converts the given relative interval widths to actual widths.

    :param relative_widths: the relative widths to convert
    :return: the actual widths
    """
    sum_relative_widths = sum(relative_widths)
    return [r / sum_relative_widths for r in relative_widths]
