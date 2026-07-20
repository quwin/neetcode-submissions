class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def calcRob(nums):
            prior = 0
            current = 0
            for num in nums:
                new = max(prior + num, current)

                prior = current
                current = new
            return current

        return max(nums[0], calcRob(nums[1:]), calcRob(nums[:-1]))