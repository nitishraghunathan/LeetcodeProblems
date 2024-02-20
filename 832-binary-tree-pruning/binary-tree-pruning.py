# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root:Optional[TreeNode]):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if right !=1:
                    root.right = None
            if left !=1:
                    root.left = None
            if left == 1 or right == 1 or root.val == 1:
                return 1
            return root.val
        val = dfs(root)
        return root if val else None