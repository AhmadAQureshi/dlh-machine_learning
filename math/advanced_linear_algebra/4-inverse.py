#!/usr/bin/env python3
"""Module for calculating the inverse matrix of a matrix."""


def determinant(matrix):
    """Calculate the determinant of a square matrix."""
    size = len(matrix)

    if size == 1:
        return matrix[0][0]

    if size == 2:
        return (
            matrix[0][0] * matrix[1][1]
            - matrix[0][1] * matrix[1][0]
        )

    det = 0

    for col in range(size):
        minor = minor_matrix(matrix, 0, col)
        det += ((-1) ** col) * matrix[0][col] * determinant(minor)

    return det


def minor_matrix(matrix, row_to_remove, col_to_remove):
    """Return the minor matrix of a matrix."""
    minor = []

    for row in range(len(matrix)):
        if row == row_to_remove:
            continue

        minor_row = []

        for col in range(len(matrix)):
            if col != col_to_remove:
                minor_row.append(matrix[row][col])

        minor.append(minor_row)

    return minor


def inverse(matrix):
    """Calculate the inverse of a matrix."""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if len(matrix) == 0:
        raise ValueError("matrix must be a non-empty square matrix")

    size = len(matrix)

    if not all(len(row) == size for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    det = determinant(matrix)

    if det == 0:
        return None

    if size == 1:
        return [[1 / det]]

    inverse_matrix = []

    for row in range(size):
        inverse_row = []

        for col in range(size):
            minor = minor_matrix(matrix, col, row)
            cofactor = ((-1) ** (row + col)) * determinant(minor)
            inverse_row.append(cofactor / det)

        inverse_matrix.append(inverse_row)

    return inverse_matrix
