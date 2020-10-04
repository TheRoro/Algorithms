adj = []

n, m = [int(x) for x in input().split()]

for i in range(n):
    adj.append([])

for i in range(m):
    x,y = [int(x) for x in input().split()]
    x-=1
    y-=1
    adj[x].append(y)
    adj[y].append(x)

n = len(adj)

visited = [False]*n

cont = 0

group = []

def dfs(v):
    visited[v] = True
    for u in adj[v]:
        if visited[u] == False:
            visited[u] = True
            dfs(u)

for i in range(len(adj)):
    if visited[i] == False:
        cont+=1
        group.append(i)
        dfs(i)


rpta = cont-1

print(rpta)

for i in range(rpta):
    print(group[i]+1, group[i+1]+1)

#O(e+v)