#!/usr/bin/env python3
"""8-ridin_bareback.py"""

import numpy as np

def mat_mul(mat1, mat2):
    """Multiplies two matrices using numpy"""
    if np.array(mat1).shape[1] != np.array(mat2).shape[0]:
        return None
    else:
        mat_mul = np.matmul(mat1, mat2)
    return np.matmul(mat1, mat2)