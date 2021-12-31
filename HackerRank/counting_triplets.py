def count_triplets(arr, r):
    before = {}
    after = {}
    counter = 0

    for x in arr:
        if x in after:
            after[x] += 1
        else:
            after[x] = 1

    for x in arr:
        after[x] -= 1
        if x % r == 0:
            if (x/r) in before:
                if (x * r) in after:
                    counter += before[(x/r)] * after[(x*r)]
        if x in before:
            before[x] += 1
        else:
            before[x] = 1

    return counter


print(count_triplets([1, 2, 2, 4], 2))
