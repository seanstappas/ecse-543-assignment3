from __future__ import division
from lagrange import lagrange_interpolation

import matplotlib.pyplot as plt
from matplotlib import rc
rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)

B = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]
H = [0.0, 14.7, 36.5, 71.7, 121.4, 197.4, 256.2, 348.7, 540.6, 1062.8, 2317.0, 4781.9, 8687.4, 13924.3, 22650.2]


def q1():
    print('\n=== Question 1 ===')
    q1a()
    q1b()


def q1a():
    print('\n=== Question 1(a) ===')
    num_points = 6
    y_values = B[:num_points]
    x_values = H[:num_points]

    print('B: {}'.format(y_values))
    print('H: {}'.format(x_values))

    lagrange_interpolation_polynomial = lagrange_interpolation(x_values, y_values)

    print('Interpolation polynomial: {}'.format(lagrange_interpolation_polynomial))

    plot_polynomial(0, 200, lagrange_interpolation_polynomial, x_values, y_values, filename='q1a')


def q1b():
    print('\n=== Question 1(b) ===')
    y_values = [0.0, 1.3, 1.4, 1.7, 1.8, 1.9]
    x_values = [H[B.index(b)] for b in y_values]

    print('B: {}'.format(y_values))
    print('H: {}'.format(x_values))

    lagrange_interpolation_polynomial = lagrange_interpolation(x_values, y_values)

    print('Interpolation polynomial: {}'.format(lagrange_interpolation_polynomial))

    plot_polynomial(0, 22700, lagrange_interpolation_polynomial, x_values, y_values, filename='q1b')


def plot_polynomial(x_min, x_max, polynomial, data_x_points, data_y_points, num_points=1000, filename='q1a'):
    subdivision = (x_max - x_min) / num_points
    x_range = [x_min + i * subdivision for i in range(num_points)]
    y_range = [polynomial.evaluate(x) for x in x_range]
    f = plt.figure()
    plt.plot(x_range, y_range)
    plt.plot(data_x_points, data_y_points, 'oC0')
    plt.xlabel('$H$')
    plt.ylabel('$B$')
    plt.grid(True)
    f.savefig('report/plots/{}.pdf'.format(filename), bbox_inches='tight')


if __name__ == '__main__':
    q1()
