# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_path = float('-inf')
        def recursion(root):
            nonlocal max_path
            if not root:
                return 0, max_path
            left = recursion(root.left)
            right = recursion(root.right)
            max_path = max(max_path, left[0] + right[0])
            return 1 + max(left[0], right[0]), max_path
        return recursion(root)[1]

        