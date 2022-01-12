def num_jewels_in_stones(jewels, stones):
    counter = 0
    memo = {}

    for c in jewels:
        if c in memo:
            memo[c] += 1
        else:
            memo[c] = 1

    for c in stones:
        if c in memo:
            counter += 1

    return counter


print(num_jewels_in_stones("z", "ZZ"))
