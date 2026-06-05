#!/usr/bin/env python3
"""Task9-calculatin the sum of squares."""


def summation_i_squared(n):
    """Returns the sum of i^2 from i=1 to n."""
    if not isinstance(n, (int, float)) or n < 1:
        return None

    n = int(n)
    return n * (n + 1) * (2 * n + 1) // 6
