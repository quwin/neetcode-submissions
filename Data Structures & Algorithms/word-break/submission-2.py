class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s) + 1
        dp = [False] * n
        dp[0] = True
        for right in range(1, n):
            for left in range(0, right):
                if s[left:right] in wordSet:
                    dp[right] = dp[right] or dp[left]
        return dp[n-1]