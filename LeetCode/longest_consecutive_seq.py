from collections import Counter


class Solution(object):
    def longestConsecutive(self, nums):
        count = Counter(nums)

        max_sequence = 0

        for n in count:
            if n - 1 in count:
                continue
            else:
                # we are at the start of a subsequence
                actual_count = 0
                actual_value = n
                while actual_value in count:
                    actual_count += 1
                    actual_value += 1

                max_sequence = max(max_sequence, actual_count)

        return max_sequence
