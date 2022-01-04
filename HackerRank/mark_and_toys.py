def maximum_toys(prices, k):
    toys = []
    prices.sort()
    for p in prices:
        if p <= k:
            toys.append(p)
            k -= p
        if p > k:
            break
    return len(toys)


maximum_toys([1, 12, 5, 1000, 10000, 10], 50)
