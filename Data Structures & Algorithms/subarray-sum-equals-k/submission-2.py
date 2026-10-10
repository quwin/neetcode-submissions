class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Subarrays, not substrings
        # So prefix sums are rly useful
        # prefix[i] - prefix[j] = nums[i::=j]
        prefixCounts: dict[int, int] = {}
        prefixCounts[0] = 1
        runningPrefix = 0
        count = 0
        for num in nums:
            # add to running prefix
            runningPrefix += num

            # Check how many times the necessary prefix nums[i::=j] has appeared
            count += prefixCounts.get(runningPrefix - k, 0)

            curr = prefixCounts.setdefault(runningPrefix, 0)
            prefixCounts[runningPrefix] = curr + 1


        return count