#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def line():

    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))
    plt.plot(y, label='y = x^3')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
if __name__ == "__main__":
    line()
