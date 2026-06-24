class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        nums = sorted(nums)
        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i+1
            k = len(nums) - 1
            while j < k:
                ijkSum = nums[i] + nums[j] + nums[k]
                if ijkSum == 0:
                    solutions.append([nums[i], nums[j], nums[k]])
                    # Move both pointers after using this pair
                    j += 1
                    k -= 1
                    # Skip duplicate second values
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    # Skip duplicate third values
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif ijkSum > 0:
                    k -= 1
                else:
                    j += 1
        return solutions