def updateMatrix(self, mat):
    rows = len(mat)
    cols = len(mat[0])

    queue = []

    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 0:
                queue.append((i, j))
            else:
                mat[i][j] = "#"

    while queue:
        x, y = queue.pop(0)

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for d in directions:
            dx = d[0] + x
            dy = d[1] + y

            if dx in range(rows) and dy in range(cols) and mat[dx][dy] == "#":
                mat[dx][dy] = mat[x][y] + 1
                queue.append((dx, dy))

    return mat