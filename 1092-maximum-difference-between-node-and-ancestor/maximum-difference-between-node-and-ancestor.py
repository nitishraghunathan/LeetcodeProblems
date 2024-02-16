# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        difference = float('-inf')
        def dfs(root, result):
            nonlocal difference
            if root is None:
                return
            for val in result:
                difference = max(abs(root.val-val), difference)
            result.append(root.val)
            copy_a = list(result)
            copy_b = list(result)
            dfs(root.left, copy_a)
            dfs(root.right, copy_b)
            return
        dfs(root, [])
        return difference

