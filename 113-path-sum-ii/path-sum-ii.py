# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(root: Optional[TreeNode], result:list, total_path:list, targetSum:int, total_sum:int):
            if not root:
                return total_path
            result.append(root.val)
            if not root.left and not root.right:
                if root.val + total_sum == targetSum:
                    total_path.append(list(result))
                    return total_path
            total_path = dfs(root.left, list(result), total_path, targetSum, total_sum + root.val)
            total_path = dfs(root.right, list(result), total_path, targetSum, total_sum + root.val)
            return total_path
        return dfs(root,[],[], targetSum, 0)

        