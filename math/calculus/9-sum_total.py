#!/usr/bin/env python3
"""Task9-calculating the sum of squares."""


def summation_i_squared(n):
    """Return the sum of squares from 1 to n."""
    if type(n) is not int or n < 1:
        return None

    return sum(i ** 2 for i in range(1, n + 1))
