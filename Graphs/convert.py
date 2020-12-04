mat = [
    [0, 1, 2, 3, 4, 5]
]
# print(mat)

adj = []
row = 1 #Replace with n, amount of rows
col = 6 #Replace with m, amount of columns
size = row*col

top = []
bottom = []
left = []
right = []
weights = []

for i in range(len(mat)):
    for j in range(len(mat[i])):
        weights.append(mat[i][j])

# print(weights)
for i in range(col):
    top.append(i)

val = size - 1
for i in range(col):
    bottom.append(val)
    val-=1
bottom.sort()

val = 0
for i in range(row):
    left.append(val)
    val+=col

val = col - 1
for i in range(row):
    right.append(val)
    val+=col

# print("TOP is", top)
# print("BOTTOM is", bottom)
# print("LEFT is", left)
# print("RIGHT is", right)

for _ in range(size):
    adj.append([])

for i in range(size):
    friends = [-1, +1, -col, +col]
    nodes = []
    #LEFT TO RIGHT
    if(i not in right):
        nodes.append((i+friends[1], weights[i+friends[1]]))
    #RIGHT TO LEFT
    if(i not in left):
        nodes.append((i+friends[0], weights[i]))
    #TOP TO BOTTOM
    if(i not in bottom):
        nodes.append((i+friends[3], weights[i+friends[3]]))
    #BOTTOM TO TOP
    if(i not in top):
        nodes.append((i+friends[2], weights[i]))
    nodes.sort()
    for e in nodes:
        adj[i].append(e)

for line in adj:
    print(line)
