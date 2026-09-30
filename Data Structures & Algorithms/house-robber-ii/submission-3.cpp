class Solution {
public:
    int rob(vector<int>& nums) {
        // Since it's a circle, ans = max(rob from 1::end, 0::end-1)
        if (nums.size() == 1) {
            return nums[0];
        }
        int priorPrior = 0, prior = 0;
        for (int i = 1; i < nums.size(); i++) {
            int temp = max(priorPrior + nums[i], prior);
            priorPrior = prior;
            prior = temp;
        }
        int priorPrior2 = 0, prior2 = 0;
        for (int i = 0; i < nums.size()-1; i++) {
            int temp = max(priorPrior2 + nums[i], prior2);
            priorPrior2 = prior2;
            prior2 = temp;
        }
        return max(prior, prior2);
    }
};
