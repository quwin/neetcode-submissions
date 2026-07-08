class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowSize = len(s1)
        if len(s2) < windowSize:
            return False
        # Only lowercase letters
        diff = [0]*26
        for i in range(windowSize):
            diff[ord(s1[i]) - ord('a')] += 1
            diff[ord(s2[i]) - ord('a')] -= 1
        if all(x == 0 for x in diff):
            return True
        for end in range(windowSize, len(s2)):
            start = end - windowSize
            diff[ord(s2[end]) - ord('a')] -= 1
            diff[ord(s2[start]) - ord('a')] += 1
            if all(x == 0 for x in diff):
                return True
        return False