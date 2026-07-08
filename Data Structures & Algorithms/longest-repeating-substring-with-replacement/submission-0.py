class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 1 or k >= len(s):
            return len(s)
        start, maxLen, maxFreq = 0, 0, 0
        counts = {}
        for end in range(len(s)):
            counts[s[end]] = counts.get(s[end], 0) + 1
            maxFreq = max(maxFreq, counts[s[end]])

            while (end - start + 1) - maxFreq > k:
                counts[s[start]] -= 1
                start += 1

            maxLen = max(maxLen, end - start + 1)

        return maxLen