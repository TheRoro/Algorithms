import math


def coin_change(self, coins, amount: int) -> int:
    memo = [math.inf] * (amount + 1)
    memo[0] = 0

    for coin in coins:
        for j in range(coin, amount + 1):
            memo[j] = min(memo[j - coin] + 1, memo[j])

    return memo[amount] if memo[amount] != math.inf else -1
