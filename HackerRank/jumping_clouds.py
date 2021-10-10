def jumpingOnClouds(c):
    i = 0
    result = 0
    while i < len(c):
        if i + 2 < len(c) and c[i] == 0 and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        result += 1
    return result - 1


print(jumpingOnClouds([0, 0, 0, 0, 1, 0]))
