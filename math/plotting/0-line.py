#!/usr/bin/env python3
"""Task00-Line plot"""

import numpy as np
import matplotlib.pyplot as plt


def line():
    """Line plot"""
    y = np.arange(0, 11) ** 3

    plt.plot(y, 'r')
    plt.xlim(0, 10)
    plt.show()


if __name__ == "__main__":
    line()
