#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> seen;
        vector<int> ans;
        for (int i = 0; i < nums.size(); i++) {
            int needed = target - nums[i];
            if (seen.find(needed) != seen.end()) {
                ans.push_back(seen[needed]);
                ans.push_back(i);
                return ans;
            }
            seen[nums[i]] = i;
        }
        return ans;
    }
};
