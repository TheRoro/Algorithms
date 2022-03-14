def findAnagrams(s, p):
    if len(p) > len(s):
        return []

    sCount = {}
    pCount = {}

    # initialize both hashmaps
    for i in range(len(p)):
        sCount[s[i]] = sCount.get(s[i], 0) + 1
        pCount[p[i]] = pCount.get(p[i], 0) + 1

    ans = []

    if sCount == pCount:
        ans.append(0)

    l = 0
    for r in range(len(p), len(s)):

        sCount[s[r]] = sCount.get(s[r], 0) + 1

        sCount[s[l]] -= 1

        if sCount[s[l]] <= 0:
            sCount.pop(s[l])

        l += 1

        if sCount == pCount:
            ans.append(l)

    return ans
