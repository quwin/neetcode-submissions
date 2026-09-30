class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        // What does dp[i] mean?:
            // The min cost to reach that step
        // What is the recurrence?: 
            // The min cost of reaching a step =
            // min(cost[i-1] + dp[i-1], cost[i-2] + dp[i-2])
        // What are the base cases?: 
            // dp[0] = 0, dp[1] = 0
        // In what order must states be computed?: 
            // linearly
        // Where is the final answer?: 
            // dp[cost.size()]
        vector<int> dp(cost.size()+1, 0);
        for (int i = 2; i < dp.size(); i++) {
            dp[i] = std::min(cost[i-1] + dp[i-1], cost[i-2] + dp[i-2]);
        }
        return dp[cost.size()];
    }
};
