def climb_stairs(n: int) -> int:
    t1, t2 = 0, 1

    for i in range(n):
        t1, t2 = t2, t1 + t2

    return t2
