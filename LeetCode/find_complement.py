def findComplement(num: int) -> int:
    binstr = bin(num)[2:]
    ans = []
    for c in binstr:
        if c == '0':
            ans.append('1')
        else:
            ans.append('0')

    return int(''.join(ans), 2)
