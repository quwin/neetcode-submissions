class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // For each day, there are a few options:
            // if cooldown, only do nothing
            // If can buy, buy or do nothing
            // if can sell, sell or do nothing
        // so max profit = max(profit if you do nothing, profit if you buy, profit if you sell)
        // and branches are created/combined
        // Max profit if you can buy this day vs can only sell
        vector<tuple<int, int>> dp(prices.size() + 1, tuple<int, int>{0,0});
        // For each day
        for (int i = prices.size()-1; i > -1; i--) {
            for (int buying = 1; buying >= 0; --buying) {
                if (buying == 1) {
                    int buy = get<0>(dp[i + 1]) - prices[i];
                    int cooldown = get<1>(dp[i + 1]);
                    dp[i] = tuple<int, int>{get<0>(dp[i]), max(buy, cooldown)};
                } else {
                    int sell = (i + 2 < prices.size()) ? get<1>(dp[i + 2]) + prices[i] : prices[i];
                    int cooldown = get<0>(dp[i + 1]);
                    dp[i] =tuple<int, int>{max(sell, cooldown), get<1>(dp[i])};
                }
            }
        }
        return get<1>(dp[0]);
    }
};
