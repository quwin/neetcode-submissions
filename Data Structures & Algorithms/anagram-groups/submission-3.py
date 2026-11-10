class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Given a question which receives an array of strings,
        # Return an array of groups of strings, such that each group
        # contains strings where are anagrams of each other
        # Two strings are anagrams of they have the same count of each character
        # The intuitive way to answer this problem is to reduce each string to a 
        # a common key
        # You can use a 26 len tuple of character counts
        # Or sort each anagram, 26 len tuple is preferred for 
        # After that, just use a map of each key -> array and convert to array
        # Time: O(n), iterates over every string (twice)
        # Space: O(n), holds a copy of each string
        def getKey(string: str) -> tuple[int, ...]:
            array = [0] * 26
            for char in string:
                index = ord(char) - ord('a')
                array[index] += 1
            return tuple(array)

        anagrams: map[tuple[int, ...], list[str]] = {}

        for string in strs:
            key = getKey(string)
            anagrams.setdefault(key, []).append(string)

        return list(anagrams.values())