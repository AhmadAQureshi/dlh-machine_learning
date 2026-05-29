#!/usr/bin/env python3
"""Module for calculating the inverse matrix of a matrix."""


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

    augmented = []

    for row in range(size):
        identity_row = [0] * size
        identity_row[row] = 1
        augmented.append(matrix[row][:] + identity_row)

    for col in range(size):
        pivot_row = col

        while pivot_row < size and augmented[pivot_row][col] == 0:
            pivot_row += 1

        if pivot_row == size:
            return None

        if pivot_row != col:
            augmented[col], augmented[pivot_row] = (
                augmented[pivot_row],
                augmented[col]
            )

        pivot = augmented[col][col]

        for j in range(2 * size):
            augmented[col][j] /= pivot

        for row in range(size):
            if row != col:
                factor = augmented[row][col]

                for j in range(2 * size):
                    augmented[row][j] -= factor * augmented[col][j]

    return [row[size:] for row in augmented]
