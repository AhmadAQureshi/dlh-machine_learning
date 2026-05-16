#!/usr/bin/env python3
"""Slice Like A Ninja module."""


def np_slice(matrix, axes={}):
    """Slice a matrix along specific axes."""
    slices = [slice(None)] * matrix.ndim

    for axis, value in axes.items():
        slices[axis] = slice(*value)

    return matrix[tuple(slices)]