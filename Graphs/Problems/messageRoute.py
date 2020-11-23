n, m = [int(x) for x in input().split()]

adj = [[] for x in range(n)]

conn = []

for i in range(m):
    x, y = [int(x) for x in input().split()]
    x-=1
    y-=1
    adj[x].append(y)
    adj[y].append(x)

visited = [False for y in range(n)]

start = 0
finish = len(adj) - 1
path = []
prev = [None]*n

def bfs():
    searchPath = True
    visited[start] = True
    queue = []
    queue.append(start)
    while queue and searchPath:
        v = queue.pop(0)
        for u in adj[v]:
            if visited[u] == False:
                visited[u] = True
                queue.append(u)
                prev[u] = v
            if u == finish:
                searchPath = False

def build_path():
    v = finish
    while v != None:
        path.append(v+1)
        v = prev[v]
    return path
    

bfs()
path = build_path()
path.reverse()

if len(path) <= 1:
    print("IMPOSSIBLE")
else:
    print(len(path))
    for e in path:
        print(e, sep="",end=" ")

