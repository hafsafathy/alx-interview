#!/usr/bin/python3
"""unlock list of lists"""


def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened
    """

    keys = [0]
    for key in keys:
        for boxKey in boxes[key]:
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)
    if len(keys) == len(boxes):
        return True
    return False
