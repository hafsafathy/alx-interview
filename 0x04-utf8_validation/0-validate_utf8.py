#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    method that determines if a given data set represents a valid UTF-8 encoding.
    """

    numby = 0
    n1 = 1 << 7
    n2 = 1 << 6

    for i in data:

        mskby = 1 << 7

        if numby == 0:

            while mskby & i:
                numby += 1
                mskby = mskby >> 1

            if numby == 0:
                continue

            if numby == 1 or numby > 4:
                return False
        else:
            if not (i & n1 and not (i & n2)):
                return False

        numby -= 1

    if numby == 0:
        return True

    return False

