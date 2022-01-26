def checkMagazine(magazine, note):
    chars = {}
    char_not_found = False

    for c in magazine:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1

    for c in note:
        if c in chars:
            if chars[c] == 0:
                print("No")
                char_not_found = True
                break
            chars[c] -= 1
        else:
            print("No")
            char_not_found = True
            break

    if not char_not_found:
        print("Yes")
