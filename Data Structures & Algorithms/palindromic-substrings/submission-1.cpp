class Solution {
public:
    int countSubstrings(string s) {
        // Two pointers 
        int count = 0;
        for (int i = 0; i < s.size(); i++) {
            // odd
            int l = i, r = i;
            while (l >= 0 && r < s.size() && s[l] == s[r]) {
                count++;
                l--;
                r++;
            }
            // even
            l = i;
            r = i + 1;
            while (l >= 0 && r < s.size() && s[l] == s[r]) {
                count++;
                l--;
                r++;
            }
        }
        return count;
    }
};
