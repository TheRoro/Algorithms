n = 10
dp = [0]*(n+1)
#1,2
k = [1,2,3]
def staircase_bottom_up():
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n+1):
        val = 0
        for j in k:
            if(i-j>=0):
                val+=dp[i-j]
        dp[i] = val

#O(nk)
#staircase_bottom_up()

#print(dp)



#Staircase dynamic
def staircase_dynamic():
    n = 10
    dp = [None]*(n+1)
    k = [1,2]
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n+1):
        total = 0
        for j in k:
            if(i - j >= 0):
                total += dp[i-j]
        dp[i] = total
    print(dp)
staircase_dynamic()


