from __future__ import division

from data_saver import save_rows_to_latex
from newton_raphson_matrix import newton_raphson_matrix_solve


import numpy as np
import numpy.polynomial.polynomial as poly
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib import rc

rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)


def q3():
    print('\n=== Question 3 ===')
    v_n, error_values, norm_values, vA_values, vB_values, fA_values, fB_values = newton_raphson_matrix_solve()
    print('Solution: {}'.format(v_n))
    v_a, v_b = v_n.values
    print('v_a: {:.3f} mV'.format(v_a * 1000))
    print('v_b: {:.3f} mV'.format(v_b * 1000))
    save_rows_to_latex('report/latex/q3.txt', zip(vA_values, vB_values, fA_values, fB_values))
    plot_error(error_values)
    plot_error_quadratic_fit(error_values)


def plot_error(error_values):
    x_range = [i for i in range(len(error_values))]
    y_range = error_values
    f = plt.figure()
    plt.plot(x_range, y_range, 'o-')
    plt.xlabel('Step')
    plt.ylabel('Error')
    plt.grid(True)
    f.savefig('report/plots/q3.pdf', bbox_inches='tight')


def plot_error_quadratic_fit(error_values):
    f = plt.figure()

    x_range = [i for i in range(len(error_values))]
    y_range = [float(error) for error in error_values]
    print(y_range)
    plt.plot(x_range, y_range, 'o')

    x_new = np.linspace(x_range[0], x_range[-3], num=len(x_range) * 10)
    polynomial_coeffs = poly.polyfit(x_range, y_range, deg=2)
    polynomial_fit = poly.polyval(x_new, polynomial_coeffs)
    N = sp.symbols("1/h")
    poly_label = sum(sp.S("{:.5f}".format(v)) * N ** i for i, v in enumerate(polynomial_coeffs))
    equation = '${}$'.format(sp.printing.latex(poly_label))
    plt.plot(x_new, polynomial_fit, 'C0-', label=equation)

    plt.xlabel('Step')
    plt.ylabel('Error')
    plt.grid(True)
    plt.legend()
    f.savefig('report/plots/q3_fit.pdf', bbox_inches='tight')


if __name__ == '__main__':
    q3()
