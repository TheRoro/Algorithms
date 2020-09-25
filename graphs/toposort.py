adj2 = [[1],
    [2],
    [0,4],
    [4],
    [5],
    [3]]

adj = [[1,2],
        [3],
        [3]
        [],
        [5],
        []]

visited = len(adj) * [False]

topo = []

def dfs(v):
    visited[v] = True
    for u in adj[v]:
        if(visited[u] == False):
            dfs(u)
    topo.append(v)

topo.reverse()

dfs(0)
print(topo)