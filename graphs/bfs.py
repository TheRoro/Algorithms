from collections import deque

adj = [[1, 3],
[0,2],
[1,3],
[0,1]]

used = []
s = 0
q = []

for i in range(len(adj)):
    used.append(False)

def bfs():
    q.append(s)
    used[s] = True
    while(q):
        v = q.pop(0)
        print("i'm in node:", v)
        for u in adj[v]:
            if(used[u] == False):
                used[u] = True
                q.append(u)

bfs()