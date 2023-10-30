#!/usr/bin/python3

import sys

def is_safe(board, row, col):
    """ Check if it is safe to place a queen at the specified position on the chessboard """
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True

def solve_nqueens(n):
    """ Solve the N-Queens problem and return all possible solutions """
    def solve(board, col):
        if col == n:
            solutions.append(board[:])
            return
        for row in range(n):
            if is_safe(board, row, col):
                board.append(row)
                solve(board, col + 1)
                board.pop()

    solutions = []
    solve([], 0)
    return solutions

def print_solutions(solutions):
    """ Print the solutions for the N-Queens problem to the console """
    for solution in solutions:
        for row in solution:
            print("[{}, {}]".format(solution.index(row), row), end=" ")
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_nqueens(N)
    print_solutions(solutions)

