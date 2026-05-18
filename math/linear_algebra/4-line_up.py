#!/usr/bin/env python3
#!/usr/bin/python3
"""This module contains a function that adds two 2D matrices."""


def add_matrices2D(mat1, mat2):
    """Add two matrices element by element."""
    if len(arr1) != len(arr2):
        return None
    else:
        return [arr1[i] + arr2[i] for i in range(len(arr1))]
