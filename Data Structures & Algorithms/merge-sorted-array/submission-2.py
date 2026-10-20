import heapq

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # To solve this, u essentially have to perform merge-sort inplace
        # How can u do that?
        # You can shift the entire nums1 whenever an item from nums2 is added
        # But that's O(n + m^2)
        # You can turn nums2 into a minHeap (so it stays sorted), and swap between nums1 and nums2
        # That's O(n + mlogn)
        # Then just keep track of m so the '0' placeholders dont mess you up
        # An O(n + m) solution probably exists but idk
        if not nums2:
            return
        for i in range(len(nums1)):
            if i >= m:
                nums1[i] = heapq.heappop(nums2)
            elif nums1[i] > nums2[0]:
                temp = nums1[i]
                nums1[i] = heapq.heappop(nums2)
                heapq.heappush(nums2, temp)
            



