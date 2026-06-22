class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer = 0
        length = len(s)
        for char in t:
            if pointer == length:
                return True
            if s[pointer] == char:
                pointer += 1
        return pointer == length