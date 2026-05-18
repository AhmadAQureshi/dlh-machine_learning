#!/usr/bin/env python3
import numpy as np


def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenates two 2D matrices along a specific axis"""
    if axis == 0 or axis == 1:
        return np.concatenate((mat1, mat2), axis=axis)
    else:
        return None
