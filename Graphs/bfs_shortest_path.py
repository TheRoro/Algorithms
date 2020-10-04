def bfs_shortest():

    adj = [[1, 3],
    [0,2],
    [1,3],
    [0,1,2]]

    used = []

    start = 0
    goal = 2 

    for i in range(len(adj)):
        used.append(False)

    queue = [[start]]

    if start == goal:
        print("You already reached the node!!")
        return
        

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if used[node] == False:
            neighbours = adj[node]
            for nei in neighbours:
                new_path = list(path)
                new_path.append(nei)
                queue.append(new_path)

                if nei == goal:
                    print("The shortest path is", new_path)
                    return
                    
                
            used[node] = True

bfs_shortest()