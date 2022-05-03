import math


def find_unsorted_subarray(nums) -> int:
    end = 0
    max_seen = -math.inf

    for i in range(len(nums)):
        max_seen = max(max_seen, nums[i])

        if nums[i] < max_seen:
            end = i

    start = 0
    min_seen = math.inf
    for i in range(len(nums) - 1, -1, -1):
        min_seen = min(min_seen, nums[i])

        if nums[i] > min_seen:
            start = i

    if end > 0:
        return end - start + 1

    return 0
