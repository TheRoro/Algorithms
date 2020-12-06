N = 4
origen, destino = 0, 1
aristas = [(0,1,12),(0,2,20),(1,2,15)]

adj = []

for _ in range(N):
    adj.append([])

for tup in aristas:
    adj[tup[0]].append((tup[1], tup[2]))
    adj[tup[1]].append((tup[0], tup[2]))

# for el in adj:
#     print(el)

infinity = 10**10

start = origen #necessary
end = destino # not necessary since Dijkstra calculates a single source shortest path (SSSP)
n = len(adj)
dist = n * [infinity]
pred = []
for _ in range(n):
    pred.append([None, None])
path = []
def dijkstra():

    dist[start] = 0

    q = set()
    q.add((start, 0))

    while q:
        v = q.pop()[0] # 0 es v

        for elem in adj[v]:
            u = elem[0] #adjacent node -> 1
            weight = elem[1] #weight asociated to that adjacent node -> 10

            if dist[v] + weight < dist[u]:
                q.discard((u, dist[u]))
                dist[u] = dist[v] + weight
                q.add((u, dist[u]))
                if pred[u][0] != v:
                    pred[u][1] = pred[u][0]
                    pred[u][0] = v
            
            if pred[u][1] == None or pred[u][0] == None:
                if pred[u][0] != v and pred[u][1] != v and u != start:
                    pred[u][1] = pred[u][0]
                    pred[u][0] = v
            
    

def restore_path():
    v = end
    visited = n * [False]
    while v != None:
        path.append(v)
        visited[v] = True
        if pred[v][0] != None and visited[pred[v][0]] == True:
            v = pred[v][1]
        else:
            v = pred[v][0]
    path.reverse()

dijkstra()
restore_path()
# for e in pred:
#     print("A:",e)
# print(pred)
# print(dist)
# print(adj)
total = 0
for i in range(len(path) - 1) :
    for j in range(len(adj[i])):
        if (adj[path[i]][j][0] == path[i+1]):
            total+=adj[path[i]][j][1]
            #print(adj[path[i]][j][1])
    #print(adj[path[i]][path[i+1]])

print("Costo:", total)
print("Ruta:", end="", sep="")
for i in range(len(path)):
    if(i == len(path) - 1):
        print(path[i], sep="", end="")
    else:
        print(path[i], "->", sep="", end="")

# print("The shortest path is:", path)
# print("With a total weight of:", dist[end])