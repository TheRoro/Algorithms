n, m = [int(x) for x in input().split()]

adj = [[] for x in range(n)]

for i in range(m):
    x, y = [int(x) for x in input().split()]
    x-=1
    y-=1
    adj[x].append(y)
    adj[y].append(x)

# adj = [
# [1],
# [2],
# [0,3],
# []]

adjtr = []

for _ in range(len(adj)):
    adjtr.append([])

for i in range(len(adj)):
    for j in adj[i]:
        adjtr[j].append(i)

visited = len(adj) * [False]


print(adj)
order = []
comp = []
conn = []

def dfs(s):
    n = len(adj)
    P = []
    P.append(s)
    while len(P) > 0:
        u = P.pop()
        if visited[u]: continue
        visited[u] = True
        for v in adj[u]:
            if visited[v] != True:
                P.append(v)
        order.append(u)
        print(order)

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
            dfs(u)
    #print(comp)
    order.reverse()
    conn.append(comp)

#KOSARAJU

for i in range(len(adj)):
    if visited[i]==False:
        dfs(i)

visited = len(adj) * [False]

order.reverse()
print("Order:", order)
order.reverse()

def calc_scc():
    for i in range(len(adj)):
        v = order[len(adj) - 1 - i]
        if visited[v] == False:
            dfs2(v)
            print(comp)
            comp.clear()

calc_scc()
# for e in conn:
#     print(e)

# def setTeams():
#     for e in 


