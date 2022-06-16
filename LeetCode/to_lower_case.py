def isUppercase(c: str) -> bool:
    asc = ord(c)
    if 65 <= int(asc) <= 90:
        return True
    return False


def toLowerCase(s: str) -> str:
    temp = ""
    for c in s:
        if isUppercase(c):
            temp += chr(ord(c) + 32)
        else:
            temp += c
    return temp


toLowerCase("Lovely")
