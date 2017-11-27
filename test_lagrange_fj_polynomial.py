import unittest

from lagrange import lagrange_fj_polynomial


class TestLagrange(unittest.TestCase):
    def test_lagrange_fj_polynomial(self):
        expected_coefficients = [-1, 1]

        actual_coefficients = (lagrange_fj_polynomial(1, [1, 2])).coefficients

        self.assertEqual(expected_coefficients, actual_coefficients)


if __name__ == '__main__':
    unittest.main()
