t = int(input())

for _ in range(t):
    n = int(input())
    m = int(input())
    adj = []
    for _ in range(n):
        li = [int(x) for x in input().split()]
        adj.append(li)
    #print(t)
    #print(n, m)
    #print(adj)


    nodos = n*m
    start = 0
    finish = nodos - 1
    garb = []
    adjREAL = []
    valores = []
    val = 0
    num = 0
    for i in range(nodos):
        if(val == m):
            val = 0
            num+=1
        valores.append(num)
        val+=1
    #print(valores)

    valores2 = []
    val2 = 0
    num2 = 1
    for i in range(nodos):
        if(val2 == m):
            val2 = 0
        valores2.append(val2)
        val2+=1
    #print(valores2)


    for i in range(nodos):
        nodes = []
        #vertical connections
        conditions = [-m, +m]
        for j in range(len(conditions)):
            node = i + conditions[j]
            if(node >= 0 and node <= nodos - 1):
                if(i+1 < nodos):
                    nodes.append((node, adj[valores[i+1]][valores2[i+1]]))

        #horizontal connections
        condi = [-1, +1]
        for j in range(len(condi)):
            node = i + condi[j]
            if(node % m == 0 and (i - (m-1)) % m == 0):
                garb.append("No agrego")
            elif(i % m == 0 and j == 0):
                garb.append("No agrego")
            elif(node >= 0 and node <= nodos - 1):
                if(i+1 < nodos):
                    nodes.append((node, adj[valores[i+1]][valores2[i+1]]))
                
        nodes.sort()
        adjREAL.append(nodes)
    #print(adjREAL)
    start = 0
    end = nodos - 1
    infinity = 1000000000
    dist = nodos * [infinity]
    pred = nodos * [None]
    path = []

    def dijkstra():

        dist[start] = 0

        q = set()
        q.add((start, 0))

        while q:
            v = q.pop()[0] # 0 es v

            for elem in adjREAL[v]:
                u = elem[0] #adjacent node -> 1
                weight = elem[1] #weight asociated to that adjacent node -> 10

                if dist[v] + weight < dist[u]:
                    q.discard((u, dist[u]))
                    dist[u] = dist[v] + weight
                    q.add((u, dist[u]))
                    pred[u] = v

    dijkstra()

    def restore_path():
        v = end
        while v != None:
            path.append(v)
            v = pred[v]
        path.reverse()

    dijkstra()
    restore_path()
    #print(pred)
    #print(dist)

    #print("The shortest path is:", path)
    print(dist[end])