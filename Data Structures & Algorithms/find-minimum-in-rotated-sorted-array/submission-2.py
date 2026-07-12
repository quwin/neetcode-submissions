class Solution:
    def findMin(self, nums: List[int]) -> int:
        s, e = 0, len(nums) - 1
        while s <= e:
            if nums[e] < nums[s]: # Rotated
                mid = (e+s)//2
                num = nums[mid]
                if num < nums[s]:
                    if num > nums[e]:
                        s = mid+1
                    else: #num <= nums[e]
                        e = mid
                else: #num >= nums[s]
                    s = mid + 1
            else: # Correct order
                return nums[s]
                

            
            