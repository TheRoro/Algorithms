import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**32, -1))
sys.setrecursionlimit(10**9)

n, change = [int(x) for x in input().split()]

coins = [int(x) for x in input().split()]

infinity = (10**6)+1

dp = [infinity]*(change+1)

def coins_bottom_up():
    dp[0] = 0
    for coin in coins:
        for j in range(change+1):
            if j >= coin:
                if dp[j - coin] + 1 < dp[j]:
                    dp[j] = dp[j - coin] + 1

coins_bottom_up()

if dp[change] == infinity:
    print(-1)
else:
    print(dp[change])