class Solution {
public:
    int minDistance(string word1, string word2) {
        // There are 3 actions - add, delete, replace
        // Need to consider all actions, even when it seems unorthidox
            // Bc no rule cements which action to do without prior knowledge
        // Example 2D Array: (I accidentaly used monkey, not monkeys)
        // |   | m | o | n | e | y |   |
        // | m | 1 | 2 | 3 | 4 | 5 | 6 |
        // | o | 2 | 1 | 2 | 3 | 4 | 5 |
        // | n | 3 | 2 | 1 | 2 | 3 | 4 |
        // | k | 3 | 2 | 1 | 1 | 2 | 3 |
        // | e | 3 | 2 | 1 | 0 | 1 | 2 |
        // | y | 4 | 3 | 2 | 1 | 0 | 1 |
        // |   | 5 | 4 | 3 | 2 | 1 | 0 |
        // Pattern: 
            // if word1[j] == word2[x]:
                // min(1 + min(dp[i+1][j], dp[i][j+1]), dp[i+1][j+1])
            //  else:
                // 1 + min(min(dp[i+1][j], dp[i][j+1]), dp[i+1][j+1])
        int word1Size = word1.size(), word2Size = word2.size();
        vector<vector<int>> dp(word2Size+1, vector<int>(word1Size+1, 0));
        // Set outer edge defaults
        for (int i = 0; i <= word1Size; i++) {
            dp[word2Size][i] = word1Size - i;
        }
        for (int i = 0; i <= word2Size; i++) {
            dp[i][word1Size] = word2Size - i;
        }
        for (int y = word2Size-1; y > -1; y--) {
            for (int x = word1Size-1; x > -1; x--) {
                if (word1[x] == word2[y]) {
                    dp[y][x] = min(1 + min(dp[y+1][x], dp[y][x+1]), dp[y+1][x+1]);
                } else {
                    dp[y][x] = 1 + min(min(dp[y+1][x], dp[y][x+1]), dp[y+1][x+1]);
                }
            }
        }
        return dp[0][0];
    }
};
