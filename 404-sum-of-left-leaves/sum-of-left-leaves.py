# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total_sum = [0]
        def recursion(root, left=False):
            if root is None:
                return 
            if left and not root.right and not root.left:
                total_sum[0] +=root.val
                return
            recursion(root.left, True)
            recursion(root.right, False)
            return total_sum[0]
        recursion(root, False)
        return total_sum[0]
        