def fib1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib1(n - 1) + fib1(n - 2)


def fib2(n):
    t1 = 0
    t2 = 1
    for i in range(n + 1):
        t, t1, t2 = t1, t2, t1 + t2
    return t


def fib3(n):
    dp = [-1] * (n + 1)

    if n < 1:
        return 0

    dp[0] = 0
    dp[1] = 1

    for i in range(2, len(dp)):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
