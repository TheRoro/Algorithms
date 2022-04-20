from collections import defaultdict


def can_finish(num_courses, prerequisites) -> bool:
    adj_list = defaultdict(list)

    for course, pre in prerequisites:
        adj_list[course].append(pre)

    visited = set()

    def dfs(course):
        if course in visited:
            return False

        if not adj_list[course]:
            return True

        visited.add(course)

        for neigh in adj_list[course]:
            if not dfs(neigh):
                return False

        adj_list[course] = []
        visited.remove(course)

        return True

    for i in range(num_courses):
        if not dfs(i):
            return False

    return True
