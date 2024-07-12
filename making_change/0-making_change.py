#!/usr/bin/python3
""" Change comes from within """


def makeChange(coins: list, total: int) -> int:
    """
    Given a pile of coins of different values, determine the fewest number
    of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    inf = float('inf')
    cache = [0] + [inf] * total

    for i in range(len(cache)):
        for coin in coins:
            if coin <= i:
                cache[coin] = min(cache[i - coin], cache[coin])

    if cache[total] != inf:
        return cache[total]

    return -1
