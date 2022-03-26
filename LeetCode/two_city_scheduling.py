def two_city(costs) -> int:
    diff_costs = []

    for i in range(len(costs)):
        cost_a = costs[i][0]
        cost_b = costs[i][1]

        diff = cost_b - cost_a

        diff_costs.append([diff, cost_a, cost_b])

    diff_costs.sort()

    total = 0

    for i in range(len(diff_costs)):
        if i < len(diff_costs) // 2:
            total += diff_costs[i][2]
        else:
            total += diff_costs[i][1]

    return total
