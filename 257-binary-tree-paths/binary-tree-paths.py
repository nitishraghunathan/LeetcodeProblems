# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(root, path, result):
            if root is None:
                return result
            if not root.left and not root.right:
                path += str(root.val)
                result.append(path)
                return result
            path += str(root.val) + '->'
            result = dfs(root.left, str(path), result)
            result = dfs(root.right, str(path), result)
            return result
        return dfs(root, '', [])