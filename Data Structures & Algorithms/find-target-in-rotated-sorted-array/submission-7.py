class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo+hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[lo] <= nums[hi]: # Non-rotated == Sorted
                if lo == hi:
                    return -1
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else: # nums[lo] > nums[hi]
                if nums[mid] < target:
                    if nums[lo] > target: # Target must be right of mid, sorted
                        lo = mid + 1
                    elif nums[lo] < target:
                        if nums[mid] > nums[lo]:
                            lo = mid + 1
                        elif nums[mid] < nums[lo]:
                            hi = mid - 1
                        else:
                            lo = mid + 1
                    else:
                        return lo
                else: # nums[mid] > target
                    if nums[hi] > target:
                        if nums[mid] > nums[lo]:
                            lo = mid + 1
                        elif nums[mid] < nums[lo]:
                            hi = mid - 1
                        else:
                            lo = mid + 1
                    elif nums[hi] < target:
                        hi = mid - 1
                    else:
                        return hi
    
        return -1
            