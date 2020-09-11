a = [1,4,2,3,6,5,0,7,8,9]

n = len(a)

for i in range(n - 1):
    print(i, "Iteration")
    print(a)
    for j in range(i+1, n):
        if(a[j] < a[i]):
            a[j], a[i] = a[i], a[j]

print("Sorted array")
print(a)    