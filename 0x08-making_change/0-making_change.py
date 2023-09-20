#!/usr/bin/python3
"""Making Change"""


def makeChange(coins, total):
    """A function that determines the fewest number of coins needed to
    meet a given amount"""
    if total < 0:
        return -1

    # Initialize a list to store the minimum number of
    # coins needed for each amount from 0 to total.
    # Set all values to float('inf') initially, except for s[0] which is 0.
    s = [float('inf')] * (total + 1)
    s[0] = 0

    for coin_val in coins:
        for i in range(coin_val, total + 1):
            # Calculate the minimum number of coins needed
            # for amount 'i' by considering the current coin.
            s[i] = min(s[i], 1 + s[i - coin_val])

    # If s[total] is still float('inf'), it means the total
    # cannot be met by any combination of coins.
    return -1 if s[total] == float('inf') else s[total]
