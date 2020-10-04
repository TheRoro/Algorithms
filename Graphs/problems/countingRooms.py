#import resource, sys
#resource.setrlimit(resource.RLIMIT_STACK, (2**32, -1))
#sys.setrecursionlimit(10**9)

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
        #VALIDAR EN CRUZ ARRIBA ABAJO DERECHA IZQUIERA
        if(r + 1 < n):
            if(matrix[r+1][c] == '@' and visited[r+1][c] == False):
                dfs(r+1, c)
        if(r - 1 >= 0):
            if(matrix[r-1][c] == '@' and visited[r-1][c] == False):
                dfs(r-1, c)
        if(c - 1 >= 0):
            if(matrix[r][c-1] == '@' and visited[r][c-1] == False):
                dfs(r, c-1)
        if(c + 1< m):
            if(matrix[r][c+1] == '@' and visited[r][c+1] == False):
                dfs(r, c+1)
        
        #VALIDAR LAS ESQUINAS
        if(r + 1 < n and c + 1 < m):
            if(matrix[r+1][c+1] == '@' and visited[r+1][c+1] == False):
                dfs(r+1, c+1)
        if(r - 1 >= 0 and c + 1 < m):
            if(matrix[r-1][c+1] == '@' and visited[r-1][c+1] == False):
                dfs(r-1, c+1)
        if(r - 1 >= 0 and c - 1 >= 0):
            if(matrix[r-1][c-1] == '@' and visited[r-1][c-1] == False):
                dfs(r-1, c-1)
        if(r + 1 < n and c - 1 >= 0):
            if(matrix[r+1][c-1] == '@' and visited[r+1][c-1] == False):
                dfs(r+1, c-1)


    for i in range(n):
        for j in range(m):
            if(matrix[i][j] == '@' and visited[i][j] == False):
                #print("Un pocket")
                dfs(i, j)
                rooms+=1

    return rooms

print(solve())
