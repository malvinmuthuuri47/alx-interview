#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, amount):
    """This function determines the fewest number of coins needed
    to meet a given amount

    Args:
        coins: A list of coins which are just numbers in a list
        total: The total amount to be obtained by the coins

    Returns:
        - The fewest number of coins that add up to the total
    """
    if amount == 0 or coins is None or len(coins) == 0:
        return 0

    dp = [0] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if i == coin:
                dp[i] = 1
            elif dp[i] == 0 and dp[i - coin] != 0:
                dp[i] = dp[i - coin] + 1
            elif dp[i - coin] != 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return -1 if dp[amount] == 0 else dp[amount]
