def floydWarshall(G):
    n = len(G)
    dist = [[10000000]*n for _ in range(n)]
    pred = [[-1]*n for _ in range(n)]

    for u in range(n):
        for v, w in G[u]:
            dist[u][v] = w
            pred[u][v] = u

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i != j and k != j and k != i:
                    f = dist[i][k] + dist[k][j]
                    if f < dist[i][j]:
                        dist[i][j] = f
                        pred[i][j] = pred[k][j]

    return pred, dist

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
pred, dist = floydWarshall(adj)
for el in pred:
    print(el)
for el in dist:
    print(el)