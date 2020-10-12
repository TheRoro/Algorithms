#A star implementation (not finished)

adj = [
[(1,10),(2,15)],
[(0,10),(3,19)],
[(0,15),(3,17),(4,13)],
[(1,19),(2,17),(4,11)],
[(2,13),(3,11)]
]

start = 0
end = 4

n = len(adj)
infinity = 10**10
dist = n * [infinity]
pred = n * [None]
path = []

heuristic = [(0,14),(1,12),(2,7),(3,6),(4,6)]

def a_star():

    cost = {0: 0}

    dist[start] = 0

    q = set()
    q.add((start, 0))

    goal = False

    closed = []
    opened = [heuristic[start]] # opened = [(0,14)]
    
    while goal == False:
        
        fn = [i[1] for i in opened]
        min_cost = opened[0][1]
        node = opened[0][0]
        for i in range(len(opened)):
            if(opened[i][1] < min_cost):
                min_cost = opened[i][1]
                node = opened[i][0]

        closed.append(node)
        opened.remove((node, min_cost))

        if closed[-1] == end:
            goal = True
            break

        for elem in adj[node]:
            if elem[0] in closed:
                continue
            else:
                cost.update({elem[0]: cost[node] + elem[1]})
                fn_node = cost[node] + elem[1] + heuristic[node][1]
                temp = (elem[0], fn_node)
                opened.append(temp)
                pred[elem[0]] = node

    print(cost)
    print(closed)
    print(pred)
    #Build the path
    v = end
    while v != None:
        path.append(v)
        v = pred[v]
    path.reverse()

    print(path)
a_star()

