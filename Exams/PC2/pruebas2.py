valores2 = []
val2 = 0
num2 = 1
m = 5
n = 4
nodos = n*m
for i in range(nodos):
    if(val2 == m):
        val2 = 0
    valores2.append(val2)
    val2+=1
print(valores2)