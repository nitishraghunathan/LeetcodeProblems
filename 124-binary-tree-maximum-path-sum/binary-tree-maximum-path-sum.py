# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    """
    There are three use cases in this scenairos 
    1. Return value = max of left and right + root.val 
    2. Root value 
    3. path within subtree -> root.val, left, right 
    4. When we return value max of return value + root.value
    """
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_value = float('-inf')
        def dfs(root):
            nonlocal max_value
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            return_value = root.val + max(left, right)
            max_value = max(max_value, max(return_value , root.val, left + right + root.val))
            return max(root.val, return_value)
        max_value = max(dfs(root), max_value)
        return max_value
        