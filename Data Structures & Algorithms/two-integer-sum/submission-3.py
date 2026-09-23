class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {}
        for i in range(len(nums)):
            if target - nums[i] in found:
                return [found[target-nums[i]], i]
            found[nums[i]] = i
        return []