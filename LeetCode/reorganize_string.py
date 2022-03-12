import heapq
from collections import Counter


def reorganizeString(s):
    counter = Counter(s)
    maxHeap = []

    for char in counter:
        cnt = counter[char]
        maxHeap.append([-cnt, char])

    heapq.heapify(maxHeap)

    ans = ""
    temp = None
    while maxHeap or temp:
        if not maxHeap and temp:
            return ""

        cnt, char = heapq.heappop(maxHeap)
        ans += char
        cnt += 1

        if temp:
            heapq.heappush(maxHeap, temp)
            temp = None

        if cnt != 0:
            temp = [cnt, char]

    return ans
