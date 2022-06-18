def uncommonFromSentences(s1: str, s2: str):
    list1 = s1.split(" ")  # ["this", "apple", "is", "sweet"]
    list2 = s2.split(" ")  # ["this", "apple", "is", "sour"]

    memo = {}

    for word in list1:
        if word in memo:
            memo[word] += 1
        else:
            memo[word] = 1

    for word in list2:
        if word in memo:
            memo[word] += 1
        else:
            memo[word] = 1

    ans = []

    for word in memo:
        if memo[word] == 1:
            ans.append(word)

    return ans


uncommonFromSentences("this apple is sweet", "this apple is sour")
