class Solution(object):
    def merge(self, intervals):
        overlapping = []
        i = 1
        intervals.sort(key=lambda x: x[0])
        actual = intervals[0]
        while i < len(intervals):
            if actual[1] >= intervals[i][0] and actual[0] <= intervals[i][1]:
                actual = [min(actual[0], intervals[i][0]), max(actual[1], intervals[i][1])]
            else:
                overlapping.append(actual)
                actual = intervals[i]
            i += 1

        overlapping.append(actual)

        return overlapping