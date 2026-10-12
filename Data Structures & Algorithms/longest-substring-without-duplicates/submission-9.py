class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = maxLen = 0
        seen = set()
        for r, c in enumerate(s):
            while c in seen:
                seen.remove(s[l])
                l += 1 
            seen.add(c)
            maxLen = max(maxLen, r - l + 1)
        return maxLen