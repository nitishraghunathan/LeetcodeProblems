# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        min_value = float('inf')
        value = -1
        def dfs(root: Optional[TreeNode], target: float):
            if root is None:
                return
            nonlocal min_value, value
            diff = abs(target - root.val)
            if diff < min_value:
                min_value = diff
                value = root.val
            if diff == min_value:
                value = min(root.val, value)
            dfs(root.left, target)
            dfs(root.right, target)
            return
        dfs(root, target)
        return value
            
