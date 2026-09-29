class Solution {
public:
    int characterReplacement(std::string s, int k) {
        std::unordered_map<char, int> counts;
        int result = 0;
        int l = 0;
        int maxF = 0;
        for (int r = 0; r < s.size(); r++) {
            // Add new item to window counts
            counts[s[r]]++;
            // maxF -> maxFrequency, tracks most common item
            maxF = max(counts[s[r]], maxF);
            // while the window size for the given k is invalid
            while ((r - l + 1) - maxF > k) {
                // Remove the count of the last item
                counts[s[l]]--;
                l++;
                // It's ok if the most freq char is removed
            }
            result = max(result, r - l + 1);
        }
        return result;
        // Key idea: count the sliding window
        // Highest freq within window is optimal
        // when window gets too large
        // shrink to support highest freq
        // Even if that makes maxF temporarily wrong
    }
};