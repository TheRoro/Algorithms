def pacific_atlantic(heights):
    rows, cols = len(heights), len(heights[0])
    pacific, atlantic = set(), set()

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(x, y, visited, prev_height):
        if (x, y) in visited or x not in range(rows) or y not in range(cols) or heights[x][y] < prev_height:
            return

        visited.add((x, y))

        for d in directions:
            dx = d[0] + x
            dy = d[1] + y
            dfs(dx, dy, visited, heights[x][y])

    for r in range(rows):
        dfs(r, 0, pacific, heights[r][0])
        dfs(r, cols - 1, atlantic, heights[r][cols - 1])

    for c in range(cols):
        dfs(0, c, pacific, heights[0][c])
        dfs(rows - 1, c, atlantic, heights[rows - 1][c])

    ans = []

    for r in range(rows):
        for c in range(cols):
            if (r, c) in pacific and (r, c) in atlantic:
                ans.append([r, c])

    return ans
