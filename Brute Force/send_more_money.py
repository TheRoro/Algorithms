def solutions():
    # letters = ('s', 'e', 'n', 'd', 'm', 'o', 'r', 'y')
    all_solutions = list()
    for s in range(9, -1, -1):
        for e in range(9, -1, -1):
            for n in range(9, -1, -1):
                for d in range(9, -1, -1):
                    for m in range(9, 0, -1):
                        for o in range(9, -1, -1):
                            for r in range(9, -1, -1):
                                for y in range(9, -1, -1):
                                    if len(set([s, e, n, d, m, o, r, y])) == 8:
                                        send = 1000 * s + 100 * e + 10 * n + d
                                        more = 1000 * m + 100 * o + 10 * r + e
                                        money = 10000 * m + 1000 * o + 100 * n + 10 * e + y

                                        if send + more == money:
                                            send = str(send)
                                            more = str(more)
                                            money = str(money)
                                            all_solutions.append(send)
                                            all_solutions.append(more)
                                            all_solutions.append(money)
    return all_solutions

solution = solutions()

print('S =',solution[0][0])
print('E =',solution[0][1])
print('N =',solution[0][2])
print('D =',solution[0][3])

print('M =',solution[1][0])
print('O =',solution[1][1])
print('R =',solution[1][2])
print('E =',solution[1][3])

print('M =',solution[2][0])
print('O =',solution[2][1])
print('N =',solution[2][2])
print('E =',solution[2][3])
print('Y =',solution[2][4])



