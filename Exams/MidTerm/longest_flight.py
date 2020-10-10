#import sys, resource
#resource.setrlimit(resource.RLIMIT_STACK, (2**32, -1))
#sys.setrecursionlimit(10**9)

adj = []

n, m = [int(x) for x in input().split()]

for i in range(n):
    adj.append([])

for i in range(m):
    x,y = [int(x) for x in input().split()]
    x-=1
    y-=1
    adj[x].append((y,1))

n = len(adj)

infinity = 0

start = 0
n = len(adj)
end = n - 1
dist = n * [infinity]
pred = n * [None]
path = []

bailarina_77 = []

visited = [int(0)]*n

def dijkstra():

    dist[start] = 0

    q = set()
    q.add((start, 0))

    while q:
        v = q.pop()[0]

        for elem in adj[v]:
            u = elem[0] #adjacent node
            weight = elem[1] #weight asociated to that adjacent node

            if dist[v] + weight > dist[u]:
                q.discard((u, dist[u]))
                dist[u] = dist[v] + weight
                pred[u] = v
                q.add((u, dist[u]))

def restore_path():
    v = end
    while v != None:
        path.append(v)
        v = pred[v]
    path.reverse()

dijkstra()
restore_path()

if(len(path) == 1):
    print("IMPOSSIBLE")
else:
    print(len(path))
    for i in range(len(path)):
        print(path[i]+1, end=" ", sep=" ")