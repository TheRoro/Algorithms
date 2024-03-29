def majority_element(nums) -> int:
    ans, count = 0, 0

    for n in nums:
        if count == 0:
            ans = n

        if ans != n:
            count -= 1
        else:
            count += 1

    return ans
