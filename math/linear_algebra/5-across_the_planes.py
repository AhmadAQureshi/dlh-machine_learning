#!/usr/bin/env python3
"""Module performs matrix addition."""


def add_matrices2D(mat1, mat2):
    if len(mat1) != len(mat2):
        return None
    else:
        for i in range(len(mat1)):
            if len(mat1[i]) != len(mat2[i]):
                return None

    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[i]))]
            for i in range(len(mat1))]
