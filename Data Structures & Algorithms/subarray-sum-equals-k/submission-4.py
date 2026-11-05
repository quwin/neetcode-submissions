class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Given an array of integers and a target sum
        # How many subarrays of the integers reach that target sum?
        # The initial approach that comes to my mind is to iterate over
        # every single subarray, and calculate their sums
        # Then, if the sum is equal to the target, increase the count by 1
            # This would be O(n^2) time, O(1) space
        # However, there exists another opportunity to speed this process up
        # By caching prior subarray sums
        # The sum of a subarray between i and j (assume j >= i) is equal to
        # The difference between the array from 0 to j and 0 to i
        # Because the subarray from 0 to i cancels itself out
        # Therefore, moving one step allows you to easily calculate the subarray
        # Between that step and all previous steps
        # This caches the math, but you still have to check every other idx for
        # each idx
        # Because we are looking for a specific target, we can see if the
        # prefixSum (subarray from 0 to j) - target is equal to some 
        # subarray from 0 to i. If so, the number of times that target is a 
        # reachable subarray is added to the count
        # We need to keep track of a prefixSum, a map of prefixSum x counts
        # and default 0 : 1 because a prefixSum of 0 is always reachable with
        # an empty array
        prefix_sum = 0
        result = 0
        counts = {0: 1}

        for num in nums:
            prefix_sum += num

            result += counts.get(prefix_sum - k, 0)

            counts[prefix_sum] = counts.get(prefix_sum, 0) + 1

        return result

        