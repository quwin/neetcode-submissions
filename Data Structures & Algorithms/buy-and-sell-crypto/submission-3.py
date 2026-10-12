class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyP = prices[0]
        maxP = 0
        for price in prices:
            if price > buyP:
                maxP = max(maxP, price - buyP)
            else:
                buyP = price
        return maxP