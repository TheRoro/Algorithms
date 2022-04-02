def combination_sum_2(candidates, target):
    candidates.sort()

    ans = []
    combination = []

    def get_combination(index=0, current_sum=0):
        if current_sum == target:
            ans.append(combination.copy())
            return
        if current_sum > target or index >= len(candidates):
            return

        combination.append(candidates[index])
        get_combination(index + 1, current_sum + candidates[index])
        combination.pop(-1)

        while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
            index += 1
        get_combination(index + 1, current_sum)

    get_combination()

    return ans
