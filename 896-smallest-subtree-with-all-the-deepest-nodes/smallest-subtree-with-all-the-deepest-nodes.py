# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if not root:
                return None, 0 
            node1, depth1 = dfs(root.left)
            node2, depth2 = dfs(root.right)
            if depth1 == depth2:
                return root, depth1+1
            elif depth1 < depth2:
                return node2, depth2+1
            else:
                return node1, depth1+1
        node1, depth1= dfs(root)
        return node1
            