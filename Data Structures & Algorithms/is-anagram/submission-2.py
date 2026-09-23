class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        for char in s:
            count = counts.setdefault(char, 0)
            counts[char] = count + 1
        for char in t:
            count = counts.get(char, 999)
            counts[char] = count - 1
            if counts[char] == 0:
                del counts[char]
        return not counts