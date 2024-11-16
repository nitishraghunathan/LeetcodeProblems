# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        We have a root node left, right child 
        Need to find the deepest level and return the max depth(level)
        if the return is None we return 0
        """
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))


        
        