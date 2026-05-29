#!/usr/bin/env python3
"""Minor: Calculate the minor matrix of a non-empty square matrix."""


def minor(matrix):
    """Calculate the minor matrix of a non-empty square matrix."""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if not matrix or not matrix[0]:
        raise ValueError("matrix must be a non-empty square matrix")

    if not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    if len(matrix) == 1:
        return [[1]]

    minor_matrix = []

    for i in range(len(matrix)):
        minor_row = []

        for j in range(len(matrix)):
            submatrix = [
                row[:j] + row[j + 1:]
                for row in matrix[:i] + matrix[i + 1:]
            ]

            minor_row.append(determinant(submatrix))

        minor_matrix.append(minor_row)

    return minor_matrix


def determinant(matrix):
    """Calculate the determinant of a square matrix."""
    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0

    for j in range(len(matrix)):
        submatrix = [
            row[:j] + row[j + 1:]
            for row in matrix[1:]
        ]

        det += (-1) ** j * matrix[0][j] * determinant(submatrix)

    return det
