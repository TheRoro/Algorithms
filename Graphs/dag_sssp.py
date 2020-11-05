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

start = 0
end = 4 # not necessary since DAG calculates a single source shortest path (SSSP)
n = len(adj)
dist = n * [infinity]
pred = n * [None]
path = []

def dag_shortest():
    topo_sort = topoSort(G)

    for u in topo_sort:
        for v, w in G[u]:
            f = dist[u] + w
            if dist[v] > f:
                dist[v] = f
                path[v] = u