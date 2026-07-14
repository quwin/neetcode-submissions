# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], leftMin = None, rightMax = None) -> bool:
        if not root:
            return True
        if root.left and (root.left.val >= root.val or (leftMin is not None and root.left.val <= leftMin)):
            return False
        if root.right and (root.right.val <= root.val or (rightMax is not None and root.right.val >= rightMax)):
            return False
        leftValid = self.isValidBST(root.left, leftMin, min(rightMax, root.val) if rightMax else root.val)
        rightValid = self.isValidBST(root.right, max(leftMin, root.val) if leftMin else root.val, rightMax)
        return leftValid and rightValid
        