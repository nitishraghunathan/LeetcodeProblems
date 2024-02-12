# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        min_value = float('inf')
        def dfs(root:Optional[TreeNode], node_count):
            if root is None:
                return
            nonlocal min_value
            if not root.left and not root.right:
                node_count +=1
                min_value = min(min_value, node_count)
                return
            dfs(root.left, node_count +1)
            dfs(root.right, node_count +1)
            return 
        dfs(root, 0)
        return min_value if min_value!= float('inf') else 0
