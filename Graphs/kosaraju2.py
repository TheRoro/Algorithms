adj = [
[1],
[2],
[0,3],
[]]

adjtr = [
[2],
[0],
[1],
[2]]

visited = len(adj) * [False]

order = []
comp = []

def dfsIt(G, s):
    P = []
    P.append(s)
    while len(P) > 0:
        u = P.pop()
        if visited[u]: continue
        visited[u] = True
        for v in G[u]:
            if visited[v] != True:
                P.append(v)

def dfsIt2(G, s):
    P = []
    P.append(s)
    while len(P) > 0:
        u = P.pop()
        if visited[u]: continue
        visited[u] = True
        for v in G[u]:
            if visited[v] != True:
                P.append(v)


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
        dfsIt(adj, i)

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
