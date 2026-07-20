class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nCurrent, current, maxP = nums[0], nums[0], nums[0]

        for num in nums[1:]:
            temp = current
            current = max(current * num, num, nCurrent * num)
            nCurrent = min(temp * num, num, nCurrent * num)
            maxP = max(current, maxP)
            print(current, nCurrent, maxP)

        return maxP