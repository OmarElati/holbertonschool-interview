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


def nqueen(t_arr, arr, col, i, n):
    """
    Find all posibles solution for N-queen problem
    """
    if (i > n):
        arr.append(t_arr[:])
        return arr

    for j in range(n + 1):
        if i == 0 or ([i - 1, j - 1] not in t_arr and
                      [i - 1, j + 1] not in t_arr and
                      j not in col):
            if i > 1:
                dia = 0
                for k in range(2, i + 1):
                    if ([i - k, j - k] in t_arr) or ([i - k, j + k] in t_arr):
                        dia = 1
                        break
                if dia:
                    continue
            t_arr.append([i, j])
            col.append(j)
            nqueen(t_arr, arr, col, i + 1, n)
            col.pop()
            t_arr.pop()

    return arr


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(sys.argv[1])
    except:
        print("N must be a number")
        exit(1)

    if not isinstance(n, int):
        print("N must be a number")
        exit(1)

    elif n < 4:
        print("N must be at least 4")
        exit(1)

    queens = nqueen([], [], [], 0, n - 1)
    for i in queens:
        print(i)
