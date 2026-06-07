#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def two():

    x = np.arange(0, 21000, 1000)
    r = np.log(0.5)
    t1 = 5730
    t2 = 1600
    y1 = np.exp((r / t1) * x)
    y2 = np.exp((r / t2) * x)
    plt.figure(figsize=(6.4, 4.8))
    plt.plot(x, y1, label='C-14')
    plt.plot(x, y2, label='Ra-226')
    plt.yscale('linear')
    xticks = [0, 2500, 5000, 7500, 10000, 12500, 15000, 17500, 20000]
    plt.xticks(xticks)
    yticks = [0.0, 0.25, 0.5, 0.75, 1.0]
    plt.xlabel('Time (years)')
    plt.ylabel('Fraction Remaining')
    plt.title('Exponential Decay of Radioactive Elements')
    plt.legend()
    plt.show()
if __name__ == "__main__":
    two()