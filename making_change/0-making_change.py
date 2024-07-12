#!/usr/bin/python3
""" Change comes from within """
import heapq


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest number
    of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    heap = [(0, 0)]
    visited = set()

    while heap:
        num_coins, amount = heapq.heappop(heap)

        if amount == total:
            return num_coins

        if amount > total or (amount, num_coins) in visited:
            continue

        visited.add((amount, num_coins))

        for coin in coins:
            new_amount = amount + coin
            heapq.heappush(heap, (num_coins + 1, new_amount))

    return -1
