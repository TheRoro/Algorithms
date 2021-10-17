def left_rotation(a, d):
    size = len(a)
    values = a.copy()

    for i in range(size):
        a[(size - d + i) % size] = values[i]

    return a


print(left_rotation(5, 4))
