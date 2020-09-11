#Nlog(n) unnecessary algorithm implementation, just for learning resources
# A lineal scan is way more efficient since n < nlogn
#don't use
#please

def wordCount(s, i, j, words):
    if i == j:
        if s[i] == " ":
            return words+1
        else:
            return 0
    else:
        med = (i+j)//2
        left = wordCount(s, i, med, words)
        right = wordCount(s, med+1, j, words)
        return left+right

s = "How many words are here?"
print(wordCount(s, 0, len(s)-1, 0) + 1)