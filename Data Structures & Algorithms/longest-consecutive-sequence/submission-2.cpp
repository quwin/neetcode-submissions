class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        // Track the beginnings, every sequence must have only 1 begin
        std::unordered_set<int> seen;
        for (int num : nums) {
            seen.insert(num);
        }
        int maxLen = 0;
        for (int num : nums) {
            if (!seen.contains(num-1)) {
                int count = 0;
                while (seen.contains(num)) {
                    count++;
                    num++;
                    maxLen = std::max(maxLen, count);
                }
            }
        } 
        return maxLen;
    }
};
