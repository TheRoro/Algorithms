def my_sqrt(x) -> int:
    l, r = 0, x

    while l <= r:
        mid = (l + r) // 2

        if mid * mid == x:
            return mid

        if mid * mid > x:
            r = mid - 1
        else:
            l = mid + 1

    return r
