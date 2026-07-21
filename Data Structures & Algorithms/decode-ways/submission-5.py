class Solution:
    def numDecodings(self, s: str) -> int:
        # Iterate in reverse
        dp2 = 0
        dp1 = 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                curr = 0
            else:
                curr = dp1
            # If s[i:] is 10 - 26:
            if i + 1 < len(s) and 9 < int(s[i] + s[i+1]) <= 26:
                curr += dp2
            curr, dp1, dp2 = 0, curr, dp1    

        return dp1