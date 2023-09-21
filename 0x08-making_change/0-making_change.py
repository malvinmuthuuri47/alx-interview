#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """This function determines the fewest number of coins needed
    to meet a given amount

    Args:
        coins: A list of coins which are just numbers in a list
        total: The total amount to be obtained by the coins

    Returns:
        - The fewest number of coins that add up to the total
    """

    if total <= 0:
        return 0

    # Sort the array of coins in decresing order
    coins.sort(reverse=True)

    # Initialize variables
    num_coins = 0
    remaining_total = total

    # Iterate through each denomination of coin
    for coin in coins:
        while remaining_total >= coin:
            remaining_total -= coin
            num_coins += 1

    # If remaining_total becomes 0, return the no. of coins used
    if remaining_total == 0:
        return num_coins
    else:
        return -1  # Cannot make the total with the given coins
