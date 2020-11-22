import math

def dfs(G, s, t):
    n = len(G)
    visited = [False]*n
    path = [-1]*n
    bottleneck = math.inf
    P = []
    P.append(s)
    while len(P) > 0:
        u = P.pop()
        if u == t: break
        if visited[u]: continue
        visited[u] = True
        for v in range(n):
            if G[u][v] > 0 and not visited[v]:
                P.append(v)
                path[v] = u
                bottleneck = G[u][v] if G[u][v] < bottleneck else bottleneck

    return path, bottleneck, path[t] != -1

def fordFulkerson(G, s, t):
    n = len(G)
    Gp = [[G[u][v] for v in range(n)] for u in range(n)]
    maxflow = 0
    while True:
        path, bottleneck, existsPath = dfs(Gp, s, t)
        if not existsPath: break
        maxflow += bottleneck
        print(path)
        end = t
        while path[end] != -1:
            u, v = path[end], end
            Gp[u][v] -= bottleneck
            Gp[v][u] += bottleneck
            end = path[end]

    return maxflow

V = [ 'S', 'T', 'u', 'v', 'w', 'z' ]
G = [[  0,   0,  16,   0,  13,   0], # S
     [  0,   0,   0,   0,   0,   0], # T
     [  0,   0,   0,  12,   0,   0], # u
     [  0,  20,   0,   0,   9,   0], # v
     [  0,   0,   4,   0,   0,  14], # w
     [  0,   4,   0,   7,   0,   0]] # z

print(fordFulkerson(G, 0, 1))