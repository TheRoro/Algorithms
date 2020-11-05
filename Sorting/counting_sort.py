arr = [1, 0, 4, 3, 8, 7, 2, 5, 9, 6]

def counting_sort():
    mydic = {}
    for el in arr:
        if el in mydic:
            mydic[el]+= 1
        else:
            mydic[el] = 1
    return mydic

mydic = counting_sort()

sortedArray = []

maxi = 0
for el in mydic:
    maxi = max(maxi, el)

for i in range(maxi+1):
    if i in mydic:
        for j in range(mydic[i]):
            sortedArray.append(i)

print(sortedArray)