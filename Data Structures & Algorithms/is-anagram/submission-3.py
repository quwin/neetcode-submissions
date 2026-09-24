class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count: dict = {}
        for char in s:
            curr = count.setdefault(char, 0)
            count[char] = curr + 1
        for char in t:
            curr = count.setdefault(char, 0)
            count[char] = curr - 1
            if count[char] == 0:
                del count[char]
        return not count