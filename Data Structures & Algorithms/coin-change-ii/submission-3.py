class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # DP problem
        # For each coin, iterate over 
        dp = [0] * (amount + 1)
        dp[0] = 1
        # For each coin, run through the # of ways it can reach each num
        # Do coin -> amount for combinations instead of permutations
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]

        return dp[amount]