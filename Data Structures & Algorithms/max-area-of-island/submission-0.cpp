class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int maxArea = 0;
        for (int y = 0; y < grid.size(); y++) {
            for (int x = 0; x < grid[y].size();x++) {
                if (grid[y][x] == 1) {
                    maxArea = max(maxArea, areaOfIsland(grid,y,x));
                }
            }
        }
        return maxArea;
    }

    int areaOfIsland(vector<vector<int>>& grid, int y, int x) {
        if (y < 0 || y >= grid.size() || x < 0 || x >= grid[y].size() || grid[y][x] == 0) {
            return 0;
        }
        grid[y][x] = 0;
        return 1 + 
            areaOfIsland(grid, y-1, x) + 
            areaOfIsland(grid, y+1, x) + 
            areaOfIsland(grid, y, x+1) + 
            areaOfIsland(grid, y, x-1);

    }
};
