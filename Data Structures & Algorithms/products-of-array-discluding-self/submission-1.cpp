class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> ans(nums.size(), 1);
        int running = 1;
        for (int i = 0; i < nums.size(); i++) {
            ans[i] *= running;
            running *= nums[i];
        }
        running = 1;
        for (int i = nums.size() - 1; i >= 0; i--) {
            ans[i] *= running;
            running *= nums[i];
        }
        return ans;
    }
};
