#recursive fibonacci O(n^2) don't use

def fibonacci_rec(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_rec(n-1)+fibonacci_rec(n-2)

#iterative fibonacci O(n) for any query more optimized than recursive

def fibonacci_it(n):
    t1, t2 = 0, 1
    for i in range(n+1):
        t, t1, t2 = t1, t2, t1+t2
    return t

#dynamic programming fibonacci O(n) to calculate all of the fibonacci secuence
#O(1) for any query

n = 10 #the length of the fibonacci sequence
dp = [-1]*(n) #a list to store the values to have a O(1) time

def fibo_dp(n):
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n):
        dp[i] = dp[i-1]+dp[i-2]
fibo_dp(n)

for i in range(len(dp)):
    print(dp[i])
