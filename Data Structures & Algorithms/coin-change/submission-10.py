class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Given an array of coins and a target value,
        # What's the fewest # of coins to reach that target value?
        # Lets start with an example value of 10, with two coins:
        # 1 and 2
        # There are a few ways to get the answer:
        # 2 (5x), 1 (10x), and a combo, where the correct ans is 5
        # But that ans is calculated starting from a small val:
        # Looking at every num from one to 10:
        # For 1, only 1 1 works
        # For 2, 1 2 or 2 1s works
        # For 3, only 1 1 and 1 2 works
        # Since the answer for 3 is the sum of the most effecient ans for 
        # 1 and 2, this is a dynamic programming problem.
        # For any given coin, the most effecient way that coin can be used to reach a num
        # Is the most effecient way to reach that num - coin_val + 1
        # Where the base case is 0 = 0
        # This can be done by iterating over every target value from 0 to amount
        # Then iterating over every available coin
        # Where the current # of coins = Is the most effecient way to reach that num-coin_val+1

        dp = [-1] * (amount + 1)
        dp[0] = 0
        # From my understanding order doesn't matter here
        for targetVal in range(amount+1):
            for coin in coins:
                if targetVal - coin >= 0 and dp[targetVal - coin] != -1:
                    if dp[targetVal] == -1:
                        dp[targetVal] = dp[targetVal - coin] + 1
                    else:
                        dp[targetVal] = min(dp[targetVal], dp[targetVal - coin] + 1)

        return dp[amount]