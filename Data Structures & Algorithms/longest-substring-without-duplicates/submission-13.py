class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Given a method which takes an input a string of a variable length
        # and returns the length of the longest substring 
        # without repeating characters
        # My first thought is to iterate over every single substring
        # Then check if they are valid (no repeating characters)
        # If they are, record their length
        # And return the max(lengths)
        # This would require each position in the string 
        # To iterate over all later positions:
            # O(n^2) time
        # To check for validity, a set of chars/positions must be maintained
            # O(n) space
        # However, I believe that this can be optimized.
        # Instead of iterating over each substring,
        # You can progress from a given starting index while a dupe is found
        # Since no longer substrings starting at the same index are valid
            # This is still O(n^2) time, and O(n) space
        # Further, there is no need to check every single substring of a shorter
        # length at that next index, since you already have a set of chars
        # This further optimizes the algorithm such that you only need to check
        # each position at most once:
            # Once as a starting position
            # Once as an ending position
        # This can be done using the "Two Pointer" pattern of iteration
            # O(n) time, O(n) space
        left = maxLen = 0
        seen = set()
        for right, char in enumerate(s):
            while char in seen:
                seen.remove(s[left])
                left += 1
            seen.add(char)
            maxLen = max(maxLen, right-left + 1)
        return maxLen