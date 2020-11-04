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
    q.add((start, infinity))

    while q:
        v = q.pop()[0]
        print("Node", v)
        visited[v] = True
        for elem in adj[v]:
            print("Hijo de:", v, "es:", elem)
            u = elem[0] #adjacent node
            weight = elem[1] #weight asociated to that adjacent node
            if  weight < dist[u] and visited[u] == False:
                q.add(elem)
                dist[u] = weight
                pred[u] = v

prim()

total = 0
print("The minimum spanning tree is:")
for i in range(1, len(pred)):
    print(pred[i], "->", i, "weight:", dist[i])
    total+=dist[i]
print("With a total weight of:", total);