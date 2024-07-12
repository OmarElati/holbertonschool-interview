#!/usr/bin/python3
""" 0. Change comes from within """


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest number
    of coins needed to meet a given amount total.
    """
    if total < 1:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
