class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + ((r-l) // 2)
            if nums[mid] == target:
                return mid
            elif nums[r] == target:
                return r
            elif nums[l] == target:
                return l
            # Rotation Point on right if exists, greater and lesser on right
            if nums[mid] > nums[r]:
                if target < nums[mid] and target > nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            else: # Rotation point on left, greater and lesser on left
                if target > nums[mid] and target < nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1