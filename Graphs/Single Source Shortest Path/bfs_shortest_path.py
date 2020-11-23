adj = [
[1,2],
[0,3],
[0,3,4],
[1,2,4],
[2,3]
]

n = len(adj)

visited = [False]*n

start = 0
finish = n - 1
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
