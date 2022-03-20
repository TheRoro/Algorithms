def word_pattern(pattern: str, s: str) -> bool:
    words = s.split()

    if len(pattern) != len(words):
        return False

    if len(set(pattern)) != len(set(words)):
        return False

    word_map = {}

    for i in range(len(words)):
        p = pattern[i]
        w = words[i]

        if w not in word_map:
            word_map[w] = p

        elif word_map[w] != p:
            return False

    return True
