class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Area = (r - l) * min height
        # Uses two pointers
        l, r, maxA = 0, len(heights)-1, 0
        while l < r:
            if heights[l] < heights[r]:
                maxA = max(maxA, (r - l) * heights[l])
                l += 1
            elif heights[r] < heights[l]:
                maxA = max(maxA, (r - l) * heights[r])
                r -= 1
            else:
                maxA = max(maxA, (r - l) * heights[l])
                # This is the best for both these heights, move both pointers
                l += 1
                r -= 1
        return maxA
