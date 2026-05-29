#!/usr/bin/env python3
"""Module for calculating the adjugate matrix of a matrix."""


def determinant(matrix):
    """Calculate the determinant of a square matrix using Bareiss algorithm."""
    size = len(matrix)

    if size == 1:
        return matrix[0][0]

    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    mat = [row[:] for row in matrix]
    sign = 1
    previous = 1

    for col in range(size - 1):
        if mat[col][col] == 0:
            swap_row = col + 1

            while swap_row < size and mat[swap_row][col] == 0:
                swap_row += 1

            if swap_row == size:
                return 0

            mat[col], mat[swap_row] = mat[swap_row], mat[col]
            sign *= -1

        pivot = mat[col][col]

        for row in range(col + 1, size):
            for inner_col in range(col + 1, size):
                mat[row][inner_col] = (
                    mat[row][inner_col] * pivot
                    - mat[row][col] * mat[col][inner_col]
                ) // previous

        previous = pivot

        for row in range(col + 1, size):
            mat[row][col] = 0

    return sign * mat[size - 1][size - 1]


def minor_matrix(matrix, row_to_remove, col_to_remove):
    """Return the minor matrix after removing one row and one column."""
    return [
        [
            matrix[row][col]
            for col in range(len(matrix))
            if col != col_to_remove
        ]
        for row in range(len(matrix))
        if row != row_to_remove
    ]


def adjugate(matrix):
    """Calculate the adjugate matrix of a matrix."""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if len(matrix) == 0:
        raise ValueError("matrix must be a non-empty square matrix")

    size = len(matrix)

    if not all(len(row) == size for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    if size == 1:
        return [[1]]

    return [
        [
            ((-1) ** (row + col))
            * determinant(minor_matrix(matrix, row, col))
            for row in range(size)
        ]
        for col in range(size)
    ]