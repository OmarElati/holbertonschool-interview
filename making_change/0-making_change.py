#!/usr/bin/python3
""" Change comes from within """
from collections import deque


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest number
    of coins needed to meet a given amount total.
    """
    if total < 1:
        return 0

    queue = deque([(0, 0)])
    visited = set([0])

    while queue:
        current_amount, num_coins = queue.popleft()

        for coin in coins:
            next_amount = current_amount + coin

            if next_amount == total:
                return num_coins + 1

            if next_amount < total and next_amount not in visited:
                visited.add(next_amount)
                queue.append((next_amount, num_coins + 1))

    return -1
