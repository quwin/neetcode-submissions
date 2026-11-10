class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def validEatingSpeed(speed: int) -> bool:
            count = 0
            for pile in piles:
                if pile <= speed:
                    count += 1
                else:
                    remainder = 0 if pile % speed == 0 else 1
                    count += (pile // speed) + remainder
                if count > h:
                    return False
            return count <= h

        left = 1
        right = max(piles)
        while left <= right:
            mid = left + ((right - left) // 2)
            if validEatingSpeed(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
