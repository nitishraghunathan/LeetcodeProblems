# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        def dfs(root, targetSum, number_list):
            nonlocal result
            if not root:
                return result
            number_list.append(root.val)
            if root.left is None and root.right is None:
                if targetSum - root.val == 0:
                    result.append(list(number_list))
                number_list.pop()
                return result
            result = dfs(root.left, targetSum-root.val, number_list)
            result = dfs(root.right, targetSum-root.val, number_list)
            number_list.pop()
            return result
        return dfs(root, targetSum, [])

        