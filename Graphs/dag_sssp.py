#Shortest path implementation for DAGs (Directed acyclic graphs)
adj = [
[],
[(6, 3)],
[(0, 1)],
[(1, 8), (4, 3), (5, 2), (7, 7)],
[(2, 9), (7, 3)],
[(1, 2)],
[],
[(0, 2), (6, 6)]
]

infinity = 10**10

start = 3
end = 6 # not necessary since DAG calculates a single source shortest path (SSSP)
n = len(adj)
dist = n * [infinity]
pred = n * [None]
path = []
visited = [False]*n
order = []

def topoSort(G):
    def dfsVisit(v):
        if visited[v]: return
        visited[v] = True
        for u, _ in G[v]:
            if not visited[u]:
                dfsVisit(u)
        order.append(v)

    for v in range(n):
        if not visited[v]:
            dfsVisit(v)

    return list(reversed(order))

def dag_shortest():
    dist[start] = 0
    topo_sort = topoSort(adj)
    for v in topo_sort:
        for u, w in adj[v]:
            if dist[v] + w < dist[u]:
                dist[u] = dist[v] + w
                pred[u] = v

def restore_path():
    v = end
    while v != None:
        path.append(v)
        v = pred[v]
    path.reverse()

dag_shortest()
restore_path()
print(dist)
print(pred)
print(path)

