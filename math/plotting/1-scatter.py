#!/usr/bin/env python3
"""Task01-Scatter plot"""

import numpy as np
import matplotlib.pyplot as plt


def scatter():
    """Scatter plot"""
    mean = [69, 0]
    cov = [[15, 8], [8, 15]]

    np.random.seed(5)
    x, y = np.random.multivariate_normal(mean, cov, 2000).T
    y += 180

    plt.scatter(x, y, c='magenta')
    plt.xlabel('Height (in)')
    plt.ylabel('Weight (lbs)')
    plt.title('Men\'s Height vs Weight')
    plt.show()


if __name__ == "__main__":
    scatter()
