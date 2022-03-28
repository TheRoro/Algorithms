def max_frequency(nums, k: int) -> int:
    nums.sort()

    l, r = 0, 0
    res, total = 0, 0

    while r < len(nums):
        total += nums[r]

        while nums[r] * (r - l + 1) > k + total:
            total -= nums[l]
            l += 1

        res = max(r - l + 1, res)
        r += 1

    return res
