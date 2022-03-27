def count_substrings(s):
    count = 0
    for i in range(len(s)):
        l = r = i
        # count even length palindromes
        count += count_palindromes(s, l, r)

        r = i + 1
        # count odd length palindromes
        count += count_palindromes(s, l, r)

    return count


def count_palindromes(s, l, r):
    count = 0

    while l >= 0 and r < len(s) and s[l] == s[r]:
        count += 1
        l -= 1
        r += 1

    return count
