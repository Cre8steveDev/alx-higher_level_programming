#!/usr/bin/python3

import sys
"""N Queens Advanced Task"""


def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def print_solution(board):
    for row, col in enumerate(board):
        print("[{}, {}]".format(row, col), end=' ')
    print()


def solve_nqueens(n, board, row=0):
    if row == n:
        print_solution(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(n, board, row + 1)


def main():
    # Check for the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is greater or equal to 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve_nqueens(n, board)


if __name__ == "__main__":
    main()
