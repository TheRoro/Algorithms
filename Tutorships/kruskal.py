class DisjointSet:
    def __init__(self, n):
        self.id = [-1]*n

    def find(self, a):
        if self.id[a] >= 0:
            grandpa = self.find(self.id[a])
            self.id[a] = grandpa
            return grandpa

        return a

    def union(self, a, b):
        parentA = self.find(a)
        parentB = self.find(b)
        if parentA == parentB:
            return

        if -self.id[parentA] < -self.id[parentB]:
            self.id[parentB] += self.id[parentA]
            self.id[parentA] = parentB
        else:
            self.id[parentA] += self.id[parentB]
            self.id[parentB] = parentA

import heapq #heapq = priority queue

def kruskal(adj):
    n = len(adj)
    ans = [[] for _ in range(n)]
    ds = DisjointSet(n)
    edges = []
    for u in range(n): #guardar todas las aristas de forma ascendente
        for v, w in adj[u]:
            heapq.heappush(edges, (w, u, v))

    numEdges = 0
    while numEdges < n-1: #mejora la eficiencia de kruskal
        w, u, v = heapq.heappop(edges)
        if ds.find(u) != ds.find(v):
            ds.union(u, v) #lo mas importante y esto altera el estado de la estructura de datos
            ans[u].append((v, w))
            ans[v].append((u, w))
            numEdges += 1

    return ans

adj = [[(2, 2), (3, 9), (4, 6)],
     [(2, 6), (5, 5)],
     [(0, 2), (1, 6), (6, 6)],
     [(0, 9)],
     [(0, 6), (6, 1)],
     [(1, 5), (6, 4), (7, 4)],
     [(2, 6), (4, 1), (5, 4)],
     [(5, 4)]]


adj2 = [
    [(1,10),(2,5)],
    [(0,10), (2,8), (3,9), (4,25)],
    [(0,5), (1,8), (3,7)],
    [(2,7), (1,9), (4,13)],
    [(1,25), (3,13)]
]


mst = kruskal(adj2)

for i in range(len(mst)):
    for j in range(len(mst[i])):
        print(i, "->", mst[i][j][0], "peso:", mst[i][j][1])
