import heapq

class MedianFinder:
    def __init__(self):
        self.lower = []  # Max-heap, uses Negative Values to ensure order
        self.upper = []  # Min-heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lower, -num)
        heapq.heappush(self.upper, -heapq.heappop(self.lower))

        # Keep lower equal in size or one element larger.
        if len(self.upper) > len(self.lower):
            heapq.heappush(self.lower, -heapq.heappop(self.upper))

    def findMedian(self) -> float:
        if len(self.lower) > len(self.upper):
            return float(-self.lower[0])

        return (-self.lower[0] + self.upper[0]) / 2.0
        