class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Can be done with a Counter easily
        # Can be done with bit shifting too but its stupid
        # I'll implement it with a 1 idx voting system
        winner = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != winner:
                count -= 1
            else:
                count += 1
            if count == 0:
                winner = nums[i]
                count += 1
        return winner