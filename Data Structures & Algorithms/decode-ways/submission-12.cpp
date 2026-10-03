class Solution {
public:
    int numDecodings(string s) {
        // State: f(i) # of ways to decode suffix starting at i
        // Choices: take solo and/or take combined / invalid
        // Transition: SUM(priorPrior + prior) if valid else priorPrior
        // Base cases: prior = 1 (one way to make empty string)
        // Evaluation order: bottom-up suffixes
        int priorPrior = 0, prior = 1;
        for (int i = s.size()-1; i > -1; i--) {
            if (s[i] == '0') {
                priorPrior = prior;
                prior = 0;
            } else if (s.size() - 1 != i and stoi(s.substr(i, 2)) > 26) {
                priorPrior = prior;
            }
            else {
                int temp = priorPrior;
                priorPrior = prior;
                prior += temp;
            }
        }
        return prior;
    }
};
