#!/usr/bin/python3
""" Module for gettibg minoperations"""


def minOperations(n):
    """
    min-Operations
    Gets fewest # of operations needed to result in n characters
    """
    if (n < 2):
        return 0
    oprs, root = 0, 2
    while root <= n:
        if n % root == 0:
            oprs += root
            n = n / root
            root -= 1
        root += 1
    return oprs
