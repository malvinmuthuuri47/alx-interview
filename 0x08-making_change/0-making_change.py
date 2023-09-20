#!/usr/bin/python3
"""Making Change"""


def makeChange(coins, total):
    """A function that determines the fewest number of coins needed to
    meet a given amount"""
    s = [0]
    for i in range(1, total+1):
        s.append(-1)
        for coin_val in coins:
            if i-coin_val >= 0 and \
                    s[i-coin_val] != -1 and \
                    (s[i] > s[i-coin_val] or
                        s[i] == -1):
                s[i] = 1 + s[i-coin_val]

    return s[total]
