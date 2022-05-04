from collections import Counter


def max_operations(nums, k) -> int:
    count = Counter(nums)
    ans = 0

    for num in nums:
        diff = k - num

        if diff in count and count[diff] > 0 and num in count and count[num] > 0:
            if diff == num and count[diff] <= 1:
                continue
            ans += 1
            count[diff] -= 1
            count[num] -= 1

    return ans
