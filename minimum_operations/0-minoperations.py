#!/usr/bin/python3
"""Minimum Operations."""


def minOperations(n):
    """
    calculates the fewest number of operations needed
    to result in exactly n H characters in the file
    """
    if n <= 1:
        return 0

    total = 0
    divider = 2

    while n > 1:

        # Check if divider is a factor of n
        # At first if 2 is a factor, then divider is incremented
        while n % divider == 0:
            total += divider
            n = n // divider

        divider += 1

    return total


if __name__ == "__main__":

    n = 4
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 130
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
