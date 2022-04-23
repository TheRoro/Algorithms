def combine(n, k):
    #   [1, 2, 3, 4]
    #   []      [1]
    # []     [2]     [1]     [1, 2]

    ans = []
    combination = []

    def get_combinations(index=1):
        if len(combination) == k:
            ans.append(combination.copy())
            return

        for number in range(index, n + 1):
            combination.append(number)
            get_combinations(number + 1)
            combination.pop(-1)

    get_combinations()

    return ans
