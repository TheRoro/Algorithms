def encode(strs):
    encoded_string = ""
    for s in strs:
        encoded_string += str(len(s)) + "#" + s
    return encoded_string


def decode(s):
    strs, i = [], 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        strs.append(s[j + 1:j + 1 + length])
        i = j + 1 + length
    return strs
