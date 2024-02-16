# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        def dfs(root, result:list[int]):
            if not root:
                return 0
            left = dfs(root.left, result)
            right =dfs(root.right, result)
            if left+right == root.val:
                result[0] += 1
            return root.val +left +right
        result = [0]
        dfs(root,result)
        return result[0]