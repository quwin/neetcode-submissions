class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        chars = {}
        slow = 0
        maxLen = 0
        for fast in range(0, len(s)):
            maxLen = max(maxLen, fast - slow)
            if s[fast] in chars:
                slow = max(slow, chars[s[fast]] + 1)
            chars[s[fast]] = fast
        return max(maxLen, len(s)-slow)
