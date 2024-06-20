#!/usr/bin/python3
"""Module for solving Prime Game algorithms"""


def sieve(n):
    """Generate list of primes up to n using the Sieve of Eratosthenes."""
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    is_prime[0], is_prime[1] = False, False
    primes = [p for p in range(n + 1) if is_prime[p]]

    return primes


def isWinner(x, numbers):
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
    if x < 1 or not numbers:
        return None

    max_num = max(numbers)
    primes = sieve(max_num)

    maria = 0
    ben = 0

    for n in numbers:
        if n == 1:
            ben += 1
            continue

        available = [True] * (n + 1)
        available[0] = available[1] = False

        turn = 0

        while True:
            move_made = False
            for prime in primes:
                if prime > n:
                    break
                if available[prime]:
                    move_made = True
                    for multiple in range(prime, n + 1, prime):
                        available[multiple] = False
                    break
            if not move_made:
                break
            turn += 1

        if turn % 2 == 0:
            ben += 1
        else:
            maria += 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None
