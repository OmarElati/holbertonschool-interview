#!/usr/bin/python3
"""
Defines function that determines the fewest number of coins to make change
"""

def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total

    parameters:
        coins [list of positive ints]:
            the values of the coins in your possession
            you can assume you have an infinite number of coins of all values
        total [int]:
            total amount of change to make
            if total is 0 or less, return 0

    returns:
        the fewest number of coins to make the change
        or -1 if the total change cannot be made with the given coins
    """
    if total <= 0:
        return 0

    coins = sorted(coins)
    memo = {}

    def dp(n):
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        min_coins = float('inf')
        for coin in coins:
            if coin > n:
                break
            result = dp(n - coin)
            if result != -1:
                min_coins = min(min_coins, result + 1)
        memo[n] = -1 if min_coins == float('inf') else min_coins
        return memo[n]

    return dp(total)
