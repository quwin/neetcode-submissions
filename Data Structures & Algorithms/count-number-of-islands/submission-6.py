from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]

        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for y in range(rows):
            for x in range(cols):
                if grid[y][x] != "1":
                    continue

                count += 1
                queue = deque([(y, x)])
                grid[y][x] = "0"

                while queue:
                    curr_y, curr_x = queue.popleft()

                    for dy, dx in directions:
                        new_y = curr_y + dy
                        new_x = curr_x + dx

                        if (
                            0 <= new_y < rows
                            and 0 <= new_x < cols
                            and grid[new_y][new_x] == "1"
                        ):
                            grid[new_y][new_x] = "0"
                            queue.append((new_y, new_x))

        return count