#!/usr/bin/python3
"""
Defines a function to rotate a 2D NxN matrix 90 degrees clockwise in place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D NxN matrix 90 degrees clockwise in place.

    Parameters:
        matrix (list of lists of ints): The matrix to rotate.
            Assumed to have 2 dimensions and will not be empty.
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
