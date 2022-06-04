class Solution(object):
    def greater(self, a, b):
        if int(str(a) + str(b)) > int(str(b) + str(a)):
            return 1
        return -1

    def largestNumber(self, nums):
        sorted_nums = sorted(nums, cmp=self.greater, reverse=True)
        ans = "".join(map(str, sorted_nums))
        return "0" if ans[0] == "0" else ans
