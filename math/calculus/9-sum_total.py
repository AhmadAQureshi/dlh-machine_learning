#!/usr/bin/env python3
"""Task9-calculating the sum of squares."""


def summation_i_squared(n):
    """Return the sum of squares from 1 to n.

    If n is not a valid positive integer, return None.
    """
    if not isinstance(n, int) or n < 1:
        return None

    if n == 1:
        return 1

    return n ** 2 + summation_i_squared(n - 1)