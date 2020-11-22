import math
from queue import Queue

def bfs(G, s, t):
    n = len(G)
    visited = [False]*n
    path = [-1]*n
    bottleneck = math.inf
    Q = Queue()
    Q.put(s)
    visited[s] = True
    while not Q.empty():
        u = Q.get()
        if u == t: break
        for v in range(n):
            if G[u][v] > 0 and not visited[v]:
                visited[v] = True
                Q.put(v)
                path[v] = u
                bottleneck = G[u][v] if G[u][v] < bottleneck else bottleneck

    return path, bottleneck, path[t] != -1

def edmondKarp(G, s, t):
    n = len(G)
    Gp = [[G[u][v] for v in range(n)] for u in range(n)]
    maxflow = 0
    while True:
        path, bottleneck, existsPath = bfs(Gp, s, t)
        if not existsPath: break
        maxflow += bottleneck
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


print(edmondKarp(G, 0, 1))