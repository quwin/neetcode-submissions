class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        exists = set()
        for num in nums:
            exists.add(num)
        longest = 0
        for num in nums:
            if num-1 in exists:
                continue
            length = 1
            number = num+1
            while number in exists:
                length = length + 1
                number = number + 1
            if length > longest:
                longest = length
        return longest

