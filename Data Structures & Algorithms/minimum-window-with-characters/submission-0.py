class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        counts  = [0] * 52 #Upper+Lowercase Letter
        for char in t:
            counts[ord(char) - ord('a')] += 1
        start, minLength = 0, len(s)
        minString = ""
        for end in range(len(s)):
            counts[ord(s[end]) - ord('a')] -= 1
            while all(x <= 0 for x in counts):
                if end - start < minLength: # This can probably be optimized
                    minLength = end-start
                    minString = ""
                    for i in range(start, end+1):
                        minString += s[i]
                counts[ord(s[start]) - ord('a')] += 1
                start += 1
        return minString

