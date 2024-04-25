#!/usr/bin/python3
"""
Module to calculate the minimum operation required for a given task
"""


def minOperations(n):
    """
    Method to calculate the minimum operations required to
    reach n characters in a file, using only two operations:
    Copy All and Paste.

    Args:
        n (int): the number to calculate the minimum operation required for.

    Returns:
        The minimum operations required for a given task.
    """
    if n <= 1:
        return 0

    # using Prime Factorization algorithm
    opr_count = 0
    div = 2

    while div * div <= n:
        while n % div == 0:
            opr_count += div
            n = n // div
        div += 1

    if n > 1:
        opr_count += n

    return opr_count
