class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients
        self.order = len(coefficients) - 1

    def __getitem__(self, item):
        return self.coefficients[item]

    def __add__(self, other):
        result_coefficients = []
        common_order = min(self.order, other.order)
        for i in range(common_order + 1):
            result_coefficients.append(self[i] + other[i])
        if self.order > other.order:
            for i in range(common_order + 1, self.order + 1):
                result_coefficients.append(self[i])
        elif other.order > self.order:
            for i in range(common_order + 1, other.order + 1):
                result_coefficients.append(other[i])
        return Polynomial(result_coefficients)

    def __sub__(self, other):
        result_coefficients = []
        common_order = min(self.order, other.order)
        for i in range(common_order + 1):
            result_coefficients.append(self[i] - other[i])
        if self.order > other.order:
            for i in range(common_order + 1, self.order + 1):
                result_coefficients.append(self[i])
        elif other.order > self.order:
            for i in range(common_order + 1, other.order + 1):
                result_coefficients.append(-other[i])
        return Polynomial(result_coefficients)

    def __mul__(self, other):
        result_coefficients = []
        max_result_order = self.order + other.order
        for result_order in range(max_result_order + 1):
            coefficient = 0
            for order1 in range(self.order + 1):
                for order2 in range(other.order + 1):
                    if order1 + order2 == result_order:
                        coefficient += self[order1] * other[order2]
            result_coefficients.append(coefficient)
        return Polynomial(result_coefficients)

    def scalar_multiply(self, scalar):
        return Polynomial([scalar * coefficient for coefficient in self.coefficients])
