class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer1 = 1
        pointer2=len(numbers)
        while True:
            add = numbers[pointer1-1] + numbers[pointer2-1]
            if add == target:
                return [pointer1, pointer2]
            if add > target:
                pointer2 = pointer2-1
            if add < target:
                pointer1 = pointer1 + 1