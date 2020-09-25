import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**32, -1))
sys.setrecursionlimit(10**9)

def solve():
    #input for CSES labyrinth
    n, m = [int(x) for x in input().split()]
    matrix = [[] for x in range(n)]
    for i in range(n):
        matrix[i] = list(input())

    visited = [[False for y in range(m)] for x in range(n)]
    answer = []
    def convert(path):
        s = ""
        for i in range(len(path)-1):
            tup = path[i]
            tup2 = path[i+1]
            #print(tup, tup2)
            if(tup[0] < tup2[0]):
                s+="D"
            if(tup[0] > tup2[0]):
                s+="U"
            if(tup[1] < tup2[1]):
                s+="R"
            if(tup[1] > tup2[1]):
                s+="L"
        return s

    def bfs(x, y):
        queue = [[(x, y)]]
        while queue:
            path = queue.pop(0)
            coord = path[-1]
            if visited[coord[0]][coord[1]] != True:
                neighbours = []
                if(coord[0] + 1 < n and matrix[coord[0] + 1][coord[1]] != '#' and visited[coord[0]+1][coord[1]] == False):
                    neighbours.append((coord[0] + 1, coord[1]))

                if(coord[0] - 1 >= 0 and matrix[coord[0] - 1][coord[1]] != '#' and visited[coord[0]-1][coord[1]] == False):
                    neighbours.append((coord[0] - 1, coord[1]))

                if(coord[1] + 1 < m and matrix[coord[0]][coord[1] + 1] != '#' and visited[coord[0]][coord[1] + 1] == False):
                    neighbours.append((coord[0], coord[1] + 1))

                if(coord[1] - 1 >= 0 and matrix[coord[0]][coord[1] - 1] != '#' and visited[coord[0]][coord[1] - 1] == False):
                    neighbours.append((coord[0], coord[1] - 1))

                #print("Im in position:", coord[0], coord[1])
                #print("My neighbours are:", neighbours)
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    if (matrix[neighbour[0]][neighbour[1]] == 'B'):
                        answer.append("Bailarina 77")
                        print("YES")
                        print(len(new_path)-1)
                        print(convert(new_path))
    
                # mark node as explored
                visited[coord[0]][coord[1]] = True

    for i in range(n):
        for j in range(m):
            if(matrix[i][j] == 'A'):
                bfs(i, j)

    if(len(answer) == 0):
        print("NO")

solve()