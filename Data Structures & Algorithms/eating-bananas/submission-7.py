class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # This can be solved O(n) math
        # But idk the math so it can be solved via O(log(max(n))) binary search
        left, right = 1, max(pile for pile in piles)

        def eatPiles(eatingSpeed: int) -> bool:
            count = 0
            for pile in piles:
                if count > h:
                    return False
                if pile <= eatingSpeed:
                    count += 1
                elif pile % eatingSpeed == 0:
                    count += pile // eatingSpeed
                else:
                    count += 1 + (pile // eatingSpeed)
            return count <= h


        # If left < mid = right cant happen so we chill
        # Only left = mid < right
        while left < right:
            mid = left + ((right - left) // 2)
            if eatPiles(mid):
                right = mid # Slowest acceptable is mid
            else:
                left = mid + 1 # Fastest acceptable is mid + 1

        return left
        
