class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        std::vector<int> key(26, 0);
        for (char c: s1) {
            key[c - 'a']++;
        }
        for (int i = 0; i < s2.size(); i++) {
            if (i >= s1.size()) {
                key[s2[i-s1.size()] - 'a']++;
            }
            key[s2[i] - 'a']--;
            if (vecZeros(key)) {
                return true;
            }
        }
        return false;
    }
    bool vecZeros(std::vector<int> key) {
        return std::all_of(key.begin(), key.end(), [](int i) { 
            return i == 0; 
        });
    }
};
