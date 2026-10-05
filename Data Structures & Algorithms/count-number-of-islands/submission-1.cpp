class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int count = 0;
        for (int y = 0; y < grid.size(); y++) {
            for (int x = 0; x < grid[y].size(); x++) {
                if (grid[y][x] == '1') {
                    count++;
                    bfsClear(grid, y, x);
                }
            }
        }
        return count;
    }

    void bfsClear(vector<vector<char>>& grid, int y, int x) {
        if (y < 0 || y >= grid.size() || x < 0 || x >= grid[y].size() || grid[y][x] == '0') {
            return;
        }
        grid[y][x] = '0';
        bfsClear(grid, y-1, x);
        bfsClear(grid, y+1, x);
        bfsClear(grid, y, x+1);
        bfsClear(grid, y, x-1);
    }

};
