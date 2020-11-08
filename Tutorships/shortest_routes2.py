import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**32, -1))
sys.setrecursionlimit(10**9)

n, m = [int(x) for x in input().split()]

adj = [[] for x in range(n)]

start = 0
dist = n * [10**13+1]
pred = n * [None]
order = []

for i in range(m):
    x, y, z = [int(x) for x in input().split()]
    x-=1
    y-=1
    adj[x].append((y, z))

visited = [False for y in range(n)]


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

dag_shortest()

for el in dist:
    print(el, sep=" ", end=" ")