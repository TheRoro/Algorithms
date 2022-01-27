def sherlock_and_anagrams(s):
    counter = {}
    anagrams = 0
    for i in range(len(s)-1):
        for j in range(len(s)):
            s2 = s
            c = s2[j:j+i+1]
            if len(c) == i + 1:
                c = "".join(sorted(c))
                if c in counter:
                    counter[c] += 1
                else:
                    counter[c] = 1

    for c in counter:
        if counter[c] > 1:
            anagrams += (counter[c] * (counter[c] - 1) // 2)

    return anagrams


print(sherlock_and_anagrams("cdcd"))

