#Implementation of Floyd Warshall for APSP. Complexity: O(v^3). Where v = vertices
#Recomended for graphs with a lot of edges (Dense graphs)

def floydWarshall(G):
    n = len(G)
    dist = [[10000000]*n for _ in range(n)]
    pred = [[None]*n for _ in range(n)]

    for u in range(n):
        for v, w in G[u]:
            dist[u][v] = w
            pred[u][v] = u

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i != j and k != j and k != i:
                    f = dist[i][k] + dist[k][j]
                    if f < dist[i][j]:
                        dist[i][j] = f
                        pred[i][j] = pred[k][j]

    return pred, dist

adj = [
[(1,20), (2,8), (3,27)],
[(0, 20), (2,6), (4,14)],
[(0, 8), (1,6), (3,7), (4,11)],
[(0,27), (2,7), (4,13)],
[(1,14), (2,11), (3,13)]
]

pred, dist = floydWarshall(adj)

for el in pred:
    print(el)
print()

for el in dist:
    print(el)
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