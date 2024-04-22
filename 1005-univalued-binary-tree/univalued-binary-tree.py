# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, prev):
            if not root:
                return True 
            if root.val != prev.val:
                return False 
            return dfs(root.left, root) and dfs(root.right, root)
        return dfs(root, root)
        