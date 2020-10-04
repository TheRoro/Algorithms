def solve():
    rooms = 0
    n, m = [int(x) for x in input().split()]

    matrix = [[] for x in range(n)]
    for i in range(n):
        matrix[i] = list(input())

    visited = [[False for y in range(m)] for x in range(n)]
        
    def dfs(r, c):
        visited[r][c] = True
        #print("estoy en la posi:", r, c)
        if(r + 1 < n):
            if(matrix[r+1][c] == '@' and visited[r+1][c] == False):
                dfs(r+1, c)
        #... completar ifs


    for i in range(n):
        for j in range(m):
            if(matrix[i][j] == '@' and visited[i][j] == False):
                #print("Un pocket")
                dfs(i, j)

    return rooms

print(solve())