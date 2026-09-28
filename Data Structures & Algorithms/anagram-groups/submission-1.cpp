class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<string, vector<string>> ans;
        for (int i = 0; i < strs.size(); i++) {
            std::string str = strs[i];
            std::sort(str.begin(), str.end());
            if (ans.find(str) == ans.end()) {
                ans[str] = std::vector<string>();
            }
            ans.at(str).push_back(strs[i]);
        }
        std::vector<vector<string>> values;
        values.reserve(ans.size());
        for (const auto& pair : ans) {
            values.push_back(pair.second);
        }
        return values;
    }
};
