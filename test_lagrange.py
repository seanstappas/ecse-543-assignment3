import unittest

from lagrange import lagrange_fj_polynomial, lagrange_interpolation


class TestLagrange(unittest.TestCase):
    def test_lagrange_fj_polynomial(self):
        expected_coefficients = [-1, 1]

        actual_coefficients = (lagrange_fj_polynomial(1, [1, 2])).coefficients

        self.assertEqual(expected_coefficients, actual_coefficients)

    def test_lagrange_interpolation(self):
        x_values = [1, 2, 3, 4, 5]
        y_values = [4, 5, 1, 6, 10]

        polynomial = lagrange_interpolation(x_values, y_values)

        for x, y in zip(x_values, y_values):
            self.assertAlmostEqual(y, polynomial.evaluate(x))


if __name__ == '__main__':
    unittest.main()
