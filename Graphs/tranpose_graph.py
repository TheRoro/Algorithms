adj = [
[1],
[2],
[0,3],
[]]

# adjtr = [
# [2],
# [0],
# [1],
# [2]]

adjtr = []

for _ in range(len(adj)):
    adjtr.append([])

for i in range(len(adj)):
    for j in adj[i]:
        adjtr[j].append(i)

print(adjtr)