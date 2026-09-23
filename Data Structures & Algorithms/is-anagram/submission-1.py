class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = {}
        for char in s:
            val = hashmap.setdefault(char, 0)
            hashmap[char] = val + 1
        for char in t:
            val = hashmap.setdefault(char, 999)
            hashmap[char] = val - 1
            if hashmap[char] == 0:
                del hashmap[char]
        return not hashmap