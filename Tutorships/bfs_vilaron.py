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

queue = [] #Lista que vamos a hacer que se comporte como cola

start = 0

def bfs():
    visited[start] = True
    queue.append(start)
    while queue:
        v = queue.pop(0)
        print("i'm in node:", v)
        for u in adj[v]:
            if visited[u] == False:
                visited[u] = True
                queue.append(u)

bfs()