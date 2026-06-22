class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count: dict[str, int] = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        for char in t:
            count[char] = count.get(char, 0) - 1
            if count[char] == 0:
                count.pop(char)
        return not count