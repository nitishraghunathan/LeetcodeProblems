# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def recursion(root: Optional[TreeNode], md: int) -> int:
            if not root:
                return 0, 0
            lh, lmd = recursion(root.left, md)
            rh, rmd = recursion(root.right, md)
            return max(rh,lh) + 1, max(lh+rh, lmd, rmd)
        return recursion(root, -1)[1]
        