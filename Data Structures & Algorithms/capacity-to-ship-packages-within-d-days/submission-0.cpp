class Solution {
public:
    int shipWithinDays(vector<int>& weights, int days) {
        // Minimum possible capacity: max(weights)
        // Maximum possible capacity: sum(weights)
        // Monotonic feasibility predicate: idk
        // Why the simulation is greedy: packing as much as possible
        // is always helpful for later days
        // Why the result is the first feasible capacity: duh
        // Trying binary search first
        int l = 0, r = 0;
        for (int& weight : weights) {
            r += weight;
            l = std::max(l, weight);
        }
        while(l < r) {
            int m = l + ((r - l) / 2);
            long long daysTaken = shipDays(weights, m);
            if (daysTaken > days) {
                l = m + 1;
            } else {
                r = m;
            }
        }
        return r;
    }

    long long shipDays(vector<int>& weights, int size) {
        long long count = 1;
        int carrying = 0;
        for (int& weight : weights) {
            if (carrying + weight > size) {
                count++;
                carrying = 0;
            }
            carrying += weight;
        }
        return count;
    }
};