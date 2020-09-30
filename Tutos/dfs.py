adj = [[1, 3],
[0,2],
[1,3],
[0,1,2]]

visited = []

for i in range(len(adj)):
    visited.append(False)

nodo = 3

def dfs(v):
    visited[v] = True
    for u in adj[v]:
        if visited[u] == False:
            if u == nodo:
                print(v, "es el antecesor de", u)
            dfs(u)

