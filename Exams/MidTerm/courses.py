import sys, resource
resource.setrlimit(resource.RLIMIT_STACK, (2**32, -1))
sys.setrecursionlimit(10**9)

adj = []

n, m = [int(x) for x in input().split()]

for i in range(n):
    adj.append([])

for i in range(m):
    x,y = [int(x) for x in input().split()]
    x-=1
    y-=1
    adj[x].append(y)

n = len(adj)

topo = []

bailarina_77 = []

visited = [int(0)]*n

def dfs(v):
    visited[v] = 1
    for u in adj[v]:
        if(visited[u] == 0):
            dfs(u)
        elif(visited[u] == 1):
            bailarina_77.append("bailarina 77")
    topo.append(v)
    visited[v] = 2

for i in range(len(adj)):
    if visited[i] == 0:
        dfs(i)

for i in range(len(topo)):
    topo[i]= topo[i]+1
    
topo.reverse()

if len(bailarina_77) != 0 or len(topo) == 0:
    print("IMPOSSIBLE")
else:
    for i in range(len(topo)):
        print(topo[i], end=" ", sep=" ")

