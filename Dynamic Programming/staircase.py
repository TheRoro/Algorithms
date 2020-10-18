#Dada una escalera de tamaño N (con N escalones)
#Y dada una denominación de pasos posibles que puedes dar
#Ejemplo pasos de 1 o pasos de 2
#Determine la cantidad de formas que hay de subir esa escalera

n = 10
dp = [None]*(n+1)


def num_ways_static():
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
#num_ways_static()
#print(dp)

def num_ways():
    n = 10
    dp = [None]*(n+1)
    k = [1,2]
    dp[0] = 1
    for i in range(1, n+1):
        total = 0
        for j in k:
            if(i - j >= 0):
                total += dp[i-j]
        dp[i] = total
    print(dp)
num_ways()
#print(dp)