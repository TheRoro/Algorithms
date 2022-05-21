import heapq


class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def add_num(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        if self.small and self.large and -self.small[0] > self.large[0]:
            num = heapq.heappop(self.small)
            num *= -1
            heapq.heappush(self.large, num)

        if len(self.small) > len(self.large) + 1:
            num = heapq.heappop(self.small)
            num *= -1
            heapq.heappush(self.large, num)

        if len(self.large) > len(self.small) + 1:
            num = heapq.heappop(self.large)
            num *= -1
            heapq.heappush(self.small, num)

    def find_median(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.small) < len(self.large):
            return self.large[0]

        return (-1 * self.small[0] + self.large[0]) / 2
