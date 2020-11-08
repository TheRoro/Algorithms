import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**32, -1))
sys.setrecursionlimit(10**9)

n, m = [int(x) for x in input().split()]

adj = [[] for x in range(n)]

start = 0
dist = n * [10**13+1]
pred = n * [None]

for i in range(m):
    x, y, z = [int(x) for x in input().split()]
    x-=1
    y-=1
    adj[x].append((y, z))

visited = [False for y in range(n)]

def dijkstra():

    dist[start] = 0

    q = set()
    q.add((start, 0))

    while q:
        v = q.pop()[0] # 0 es v

        for elem in adj[v]:
            u = elem[0] #adjacent node -> 1
            weight = elem[1] #weight asociated to that adjacent node -> 10

            if dist[v] + weight < dist[u]:
                q.discard((u, dist[u]))
                dist[u] = dist[v] + weight
                q.add((u, dist[u]))
                pred[u] = v


dijkstra()
for el in dist:
    print(el, sep=" ", end=" ")