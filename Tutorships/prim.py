adj = [[(1, 4), (7, 8)], [(0, 4), (2, 8), (7, 11)], [(1, 8), (3, 7), (5, 4), (8, 2)], [(2, 7), (4, 9), (5, 14)], [(3, 9), (5, 10)], [(2, 4), (3, 14), (4, 10), (6, 2)], [(5, 2), (7, 1), (8, 6)], [(0, 8), (1, 11), (6, 1), (8, 7)], [(2, 2), (6, 6), (7, 7)]]

infinity = 10**10
start = 5
n = len(adj)
dist = n * [infinity]
pred = n * [None]
visited = [False]*n
path = []

def prim():

    q = set()
    dist[start] = 0
    q.add((start, 0))

    while q:
        v = q.pop()[0]
        #print("Node", v)
        visited[v] = True
        for elem in adj[v]:
            #print("Hijo de:", v, "es:", elem)
            u = elem[0] #adjacent node
            weight = elem[1] #weight asociated to that adjacent node
            if  weight < dist[u] and visited[u] == False:
                q.add(elem)
                dist[u] = weight
                pred[u] = v
                #print("El predecesor de", u, "es:", pred[u])

prim()

total = 0
#print("The minimum spanning tree is:")
for i in range(len(dist)):
    #print(pred[i], "->", i, "weight:", dist[i])
    total+=dist[i]
print(dist)
print(pred)
print("With a total weight of:", total);