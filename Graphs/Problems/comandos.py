infinity = 10000000

def floydWarshall(G):
    n = len(G)
    cost = [[infinity]*n for _ in range(n)]
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

t = int(input())

for test in range(t):
    adj = []

    n = int(input())
    m = int(input())

    for i in range(n):
        adj.append([])

    for i in range(m):
        x,y = [int(r) for r in input().split()]
        adj[x].append((y,1))
        adj[y].append((x,1))

    start, end = [int(x) for x in input().split()]

    path, dist = floydWarshall(adj)

    ans = []

    for i in range(len(dist)):
        maxi = 0
        if dist[i][start] != infinity:
            maxi+=dist[i][start]
        if dist[i][end] != infinity:
            maxi+=dist[i][end]
        ans.append(maxi)

    ansy = max(ans)
    print("Case ", test+1, ": ", ansy, sep="")