# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate_binary_search_tree(root: Optional[TreeNode] , max_value: int, min_value: int) -> bool:
            if not root:
                return True
            if root.val <= min_value or root.val >= max_value:
                return False
            return validate_binary_search_tree(root.left, root.val, min_value) and validate_binary_search_tree(root.right, max_value, root.val)
        return validate_binary_search_tree(root, float('inf'), float('-inf'))
        
        