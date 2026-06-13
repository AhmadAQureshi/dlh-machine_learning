#!/usr/bin/env python3
"""Task03-Initialize Exponential"""


class Exponential:
    """Exponential distribution"""
    def __init__(self, data=None, lambtha=1.):
        """Class constructor for Exponential distribution"""
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if type(data) is not list:
                raise ValueError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(1 / (sum(data) / len(data)))
