# N-Queens Problem
# Place n queens such that no two queens attack each other.

def print_solution(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col, n):
    # Check left side row
    for i in range(col):
        if board[row][i] == 'Q':
            return False
    # Check upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    # Check lower diagonal
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    return True

def solve_n_queens(board, col, n):
    if col >= n:
        print_solution(board)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 'Q'
            res = solve_n_queens(board, col + 1, n) or res
            board[i][col] = '.'
    return res

n = 4
board = [['.' for _ in range(n)] for _ in range(n)]

print("\nSolutions to N-Queens Problem:")
solve_n_queens(board, 0, n)
