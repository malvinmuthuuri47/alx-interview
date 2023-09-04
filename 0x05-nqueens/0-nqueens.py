#!/usr/bin/env python3
"""N queens"""
import sys
from typing import List


def is_safe(board: List[List[int]], row: int, col: int, N: int) -> bool:
    """This function checks the positioning of the queen on the board"""
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(N: int) -> None:
    """This function sets up the chessboard"""
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]

    def print_solution(board: List[List[int]]) -> None:
        """This function handles the printing of the positions of the
        queens on the board"""
        solution = []
        for row in range(N):
            queen_col = [row, board[row].index(1)]
            solution.append(queen_col)
        print(solution)

    def solve(row: int) -> None:
        """This function explores all possible queen placements ensuring
        that queens do not attack each other"""
        if row == N:
            print_solution(board)
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 1
                solve(row + 1)
                board[row][col] = 0

    solve(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
