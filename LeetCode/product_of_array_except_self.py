def productExceptSelf(self, nums):
    # input: [1, 2, 3, 4]
    # prefix Product: [1, 2, 6, 24]
    # suffix Product: [24, 24, 12, 4]
    # answer: [24, 12, 8, 6]
    # 1: prefix: [] = 1, suffix [24] = 1 * 24 = 24
    # 2: prefix: [1] = 1, suffix [12] = 1  * 12 = 12
    # 3: prefix: [2] = 2, suffix [4] = 2 * 4 = 8
    # 4: prefix: [6] = 6, suffix [] 1 = 6 * 1 = 6
    prefix = []
    suffix = []

    prefixProd = 1
    suffixProd = 1
    for i in range(len(nums)):
        prefixProd *= nums[i]
        suffixProd *= nums[len(nums) - 1 - i]
        prefix.append(prefixProd)
        suffix.append(suffixProd)

    suffix.reverse()

    ans = []
    for i in range(len(nums)):
        prefixVal = 1
        suffixVal = 1

        if i - 1 in range(len(nums)):
            prefixVal = nums[i - 1]

        if i + 1 in range(len(nums)):
            suffixVal = nums[i + 1]

        ans.append(prefixVal * suffixVal)

    return ans
