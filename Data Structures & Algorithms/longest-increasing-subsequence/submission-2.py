class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * (len(nums)+1)
        dp[0] = 0
        maxLen = 1
        # for each num,
        for i in range(1, len(nums)):
            # for each subsequ starting before,
            for j in range(i, 0, -1):
                # if subsequ strating before ends of lower than num,
                if nums[j-1] < nums[i]:
                    # current subsequ = max of that + 1 or current highest found,
                    dp[i+1] = max(dp[i+1], dp[j]+1)
                    maxLen = max(maxLen, dp[i+1])

        return maxLen