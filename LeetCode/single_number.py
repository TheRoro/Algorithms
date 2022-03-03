class Solution:
    def singleNumber(self, nums) -> int:
        ans = 0
        for n in nums:
            ans = ans ^ n

        return ans
