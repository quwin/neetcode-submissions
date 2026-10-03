class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        // State: max len of IS ending in nums[i]
        vector<int> dp(nums.size(), 0);
        int maxLIS = 1;
        for (int i = 0; i < nums.size(); i++) {
            int currMax = 1;
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    currMax = max(dp[j]+1, currMax);
                }
            }
            dp[i] = currMax;
            maxLIS = max(maxLIS, dp[i]);
        }
        return maxLIS;
    }
};
