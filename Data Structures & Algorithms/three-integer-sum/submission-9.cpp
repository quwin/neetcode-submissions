class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        std::sort(nums.begin(), nums.end()); // Sort cause solution is O(n^2) anyways
        vector<vector<int>> ans;
        int size = nums.size();
        for (int i = 0; i < size-1; i++) { // For each starting index
            if (i > 0 and nums[i] == nums[i-1]) {
                continue;
            }
            int l = i + 1;
            int r = size-1;
            while (l < r) { // Two sum over over positions
                int sum = nums[i] + nums[l] + nums[r];
                if (sum == 0) {
                    ans.push_back({nums[i], nums[l], nums[r]});
                    l++;
                    while (l < r and nums[l] == nums[l-1]) {
                        l++;
                    }
                    r--;
                    while (l < r and nums[r] == nums[r+1]) {
                        r--;
                    }
                } else if (sum < 0) {
                    l++;
                    while (l < r and nums[l] == nums[l-1]) {
                        l++;
                    }
                } else {
                    r--;
                    while (l < r and nums[r] == nums[r+1]) {
                        r--;
                    }
                }
            }
        }
        return ans;
    }
};
