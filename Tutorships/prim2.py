
import heapq as hq
from math import inf

adj = [
[(1,10),(2,15)],
[(0,10),(3,19)],
[(0,15),(3,17),(4,13)],
[(1,19),(2,17),(4,11)],
[(2,13),(3,11)]
]

def prim(G, s=0):
    n = len(G)
    visited = [False]*n
    path = [None]*n
    weight = [100000000]*n
    pqueue = []

    weight[s] = 0
    hq.heappush(pqueue, (0, s))
    while len(pqueue) > 0:
        print("iteration:", hq)
        _, u = hq.heappop(pqueue)
        if visited[u]: continue
        visited[u] = True
        for v, w in G[u]:
            if not visited[v] and w < weight[v]:
                weight[v] = w
                path[v] = u
                hq.heappush(pqueue, (w, v))

    return path, weight

path, weight = prim(adj, 0)
total = 0
for el in weight:
    total+=el
print(weight)
print(path)
print("total weight:", total)
