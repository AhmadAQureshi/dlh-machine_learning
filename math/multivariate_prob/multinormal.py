#!/usr/bin/env python3
"""Defines the MultiNormal class."""

import numpy as np


class MultiNormal:
    """Represents a multivariate normal distribution."""

    def __init__(self, data):
        """Initializes a multivariate normal distribution."""
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        d, n = data.shape

        if n < 2:
            raise ValueError("data must contain multiple data points")

        self.mean = np.mean(data, axis=1, keepdims=True)

        centered = data - self.mean
        self.cov = centered @ centered.T / (n - 1)

    def pdf(self, x):
        """Calculates the PDF at a data point."""
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")

        d = self.mean.shape[0]

        if x.shape != (d, 1):
            raise ValueError("x must have the shape ({}, 1)".format(d))

        diff = x - self.mean

        exponent = -0.5 * (
            diff.T @ np.linalg.inv(self.cov) @ diff
        )

        pdf = np.exp(exponent) / np.sqrt(
            ((2 * np.pi) ** d) * np.linalg.det(self.cov)
        )

        return pdf[0][0]
