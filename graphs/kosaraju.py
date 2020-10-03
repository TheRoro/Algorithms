adj = [[1],
    [2],
    [0,4],
    [4],
    [5],
    [3]]

adjtr = [[2],
        [0],
        [1],
        [5],
        [2,3],
        [4]]

visited = len(adj) * [False]

order = []
comp = []

def dfs1(v):
    visited[v] = True
    for u in adj[v]:
        if visited[u] == False:
            dfs1(u)
    order.append(v)

def dfs2(v):
    visited[v] = True
    comp.append(v)
    for u in adjtr[v]:
        if visited[u] == False:
            dfs2(u)

#KOSARAJU

for i in range(len(adj)):
    if visited[i]==False:
        dfs1(i)

visited = len(adj) * [False]

order.reverse()
print("Order:", order)
order.reverse()

for i in range(len(adj)):
    v = order[len(adj) - 1 - i]
    if visited[v] == False:
        dfs2(v)
        print(comp)
        comp.clear()

