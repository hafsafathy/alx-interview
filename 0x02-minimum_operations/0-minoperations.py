#!/usr/bin/python3

"""
    method that calculates the fewest number of operations needed to result in exactly n H characters in the file
"""


def minOperations(n):
    """
        A function that calculates the fewest number of operations
        needed to give a result of exactly n H characters in a file
        args: n: Number of characters to be displayed
        return:
               an integer
    """

    number = n
    x = 2
    cnt = 0

    while (number > 1):
        if number % x == 0:
            number = int(number / x)
            cnt += x
            x = 2
        else:
            x += 1

    return cnt
