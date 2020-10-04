adj = [[1, 3],
[0,2],
[1,3],
[0,1,2]]

#INEFICIENTE 10ala5*10ala5 = 10ala10
attemp = False
if(attemp):
    for i in range(len(adj)):
        print("Estoy en el nodo", i)
        for j in range(len(adj[i])):
            print("soy el vecino de", i, "y soy:", adj[i][j])

#c++ = 10ala4*10ala4 = 10ala8 = 1 segundo NORMALASOO BRO
#python = 10ala3*10ala3 = ENTRA AJUSTADOo mi pana


#DFS = O(v+a)

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

#bfs

adj = [[1, 3],
[0,2],
[1,3],
[0,1]]

used = []
s = 0
q = []

for i in range(len(adj)):
    used.append(False)

def bfs():
    q.append(s)
    used[s] = True
    while(q):
        v = q.pop(0)
        print("i'm in node:", v)
        for u in adj[v]:
            if(used[u] == False):
                used[u] = True
                q.append(u)

bfs()


#MAÑANA
#convertir un input a lista de adyacencia

#tengo 4 nodos (n = 4)
#te digo cuantas aristas hay (m = 3) (es un grafo no dirigido)
#te roto las conexiones
#imprimeme la lista de adyancencia 
#recorremela en dfs

#input:
#4
#3
#0 1
#2 3
#0 3

n = 4
m = 3

adj = []
vis = []

for i in range(n):
    adj.append([])

for i in range(m):
    x, y = [int(x) for x in input().split()]
    adj[x].append(y)

print(adj)

