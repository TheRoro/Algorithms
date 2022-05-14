import heapq
from collections import defaultdict


def network_delay_time(times, n, k) -> int:
    graph = defaultdict(list)
    for source, target, cost in times:
        graph[source].append((target, cost))

    min_heap = [(0, k)]  # first cost, then node because the sorting parameter for the min heap is the first one
    visited = set()
    total_cost = 0

    while min_heap:
        cost, node = heapq.heappop(min_heap)

        if node in visited:
            continue
        visited.add(node)

        total_cost = max(total_cost, cost)

        for new_node, new_cost in graph[node]:
            if new_node not in visited:
                heapq.heappush(min_heap, (cost + new_cost, new_node))

    if len(visited) == n:
        return total_cost

    return -1
