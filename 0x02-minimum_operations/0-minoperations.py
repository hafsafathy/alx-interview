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

    nw = 1
    start = 0
    c = 0
    while nw < n:
        remainder = n - now
        if (remainder % now == 0):
            start = nw
            nw += start
            c += 2
        else:
            nw += start
            c += 1
    return c
