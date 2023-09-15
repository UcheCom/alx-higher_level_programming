#!/usr/bin/python3

import sys

"""Defines function to solve the n queens puzzle
"""


def queens_safe(n, brd, row, col):
    """This solves the n queens problem recursively
       Args:
           n: size of the chess
         brd: chess board
         row: rows in chess
         col: columns in chess
       Return:
            The list of correct queens position
    """

    for i in range(row):
        if brd[i][col] == 'Q':
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if brd[i][j] == 'Q':
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if brd[i][j] == 'Q':
            return False

    return True


def Queens_solution(n):
    """Prints solutions for n queens problems
       Args:
           n: chess size
       Returns:
              None
    """
    def backtrack(row):
        if row == n:
            sols.append(["".join(row) for row in brd])
            return

        for col in range(n):
            if queens_safe(n, brd, row, col):
                brd[row][col] = 'Q'
                backtrack(row + 1)
                brd[row][col] = '.'

    brd = [['.' for _ in range(n)] for _ in range(n)]
    sols = []
    backtrack(0)

    for solution in sols:
        for row in solution:
            print(row)
        print()

if __name__ == "__main__":


    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    Queens_solution(N)
