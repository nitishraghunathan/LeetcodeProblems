# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def dfs(preorder, lower, upper):
            if not preorder:
                return None
            if preorder[0] < lower or preorder[0] > upper:
                return None
            root = TreeNode(preorder.pop(0))
            root.left = dfs(preorder,lower, root.val)
            root.right = dfs(preorder, root.val, upper)
            return root
        return dfs(preorder, float('-inf'), float('inf'))