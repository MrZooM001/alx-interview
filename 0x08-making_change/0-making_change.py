#!/usr/bin/python3
"""Module to rotate a 2D matrix"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    dynamic = [float('inf')] * (total + 1)
    dynamic[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dynamic[amount] = min(dynamic[amount], dynamic[amount - coin] + 1)

    return dynamic[total] if dynamic[total] != float('inf') else -1
