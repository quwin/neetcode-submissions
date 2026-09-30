class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;
        while (l <= r) {
            int i = l + ((r - l) / 2);
            if (nums[i] == target) {
                return i;
            } else if (nums[l] == target) {
                return l;
            } else if (nums[r] == target) {
                return r;
            } else if (nums[i] < nums[l]) { // Boundary on left
                if (nums[r] < target) {
                    r = i - 1;
                } else if (nums[i] > target) {
                    r = i - 1;
                } else {
                    l = i + 1;
                }
            } else if (nums[i] > nums[r]) { // Boundary on right
                if (nums[l] > target) {
                    l = i + 1;
                }  else if (nums[i] < target) {
                    l = i + 1;
                } else {
                    r = i - 1;
                }
            } else { // No rotation, do normal binary search
                if (nums[i] < target) {
                    l = i + 1;
                } else {
                    r = i - 1;
                }
            }
        }
        return -1;
    }
};
