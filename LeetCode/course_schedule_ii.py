from collections import defaultdict


def find_order(num_courses, prerequisites):
    adj_list = defaultdict(list)

    for course, pre in prerequisites:
        adj_list[course].append(pre)

    cycle = set()
    visited = set()
    ans = []

    def dfs(course):
        if course in cycle:
            return False

        if course in visited:
            return True

        cycle.add(course)

        for pre in adj_list[course]:
            if not dfs(pre):
                return False

        cycle.remove(course)
        visited.add(course)
        ans.append(course)

        return True

    for i in range(num_courses):
        if not dfs(i):
            return []

    return ans
