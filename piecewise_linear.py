from __future__ import division

from lagrange import lagrange_interpolation

B = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]
H = [0.0, 14.7, 36.5, 71.7, 121.4, 197.4, 256.2, 348.7, 540.6, 1062.8, 2317.0, 4781.9, 8687.4, 13924.3, 22650.2]
A = 1e-4


class PiecewiseLinearInterpolator:
    def __init__(self):
        self.piecewise_linear_polynomials = []
        for i in range(len(B) - 1):
            x_values = B[i:i + 2]
            y_values = H[i:i + 2]
            lagrange_interpolation_polynomial = lagrange_interpolation(x_values, y_values)
            self.piecewise_linear_polynomials.append(lagrange_interpolation_polynomial)

    def evaluate_flux(self, flux):
        b = flux / A
        return self.evaluate_b(b)

    def evaluate_b(self, b):
        if b > B[-1]:
            return self.piecewise_linear_polynomials[-1].evaluate(b)
        elif b < B[0]:
            return self.piecewise_linear_polynomials[0].evaluate(b)
        for i in range(len(B) - 1):
            if B[i] <= b <= B[i + 1]:
                return self.piecewise_linear_polynomials[i].evaluate(b)
        return None
