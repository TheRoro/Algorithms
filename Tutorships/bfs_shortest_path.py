adj = [
[1,2],
[0,3,4],
[0,4,5],
[1,6],
[1,2,6],
[2,6],
[3,4,5],
]

n = len(adj)

visited = [False]*n

queue = []

prev = [None]*n

start = 0
end = 6

path = []

def bfs():
    """goal = True"""
    visited[start] = True
    queue.append(start)
    while queue"""and goal""":
        v = queue.pop(0)
        for u in adj[v]:
            if visited[u] == False:
                visited[u] = True
                queue.append(u)
                prev[u] = v
            """if u == end:
                goal = False
                break"""

def build_path():
    v = end
    while v != None:
        path.append(v)
        v = prev[v]
    

bfs()
build_path()

path.reverse()

print(path)
