def roman_to_int(s: str) -> int:
    memo = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    ans = 0

    for i in range(len(s) - 1):
        if memo[s[i]] >= memo[s[i + 1]]:
            ans += memo[s[i]]
        else:
            ans -= memo[s[i]]

    ans += memo[s[-1]]

    return ans
