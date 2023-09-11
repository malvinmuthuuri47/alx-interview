#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """This function transposes a Matrix and then reverses the order
    of the columns to complete the rotation

    Returns:
        - A matrix rotated at 90 degrees clockwise
    """
    # Transpose
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse
    N = len(matrix)
    for i in range(N // 2):
        for j in range(N):
            matrix[j][i], matrix[j][N-1-i] = matrix[j][N-1-i], matrix[j][i]
    return matrix
