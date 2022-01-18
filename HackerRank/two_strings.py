
def two_strings(s1, s2):
    chars_s1 = set(list(s1))
    chars_s2 = set(list(s2))
    union = chars_s2.intersection(chars_s1)
    if len(union) > 0:
        return "YES"
    else:
        return "NO"


two_strings("hello", "world")

