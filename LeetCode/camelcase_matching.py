def camelMatch(self, queries, pattern: str):
    ans = []
    for query in queries:
        j = 0
        otherUppercase = False
        for i in range(0, len(query)):
            if j < len(pattern) and query[i] == pattern[j]:
                j += 1
            elif ord("Z") >= ord(query[i]) >= ord("A"):
                print("hola")
                otherUppercase = True

        if j < len(pattern) or otherUppercase:
            ans.append(False)
        else:
            ans.append(True)

    return ans
