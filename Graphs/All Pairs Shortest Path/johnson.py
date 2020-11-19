adj = [
[(1,-2)],
[(2,-1)],
[(0,4),(3,2),(4,-3)],
[],
[],
[(3,1),(4,-4)]
]

modified_adj = [
[(1,-2)],
[(2,-1)],
[(0,4),(3,2),(4,-3)],
[],
[],
[(3,1),(4,-4)]
]

infinity = 10**10
negInfinity = -(infinity)
n = len(adj)

def add_extra_node(modified_adj):
    temp_adj = modified_adj
    list_extra = []
    for i in range(len(modified_adj)):
        list_extra.append((i, 0))
    temp_adj.append(list_extra)
    return temp_adj

def print_adj(adj):
    for e in adj:
        print(e)

def bellman_ford(s, adjy):
    adj_bellman = adjy
    n = len(adjy)
    dist = n * [infinity]
    dist[s] = 0
    for i in range(n-1):
        for v in range(n):
            for u, w in adj_bellman[v]:
                if dist[v] + w < dist[u]:
                    dist[u] = dist[v] + w

    for v in range(n):
        for u, w in adj_bellman[v]:
            if dist[v] + w < dist[u]:
                    dist[u] = negInfinity
                    #There's a negative cycle
    return dist


modified_adj = add_extra_node(modified_adj)
temp_node = len(modified_adj)-1 #to define that temporal node is the last one in this implementation

#print_adj(adj)
#print_adj(modified_adj)

temp_dist = bellman_ford(temp_node, modified_adj)

h = temp_dist[0:temp_node]

def replace_negative_edges(adj, h):
    final_adj = []
    for v in range(len(adj)):
        final_adj.append([])
        for u, w in adj[v]:
            new_weight = w + h[v] - h[u]
            tup = (u, new_weight)
            final_adj[v].append(tup)
    return final_adj

final_adj = replace_negative_edges(adj, h)

print_adj(final_adj)

def dijkstra(s, adj):
    dijkstra_adj = adj
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
    dist_i, pred_i = dijkstra(i, final_adj)
    dist.append(dist_i)
    pred.append(pred_i)

for el in pred:
    print(el)
print()

for el in dist:
    print(el)
print()