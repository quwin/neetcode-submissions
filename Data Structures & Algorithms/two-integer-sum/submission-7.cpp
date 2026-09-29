class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Iterates over nums once -> O(n)
        // O(n) space to hold seen
        std::unordered_map<int, int> seen; // num, index
        for (int i = 0; i < nums.size(); i++) {
            int needed = target - nums[i];
            // Check lookup first incase needed == nums[i]
            if (seen.contains(needed)) {
                return vector<int>({seen[needed], i});
            }
            seen[nums[i]] = i;
        }
        return vector<int>({});
    }
};
