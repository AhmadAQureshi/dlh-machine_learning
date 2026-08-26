#!/usr/bin/env python3
"""Calculates the posterior probability."""

import numpy as np


def posterior(x, n, P, Pr):
    """Calculate posterior probabilities given observed data."""
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    if not isinstance(x, int) or x < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0"
        )

    if x > n:
        raise ValueError("x cannot be greater than n")

    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")

    if not isinstance(Pr, np.ndarray) or Pr.shape != P.shape:
        raise TypeError(
            "Pr must be a numpy.ndarray with the same shape as P"
        )

    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")

    if np.any(Pr < 0) or np.any(Pr > 1):
        raise ValueError("All values in Pr must be in the range [0, 1]")

    if not np.isclose(np.sum(Pr), 1):
        raise ValueError("Pr must sum to 1")

    n_fact = 1
    x_fact = 1
    nx_fact = 1

    for i in range(1, n + 1):
        n_fact *= i

    for i in range(1, x + 1):
        x_fact *= i

    for i in range(1, n - x + 1):
        nx_fact *= i

    combination = n_fact / (x_fact * nx_fact)

    likelihood = combination * (P ** x) * ((1 - P) ** (n - x))

    intersection = likelihood * Pr

    marginal = np.sum(intersection)

    return intersection / marginal
