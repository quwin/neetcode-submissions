class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int rows = grid.size(), columns = grid[0].size();
        for (int y = 0; y < rows; y++) {
            for (int x = 0; x < columns; x++) {
                if (x == 0 && y == 0) {
                    continue;
                } else if (x == 0) {
                    grid[y][x] += grid[y-1][x];
                } else if (y == 0) {
                    grid[y][x] += grid[y][x-1];
                } else {
                    grid[y][x] += min(grid[y-1][x], grid[y][x-1]);
                }
            }
        }
        return grid[rows-1][columns-1];
    }
};