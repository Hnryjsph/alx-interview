#!/usr/bin/python3
"""N queens solution finder module.
"""
import sys

def is_safe(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return False
        
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
        
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
        
    return True

def solve_nqueens(board, col, N):
    if col >= N:
        for row in board:
            print([row.index(1), col - N + 1])
        print()
        return
    
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            solve_nqueens(board, col + 1, N)
            board[i][col] = 0

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
    
    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_nqueens(board, 0, N)

if __name__ == "__main__":
    main()
