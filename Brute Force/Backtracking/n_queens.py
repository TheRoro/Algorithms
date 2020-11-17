board = [2, 4, 1, 3, -1, -1, -1, -1]

def valid(board, row, col):
    n = len(board)
    for i in range(row):
        if board[i] == col:
            return False
        d = row - i
        if board[i] + d == col or board[i] - d == col:
            return False
    return True

def nqueensbt(board, row):
    n = len(board)
    if row < n:
        for col in range(n):
            if valid(board, row, col):
                board[row] = col
                if nqueensbt(board, row + 1):
                    return True
    else:
        print(board)
        return True

nqueensbt([-1]*8, 0)