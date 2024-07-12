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
    dynamic = [float('inf')] * (total + 1)
    dynamic[0] = 0
    
    for i in range(1, total + 1):
        for coin in coins:
            if coin > i:
                break
            dynamic[i] = min(dynamic[i], dynamic[i - coin] + 1)
    
    return -1 if dynamic[total] == float('inf') else dynamic[total]
