#!/usr/bin/env python3
"""Module adds element-wise"""


def add_arrays(arr1, arr2):
"""Add two matrices element by element."""
    if len(arr1) != len(arr2):
        return None
    else:
        return [arr1[i] + arr2[i] for i in range(len(arr1))]
