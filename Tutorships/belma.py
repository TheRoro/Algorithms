#Bellman ford implementation
adj = [
[(1,10),(2,15)],
[(0,10),(3,19)],
[(0,15),(3,17),(4,13)],
[(1,19),(2,17),(4,11)],
[(2,13),(3,11)]
]

infinity = 10000000
negInfinity = -(infinity)
start = 0
end = 4 # not necessary since Bellman-Ford calculates a single source shortest path (SSSP)
n = len(adj)
dist = n * [infinity]
pred = n * [None]
path = []

def bellman_ford(s):

    dist[s] = 0
    for i in range(n-1):
        for v in range(n):
            for u, w in adj[v]:
                if dist[v] + w < dist[u]:
                    dist[u] = dist[v] + w
                    pred[u] = v

    for v in range(n):
        for u, w in adj[v]:
            if dist[v] + w < dist[u]:
                    dist[u] = negInfinity
                    pred[u] = None

bellman_ford(start)
print(dist)
print(pred)