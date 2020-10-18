#Given a set of items with value and weight
#Determine the number of each item to include so
#That we have the maximum value without exceeding the 
#knapsack capacity
#For this question, we will only determine the maximum value
#Given that you can only select 1 of each item or none of it
# State = Selected or Not Selected = 0 or 1

weight = [None, 1, 2, 4, 2, 5]
value = [None, 5, 3, 5, 3, 2]
n = len(weight)-1
cap = 10 #weight capacity

#Naive Solution

def calc(n, cap):
    if n == 0 or cap == 0:
        result = 0
    elif weight[n] > cap:
        result = calc(n-1, cap)
    else:
        tmp1 = calc(n-1, cap)
        tmp2 = value[n] + calc(n-1, cap - weight[n])
        result = max(tmp1, tmp2)
    return result 

#ans = calc(n, capacity)
#print(ans)




weight = [1, 2, 4, 2, 5]
value  = [5, 3, 5, 3, 2]
k = len(weight)
cap = 10 #weight capacity
Memo = [[0 for x in range(cap + 1)] for x in range(k + 1)] 

def knapsack_bottom_up():
    for i in range(k+1): # elementos manzana chamito turron ...
        for j in range(cap+1): #capacidaddes 0 1 2 3 4 5.. 10
            if i == 0 or j == 0:
                Memo[i][j] = 0
            elif weight[i-1] <= j:
                val_1 = value[i-1] + Memo[i-1][j - weight[i-1]]
                val_2 = Memo[i-1][j]
                Memo[i][j] = max(val_1,val_2)
            else:
                Memo[i][j] = Memo[i-1][j]

knapsack_bottom_up()

#print(K)
for el in Memo:
    print(el)

print(Memo[k][cap])