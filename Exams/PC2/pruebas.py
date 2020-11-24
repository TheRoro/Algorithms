valores = []
val = 0
num = 0
m = 5
n = 4
nodos = n*m
for i in range(nodos):
    if(val == m):
        val = 0
        num+=1
    valores.append(num)
    val+=1
print(valores)