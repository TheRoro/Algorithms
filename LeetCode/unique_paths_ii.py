def unique_paths_with_obstacles(obstacle_grid) -> int:
    rows, cols = len(obstacle_grid), len(obstacle_grid[0])

    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
        if obstacle_grid[r][0] == 1:
            break
        dp[r][0] = 1

    for c in range(cols):
        if obstacle_grid[0][c] == 1:
            break
        dp[0][c] = 1

    for i in range(1, rows):
        for j in range(1, cols):
            if obstacle_grid[i][j] == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[-1][-1]
