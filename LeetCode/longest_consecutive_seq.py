class Solution(object):
    def longestConsecutive(self, nums):
        dicty = {}
        if len(nums) <= 1:
            return len(nums)

        for n in nums:
            if n not in dicty:
                dicty[n] = 1

        max_len = 0
        act_len = 1
        current = 0
        for n in dicty:
            if n - 1 not in dicty:
                current = n
                while current + 1 in dicty:
                    act_len += 1
                    current += 1
                max_len = max(act_len, max_len)
                act_len = 1
        return max_len