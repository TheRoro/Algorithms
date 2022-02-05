def two_sum(nums, target: int):
    memo = {}

    # v1 + v2 = target
    # return i1, i2

    # v1 = target - v2
    # v2 = target - v1

    for i in range(len(nums)):
        if target - nums[i] in memo:
            return [i, memo[target - nums[i]]]
        else:
            memo[nums[i]] = i
