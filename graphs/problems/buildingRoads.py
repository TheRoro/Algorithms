import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**32, -1))
sys.setrecursionlimit(10**9)

def solve():
    n, m = [int(x) for x in input().split()]

    adj = [[] for x in range(n)]

    conn = []

    for i in range(m):
        x, y = [int(x) for x in input().split()]
        x-=1
        y-=1
        adj[x].append(y)
        adj[y].append(x)
    
    visited = [False for y in range(n)]

    def dfs(v):
        visited[v] = True
        for u in adj[v]:
            if(visited[u] == False):
                dfs(u)
    
    for i in range(n):
        if visited[i] == False:
            conn.append(i)
            dfs(i)

    print(len(conn)-1)
    for i in range(len(conn) -1):
        print(conn[i] + 1, conn[i+1] + 1)

solve()
