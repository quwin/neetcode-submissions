class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int t = 0;
        for (int& num : nums) {
            t+=num;
        }
        if (t % 2 != 0) {return false;}
        t /= 2;
        // = whether dp[t] is reachable by target - nums
        vector<bool> dp(t+1, false);
        dp[0] = true;
        for (int& num : nums) {
            for (int i = t; i >= num; i--) {
                dp[i] = dp[i] or dp[i-num];
            }
        }
        return dp[t];
    }
};
