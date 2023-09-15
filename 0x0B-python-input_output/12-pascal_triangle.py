#!/usr/bin/python3
"""Defines a function that returns a list of lists
   of integers representing the Pascal's trinagle of n
"""


def pascal_triangle(n):
    """Returns the Pascal's triangle

       Args:
           n: integer
    """
    if n <= 0:
        return []

    tri = [[1]]
    for i in range(1, n):
        tmp = [1]
        for j in range(1, i):
            tmp.append(tri[i - 1][j - 1] + tri[i - 1][j])
        tmp.append(1)
        tri.append(tmp)

    return tri
