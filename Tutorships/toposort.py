adj = [[1, 3],
[2],
[3],
[]]

visited = [False]*len(adj)

topo = []

def dfs(v):
    visited[v] = True
    for u in adj[v]:
        if(visited[u] == False):
            dfs(u)
    topo.append(v)

dfs(0)

topo.reverse()

print(topo)