# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = float('inf')
        previous_val = float('inf')
        def helper(root):
            nonlocal min_diff, previous_val
            if not root:
                return
            helper(root.left)
            if min_diff > abs(root.val - previous_val):
                min_diff = abs(root.val - previous_val)
            previous_val = root.val
            helper(root.right)
        helper(root)
        return min_diff