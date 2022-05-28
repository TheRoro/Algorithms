def length_of_longest_substring(s: str) -> int:
    # "abc d"
    # "5, 3, 4"

    characters = set()
    l, r = 0, 0
    max_substring = 0

    while r < len(s):
        while s[r] in characters:
            characters.remove(s[l])
            l += 1

        characters.add(s[r])
        r += 1
        max_substring = max(max_substring, len(characters))

    return max_substring
