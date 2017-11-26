from __future__ import division

from csv_saver import save_rows_to_csv
from newton_raphson import newton_raphson_solve


def q3():
    print('\n=== Question 3 ===')
    v_n, values = newton_raphson_solve()
    print('Solution: {}'.format(v_n))
    v_a, v_b = v_n.values
    print('v_a: {:.3f} mV'.format(v_a * 1000))
    print('v_b: {:.3f} mV'.format(v_b * 1000))

    save_rows_to_csv('report/csv/q3.csv', values, header=('Iteration', 'v_A', 'v_B', 'f_A', 'f_B', '|f|'))


if __name__ == '__main__':
    q3()
