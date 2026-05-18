#!/usr/bin/env python3
"""Element-wise matrix operations without NumPy."""


def np_elementwise(mat1, mat2):
    """Return element-wise sum, difference, product and quotient."""
    add = []
    sub = []
    mul = []
    div = []

    for i in range(len(mat1)):
        add_row = []
        sub_row = []
        mul_row = []
        div_row = []

        for j in range(len(mat1[i])):
            add_row.append(mat1[i][j] + mat2[i][j])
            sub_row.append(mat1[i][j] - mat2[i][j])
            mul_row.append(mat1[i][j] * mat2[i][j])
            div_row.append(mat1[i][j] / mat2[i][j])

        add.append(add_row)
        sub.append(sub_row)
        mul.append(mul_row)
        div.append(div_row)

    return add, sub, mul, div
