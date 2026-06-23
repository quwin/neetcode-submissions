import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = clean_text = re.sub(r'[\W_]', '', s.lower())
        for i in range(0, int(len(clean)/2)):
            if clean[i] != clean[len(clean)-i-1]:
                return False
        return True


        