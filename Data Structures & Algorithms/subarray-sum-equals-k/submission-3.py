class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # looking for specific subarray #: use PrefixSum + HashMap 
        prefixCounts = {0 : 1}
        runningPfx = count = 0
        for num in nums:
            runningPfx += num
            count += prefixCounts.get(runningPfx - k, 0)
            prefixCounts[runningPfx] = prefixCounts.setdefault(runningPfx, 0) + 1
        return count
