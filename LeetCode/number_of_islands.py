def num_islands(grid) -> int:
    rows, cols = len(grid), len(grid[0])

    visited = set()
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # number of islands
    noi = 0

    def count_islands(x, y):
        if x not in range(rows) or y not in range(cols) or grid[x][y] == "0" or (x, y) in visited:
            return

        visited.add((x, y))

        for d in directions:
            count_islands(d[0] + x, d[1] + y)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1" and (i, j) not in visited:
                count_islands(i, j)
                noi += 1

    return noi
