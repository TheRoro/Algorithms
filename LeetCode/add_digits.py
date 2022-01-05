def add_digits(num):
    while len(str(num)) > 1:
        temp = 0
        for x in str(num):
            temp += int(x)
        num = temp
    return num


print(add_digits(38))
