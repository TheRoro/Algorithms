import heapq
from collections import Counter


def topKFrequent(self, nums, k):
    if k == len(nums):
        return nums

    freq = Counter(nums)

    maxHeap = []

    for val in freq:
        cnt = freq[val]
        maxHeap.append([-cnt, val])

    heapq.heapify(maxHeap)

    index = 0
    res = []

    while index < k:
        cnt, val = heapq.heappop(maxHeap)
        res.append(val)
        index += 1

    return res
