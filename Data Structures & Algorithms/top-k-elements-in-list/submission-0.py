class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        return [item[0] for item in sorted(count.items(), key=lambda item: item[1], reverse=True)[:k]]