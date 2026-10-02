class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        // the result is # of permutations not just combos
        // where dp[i] += dp[i-num]
        vector<int> dp(target +1, 0);
        dp[0] = 1;
        for (int i = 0; i <= target; i++) {
            for (int& num : nums) {
                if (i >= num) {
                    dp[i] += dp[i-num];
                }
            }
        }
        
        return dp[target];
    }
};