class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> counts(26, 0);
        for (char c : s) {
            counts[c - 'a']++;
        }
        for (char c : t) {
            counts[c - 'a']--;
        }
        return std::all_of(counts.begin(), counts.end(), [](int i) {
            return i == 0;
        });
    }
};
