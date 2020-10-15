n, change = [int(x) for x in input().split()]

coins = [int(x) for x in input().split()]

infinity = (10**6)+1

dp = [0]*(change+1)

mod = 10**9+7

def coins_bottom_up():
    dp[0] = 0
    for coin in coins:
        for j in range(change+1):
            if j >= coin:
                val = dp[j] + 1
                dp[j] = val % mod

coins_bottom_up()

if dp[change] == infinity:
    print(-1)
else:
    print(dp[change])