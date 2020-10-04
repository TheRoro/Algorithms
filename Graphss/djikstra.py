infinity = 10**10
adj = [[()]] #adjancency list
s = 0 #initial node
dist = [] #distances
pred = [] #predecesors

def dijkstra(s, dist, pred):
    n = len(adj)
    n = 10
    dist = n * [infinity]
    pred = n * [-1]
    used = n * [False]


dijkstra(0, dist, pred)