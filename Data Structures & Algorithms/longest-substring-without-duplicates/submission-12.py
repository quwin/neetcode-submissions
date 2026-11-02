class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        characters = {}
        res = 0
        for r in range(len(s)):
            c = s[r]
            if c in characters:
                l = max(characters[c]+1, l)
            characters[c] = r
            res = max(res, r - l + 1)
        return res