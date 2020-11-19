adj = [
[(1,20), (2,8), (3,27)],
[(0, 20), (2,6), (4,14)],
[(0, 8), (1,6), (3,7), (4,11)],
[(0,27), (2,7), (4,13)],
[(1,14), (2,11), (3,13)]
]

infinity = 10**10
n = len(adj)
path = []

def dijkstra(s):
    start = s
    dist = n * [infinity]
    pred = n * [None]
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
    return dist, pred

dist = []
pred = []

for i in range(n):
    dist_i, pred_i = dijkstra(i)
    dist.append(dist_i)
    pred.append(pred_i)


for e in pred:
    print(e)
print()

for e in dist:
    print(e)
print()

#Useful functions to get the path, detailed cost, etc
start = 0
end = 4

path = []
def build_path(start, end):
    path.append(end)
    v = pred[start][end]
    while v != None:
        path.append(v)
        v = pred[start][v]
    path.reverse()

build_path(start,end)
print(path)

cost = []
def get_path_cost(start, end):
    v = pred[start][end]
    last = end
    while v != None:
        cost.append(dist[v][last])
        last = v
        v = pred[start][v]
    cost.reverse()

get_path_cost(start, end)
print(cost)

total_cost = 0
total_cost = dist[start][end]
print(total_cost)