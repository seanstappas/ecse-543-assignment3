from __future__ import division

import copy
from math import exp

from matrices import Matrix

E = 220e-3
R = 500
I_SA = 0.6e-6
I_SB = 1.2e-6
kT_q = 25e-3

EPSILON = 1e-9


def newton_raphson_matrix_solve():
    error_values = []
    norm_values = []
    vA_values = []
    vB_values = []
    fA_values = []
    fB_values = []

    iteration = 1
    v_n = Matrix.empty(2, 1)
    f = Matrix.empty(2, 1)
    F = Matrix.empty(2, 2)
    update_f(f, v_n)
    f_0 = copy.deepcopy(f)
    update_jacobian(F, v_n)

    error_values.append('{:.3e}'.format(f.two_norm / f_0.two_norm))
    norm_values.append('{:.3e}'.format(f.two_norm))
    vA_values.append(v_n.scaled_values(1000)[0])
    vB_values.append(v_n.scaled_values(1000)[1])
    fA_values.append('{:.3e}'.format(f.values[0]))
    fB_values.append('{:.3e}'.format(f.values[1]))

    while f.two_norm / f_0.two_norm >= EPSILON:
        v_n -= inverse_2x2(F) * f
        update_f(f, v_n)
        update_jacobian(F, v_n)
        iteration += 1

        error_values.append('{:.3e}'.format(f.two_norm / f_0.two_norm))
        norm_values.append('{:.3e}'.format(f.two_norm))
        vA_values.append(v_n.scaled_values(1000)[0])
        vB_values.append(v_n.scaled_values(1000)[1])
        fA_values.append('{:.3e}'.format(f.values[0]))
        fB_values.append('{:.3e}'.format(f.values[1]))
    return v_n, error_values, norm_values, vA_values, vB_values, fA_values, fB_values


def update_f(f, v_n):
    v_a, v_b = v_n.values
    f[0][0] = f_a(v_a, v_b)
    f[1][0] = f_b(v_a, v_b)


def update_jacobian(F, v_n):
    v_a, v_b = v_n.values
    F[0][0] = dfa_dva(v_a, v_b)
    F[0][1] = dfa_dvb(v_a, v_b)
    F[1][0] = dfb_dva(v_a, v_b)
    F[1][1] = dfb_dvb(v_a, v_b)


def f_a(v_a, v_b):
    return v_a + R * I_SA * exp_f_term(v_a, v_b) - E


def f_b(v_a, v_b):
    return I_SA * exp_f_term(v_a, v_b) - I_SB * exp_f_term(0, -v_b)


def dfa_dva(v_a, v_b):
    return 1 + R * I_SA * exp_df_term(v_a, v_b)


def dfa_dvb(v_a, v_b):
    return - R * I_SA * exp_df_term(v_a, v_b)


def dfb_dva(v_a, v_b):
    return I_SA * exp_df_term(v_a, v_b)


def dfb_dvb(v_a, v_b):
    return - I_SA * exp_df_term(v_a, v_b) - I_SB * exp_df_term(0, -v_b)


def exp_f_term(v_a, v_b):
    return exp((v_a - v_b) / kT_q) - 1


def exp_df_term(v_a, v_b):
    return exp((v_a - v_b) / kT_q) / kT_q


def inverse_2x2(A):
    a = A[0][0]
    b = A[0][1]
    c = A[1][0]
    d = A[1][1]
    inverse = Matrix([
        [d, -b],
        [-c, a]
    ])
    return inverse.scalar_divide(a * d - b * c)
