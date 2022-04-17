def subsets_two(nums):
    res = []
    subset = []
    nums.sort()

    def generate_unique_subsets(index=0):
        if index == len(nums):
            res.append(subset.copy())
            return

        subset.append(nums[index])
        generate_unique_subsets(index + 1)

        subset.pop(-1)

        while index + 1 < len(nums) and nums[index] == nums[index + 1]:
            index += 1

        generate_unique_subsets(index + 1)

    generate_unique_subsets()

    return res
