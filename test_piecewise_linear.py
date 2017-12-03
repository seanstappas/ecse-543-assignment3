import unittest

from piecewise_linear import PiecewiseLinearInterpolator

B = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]
H = [0.0, 14.7, 36.5, 71.7, 121.4, 197.4, 256.2, 348.7, 540.6, 1062.8, 2317.0, 4781.9, 8687.4, 13924.3, 22650.2]
A = 1e-4


class TestPiecewiseLinearInterpolation(unittest.TestCase):
    def test_evaluate(self):
        interpolator = PiecewiseLinearInterpolator()
        for b, h in zip(B, H):
            self.assertAlmostEqual(h, interpolator.evaluate_b(b))
            self.assertAlmostEqual(h, interpolator.evaluate_flux(b * A))


if __name__ == '__main__':
    unittest.main()
