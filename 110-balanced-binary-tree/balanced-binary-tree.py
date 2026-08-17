# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root:
                return True, 0
            left_bal, left_height = helper(root.left)
            right_bal, right_height = helper(root.right)
            return (abs(left_height - right_height) < 2) and left_bal and right_bal, 1 + max(left_height, right_height)
        return helper(root)[0]

        