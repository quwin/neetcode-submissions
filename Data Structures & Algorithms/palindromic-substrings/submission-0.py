class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for center in range(len(s)):
            # Each center is a guarenteed start of a palindrome
            l = r = center
            # Odd palandrome (center is dead center)
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            # Even palandrome (center is left side of center)
            l, r = center, center + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            
        return count