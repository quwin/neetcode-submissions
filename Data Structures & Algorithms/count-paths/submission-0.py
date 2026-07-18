class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize DP Array
        paths = [[0] * n for _ in range(m)]
        paths[0] = [1] * n
        for i in range(m):
            paths[i][0] = 1
        
        for x in range(1, n):
            for y in range(1, m):
                paths[y][x] = paths[y - 1][x] + paths[y][x - 1]
        
        return paths[m-1][n-1]