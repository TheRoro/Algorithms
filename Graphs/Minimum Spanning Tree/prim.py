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
visi = n * [False]
path = []

def prim():

    q = []
    dist[start] = 0
    q.append((start, dist[start]))
    while q:
        print(q)
        v = q.pop()[0]
        if visi[v]: continue
        visi[v] = True
        for u, w in adj[v]:
            if not visi[u] and w < dist[u]:
                print("elem", (u, w))
                q.append((u, w))
                dist[u] = w
                pred[u] = v
                #q.sort(key=lambda x: x[0])

prim()

total = 0
print("The minimum spanning tree is:")
for i in range(1, len(pred)):
    print(pred[i], "->", i, "weight:", dist[i])

for i in range(len(dist)):
    total+=dist[i]

print("With a total weight of:", total)
print(dist)
print(pred)
print("peso total", total)