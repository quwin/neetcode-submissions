class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        // State: LIS ending at nums[i]
        // Transition: take vs skip each new i
            // take, LIS + 1
            // skip, LIS
        vector<int> dp(nums.size() + 1, 0);
        int lis = 1;
        for (int i = nums.size()-1; i > -1; i--) {
            int curr = 1;
            for (int j = nums.size()-1; j > i; j--) {
                if (nums[i] < nums[j]) {
                    curr = max(dp[j]+1, curr);
                }
            }
            dp[i] = curr;
            lis = max(dp[i], lis);
        }
        return lis;
    }
};
