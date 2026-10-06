#include <vector>
class Solution {
public:
    int rob(vector<int>& nums) {
        return max(nums[0], 
        max(
            dp(vector<int> (nums.begin(), nums.end()-1)), 
            dp(vector<int> (nums.begin()+1, nums.end()))
        ));
    }

    int dp(vector<int> nums) {
        int priorPrior = 0, prior = 0;
        for (int i = 0; i < nums.size(); i++) {
            int temp = priorPrior;
            priorPrior = prior;
            prior = max(temp + nums[i], prior);
        }
        return prior;
    }
};
