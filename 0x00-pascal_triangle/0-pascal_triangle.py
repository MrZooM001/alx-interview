#!/usr/bin/python3
"""
Module to implement Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle up to row n.

    Args:
        n (int): the row of the triangle to return.

    Returns:
        a list of lists representing Pascal's triangle up to row n.
    """
    if not isinstance(n, int) or n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        try:
            previous_row = triangle[-1]
            new_row = [1]
            for j in range(1, i):
                new_row.append(previous_row[j - 1] + previous_row[j])
            new_row.append(1)
            triangle.append(new_row)
        except Exception as e:
            print("Error:", e)
            return []

    return triangle
