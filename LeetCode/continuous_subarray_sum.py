def checkSubarraySum(self, nums, k) -> bool:
    # 23, 2, 4, 6, 7
    # 23, 25, 29, 35, 42
    # 23 % 6 = 5
    # 25 % 6 = 1
    # 29 % 6 = 5

    prefixSum = {0: -1}
    currentSum = 0

    for i in range(len(nums)):
        currentSum += nums[i]
        remainder = currentSum % k

        if remainder in prefixSum and i - prefixSum[remainder] >= 2:
            return True

        if remainder not in prefixSum:
            prefixSum[remainder] = i

    return False