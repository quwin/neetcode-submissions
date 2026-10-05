class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int count = 0;
        for (int y = 0; y < grid.size(); y++) {
            for (int x = 0; x < grid[y].size(); x++) {
                if (grid[y][x] == '1') {
                    count++;
                    dfsClear(grid, y, x);
                }
            }
        }
        return count;
    }

    void dfsClear(vector<vector<char>>& grid, int y, int x) {
        if (y < 0 || y >= grid.size() || x < 0 || x >= grid[y].size() || grid[y][x] == '0') {
            return;
        }
        grid[y][x] = '0';
        dfsClear(grid, y-1, x);
        dfsClear(grid, y+1, x);
        dfsClear(grid, y, x+1);
        dfsClear(grid, y, x-1);
    }

};
