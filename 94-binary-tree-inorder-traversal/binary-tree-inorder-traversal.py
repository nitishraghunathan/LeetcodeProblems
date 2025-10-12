# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def helper(root: Optional[TreeNode], result:List[int]):
            if root is None:
                return result 
            result = helper(root.left, result)
            result.append(root.val)
            result = helper(root.right, result)
            return result
        return helper(root, result=[])