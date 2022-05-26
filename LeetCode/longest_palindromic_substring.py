def expand_palindrome(l, r, s, max_len, max_palindrome):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        if (r - l + 1) > max_len:
            max_len = (r - l + 1)
            max_palindrome = s[l:r + 1]
        l -= 1
        r += 1

    return max_len, max_palindrome


def longest_palindrome(s: str) -> str:
    max_palindrome = ""
    max_len = 0
    for i in range(len(s)):
        max_len, max_palindrome = expand_palindrome(i, i, s, max_len, max_palindrome)
        max_len, max_palindrome = expand_palindrome(i, i + 1, s, max_len, max_palindrome)

    return max_palindrome
