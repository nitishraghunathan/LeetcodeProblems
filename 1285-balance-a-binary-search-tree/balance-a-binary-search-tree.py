# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def dfs(root:TreeNode, result):
            if root is None:
                return result
            result = dfs(root.left, result)
            result.append(root.val)
            result = dfs(root.right, result)
            return result
        def create_tree(result, low, high):
            if low > high:
                return None
            mid = low + (high-low)//2
            root = TreeNode(result[mid])
            root.left = create_tree(result, low, mid-1)
            root.right = create_tree(result, mid+1, high)
            return root
        result = dfs(root, [])
        return create_tree(result, 0, len(result)-1)
        
        
        