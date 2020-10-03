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

n = len(adj)

visited = [False]*n

topo = []
comp = []

#Recorrer el primer grafo
def dfs(v):
    visited[v] = True
    for u in adj[v]:
        if visited[u] == False:
            dfs(u)
    topo.append(v)

#Recorrer el grafo transpuesto
def dfs2(v):
    comp.append(v) # 0, 2, 1
    visited[v] = True
    for u in adjtr[v]:
        if visited[u] == False:
            dfs2(u)

for i in range(len(adj)):
    if(visited[i] == False):
        dfs(i)

topo.reverse()
visited = [False]*n
print("Ordenamiento topologico:", topo)
#topo = [0,1,2,3]

print("Las componentes fuertemente conexas con:")
for i in range(len(adjtr)):
    v = topo[i]
    if(visited[v] == False):
        dfs2(v)
        print(comp)
        comp.clear()
