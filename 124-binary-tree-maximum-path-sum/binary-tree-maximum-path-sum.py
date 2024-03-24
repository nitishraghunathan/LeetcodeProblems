# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_value = float('-inf')
        def dfs(root):
            nonlocal max_value
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            return_value = root.val + max(left, right)
            max_value = max(max_value, max(return_value , max(root.val, left + right + root.val)))
            return max(root.val, return_value)
        max_value = max(dfs(root), max_value)
        return max_value
        