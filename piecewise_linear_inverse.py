from __future__ import division

from lagrange import lagrange_interpolation

B = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]
H = [0.0, 14.7, 36.5, 71.7, 121.4, 197.4, 256.2, 348.7, 540.6, 1062.8, 2317.0, 4781.9, 8687.4, 13924.3, 22650.2]
A = 1e-4


class PiecewiseLinearInterpolatorInverse:
    """
    Piecewise-linear interpolator for the B-H curve.
    """

    def __init__(self):
        self.piecewise_linear_polynomials = []
        for i in range(len(B) - 1):
            x_values = H[i:i + 2]
            y_values = B[i:i + 2]
            lagrange_interpolation_polynomial = lagrange_interpolation(x_values, y_values)
            self.piecewise_linear_polynomials.append(lagrange_interpolation_polynomial)

    def evaluate_h(self, h):
        if h > H[-1]:
            return self.piecewise_linear_polynomials[-1].evaluate(h)
        elif h < H[0]:
            return self.piecewise_linear_polynomials[0].evaluate(h)
        for i in range(len(B) - 1):
            if H[i] <= h <= H[i + 1]:
                return self.piecewise_linear_polynomials[i].evaluate(h)
        return None
