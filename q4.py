from __future__ import division

from math import cos, log10, sin, log

import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.patches import Rectangle

from gauss_legendre import one_point_gauss_legendre, one_point_gauss_legendre_arbitrary_widths, \
    convert_relative_widths_to_widths

rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)


def q4():
    print('\n=== Question 4 ===')
    q4a()
    q4b()
    q4c()


def q4a():
    print('\n=== Question 4(a) ===')
    n_values = []
    integrals = []
    n_max = 20
    actual_integral = sin(1)
    print('Actual integral of cos(x): {}'.format(actual_integral))
    for n in range(1, n_max + 1):
        integral = one_point_gauss_legendre(n, func=cos)
        n_values.append(n)
        integrals.append(integral)
        print('Integral of cos(x) with N={}: {}'.format(n, integral))
        print('Error: {}'.format(abs(actual_integral - integral)))
    plot_error(n_values, integrals, actual_integral, func=cos, filename='q4a')


def q4b():
    print('\n=== Question 4(b) ===')
    n_values = []
    integrals = []
    n_max = 200
    actual_integral = -1
    print('Actual integral of ln(x): {}'.format(actual_integral))
    for n in range(10, n_max + 1, 10):
        integral = one_point_gauss_legendre(n, func=log)
        n_values.append(n)
        integrals.append(integral)
        print('Integral of ln(x) with N={}: {}'.format(n, integral))
        print('Error: {}'.format(abs(actual_integral - integral)))
    plot_error(n_values, integrals, actual_integral, func=log, filename='q4b')


def q4c():
    print('\n=== Question 4(c) ===')
    actual_integral = -1
    print('Actual integral of ln(x): {}'.format(actual_integral))
    relative_widths = [x for x in range(1, 11)]
    print('Relative widths: {}'.format(relative_widths))
    widths = convert_relative_widths_to_widths(relative_widths)
    print('Actual widths: {}'.format(widths))
    integral = one_point_gauss_legendre_arbitrary_widths(widths, func=log)
    print('Estimated Integral of ln(x): {}'.format(integral))
    print('Error: {}'.format(abs(actual_integral - integral)))
    plot_log_widths(widths)


def plot_error(n_values, integrals, actual_integral, func, filename='q4a'):
    x_range = [log10(n) for n in n_values]
    y_range = [log10(abs(actual_integral - integral)) for integral in integrals]
    f = plt.figure()
    plt.plot(x_range, y_range, 'o-')
    plt.xlabel('$\log_{10}{N}$')
    plt.ylabel('$\log_{10}{E}$')
    plt.grid(True)
    f.savefig('report/plots/{}.pdf'.format(filename), bbox_inches='tight')


def plot_log_widths(widths):
    x_range = [i / 100 for i in range(1, 101)]
    y_range = [log(x) for x in x_range]
    f = plt.figure()
    plt.plot(x_range, y_range, 'C9')
    axis = plt.gca()
    width_sum = 0
    for w in widths:
        axis.add_patch(Rectangle((width_sum, 0), w, log(width_sum + w / 2), facecolor='C0'))
        width_sum += w

    plt.xlabel('$x$')
    plt.ylabel('$\log_e x$')
    plt.grid(True)
    f.savefig('report/plots/q4c2.pdf', bbox_inches='tight')


if __name__ == '__main__':
    q4()
