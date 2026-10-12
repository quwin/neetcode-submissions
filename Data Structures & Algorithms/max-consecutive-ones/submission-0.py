class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        maxC = 0
        while i < len(nums):
            if nums[i] == 1:
                start = i
                while i < len(nums) and nums[i] == 1:
                    i += 1
                    maxC = max(i - start, maxC)
            else:
                i += 1

        return maxC