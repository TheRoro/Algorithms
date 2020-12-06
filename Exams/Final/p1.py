from collections import defaultdict
import math

class Graph:
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
 
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
 

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
 
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
 
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
 
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
 
    def KruskalMST(self):
 
        result = []  # This will store the resultant MST
         
        # An index variable, used for sorted edges
        i = 0
         
        # An index variable, used for result[]
        e = 0
 
        # Step 1:  Sort all the edges in 
        # non-decreasing order of their
        # weight.  If we are not allowed to change the
        # given graph, we can create a copy of graph
        self.graph = sorted(self.graph, 
                            key=lambda item: item[2])
 
        parent = []
        rank = []
 
        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
 
        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:
 
            # Step 2: Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
 
            # If including this edge does't
            #  cause cycle, include it in result 
            #  and increment the indexof result 
            # for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
            # Else discard the edge
 
        minimumCost = 0
        #print("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            #print(u, "->", v, "peso:", weight)
        #print("Minimum Spanning Tree" , minimumCost)
        return result
 
S = 2
ubicaciones = [(0,100),(0,300),(0,600),(150,750)]
n = len(ubicaciones)

dist = []


for _ in range(n):
    dist.append([])

for i in range(n):
    dists_i = []
    for j in range(n):
            disty = math.sqrt((ubicaciones[j][0] - ubicaciones[i][0])**2 + (ubicaciones[j][1] - ubicaciones[i][1])**2) 
            dists_i.append(disty)
    dist[i] = dists_i

# for e in dist:
#     print(e)

g = Graph(n)

for i in range(len(dist)):
    for j in range(len(dist[i])):
        if i != j:
            g.addEdge(i, j, dist[i][j])

# g = Graph(5)
# g.addEdge(0, 1, 10)
# g.addEdge(0, 2, 15)
# g.addEdge(1, 3, 19)
# g.addEdge(2, 3, 17)
# g.addEdge(2, 4, 13)
# g.addEdge(3, 4, 11)

ans = g.KruskalMST()

esSatelite = set()
rpta = 0

if(S == 0 or S == 1):
    print("Distancia:", round(ans[-1][2], 2))
    #no alcanzan los satelites para comunicarte
else:
    quitar = S
    i = 0
    ans.reverse()
    while quitar != 0:
        if(ans[i][0] not in esSatelite and ans[i][1] not in esSatelite):
            if (quitar - 2 >= 0):
                quitar-=2
                esSatelite.add(ans[i][0])
                esSatelite.add(ans[i][1])
                rpta+=ans[i][2]
        elif(ans[i][0] not in esSatelite):
            if (quitar - 1 >= 0):
                quitar-=1
                rpta+=ans[i][2]
                esSatelite.add(ans[i][0])
        elif(ans[i][1] not in esSatelite):
            if (quitar - 1 >= 0):
                quitar-=1
                rpta+=ans[i][2]
                esSatelite.add(ans[i][0])
        


        #i+=1
    print("Distancia:", rpta)

