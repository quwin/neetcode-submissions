class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Two pointer is intuitive here and is more effecient than dp bruh
        resIdx = resLen = 0
        for center in range(len(s)):
            # Two pointers
            l = r = center
            # While Odd Length palindrome with center [center] is valid
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1
            # Offset either l or r, it doesn't matter just choose one
            # Bc it propigates consistiently
            l, r = center, center + 1
            # While Even Length palindrome with left mid [center] is valid
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

        return s[resIdx:resIdx+resLen]