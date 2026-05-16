#!/usr/bin/env python3
"""Module for transposing a matrix."""


def matrix_transpose(matrix):
    """Return the transpose of a 2D matrix."""
    new_matrix = []

    for i in range(len(matrix[0])):
        row = []

        for j in range(len(matrix)):
            row.append(matrix[j][i])

        new_matrix.append(row)

    return new_matrix