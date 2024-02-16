# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(root1: TreeNode, root2: TreeNode, result: list):
            if not root1 and not root2:
                return result
            elif not root1:
                dfs(root1, root2.left, result)
                result.append(root2.val)
                dfs(root1, root2.right, result)
                return result
            elif not root2:
                dfs(root1.left, root2, result)
                result.append(root1.val)
                dfs(root1.right, root2, result)
                return result
            else:
                dfs(root1.left, root2.left, result)
                result.append(min(root1.val, root2.val))
                result.append(max(root1.val, root2.val))
                dfs(root1.right, root2.right, result)
            return result
        return sorted(dfs(root1, root2, []))