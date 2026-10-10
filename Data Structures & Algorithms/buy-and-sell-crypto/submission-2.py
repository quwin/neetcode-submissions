class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Two pointer Solution
        # DP also works but it unnecessary
        l, maxProfit = 0,0
        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            if profit > 0:
                maxProfit = max(maxProfit, profit)
            else:
                l = r

        return maxProfit