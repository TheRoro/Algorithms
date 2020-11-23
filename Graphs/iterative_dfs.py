adj = [
[1,2],
[0,3],
[0,3,4],
[1,2,4],
[2,3]
]


def dfs(G, s, t):
    n = len(G)
    visited = [False]*n
    path = [-1]*n
    P = []
    P.append(s)
    while len(P) > 0:
        u = P.pop()
        print("Soy el padre", u)
        if u == t: break
        if visited[u]: continue
        visited[u] = True
        for v in G[u]:
            print("Soy el hijo", v)
            if visited[v] != True:
                P.append(v)
                path[v] = u


dfs(adj, 0, 4)