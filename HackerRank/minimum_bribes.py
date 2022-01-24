def minimum_bribes(q):
    nob = 0
    chaotic = False
    temp_q = q.copy()
    positions = {}
    for i in range(len(q)):
        if q[i] in positions:
            continue
        else:
            positions[q[i]] = i

    for i in range(len(q)):
        maxi = len(q) - i
        pos = positions[maxi]
        diff = maxi - (pos + 1)
        if diff <= 2:
            nob += diff
            for j in range(diff):
                temp_q[j + pos] = temp_q[j + pos + 1]
                positions[temp_q[j + pos]] = j + pos
            temp_q[pos + diff] = maxi
            positions[maxi] = pos + diff
        else:
            chaotic = True
            print("Too chaotic")
            break

    if not chaotic:
        print(nob)


minimum_bribes([2, 1, 5, 3, 4])
