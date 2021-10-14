def hourglass_sum(arr):
    n = len(arr[0])

    h_sums = []
    h_actual = 0

    for i in range(1, n - 1):
        for j in range(1, len(arr[i]) - 1):
            h_actual += arr[i][j]  # central
            h_actual += arr[i - 1][j - 1]  # corners
            h_actual += arr[i - 1][j + 1]
            h_actual += arr[i + 1][j + 1]
            h_actual += arr[i + 1][j - 1]

            h_actual += arr[i + 1][j]  # up and down
            h_actual += arr[i - 1][j]

            h_sums.append(h_actual)
            h_actual = 0

    maxi = -100

    for h in h_sums:
        if maxi < h:
            maxi = h

    return maxi


test = [
    [-9, -9, -9, 1, 1, 1],
    [-9, -9, -9, 1, 1, 1],
    [-9, -9, -9, 1, 1, 1],
    [-9, -9, -9, 1, 1, 1],
    [-9, -9, -9, 1, 1, 1],
    [-9, -9, -9, 1, 1, 1]
]

print(hourglass_sum(test))
