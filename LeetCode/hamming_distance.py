def hamming_solution(x, y):
    xor = bin(y ^ x)
    counter = 0
    for x in xor:
        if x == '1':
            counter += 1

    print(counter)


hamming_solution(1, 3)
