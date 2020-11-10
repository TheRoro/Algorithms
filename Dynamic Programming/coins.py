change = 40 #I Want the minimum number of coins to get a change of 14
coins = [1,5,10,20,25,50] #The coins of the peruvian empire
#This set of coins is also known as denomination
infinity = 10**5
Memo = [infinity]*(change+1)
R = [None]*(change+1)

def coins_bottom_up(change, coins):
    Memo[0] = 0
    for i in range(len(coins)):
        for j in range(change):
            if(j >= coins[i]):
                if (Memo[j - coins[i]] + 1 < Memo[j]):
                    Memo[j] = 1 + Memo[j - coins[i]]
                    R[j] = i


coins_bottom_up(change+1, coins)
for i in range(len(Memo)):
    print("Para un monto de:", i, "cents, serian", Memo[i], "coins")

change_detail = []

for i in range(change+1):
    change_detail.append([])

def build_coin_types():
    for i in range(change+1):
        l = i
        print("For a change of", i)
        while l > 0:
            print(coins[R[l]], end=" ")
            change_detail[i].append(coins[R[l]])
            l = l - coins[R[l]]
        print(" ")

def build():
    l = 40
    while l > 0:
        print(coins[R[l]])
        l = l - coins[R[l]]
#for i in range(len(Memo)):
#    print(i, "->", Memo[i])

#build_coin_types()
build()
#print(R)
#for i in range(1,len(R)):
#    print(coins[R[i]])

#print(change_detail[40])