class Solution:
    def missingNumber(self, nums) -> int:
        nums_sum = (len(nums)) / 2 * (1 + len(nums))

        for n in nums:
            nums_sum -= n

        return int(nums_sum)
