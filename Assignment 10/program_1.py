# Consider the 8 queen's problem, it is a 8*8 chess board where you need to place queens
# according to the following constraints.
# a. Each row should have exactly only one queen.
# b. Each column should have exactly only one queen.
# c. No queens are attacking each other.

def safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check top-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check top-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def nqueens(board, row, n, ans):
    if row == n:
        ans.append(["".join(row) for row in board])  
        return

    for col in range(n):  
        if safe(board, row, col, n):
            board[row][col] = 'Q'  
            nqueens(board, row + 1, n, ans)
            board[row][col] = '.' 


n = 8
board = [["."] * n for _ in range(n)]
ans = []

nqueens(board, 0, n, ans)

for solution in ans:
    for row in solution:
        print(row)
    print()