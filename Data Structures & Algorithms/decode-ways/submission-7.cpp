class Solution {
public:
    int numDecodings(string s) {
        // 1. What does `dp[i]` mean?
            // if s[i] == '0', dp[i-2]
                // if i == 0 or s[i-1] == '0' or s[i-1] > '2' return 0
            // else if s[i-1::i] > '26' or s[i-1] == '0', dp[i-1]
            // else if s[i-1::i] <= '26', dp[i-1] + dp[i-2]  
        // 2. What is the recurrence?
        // 3. What are the base cases?
            // dp[i] = 1
        // 4. In what order must states be computed?
            // bottom up
        // 5. Where is the final answer?
            // dp[s.size()]
        vector<int> dp(s.size(), 0);
        dp[0] = 1;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '0') {
                if (i == 0 or s[i-1] == '0' or !(s[i-1] == '1' or s[i-1] == '2')) {
                    return 0;
                } else {
                    dp[i] = dp[std::max(0,i-2)];
                }
                continue;
            } 
            string sliced(s.begin() + std::max(0,i-1), s.begin()+i+1);
            int parsed = std::stoi(sliced);
            if (parsed > 26 or parsed < 10) {
                dp[i] = dp[std::max(0,i-1)];
            } else {
                int priorPrior = (i >= 2) ? dp[i-2] : 1;
                dp[i] = dp[std::max(0,i-1)] + priorPrior;
            }
        }
        for (const auto& elem : dp) {
            std::cout << elem << " ";
        }
        return dp[s.size()-1];
    }
};
