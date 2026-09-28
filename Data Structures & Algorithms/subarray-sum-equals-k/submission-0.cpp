class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        // Prefix sum, not sliding window
        int res = 0;
        int curr = 0;
        std::unordered_map<int, int> prefixMap;
        prefixMap[0] = 1;
        for (int i = 0; i < nums.size(); i++) {
            curr += nums[i];
            int diff = curr - k;
            if (prefixMap.contains(diff)) {
                res += prefixMap.at(diff);
            }
            if (prefixMap.contains(curr)) {
                prefixMap[curr] += 1;
            } else {
                prefixMap[curr] = 1;
            }
        }
        return res;
    }
};