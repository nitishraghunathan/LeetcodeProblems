# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(root: Optional[TreeNode]):
            if root is None:
                return 0
            if root.val > high:
                return dfs(root.left)
            if root.val < low:
                return dfs(root.right)
            return root.val + dfs(root.right) + dfs(root.left)
        return dfs(root)
