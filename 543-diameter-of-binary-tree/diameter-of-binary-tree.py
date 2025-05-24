# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_value = float('-inf')
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameter_binary_tree(root: Optional[TreeNode]):
            if not root:
                return 0
            left = diameter_binary_tree(root.left)
            right = diameter_binary_tree(root.right)
            self.max_value = max(self.max_value, left+right)
            return max(left,right) + 1
        diameter_binary_tree(root)
        return self.max_value

        