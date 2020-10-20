s = [1,3,0,5,3,5,6, 8, 8, 2, 12]
f = [4,5,6,7,9,9,10,11,12,14,16]

def activities_recursive(s, f, i, j):
    m = i + 1
    while m < j and s[m] < f[i]:
        m = m + 1
    if m <= j:
        return ([m] if i > 0 else [0, m] + activities_recursive(s, f, m, j))
    else:
        return []

def activites_iterative(s, f):
    i = 0
    j = len(s)
    resp = [0]
    for m in range(1, j):
        if s[m] < f[i]:
            continue
        resp.append(m)
        i = m
    return resp

print(activities_recursive(s,f,0,10))
print(activites_iterative(s,f))