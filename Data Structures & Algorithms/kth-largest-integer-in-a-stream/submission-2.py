class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = [-1001] * k
        for num in nums:
            heapq.heappush(self.heap, num)
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        heapq.heappop(self.heap)
        return self.heap[0]
