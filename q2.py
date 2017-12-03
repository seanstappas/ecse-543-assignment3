import math

from piecewise_linear import PiecewiseLinearInterpolator
from successive_substitution import successive_substitution_solve
from newton_raphson import newton_raphson_solve

import matplotlib.pyplot as plt
from matplotlib import rc

rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)


B = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]
H = [0.0, 14.7, 36.5, 71.7, 121.4, 197.4, 256.2, 348.7, 540.6, 1062.8, 2317.0, 4781.9, 8687.4, 13924.3, 22650.2]
L_a = 5e-3
A = 1e-4
mu_0 = 4e-7 * math.pi
L_c = 0.3
N = 1000
I = 8


def q2():
    print('\n=== Question 2 ===')
    q2a()
    q2b()
    q2c()


def q2a():
    print('\n=== Question 2(a) ===')
    print('Flux equation: ')
    coeff_1 = L_a / (A * mu_0)
    print(coeff_1)
    coeff_2 = L_c
    coeff_3 = N * I
    eq = 'f(\psi) = \SI{{{:1.3e}}}{{}} \psi + {}H(\psi) - {} = 0'.format(coeff_1, coeff_2, coeff_3)
    print(eq)
    with open('report/latex/flux_equation.txt', 'w') as f:
        f.write(eq)


def q2b():
    print('\n=== Question 2(b) ===')
    flux, iterations = newton_raphson_solve()
    print('Solved flux: {:1.3e} Wb'.format(flux))
    print('Number of iterations: {}'.format(iterations))
    plot_interpolation(0.0, 1.9, PiecewiseLinearInterpolator(), B, H)


def q2c():
    print('\n=== Question 2(c) ===')
    flux, iterations = successive_substitution_solve()
    print('Solved flux: {:1.3e} Wb'.format(flux))
    print('Number of iterations: {}'.format(iterations))


def plot_interpolation(x_min, x_max, interpolator, data_x_points, data_y_points, num_points=1000, filename='q2b'):
    subdivision = (x_max - x_min) / num_points
    x_range = [x_min + i * subdivision for i in range(num_points)]
    y_range = [interpolator.evaluate_b(x) for x in x_range]
    f = plt.figure()
    plt.plot(x_range, y_range)
    plt.plot(data_x_points, data_y_points, 'oC0')
    plt.xlabel('$B$')
    plt.ylabel('$H$')
    plt.grid(True)
    f.savefig('report/plots/{}.pdf'.format(filename), bbox_inches='tight')


if __name__ == '__main__':
    q2()
