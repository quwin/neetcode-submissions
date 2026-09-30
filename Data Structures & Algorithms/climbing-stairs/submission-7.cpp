class Solution {
public:
    int climbStairs(int n) {
        // State: Ways to climb to step 
        // Recurrence: = Ways to climb to 2 + 1 steps before
        // Base cases: 1 -> 1, 2 -> 2
        // Iteration order: bottom up
        // Can the state be compressed? Yes
        vector<int> steps{1,2};
        for (int i = 2; i < n; i++) {
            steps[i%2] = steps[0] + steps[1];
        }
        return steps[n%2 == 0]; // 0 => 1, 1 => 0
    }
};
