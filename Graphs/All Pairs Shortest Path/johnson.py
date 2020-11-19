#Bellman ford implementation
adj = [
[(1,10),(2,15)],
[(0,10),(3,19)],
[(0,15),(3,17),(4,13)],
[(1,19),(2,17),(4,11)],
[(2,13),(3,11)]
]

q = 5

infinity = 10**10
negInfinity = -(infinity)

adjPrima = [
[(1,10),(2,15)],
[(0,10),(3,19)],
[(0,15),(3,17),(4,13)],
[(1,19),(2,17),(4,11)],
[(2,13),(3,11)],
[(0,infinity),(1,infinity),(2,infinity),(3,infinity),(4,infinity)] #nuevo nodo Q
]

start = 0
n = len(adj)
dist = n * [infinity]
pred = n * [None]
path = []
#Complexity of Bellman-Ford O(VE)
def bellman_ford(s):

    dist[s] = 0
    for i in range(n-1):
        for v in range(n):
            for u, w in adjPrima[v]:
                if dist[v] + w < dist[u]:
                    dist[u] = dist[v] + w
                    pred[u] = v

    for v in range(n):
        for u, w in adjPrima[v]:
            if dist[v] + w < dist[u]:
                    dist[u] = negInfinity
                    #pred[u] = None

bellman_ford(start)
print(dist)


def dijkstra(start):

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
                pred[u] = v

for i in range(len(adj)):
    dijkstra(i)
    #print(dist)
    print(pred)
