def combination_sum(candidates, target):
    # [1, 2, 3]
    # target: 4
    #     [1]       []
    # [1, 1] [1]    [1]     []

    ans = []
    combination = []

    def get_combinations(candidate_index=0, current_sum=0):
        if current_sum == target:
            ans.append(combination.copy())
            return
        if current_sum > target or candidate_index >= len(candidates):
            return

        combination.append(candidates[candidate_index])
        # Use the same element we are at
        get_combinations(candidate_index, current_sum + candidates[candidate_index])

        combination.pop(-1)
        # we will add the next value in the candidates
        get_combinations(candidate_index + 1, current_sum)

    get_combinations()

    return ans
