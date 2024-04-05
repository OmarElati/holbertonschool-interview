#!/usr/bin/python3
"""
Description: The N queens puzzle is a classic problem in chess where N queens
must be placed on an N×N chessboard such that no two queens threaten each other
This program aims to solve the N queens problem.
Usage: nqueens N:
       If the program is called with an incorrect number
       of arguments, it prints "Usage: nqueens N" followed
       by a new line and exits with a status of 1.
where N must be an integer greater than or equal to 4:
       If N is not an integer, it prints "N must be a number"
       followed by a new line and exits with a status of 1.
       If N is smaller than 4, it prints "N must be at least 4
       " followed by a new line and exits with a status of 1.
The program should print every possible solution to the problem:
       Each solution is printed on a separate line.
       Format: see example.
       Solutions do not need to be printed in a specific order.
You are only allowed to import the sys module.
"""
import sys


def print_solution(board):
    """Prints the solution in the specified format."""
    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                solution.append([row, col])
                break
    print(solution)


def is_safe(board, row, col):
    """Check if placing a queen at board[row][col] is safe."""
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col):
    """Recursively solves the N queens problem."""
    if col >= len(board):
        print_solution(board)
        return True

    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1) or res
            board[i][col] = 0

    return res


def solve_nqueens(n):
    """Solves the N queens problem."""
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * n for _ in range(n)]
    if not solve_nqueens_util(board, 0):
        print("No solution exists")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    solve_nqueens(n)
