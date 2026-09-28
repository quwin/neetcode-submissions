class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // sliding window
        int l = 0; int r = 0;
        int max = 0;
        std::unordered_map<char, int> seen;
        while (r < s.size()) {
            if (seen.contains(s[r])) {
                l = std::max(l, seen[s[r]] + 1);
            } 
            max = std::max(r-l + 1, max);
            seen[s[r]] = r;
            r++;
        }
        return max;
    }
};