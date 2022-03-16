def letterCombinations(digits):
    if not digits:
        return []

    lettersMap = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    ans = []

    def getCombinations(index, currentStr):
        if len(currentStr) == len(digits):
            ans.append(currentStr)
            return

        letters = lettersMap[digits[index]]
        for c in letters:
            getCombinations(index + 1, currentStr + c)

    getCombinations(0, "")

    return ans
