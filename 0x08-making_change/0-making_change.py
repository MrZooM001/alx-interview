#!/usr/bin/python3
"""Module to solve making change challenge"""
from collections import deque


def makeChange(coins, total):
    """
    determine the fewest number of coins
    needed to meet a given amount

    Arguments:
        coins (list[int]): List of coin denominations.
        total (int): Amount to make change for.
    """
    if total <= 0:
        return 0

    qu = deque([(0, 0)])
    marked = set([0])

    while qu:
        current_total, num_coins = qu.popleft()
        for coin in coins:
            new_total = current_total + coin
            if new_total == total:
                return num_coins + 1

            if new_total < total and new_total not in marked:
                marked.add(new_total)
                qu.append((new_total, num_coins + 1))
    return -1
