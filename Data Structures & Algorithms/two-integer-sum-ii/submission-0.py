class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        found = {}
        for i, num in enumerate(numbers):
            if target-num in found:
                return [found[target-num], i + 1]
            found[num] = i + 1
        return []