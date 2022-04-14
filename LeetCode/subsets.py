def subsets(nums):
    res = []
    subset = []

    def get_subsets(index=0):
        if index == len(nums):
            res.append(subset.copy())
            return

        subset.append(nums[index])
        get_subsets(index + 1)

        subset.pop(-1)
        get_subsets(index + 1)

    get_subsets()

    return res
