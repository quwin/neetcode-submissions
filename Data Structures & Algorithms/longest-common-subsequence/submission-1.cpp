class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        if (text1.size() > text2.size()) {
            swap(text1, text2);
        }
        vector<int> dp(text1.size()+1, 0);
        for (int i = text2.size(); i > -1; i--) {
            int prev = 0;
            for (int j = text1.size() - 1; j >= 0; --j) {
                int temp = dp[j];
                if (text2[i] == text1[j]) {
                    dp[j] = 1 + prev;
                } else {
                    dp[j] = max(dp[j], dp[j + 1]);
                }
                prev = temp;
            }
        }
        return dp[0];
    }
};
