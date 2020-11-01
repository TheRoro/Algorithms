adj = [
[(1,10),(2,15)],
[(0,10),(3,19)],
[(0,15),(3,17),(4,13)],
[(1,19),(2,17),(4,11)],
[(2,13),(3,11)]
]

infinity = 10**10
start = 0
n = len(adj)
dist = n * [infinity]
pred = n * [None]
visited = [False]*n
path = []

def prim():

    q = set()
    q.add((start, 0))

    while q:
        v = q.pop()[0]
        visited[v] = True
        for elem in adj[v]:
            u = elem[0] #adjacent node
            weight = elem[1] #weight asociated to that adjacent node
            if  weight < dist[u] and visited[u] == False:
                q.add(elem)
                dist[u] = weight
                pred[u] = v

prim()

total = 0
print("El MST es:")
for i in range(1, len(pred)):
    print(pred[i], "->", i, "peso:", dist[i])
    total+=dist[i]
print("Con un peso total de:", total);