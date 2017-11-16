import math

L_a = 5e-3
L_c = 0.3
A = 1e-4
N = 1000
I = 8
mu_0 = 4e-7 * math.pi


def q2():
    print('\n=== Question 2 ===')
    q2b()


def q2b():
    print('Flux equation: ')
    coeff_1 = L_a / (A * mu_0)
    coeff_2 = L_c
    coeff_3 = N * I
    eq = 'f(\psi) = \SI{{{:1.3e}}}{{}} \psi + {}H - {} = 0'.format(coeff_1, coeff_2, coeff_3)
    print(eq)
    with open('report/latex/flux_equation.txt', 'w') as f:
        f.write(eq)


if __name__ == '__main__':
    q2()
