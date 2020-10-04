#Tipico enunciado de problema de programacion competitiva

#Tengo un grafo con n nodos y m aristas, compute la lista de
#adyacencia asociada al grafo que se brinda en el input a continuacion:

#la primera linea corresponde a la cantidad de nodos n
#la segunda linea corresponde a la cantidad de aristas m
#las siguientes m lineas corresponden a los nodos asociados a cada arista
#es un grafo dirigido

#encuentra las cfc, encuentre el camino mas corto, etc.

#input:
#4 3
#0 1
#2 3
#0 3

adj = []

n, m = [int(x) for x in input().split()]

for i in range(n):
    adj.append([])

for i in range(m):
    x,y = [int(x) for x in input().split()]
    adj[x].append(y)
    adj[y].append(x)

print(adj)