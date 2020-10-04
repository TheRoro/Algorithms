#My excellent brute force solution

s = "babababababaababa"
sjunior = "ba"
cont = 0
ocurrences = 0
n = len(s)
for i in range(n):
    pointer = i
    for j in range(len(sjunior)):
        if(pointer + 1 <= len(s) and sjunior[j] == s[pointer]):
            pointer+=1
            cont+=1
    if (cont == len(sjunior)):
        ocurrences+=1
    cont = 0
print("My solution:", ocurrences)

#Python laughing at me

stri = "babababababaababa"
substr = "ba"
print("Python's solution:", stri.count(substr))