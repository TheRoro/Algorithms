def letter_combinations(digits):
    if not digits:
        return []

    letters_map = {
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

    def get_combinations(index, current_str):
        if len(current_str) == len(digits):
            ans.append(current_str)
            return

        letters = letters_map[digits[index]]
        for c in letters:
            get_combinations(index + 1, current_str + c)

    get_combinations(0, "")

    return ans
