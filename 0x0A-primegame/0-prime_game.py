#!/usr/bin/python3
"""Module for solving Prime Game algorithms"""


def is_prime(num):
    """Helper function to determine if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def precompute_prime_counts(max_num):
    """Precompute the number of primes up to each number
    using dynamic programming."""
    prime_count = [0] * (max_num + 1)
    for i in range(2, max_num + 1):
        prime_count[i] = prime_count[i - 1]
        if is_prime(i):
            prime_count[i] += 1
    return prime_count


def isWinner(x, nums):
    """
    Determine the winner of the Prime Game.

    The game is played between Maria and Ben, with Maria going first.
    Each player takes turns selecting a number from the given list `nums`.
    The game continues until all numbers are selected.
    The player who selects the last prime number wins.

    Arguments:
        x (int): The number of rounds in the game.
        nums (List[int]): The list of numbers available for selection.

    Returns:
        str: The name of the winner ("Maria" or "Ben")
        or None if there is no winner.

    """
    if x < 1 or not nums:
        return None

    max_num = max(nums)
    prime_count = precompute_prime_counts(max_num)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
            continue

        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
