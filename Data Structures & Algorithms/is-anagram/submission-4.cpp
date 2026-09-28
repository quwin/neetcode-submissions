#import <unordered_map>

class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> counts;
        for (char c: s) {
            if (counts.find(c) == counts.end()) {
                counts.insert_or_assign(c, 0);
            }
            counts[c] += 1;
        }
        for (char c: t) {
            if (counts.find(c) == counts.end()) {
                return false;
            }
            counts[c] -= 1;
            if (counts.at(c) == 0) {
                counts.erase(c);
            }
        }
        return counts.empty();
    }
};
