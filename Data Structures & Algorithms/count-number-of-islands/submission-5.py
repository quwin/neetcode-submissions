class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs solution, DSU is awkward
        ROWS = len(grid)
        COLS = len(grid[0])
        def floodFill(y: int, x: int):
            if (y < 0 or y >= ROWS or
            x < 0 or x>= COLS or
            grid[y][x] == "0"):
                return
            grid[y][x] = "0"
            floodFill(y-1, x)
            floodFill(y+1, x)
            floodFill(y, x-1)
            floodFill(y, x+1)
        count = 0
        for y in range(ROWS):
            for x in range(COLS):
                if grid[y][x] == "1":
                    count += 1
                    floodFill(y, x)
        return count