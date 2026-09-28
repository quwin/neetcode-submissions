class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0;
        int r = heights.size() -1;
        int maxArea = 0;
        while ( l < r) {
            int waterHeight = std::min(heights[l], heights[r]);
            int area = (r-l) * waterHeight;
            maxArea = std::max(area, maxArea);
            if (heights[l] == heights[r]) {
                l++;
                r--;
            } else if (waterHeight == heights[l]) {
                l++;
            } else {
                r--;
            }
        }
        return maxArea;
    }
};
