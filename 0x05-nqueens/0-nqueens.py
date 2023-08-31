#!/usr/bin/python3
"""N queens solution finder module.
"""
import sys

def is_safe(board, row, col, N):
    # Check if there's a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens(N):
    def backtrack(row):
        nonlocal solutions
        if row == N:
            solutions.append([[r, c] for r, c in enumerate(board)])
            return
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 1
                backtrack(row + 1)
                board[row][col] = 0
    
    solutions = []
    board = [[0] * N for _ in range(N)]
    backtrack(0)
    return solutions

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()

