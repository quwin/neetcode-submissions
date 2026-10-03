class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int height = triangle.size();
        for (int y = 1; y < height; y++) {
            for (int x = 0; x < triangle[y].size(); x++) {
                if (x == 0) {
                    triangle[y][x] += triangle[y-1][x];
                } 
                else if (x == triangle[y].size() - 1) {
                    triangle[y][x] += triangle[y-1][x-1];
                } 
                else {
                    triangle[y][x] += min(triangle[y-1][x-1], triangle[y-1][x]);
                }
            }
        }
        int res = triangle[height-1][0];
        for (int& minCost : triangle[height-1]) {
            res = std::min(res, minCost);
        }
        return res;
    }
};