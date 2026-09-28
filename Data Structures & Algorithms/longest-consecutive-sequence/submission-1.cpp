class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        std::set<int> seen; // Set of seen vals
        for (int i = 0; i < nums.size(); i++) {
            seen.insert(nums[i]);
        }
        int max = 0;
        for (int i = 0; i < nums.size(); i++) {
            int num = nums[i];
            int count = 0;
            if (!seen.contains(num - 1)) { // If this is start of sequence
                while (seen.contains(num)) {
                    count += 1;
                    max = std::max(count, max);
                    num += 1;
                }
            }
        }
        return max;
    }
};
