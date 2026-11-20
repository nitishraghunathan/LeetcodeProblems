# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def balance(root:TreeNode | None) -> tuple:
            if not root:
                return True, 0
            left, lh = balance(root.left)
            right, rh = balance(root.right)
            return left and right and abs(lh-rh) <=1, max(lh, rh)+1
        return balance(root)[0]
        
        