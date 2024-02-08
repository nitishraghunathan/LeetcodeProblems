# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff= float('inf')
        def dfs(root: Optional[TreeNode], result: list):
            if root is None:
                return 
            nonlocal min_diff
            dfs(root.left, result)
            result.append(root.val)
            if len(result) > 1:
                min_diff = min(min_diff, result[len(result)-1]-result[len(result)-2])
            dfs(root.right, result)
            return 
        dfs(root, [])
        return min_diff



        