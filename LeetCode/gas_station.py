def can_complete_circuit(gas, cost) -> int:
    if sum(gas) < sum(cost):
        return -1

    total = 0
    start = 0

    for i in range(len(gas)):
        diff = gas[i] - cost[i]

        total += diff

        if total < 0:
            total = 0
            start = i + 1

    return start
