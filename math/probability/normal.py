#!/usr/bin/env python3
"""Task06-Initialize Normal"""


class Normal:
    """Represents a normal distribution"""
    def __init__(self, data=None, mean=0., stddev=1.):
        """Class constructor for Normal distribution"""
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = float(sum(data) / len(data))
            self.stddev = float((sum([(x - self.mean) ** 2 for x in data])
                                 / len(data)) ** 0.5)

    def z_score(self, x):
        """Calculating the z-score of a given x-value"""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculating the x-value of a given z-score"""
        return (z * self.stddev) + self.mean

    def pdf(self, x):
        """Calculating the value of the PDF for a given x-value"""
        return (1 / (self.stddev * (2 * 3.141592653589793) ** 0.5)) * \
               (2.718281828459045 ** (-0.5 * ((x - self.mean)
                                              / self.stddev) ** 2))

    def pdf(self, x):
        """Calculating the value of the PDF for a given x-value"""
        return (1 / (self.stddev * (2 * 3.141592653589793) ** 0.5)) * \
               (2.718281828459045 ** (-0.5 * ((x - self.mean)
                                              / self.stddev) ** 2))

    def cdf(self, x):
        """Calculating the value of the CDF for a given x-value"""
        pi = 3.1415926536

        z = (x - self.mean) / (self.stddev * (2 ** 0.5))

        erf = (2 / (pi ** 0.5)) * (
            z - (z ** 3) / 3 + (z ** 5) / 10 -
            (z ** 7) / 42 + (z ** 9) / 216
        )

        return 0.5 * (1 + erf)
