adj = [
[1,2],
[4],
[3],
[4],
[]
]

n = len(adj)

visited = [False]*n

queue = []

prev = [None]*n

start = 0
end = 4

path = []

def bfs():
    visited[start] = True
    queue.append(start)
    while queue:
        v = queue.pop(0)
        for u in adj[v]:
            if visited[u] == False:
                visited[u] = True
                queue.append(u)
            prev[u] = v


def build_path():
    v = end
    while v != None:
        path.append(v)
        v = prev[v]
    

bfs()
build_path()

path.reverse()

print(path)
