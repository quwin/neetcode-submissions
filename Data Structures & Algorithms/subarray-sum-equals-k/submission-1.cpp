class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        // Sliding window fails because negative values
        // means idk when to shrink window

        // prefixSum, # of ways to reach sum
        std::unordered_map<int, int> sums; 
        // Theres currently 1 way to get a prefix of 0:
        // Empty prefix
        sums[0] = 1;
        int count = 0;
        int currentSum = 0;
        for (int i = 0; i < nums.size(); i++) {
            currentSum += nums[i];
            count += sums[currentSum - k];

            sums[currentSum]++;
        }
        return count;
        // This works cause prefixSum[i] - prefixSum[j] 
        // = sum[nums from i to j inclusive]
    }
};