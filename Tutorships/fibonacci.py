#recursive fibonacci O(2^n) don't use

def fibonacci_rec(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_rec(n-1)+fibonacci_rec(n-2)

#iterative fibonacci O(n) for any query more optimized than recursive (Bottom-up)

def fibonacci_it(n):
    t1, t2 = 0, 1
    for i in range(n+1):
        t, t1, t2 = t1, t2, t1+t2
    return t


#Top-down fibonacci (recursive)
#else is called at maximum n times
n = 10
memo = [None]*(n+1)

def fib_top_down(n, memo):
    if(memo[n] != None):
        return memo[n]
    if(n == 0):
        result = 0
    elif(n == 1):
         result = 1
    else:
        result = fib_top_down(n-1, memo) + fib_top_down(n-2, memo)
    memo[n] = result
    return result

fib_top_down(n, memo)
for el in memo:
    print(el, end=" ")

#Bottom-Up
#dynamic programming fibonacci O(n) to calculate all of the fibonacci secuence
#O(1) for any query

n = 10 #the length of the fibonacci sequence
dp = [-1]*(n+1) #a list to store the values to have a O(1) time

def fibo_dp(n):
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1]+dp[i-2]

    for i in range(len(dp)):
        print(dp[i])

fibo_dp(n)