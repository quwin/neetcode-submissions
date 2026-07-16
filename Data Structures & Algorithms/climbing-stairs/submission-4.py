class Solution:
    calcd = {}
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        elif n in self.calcd:
            return self.calcd[n]
        self.calcd[n-2] = self.climbStairs(n-2)
        return self.climbStairs(n-1) + self.calcd[n-2]