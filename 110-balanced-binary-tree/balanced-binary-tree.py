# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def is_balanced(root: Optional[TreeNode]) -> [bool, int]:
            if not root:
                return True, 0
            left, lheight = is_balanced(root.left)
            right, rheight = is_balanced(root.right)
            check_height = abs(lheight-rheight) < 2 and right and left
            return [check_height, max(rheight, lheight)+1]
        return is_balanced(root)[0]




        