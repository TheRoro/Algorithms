# Provide the minimum amount of coins given different sets of denominations of coins
# E.g.
# Given a denomination of coins with values of: 1cent, 5cents and 10cents 
# Find out the minimum number of coins required to make a 25cents change.
infinity = 10**5

den = [1,5,10]
k = len(den)

n = 25
dp = [infinity]*(n+1)
s = [0]*(n+1)


dp[0] = 0 #for a change of 0cents we need 0 coins

def coin_change(den, n, k):
    coin = 0
    for i in range(1,n+1):
        mini = infinity
        for j in range(0,k):
            if i >= den[j]:
                mini = min(mini, 1+dp[i-den[j]])
                coin = j
        dp[i] = mini
        s[i] = coin

coin_change(den, n, k)

def build_coin_types():
    l = n
    while l > 0:
        print(s[l], den[s[l]])
        l = l - den[s[l]]


for i in range(int(ene)):
    print("For a change of:", int(m), "cents. ->", dp[int(m)], "coins")
