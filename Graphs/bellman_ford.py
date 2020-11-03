infinity = 10000000

def bellman_ford(G, s):
    n = len(G)
    dist = [infinity]*n
    path = [None]*n

    dist[s] = 0
    for i in range(n-1):
        for u in range(n):
            for v, w in G[u]:
                f = dist[u] + w
                if f < dist[v]:
                    dist[v] = f
                    path[v] = u

    for u in range(n):
        for v, w in G[u]:
            if dist[u] + w < dist[v]:
                return None, None, False
    

    return dist, path, True


adj = [
[(1,10),(2,15)],
[(0,10),(3,19)],
[(0,15),(3,17),(4,13)],
[(1,19),(2,17),(4,11)],
[(2,13),(3,11)]
]

print(bellman_ford(adj, 0))