from sortedcontainers import SortedList

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        outputs = []

        sortedWindow = SortedList([])
        
        for i in range(k):
            sortedWindow.add(nums[i])
        outputs.append(sortedWindow[-1])
        
        for end in range(k, len(nums)):
            sortedWindow.remove(nums[end-k])
            sortedWindow.add(nums[end])
            outputs.append(sortedWindow[-1])

        return outputs