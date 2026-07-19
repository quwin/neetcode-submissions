class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def floodfill(y: int, x: int):
            if y < 0 or y >= len(grid):
                return
            if x < 0 or x >= len(grid[y]):
                return
            if grid[y][x] == "0":
                return
            grid[y][x] = "0"
            floodfill(y-1, x)
            floodfill(y+1, x)
            floodfill(y, x-1)
            floodfill(y, x+1)
            
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == "1":
                    count += 1
                    floodfill(y, x)

        return count