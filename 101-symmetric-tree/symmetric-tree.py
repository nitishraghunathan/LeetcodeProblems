# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        We need to invert left -> right and check the inversion is equal(left maps to right and right maps to left unless they are singular), then we can call it symmetric. 
        """
        def symmetric(root1: Optional[TreeNode], root2: Optional[TreeNode])->bool:
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False
            return symmetric(root1.left, root2.right) and symmetric(root1.right, root2.left)
        return symmetric(root.right, root.left)