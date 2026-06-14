#!/usr/bin/env python3
"""Task12-Binomial CDF"""


class Binomial:
    """Calculates a binomial distribution"""
    def __init__(self, data=None, n=1, p=0.5):
        """Initializes a Binomial distribution"""
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            mean = sum(data) / len(data)
            variance = sum([(x - mean) ** 2 for x in data]) / len(data)

            self.p = 1 - (variance / mean)
            self.n = round(mean / self.p)
            self.p = mean / self.n

    def pmf(self, k):
        """Calculates the value of the PMF for a given number of successes"""
        k = int(k)

        if k < 0 or k > self.n:
            return 0

        n_factorial = 1
        k_factorial = 1
        n_minus_k_factorial = 1

        for i in range(1, self.n + 1):
            n_factorial *= i

        for i in range(1, k + 1):
            k_factorial *= i

        for i in range(1, self.n - k + 1):
            n_minus_k_factorial *= i

        combination = n_factorial / (k_factorial * n_minus_k_factorial)

        return combination * (self.p ** k) * ((1 - self.p) ** (self.n - k))
    
    def cdf(self, k):
        """Calculates the value of the CDF for a given number of successes"""
        k = int(k)

        if k < 0:
            return 0
        if k >= self.n:
            return 1

        cdf_value = 0
        for i in range(k + 1):
            cdf_value += self.pmf(i)

        return cdf_value
