# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid_bst(root, min_v, max_v):
            if not root:
                return True
            return  min_v < root.val < max_v and is_valid_bst(root.left, min_v, root.val) and is_valid_bst(root.right, root.val, max_v)
        return is_valid_bst(root, float('-inf'), float('inf'))
        
        