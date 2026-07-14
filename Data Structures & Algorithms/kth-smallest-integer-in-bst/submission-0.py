# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []

        def addToHeap(item: Optional[TreeNode]):
            if item is None:
                return
            addToHeap(item.left)
            heapq.heappush(heap, item.val)
            addToHeap(item.right)

        addToHeap(root)
        
        return heap[k-1]
            