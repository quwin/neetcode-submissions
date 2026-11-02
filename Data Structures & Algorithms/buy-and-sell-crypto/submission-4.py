class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # They key of the problem is that you only have one chance,
        # and are looking for the max of one chance
        # Because of that you can either keep a single min buy and max sell
        res = 0
        l = 0
        for r in range(len(prices)):
            price = prices[r]
            if price > prices[l]:
                res = max(res, price - prices[l])
            else:
                l = r
        return res