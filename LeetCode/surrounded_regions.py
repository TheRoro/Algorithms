def solve(board) -> None:
    rows, cols = len(board), len(board[0])
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    def dfs(x, y):
        if x not in range(rows) or y not in range(cols) or board[x][y] != "O":
            return

        board[x][y] = "N"
        for d in directions:
            dfs(d[0] + x, d[1] + y)

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == "O" and (i in [0, rows - 1] or j in [0, cols - 1]):
                dfs(i, j)

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == "O":
                board[i][j] = "X"
            elif board[i][j] == "N":
                board[i][j] = "O"
