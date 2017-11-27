import unittest

from polynomial import Polynomial


class TestPolynomial(unittest.TestCase):
    def test___add__(self):
        p1 = Polynomial([4, 5, 6])
        p2 = Polynomial([4, 5, 6, 7, 8])
        expected_coefficients = [8, 10, 12, 7, 8]

        p3 = (p1 + p2)
        actual_coefficients = p3.coefficients

        self.assertEqual(expected_coefficients, actual_coefficients)
        print('({}) + ({}) = ({})'.format(p1, p2, p3))

    def test___sub__(self):
        p1 = Polynomial([4, 5, 6])
        p2 = Polynomial([4, 5, 6, 7, 8])
        expected_coefficients = [0, 0, 0, -7, -8]

        p3 = (p1 - p2)
        actual_coefficients = p3.coefficients

        self.assertEqual(expected_coefficients, actual_coefficients)
        print('({}) - ({}) = ({})'.format(p1, p2, p3))

    def test___mul__(self):
        p1 = Polynomial([4, 5, 6])
        p2 = Polynomial([4, 5, 6, 7, 8])
        expected_coefficients = [16, 40, 73, 88, 103, 82, 48]

        p3 = (p1 * p2)
        actual_coefficients = p3.coefficients

        self.assertEqual(expected_coefficients, actual_coefficients)
        print('({}) * ({}) = ({})'.format(p1, p2, p3))

    def test_evaluate_0(self):
        p1 = Polynomial([4, 5, 6])
        expected = 4

        actual = p1.evaluate(0)

        self.assertEqual(expected, actual)

    def test_evaluate_1(self):
        p1 = Polynomial([4, 5, 6])
        expected = 4 + 5 + 6

        actual = p1.evaluate(1)

        self.assertEqual(expected, actual)

    def test_evaluate_2(self):
        p1 = Polynomial([4, 5, 6])
        expected = 4 + 10 + 24

        actual = p1.evaluate(2)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
