import math
n = int(input())

adj = [[] for i in range(n)]

for i in range(n):
    inp=list(map(int, input().split()))
    adj[i].extend(inp[1:])

t = int(input())

distance = [math.inf]*n
visited = n * [False]

def bfs(first):
    distance[first] = 0
    queue = []
    queue.append(first)

    while queue:
        v = queue.pop(0)
        for u in adj[v]:
            if(visited[u] == False):
                visited[u] = True
                distance[u] = distance[v] + 1
                queue.append(u)

for i in range(t):
    visited = n * [False] #visitados para el grafo
    distance = [math.inf]*n #distancia de los nodos
    first=int(input())

    if not len(adj[first]):
        print(0)
        continue

    visited[first] = True #se marca el primer nodo

    #llamas a bfs para cada test case
    bfs(first)

    occ = {} #dict para guardar las ocurrencias
    for key in distance: #guardas las ocurrencias de las distancias
        if key not in occ:
            occ[key] = 1 #si no se encuentra en el dict, se agrega por 1era vez
        else:
            occ[key] = occ[key] + 1 #si ya se encuentra en el dict, se suma una ocurrencia
   
    #respuestas del test case:
    d = 0
    mx = 0
    #se recorre el dict y se queda con la primera mayor ocurrencia
    for r in occ:
        if(occ[r] > mx):
            mx = occ[r]
            d = r
    #se muestran key y value de la mayor ocurrencia del dict
    print(mx,d)

