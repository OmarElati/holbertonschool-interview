#!/usr/bin/python3
"""
Defines a function that determines the winner after a certain number of rounds
of playing the Prime Game.
"""

def isWinner(x, nums):
    """
    Determines the winner after a certain
    number of rounds of playing the Prime Game.
    Maria and Ben take turns choosing primes,
    and the one who can't choose loses.

    Parameters:
    - x: int - the number of rounds
    - nums: list of int - list of n values for each round
    
    Returns:
    - Name of the player who won the most rounds ("Maria" or "Ben")
    - None if there's no clear winner
    """
    if not nums or x < 1:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    Maria_wins = 0
    Ben_wins = 0

    for n in nums:
        primes_count = sum(primes[0:n+1])

        if primes_count % 2 == 1:
            Maria_wins += 1
        else:
            Ben_wins += 1

    if Maria_wins > Ben_wins:
        return "Maria"
    elif Ben_wins > Maria_wins:
        return "Ben"
    else:
        return None


def sieve_of_eratosthenes(n):
    """
    Generate a boolean list of primes up to a given
    number n using the Sieve of Eratosthenes.
    
    Parameters:
    - n: int - the upper limit for primes
    
    Returns:
    - List where index i is True if i is prime, False otherwise
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    return primes
