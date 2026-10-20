class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for left in range(len(nums)):
            if left > 0 and nums[left] == nums[left-1]:
                continue
            for right in range(len(nums)-1, left+2, -1):
                if right < len(nums)-1 and nums[right] == nums[right+1]:
                    continue
                innerL, innerR = left+1, right-1
                while innerL < innerR:
                    found = nums[left] + nums[right] + nums[innerL] + nums[innerR]
                    if found == target:
                        res.append([nums[left], nums[right], nums[innerL], nums[innerR]])
                        innerL += 1
                        innerR -= 1
                        while innerL < innerR and nums[innerL] == nums[innerL-1]:
                            innerL += 1
                        while innerL < innerR and nums[innerR] == nums[innerR+1]:
                            innerR -= 1
                    elif found < target:
                        innerL += 1
                    else:
                        innerR -= 1

        return res