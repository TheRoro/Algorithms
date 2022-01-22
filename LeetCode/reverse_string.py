def reverse_string(s) -> None:
    for i in range(len(s) // 2):
        s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]
    print(s)


reverse_string(["h", "e", "l", "l", "o"])
