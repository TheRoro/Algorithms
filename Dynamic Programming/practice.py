def recursion(n):
    if n == 0:
        return 1
    else:
        return recursion(n-1)


n = 20
memo = [None]*(n+1)

def recu(n, memo):
    if memo[n] != None:
        return memo[n]
    if n == 0:
        value = 0
    else:
        value = recu(n-1, memo) + 1
    memo[n] = value
    return value

recu(n, memo)

for el in memo:
    print(el, end=" ")