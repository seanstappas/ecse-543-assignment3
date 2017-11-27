import unittest

from polynomial import Polynomial


class TestPolynomial(unittest.TestCase):
    def test___add__(self):
        p1 = Polynomial([4, 5, 6])
        p2 = Polynomial([4, 5, 6, 7, 8])
        expected_coefficients = [8, 10, 12, 7, 8]

        actual_coefficients = (p1 + p2).coefficients

        self.assertEqual(expected_coefficients, actual_coefficients)

    def test___sub__(self):
        p1 = Polynomial([4, 5, 6])
        p2 = Polynomial([4, 5, 6, 7, 8])
        expected_coefficients = [0, 0, 0, -7, -8]

        actual_coefficients = (p1 - p2).coefficients

        self.assertEqual(expected_coefficients, actual_coefficients)

    def test___mul__(self):
        p1 = Polynomial([4, 5, 6])
        p2 = Polynomial([4, 5, 6, 7, 8])
        expected_coefficients = [16, 40, 73, 88, 103, 82, 48]

        actual_coefficients = (p1 * p2).coefficients

        self.assertEqual(expected_coefficients, actual_coefficients)


if __name__ == '__main__':
    unittest.main()
