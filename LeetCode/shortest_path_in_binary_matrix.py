def shortest_path_binary_matrix(grid) -> int:
    if grid[0][0] != 0:
        return -1

    n = len(grid)

    start, end = (0, 0), (n - 1, n - 1)

    queue = [start]
    visited = set()
    visited.add(start)

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

    path_length = 1

    while queue:
        queue_size = len(queue)

        for i in range(queue_size):
            x, y = queue.pop(0)

            if (x, y) == end:
                return path_length

            for d in directions:
                dx = d[0] + x
                dy = d[1] + y

                if dx in range(n) and dy in range(n) and (dx, dy) not in visited and grid[dx][dy] == 0:
                    visited.add((dx, dy))
                    queue.append((dx, dy))

        path_length += 1

    return -1
