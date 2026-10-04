class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        // Iterating in reverse means u only need to check triangle[0]
        // Instead of the min of every bottom val
        for (int y = triangle.size()-2; y > -1; y--) {
            for (int x = triangle[y].size()-1; x > -1; x--) {
                triangle[y][x] += min(triangle[y+1][x], triangle[y+1][x+1]);
            }
        }
        return triangle[0][0];
    }
};