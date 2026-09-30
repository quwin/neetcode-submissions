class Solution {
public:
    int rob(vector<int>& nums) {
        // 1. What does `dp[i]` mean?
            // std::max(dp[i-2] + nums[i], dp[i-1])
        // 2. What is the recurrence?
            // Each spot after, either skip the spot before + take after or take before + skip after
        // 3. What are the base cases?
            // dp[0] = nums[0], dp[1] = max(nums[0], nums[1])
        // 4. In what order must states be computed?
            // linearly
        // 5. Where is the final answer?
            // dp[nums.size()]
        if (nums.size() == 1) {
            return nums[0];
        }
        int priorPrior = nums[0];
        int prior = std::max(nums[0], nums[1]);
        for (int i = 2; i < nums.size(); i++) {
            int temp = std::max(priorPrior + nums[i], prior);
            priorPrior = prior;
            prior = temp;
        }
        return prior;
    }
};
