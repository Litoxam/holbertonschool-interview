#!/usr/bin/python3
"""
Return the minimum number of coins needed to make a total.
"""


def makeChange(coins, total):
    """
    Return the fewest number of coins needed.
    """

    if total <= 0:
        return 0

    # Store the minimum number of coins for each amount
    min_coins = [total + 1] * (total + 1)
    min_coins[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                if min_coins[amount - coin] + 1 < min_coins[amount]:
                    min_coins[amount] = min_coins[amount - coin] + 1

    # If the total cannot be reached, return -1
    if min_coins[total] == total + 1:
        return -1

    return min_coins[total]
