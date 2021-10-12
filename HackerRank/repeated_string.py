def count_a(size, string):
    a_counts = 0
    for i in range(size):
        if string[i] == "a":
            a_counts += 1
    return a_counts


def repeated_string(s, n):
    string_size = len(s)
    noa = 0
    ans = 0

    nos = n // string_size
    rest = n % string_size

    noa = count_a(string_size, s)
    ans = noa * nos

    noa = count_a(rest, s)
    ans += noa
    return ans


print(repeated_string("a", 1000000000000))
