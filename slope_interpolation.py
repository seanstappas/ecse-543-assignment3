from __future__ import division

B = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]
H = [0.0, 14.7, 36.5, 71.7, 121.4, 197.4, 256.2, 348.7, 540.6, 1062.8, 2317.0, 4781.9, 8687.4, 13924.3, 22650.2]
A = 1e-4


class SlopeInterpolator:
    """
    Interpolator for the slope of the H-B curve.
    """

    def __init__(self):
        self.slopes = []
        for i in range(len(B) - 1):
            h_slope = (H[i + 1] - H[i]) / (B[i + 1] - B[i])
            self.slopes.append(h_slope)

    def evaluate_flux(self, flux):
        b = flux / A
        return self.evaluate_b(b)

    def evaluate_b(self, b):
        if b > B[-1]:
            return self.slopes[-1]
        elif b < B[0]:
            return self.slopes[0]
        for i in range(len(B) - 1):
            if B[i] <= b <= B[i + 1]:
                return self.slopes[i]
        return None
