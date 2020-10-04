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

#0 1 2 3

#n = 4
#m = 3

n, m = [int(x) for x in input().split()]

adj = []
vis = []

for i in range(n):
    adj.append([])

for i in range(m):
    x, y = [int(x) for x in input().split()]
    adj[x].append(y)
    adj[y].append(x)

print(adj)
