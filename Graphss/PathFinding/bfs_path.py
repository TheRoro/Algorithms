adj = [
[1, 2],
[0,3,4],
[0,4,5],
[1,6],
[1,2,6],
[2,6],
[3,4,5]
]

n = len(adj)
visited = [False]*n
prev = [None]*n
queue = []

start = 0
end = 6

path = []

def bfs():
    visited[start] = True
    queue.append(start)
    while queue:
        v = queue.pop(0)
        print("I'm in node:", v)
        for u in adj[v]:
            if visited[u] == False:
                visited[u] = True
                print("I'm", u, "the son of", v)
                prev[u] = v
                queue.append(u)

def build_path():
    v = end
    while v != None:
        path.append(v)
        v = prev[v]
    
    path.reverse()

bfs()
build_path()

print(path)