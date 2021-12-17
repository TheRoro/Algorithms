def array_manipulation(n, queries):
    arr = [0] * n
    maxi = 0
    accumulation = 0

    for q in queries:
        arr[q[0] - 1] += q[2]
        if q[1] < len(arr):
            arr[q[1]] -= q[2]

    for val in arr:
        accumulation += val
        maxi = max(accumulation, maxi)

    return maxi


print(array_manipulation(5, [[2, 4, 7], [1, 3, 1], [3, 5, 13]]))
