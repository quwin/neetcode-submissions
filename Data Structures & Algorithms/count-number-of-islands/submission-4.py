class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfsFloodFill(y: int, x: int):
            if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[y]):
                return
            if grid[y][x] == '0':
                return
            grid[y][x] = '0'
            dfsFloodFill(y-1, x)
            dfsFloodFill(y+1, x)
            dfsFloodFill(y, x-1)
            dfsFloodFill(y, x+1)

        count = 0
        for y, row in enumerate(grid):
            for x, item in enumerate(row):
                if item == '1':
                    count += 1
                    dfsFloodFill(y, x)

        return count


        
