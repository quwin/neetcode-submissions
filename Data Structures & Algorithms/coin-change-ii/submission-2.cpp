class Solution {
public:
    int change(int amount, vector<int>& coins) {
        // Subproblem: 
            // For static vec<int> coins
            // # of distinct combos for an amount
        // Relation:
            // # of distinct combos = 
            // sum(# of combos for each coin to reach amount)
        // Topological Order: 
            // For each coin, add ways it can be used to reach amount
            // This order tracks each side of equation once:
                // 1 + 3 = 4 doesn't count 3 + 1 = 4
        // Base cases:
            // dp[0] = 1, 1 way to reach 0 (no coins)
        // Original Problem:
            // subproblem for amount
        // Time analysis: 
            // O(n * m), O(m) space
        vector<int> dp(amount + 1, 0);
        dp[0] = 1;
        // coin -> amount for combinations,
        // amount -> coin for permutations
        for (auto& coin: coins) {
            for (int i = coin; i < amount+1; i++) {
                dp[i] += dp[i-coin];
            }
        }
        
        return dp[amount];
    }
};
