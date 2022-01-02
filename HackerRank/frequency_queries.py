def freq_queries(queries):
    ds = {}
    freq = {}
    ans = []

    for q in queries:
        op, val = q
        if op != 3:
            freq[ds.get(val, 0)] = max(freq.get(ds.get(val, 0), 0), 1) - 1
            if op == 1:
                ds[val] = ds.get(val, 0) + 1
            else:
                ds[val] = max(ds.get(val, 0), 1) - 1
            freq[ds.get(val, 0)] = freq.get(ds.get(val, 0), 0) + 1

        if op == 3:
            if val in freq and freq[val] >= 1:
                ans.append(1)
            else:
                ans.append(0)

    return ans


print(freq_queries([(1, 3), (2, 3), (3, 2), (1, 4), (1, 5), (1, 5), (1, 4), (3, 2), (2, 4), (3, 2)]))
