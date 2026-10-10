class Solution:
    def trap(self, height: List[int]) -> int:
        # This also uses two pointers
        # Water[i] = min(maxRightHeight, maxLeftHeight) - height[i]
        l, r, maxL, maxR, water = 0, len(height) -1, 0, 0, 0

        while l <= r:
            maxL = max(height[l], maxL)
            maxR = max(height[r], maxR)
            if height[l] < height[r]:
                water += max(0, min(maxR, maxL) - height[l])
                l += 1
            elif height[r] < height[l]:
                water += max(0, min(maxR, maxL) - height[r])
                r -= 1
            else:
                water += max(0, min(maxR, maxL) - height[l])
                if l != r:
                    water += max(0, min(maxR, maxL) - height[r])
                l += 1
                r -= 1
            
        return water