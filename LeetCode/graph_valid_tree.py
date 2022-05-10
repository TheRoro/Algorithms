def valid_tree(n: int, edges) -> bool:
    if n == 0:
        return True

    adj = {i: [] for i in range(n)}
    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)

    visited = set()

    def dfs(actual=0, prev=-1):
        if actual in visited:
            return False

        visited.add(actual)

        for neigh in adj[actual]:
            if neigh == prev:
                continue
            if not dfs(neigh, actual):
                return False

        return True

    return dfs() and n == len(visited)
