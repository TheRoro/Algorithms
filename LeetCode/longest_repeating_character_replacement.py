def character_replacement(s: str, k: int) -> int:
    count = {}
    l, r = 0, 0
    longest_replace = 0

    while r < len(s):
        count[s[r]] = 1 + count.get(s[r], 0)

        while (r - l + 1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1

        longest_replace = max(longest_replace, r - l + 1)
        r += 1

    return longest_replace
