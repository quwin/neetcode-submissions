class Solution {
public:
    bool canPartition(vector<int>& nums) {
        // Subproblem: 
            // Can a sequence of nums in nums equals a target val
        // Relation: 
            // dp[t][0] = whether t can be made from sums nums[0]
        // Topological Order: 
            // until sum/2, see if i - num for each num is possible
        // Base cases:
            // dp[nums[0]][i] = true
        // Original Problem:
            // dp[sum/2][0]
        // Time analysis:
            // O(n * m)
        int sum = 0;
        for (int& num : nums) {
            sum += num;
        }
        if (sum % 2 != 0 || nums.size() == 1) {
            return false;
        }
        // bc the ans must be reachable from any start,
        // O(n) instead of O(n2) just using 1st element
        int start = nums[0];
        vector<vector<bool>> dp((sum/2)+1, vector<bool>(nums.size(), false));
        for (int i = 0; i < nums.size(); i++) {
            dp[start][i] = true;
            dp[0][i] = true;
        }
        for (int t = start+1; t <= sum/2; t++) {
            for (int i = 1; i < nums.size(); i++) {
                if (t >= nums[i]) {
                    if (dp[t][0]) {
                        dp[t][i] = true;
                    } else {
                        dp[t][0] = dp[t][0] or dp[t-nums[i]][i];
                    }
                    dp[t-nums[i]][i] = false;
                }
            }
        }
        return dp[sum/2][0];
    }
};
