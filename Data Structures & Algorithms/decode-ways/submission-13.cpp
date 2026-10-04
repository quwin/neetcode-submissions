class Solution {
public:
    int numDecodings(string s) {
        // State 1: # of possible combinations of decoding suffix at i
        // Change: 
            // If new num is separate (9 < num < 26), prior + priorPrior
            // If not separate = prior, unless prior = 0 then priorPrior
            // If 0 = 0
        int priorPrior = 0, prior = 1;
        for (int i = s.size()-1; i > -1 ; i--) {
            if (s[i] == '0') {
                priorPrior = prior;
                prior = 0;
            } else if (i < s.size()-1 && stoi(s.substr(i, 2)) <= 26) {
                int temp = priorPrior;
                priorPrior = prior;
                prior += temp;
            } else {
                priorPrior = prior;
            }
        }
        return prior;
    }
};
