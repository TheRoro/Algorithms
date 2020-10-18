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
value = [5, 3, 5, 3, 2]
n = len(weight)
cap = 10 #weight capacity
K = [[0 for x in range(cap + 1)] for x in range(n + 1)] 

def knapsack_bottom_up():
    for i in range(n+1):
        for j in range(cap+1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif weight[i-1] <= j:
                val_1 = value[i-1] + K[i-1][j- weight[i-1]]
                val_2 = K[i-1][j]
                K[i][j] = max(val_1,val_2)
            else:
                K[i][j] = K[i-1][j]

knapsack_bottom_up()
for el in K:
    print(el)