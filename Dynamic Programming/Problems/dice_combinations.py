n = [int(x) for x in input().split()]
n = n[0]
dice = [1,2,3,4,5,6]

infinity = (10**6)+1

dp = [0]*(n+1)

mod = 10**9+7

def dice_bottom_up():
    dp[0] = 1
    for i in range(1, n+1):
        for j in range(len(dice)):
            if i >= dice[j]:
                val = dp[i] + dp[i-dice[j]]
                dp[i] = val % mod

dice_bottom_up()

print(dp[n])
