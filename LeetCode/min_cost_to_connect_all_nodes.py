import heapq


def min_cost_connect_points(points) -> int:
    n = len(points)

    # build adjacency list
    adj = {i: [] for i in range(n)}

    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            adj[i].append([dist, j])
            adj[j].append([dist, i])

    # Prim's algorithm O(n^2*log(n))
    total_cost = 0
    visit = set()
    min_heap = [[0, 0]]

    while len(visit) < n:
        cost, index = heapq.heappop(min_heap)
        if index in visit:
            continue

        total_cost += cost
        visit.add(index)

        for neigh in adj[index]:
            nei_cost, nei_index = neigh
            if nei_index not in visit:
                heapq.heappush(min_heap, neigh)

    return total_cost
