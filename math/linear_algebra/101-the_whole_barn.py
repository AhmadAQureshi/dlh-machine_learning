#!/usr/bin/env python3
"""Add matrices of the same dimension."""


def add_matrices(mat1, mat2):
    """Add two matrices of the same dimension."""
    if type(mat1) is not type(mat2):
        return None

    if isinstance(mat1, list) and isinstance(mat2, list):
        if len(mat1) != len(mat2):
            return None

        result = []

        for i in range(len(mat1)):
            added = add_matrices(mat1[i], mat2[i])

            if added is None:
                return None

            result.append(added)

        return result

    return mat1 + mat2