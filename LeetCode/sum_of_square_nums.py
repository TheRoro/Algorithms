from math import sqrt


def judge_square_sum(c: int) -> bool:
    # a^2 + b^2 = c
    # b^2 = c - a^2

    square = int(sqrt(c))

    for i in range(square + 1):
        a = i ** 2
        b = sqrt(c - a)

        if b == int(b):
            return True

    return False
