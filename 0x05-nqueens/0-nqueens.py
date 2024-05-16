#!/usr/bin/python3
"""Program to solve N-Queens puzzle"""
import sys


def is_safe_possition(board, row, col):
    """
    Check if the given position is safe to place the queen on the board.

    Arguments:
        board (list[list[int]]): The current state of the chessboard,
        1 represents a queen, 0 represents an empty cell.
        row (int): The row index where the queen will be placed.
        col (int): The column index where the queen will be placed.

    Returns:
        bool: True if it is safe position, False otherwise.
    """
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True


def n_queens_solution(board, row, n):
    """
    Solve the N-Queens puzzle on a given chessboard.

    Arguments:
        board (list[list[int]]): The current state of the chessboard,
        1 represents a queen, 0 represents an empty cell.
        row (int): The current row index where the queen will be placed.
        n (int): The size of the chessboard.

    Returns:
        bool: True if a solution is found, False otherwise.
    """
    if row == n:
        for i, row in enumerate(board):
            for col, val in enumerate(row):
                if val == 1:
                    print([i, col], end=" ")
        print()
        return True

    for col in range(n):
        if is_safe_possition(board, row, col):
            board[row][col] = 1
            n_queens_solution(board, row + 1, n)
            board[row][col] = 0


def n_queens(n):
    """
    Solves the N-Queens puzzle by placing N non-attacking queens
    on an N*N chessboard.

    Arguments:
        n (str): A string representing the size of the chessboard.
        It must be a number and at least 4.
    """
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(n)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * n for _ in range(n)]
    n_queens_solution(board, 0, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    n_queens(sys.argv[1])
