class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        // dp[i] = whether suffix is a word/set of words
        int size = s.size();
        vector<bool> dp(size+1);
        dp[s.size()] = true;
        for (int i = size-1; i > -1; i--) {
            for (string& w : wordDict) {
                if (w.size() + i <= size && 
                s.substr(i, w.size()) == w) {
                    dp[i] = dp[i + w.size()];
                }
                if (dp[i]) {
                    break;
                }
            }
        }
        return dp[0];
    }
};
