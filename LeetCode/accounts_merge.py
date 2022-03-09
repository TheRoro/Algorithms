from collections import defaultdict


def accountsMerge(self, accounts):
    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])

        return parents[x]

    def union(x, y):
        r1 = find(x)
        r2 = find(y)

        if r1 != r2:
            parents[r2] = r1

    parents = {}
    emailToName = {}

    for act in accounts:
        name = act[0]
        emails = act[1:]
        for email in emails:
            emailToName[email] = name
            parents[email] = email

    for act in accounts:
        email1 = act[1]
        emails = act[2:]

        for email2 in emails:
            union(email1, email2)

    groups = defaultdict(list)

    for email in parents:
        root = find(email)
        groups[root].append(email)

    ans = []

    for key in groups:
        name = emailToName[key]
        emails = sorted(groups[key])
        ans.append([name] + emails)

    return ans
