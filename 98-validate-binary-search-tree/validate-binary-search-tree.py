# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        1.left child's value < root node's value
        2.right child's value > root node's value
        3. we need to check this at all subtrees.
        4. If node is None return True 
        """
        def validate_bst(root: Optional[TreeNode], min_value:int, max_value:int):
            if root is None:
                return True
            return (root.val > min_value and root.val < max_value) and validate_bst(root.left, min_value,  root.val) and validate_bst(root.right, root.val, max_value)
        return validate_bst(root, float('-inf'), float('inf'))
        