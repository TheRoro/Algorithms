
adj = []

n, m = [int(x) for x in input().split()]

for i in range(n):
    adj.append([])

for i in range(m):
    x,y,z = [int(r) for r in input().split()]
    x-=1
    y-=1
    adj[x].append((y,z))

print(adj)
