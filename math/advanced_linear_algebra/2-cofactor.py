#!/usr/bin/env python3
"""Module for calculating the cofactor matrix of a matrix."""


def determinant(matrix):
    """Calculate the determinant of a square matrix."""
    size = len(matrix)

    if size == 1:
        return matrix[0][0]

    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for col in range(size):
        minor = []
        for row in range(1, size):
            minor_row = []
            for c in range(size):
                if c != col:
                    minor_row.append(matrix[row][c])
            minor.append(minor_row)

        det += ((-1) ** col) * matrix[0][col] * determinant(minor)

    return det


def minor_matrix(matrix, row_to_remove, col_to_remove):
    """Return the minor matrix after removing one row and one column."""
    minor = []

    for row_index in range(len(matrix)):
        if row_index == row_to_remove:
            continue

        row = []
        for col_index in range(len(matrix)):
            if col_index != col_to_remove:
                row.append(matrix[row_index][col_index])

        minor.append(row)

    return minor


def cofactor(matrix):
    """Calculate the cofactor matrix of a matrix."""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if len(matrix) == 0:
        raise ValueError("matrix must be a non-empty square matrix")

    size = len(matrix)

    if not all(len(row) == size for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    size = len(matrix)

    if not all(len(row) == size for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    if size == 1:
        return [[1]]

    cofactors = []

    for row in range(size):
        cofactor_row = []

        for col in range(size):
            minor = minor_matrix(matrix, row, col)
            value = ((-1) ** (row + col)) * determinant(minor)
            cofactor_row.append(value)

        cofactors.append(cofactor_row)

    return cofactors
