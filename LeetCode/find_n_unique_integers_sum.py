def sum_zero(n):
    sum_zero_array = []

    for i in range(n // 2):
        sum_zero_array.append(i + 1)
        sum_zero_array.append(-i - 1)

    if n % 2 != 0:
        sum_zero_array.append(0)

    return sum_zero_array
