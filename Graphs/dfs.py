adj = [[1, 3],
[0,2],
[1,3],
[0,1]]

visited = []

for i in range(len(adj)):
    visited.append(False)

def dfs(v):
    visited[v] = True
    print("I'm in node:", v)
    print(v,"->", adj[v])
    for u in adj[v]:
        if(visited[u] == False):
            dfs(u)

dfs(0)