from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Keep an ascending list of unique increasing subsequence heads, 
        # Where for dp[i], i = subsequence length, dp[i] = current highest num
        dp = []
        # Minimum of one subsequence with length 1
        dp.append(nums[0])
        for num in nums:
            # If dp.back() is less than num, it's a new possible subsequence
            # With highest num [num]
            if dp[-1] < num:
                dp.append(num)
                continue
            # Otherwise, it must be lower than some existing subsequence
            # And can take over that as the current highest num 
            idx = bisect_left(dp, num) 
            dp[idx] = num
        # len(dp) is equal to the longest subsequence length
        return len(dp)