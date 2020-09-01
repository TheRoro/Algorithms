def maxElem(a, i, j):
    if i == j:
        return a[i]
    else:
        med = (i+j)//2
        maxi = maxElem(a, i, med)
        maxd = maxElem(a, med+1, j)
        return max(maxi, maxd)

a = [0,1,2,3,6,5,6,7,8,9]
print(maxElem(a, 0, 9))