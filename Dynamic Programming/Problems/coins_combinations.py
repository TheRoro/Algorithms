n, change = [int(x) for x in input().split()]

coins = [int(x) for x in input().split()]

infinity = (10**6)+1

dp = [0]*(change+1)

mod = 10**9+7

def coins_bottom_up():
    dp[0] = 1
    for i in range(1, change+1):
        for j in range(len(coins)):
            if i >= coins[j]:
                val = dp[i] + dp[i-coins[j]]
                dp[i] = val % mod

coins_bottom_up()

print(dp[change])
