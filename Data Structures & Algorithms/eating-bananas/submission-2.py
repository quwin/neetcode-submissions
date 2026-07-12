class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minK, maxK = 1, 0
        for pile in piles:
            if pile > maxK:
                maxK = pile
        while maxK >= minK:
            k = (maxK+minK) // 2
            foundH = h
            for pile in piles:
                foundH -= -(-pile // k) # Ceil divide
            if foundH == 0:
                maxK = k - 1
            elif foundH > 0:
                maxK = k - 1
            else:
                minK = k + 1

        return maxK + 1
        