change = 13 #I Want the minimum number of coins to get a change of 13
coins = [1,5,10,20,50] #The coins of the peruvian empire
#This set of coins is also known as denomination
infinity = 10**5
Memo = [infinity]*(change+1)

def coins_bottom_up(change, coins):
    Memo[0] = 0
    for coin in coins: # 1 5 10 20 50
        for j in range(change): # 0 1 2 3 4 5....
            if(j >= coin):
                if (Memo[j - coin] + 1 < Memo[j]):
                    Memo[j] = Memo[j - coin] + 1

bottom_up = False
if bottom_up:
    coins_bottom_up(change+1, coins)
    for i in range(len(Memo)):
        print("Para un monto de:", i, "cents, serian", Memo[i], "coins")


#Coins top-down
change = 40
coins = [1,5,10,20,25,50]
infinity = 10**5
Memo = [infinity]*(change+1)
R = [None]*(change+1)

def coins_top_down(change, coins, memo):
    if change == 0 or change == 1:
        value = change #cuando el vuelto es 0 necesito 0 coins cuando es 1 necesito 1 coin
        memo[change] = value
        R[change] = 0
        return value
    else:
        mini = infinity
        for i in range(len(coins)):
            if coins[i] <= change:
                value = coins_top_down(change - coins[i], coins, memo)
                R[change] = i
            if value < mini:
                mini = value + 1
                
        memo[change] = mini
        return mini

top_down = True
if top_down:
    coins_top_down(change, coins, Memo)

def build():
    l = 39
    print("Para un valor de:", l, "necesito monedas de:")
    while l > 0:
        print(coins[R[l]], sep=" ")
        l = l - coins[R[l]]

build()