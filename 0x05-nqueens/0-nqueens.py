#!/usr/bin/python3
""" N queens """
import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])


def queensgame(n, i=0, a=[], b=[], c=[]):
    """ find positions """
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from queensgame(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def solvig(n):
    """ solve """
    h = []
    i = 0
    for solution in queensgame(n, 0):
        for s in solution:
            h.append([i, s])
            i += 1
        print(h)
        h = []
        i = 0


solvig(n)
