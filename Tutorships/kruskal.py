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

import heapq

def kruskal(G):
    n = len(G)
    Gprima = [[] for _ in range(n)]
    ds = DisjointSet(n)
    edges = []
    for u in range(n):
        for v, w in G[u]:
            heapq.heappush(edges, (w, u, v))

    numEdges = 0
    while numEdges < n-1:
        w, u, v = heapq.heappop(edges)
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            Gprima[u].append((v, w))
            Gprima[v].append((u, w))
            numEdges += 1

    return Gprima

adj = [[(2, 2), (3, 9), (4, 6)],
     [(2, 6), (5, 5)],
     [(0, 2), (1, 6), (6, 6)],
     [(0, 9)],
     [(0, 6), (6, 1)],
     [(1, 5), (6, 4), (7, 4)],
     [(2, 6), (4, 1), (5, 4)],
     [(5, 4)]]

mst = kruskal(adj)

for i in range(len(mst)):
    for j in range(len(mst[i])):
        print(i, "->", mst[i][j][0], "peso:", mst[i][j][1])
