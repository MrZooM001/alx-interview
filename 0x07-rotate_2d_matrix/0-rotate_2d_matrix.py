#!/usr/bin/python3
"""Module to rotate a 2D matrix"""


def rotate_2d_matrix(matrix):
    """
    Rotate an n x n 2D matrix, rotate it 90 degrees clockwise.

    Arguments:
        matrix (list[list]): List of lists representing the given matrix
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
