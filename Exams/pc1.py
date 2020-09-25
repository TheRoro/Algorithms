#Pregunta 1
text = "El correo de juan perez es juan@gmail.com y su contrasena es 12345678"
mydict = {}
for i in range(len(text)):
    if text[i] in mydict:
        val = mydict[text[i]]
        val+=1
        mydict[text[i]] = val
    else:
        mydict[text[i]] = 1
#amortized complexity O(n), accessing in a dict is O(1), cheking if key exists O(1) and adding is O(1)
#print(mydict)

#pregunta 2
#dict of chars, num of occurrences
poem = "con tu rostro en mi mirada, con tu casa en mi frazada"
words = poem.split()
#print(words)

occ = []
for word in words:
    dicty = {}
    for i in range(len(word)):
        if word[i] in dicty:
            val = dicty[word[i]]
            val+=1
            dicty[word[i]] = val
        else:
            dicty[word[i]] = 1
    occ.append(dicty)

#print(occ)
for i in range(len(words)):
    print("Similar words to:", words[i])
    for j in range(i+1, len(words)):
        val = 0
        #print("Word:", words[j])
        for ele in occ[j]:
            if ele in occ[i]:
                #print(ele)
                val+=1
        if(val >= 2):
            print(words[j])
                


#pregunta 3
#DFS
adj = [[1,3,4],
    [0,2],
    [1,3,5],
    [0,2,4,5],
    [0,3,5],
    [2,3,4]]

n = len(adj)
visited = n * [False]
def dfs(v):
    print("I'm in node: E", v+1, sep="")
    visited[v] = True
    for u in adj[v]:
        if visited[u] == False:
            dfs(u)

#dfs(0)
#BFS
used = n * [False]
q = []
def bfs(s):
    q.append(s)
    used[s] = True
    while q:
        v = q.pop(0)
        print("I'm in node: E", v+1, sep="")
        for u in adj[v]:
            if(used[u] == False):
                used[u] = True
                q.append(u)

#bfs(0)

#pregunta 4, muy tryhard 