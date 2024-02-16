# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(root, result):
            if not root:
                return result, True
            if root.right is None and root.left is None:
                result.append(root.val)
                return result, True
            result, left = dfs(root.left, result)
            result, right = dfs(root.right, result)
            if left:
                root.left = None
            if right:
                root.right = None
            return result, False
        final_result=[]
        start = root
        while root:
            if root.left is None and root.right is None:
                final_result.append([root.val])
                break
            final_result.append(dfs(root, [])[0])
        return final_result

        