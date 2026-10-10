from collections import Counter;

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # For every index, a variable sliding window can be maintained
        # For any given window size,
        # the optimal char to replace with is the highest pop char
        l, r, res = 0, 0, 1
        counts = Counter()
        while l <= r and r < len(s):
            counts[s[r]] += 1
            r += 1
            while counts.total() - counts.most_common(1)[0][1] > k:
                counts[s[l]] -= 1
                l += 1
            res = max(res, r - l)
                

        return res