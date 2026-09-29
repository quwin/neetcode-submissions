class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        // The answer is bounded between 0 and max(piles)
        // just binary search it ig
        int l = 1, r = 0;
        for (int pile : piles) {
            r = std::max(r, pile);
        }
        int minSpeed = r;
        while (l <= r) {
            int k = l + ((r - l) / 2);
            int steps = eatingSpeed(piles, k);
            if (steps > h) { // k too small
                l = k + 1;
            } else {
                r = k - 1;
            }
        }
        return l;
    }

    int eatingSpeed(vector<int>& piles, int k) {
        int count = 0;
        if (k == 0) {
            return 0;
        }
        for (auto pile : piles) {
            if (k >= pile) {
                count++;
            } else if (pile % k == 0) {
                count += pile/k;
            }
            else {
                count += (pile/k) + 1;
            }
        }
        return count;
    }
};
