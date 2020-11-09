def floydWarshall(G):
    n = len(G)
    cost = [[10000000]*n for _ in range(n)]
    path = [[-1]*n for _ in range(n)]

    for u in range(n):
        for v, w in G[u]:
            cost[u][v] = w
            path[u][v] = u

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i != j and k != j and k != i:
                    f = cost[i][k] + cost[k][j]
                    if f < cost[i][j]:
                        cost[i][j] = f
                        path[i][j] = path[k][j]

    return path, cost

adj = [
[],
[(0, 5), (5, 6), (6, 7)],
[(0, 6), (4, 4), (6, 4)],
[(1, 3)],
[(6, 5), (7, 6)],
[(3, 3)],
[],
[],
]
path, dist = floydWarshall(adj)
for el in path:
    print(el)
for el in dist:
    print(el)