#Dijkstra implementation using sets
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
path = []
visited = [False]*n

def prim():

    q = set()
    q.add((start, 0))
    visited[start] = True

    while len(q) != 0:
        v = q.pop()[0]

        mini = infinity
        for elem in adj[v]:
            u = elem[0] #adjacent node
            weight = elem[1] #weight asociated to that adjacent node
            print("Im in node", u, "With cost:", weight)
            visited[v] = True
            if  weight < dist[v] and visited[u] == False:
                dist[v] = weight
                mini = (u, dist[v])
                pred[v] = u
        if mini != infinity:
            q.add(mini)

def restore_path():
    v = start
    while v != None:
        path.append(v)
        v = pred[v]

prim()
restore_path()
print(pred)
print(dist)

print("The Minimum spanning tree is:", path)

total = 0
for i in range(len(path)-1):
    node1 = path[i]
    node2 = path[i+1]
    print(node1,"->",node2, "peso:", dist[node1])
    total+=dist[node1]

print("With a total weight of:", total)