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
dist = n * [infinity]
pred = n * [None]
path = []

def a_star():

    dist[start] = 0

    q = set()
    q.add((start, 0))

    goal = False

    while q and !goal:
        v = q.pop()[0]

        for elem in adj[v]:
            u = elem[0]
            weight = elem[1]

            #Heuristic

            if u == end:
                goal = True
                break


a_star()