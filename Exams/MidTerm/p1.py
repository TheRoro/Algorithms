def solve():
    #change static_list to False in order to input a user generated adjacency list
    static_list = False
    #change nice_output to True in order to get a more clear output
    nice_output = False

    if(static_list):
        adj = [
            [1,4],
            [0,5],
            [3,4,5],
            [2,4],
            [0,2,3,5],
            [1,2,4]
            ]
    else:
        #input nodes starting from 1
        g = [int(x) for x in input().split()]
        g = g[0]
        for i in range(g):
            n, m = [int(x) for x in input().split()]
            adj = []
            for i in range(n):
                adj.append([])
            for i in range(m):
                x, y = [int(x) for x in input().split()]
                x-=1
                y-=1
                adj[x].append(y)
                adj[y].append(x) #remove line of code for directed graphs

            n = len(adj)

            visited = [False]*n

            #color 0 -> not visited
            #color 1 -> black
            #color 2 -> white

            color = [int(0)]*n

            def mark_neighbours(v):
                visited[v] = True
                color[v] = 1
                for u in adj[v]:
                    if visited[u] == False:
                        visited[u] = True
                        color[u] = 2

            #maximize the amount of black nodes
            max_black = 0
            max_color = []

            #you have to start in different positions of
            #the graph in order to generate all the possible combinations
            #For that, we use a queue to change the starting point of the graph
            queue = []

            for i in range(n):
                queue.append(i)


            for every in range(n):
                black = 0
                for v in queue:
                    if visited[v] == False:
                        mark_neighbours(v)
                        #every time we enter to the function we are marking 1 black node
                        black+=1
                #this allows us to change the starting node
                swap = queue.pop(0)
                queue.append(swap)
                
                #then we compare if the new iteration give us a bigger number of black nodes
                if(max_black < black):
                    max_black = black
                    max_color = color
                #then we reset the variables to iterate over the graph again
                color = [int(0)]*n
                visited = [False]*n

            if(nice_output):
                print("The maximum number of black nodes is:", max_black)
                for i in range(n):
                    if max_color[i] == 1:
                        print("Node:", i+1,"-> Black")
                    else:
                        print("Node:", i+1,"-> White")
            else:
                print(max_black)
                for i in range(len(max_color)):
                    if(max_color[i] == 1):
                        print(i+1, end=" ", sep=" ")
                print("")
                garb = [int(x) for x in input().split()]

solve()