def count_swaps(a):
    counter = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                counter += 1

    print("Array is sorted in", counter, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[-1])


count_swaps([1,2,3])
