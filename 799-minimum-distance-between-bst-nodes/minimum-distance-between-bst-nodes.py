# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode | None) -> int:
        result = []
        min_val = float('inf')
        def recursion(root:TreeNode):
            if not root:
                return None
            recursion(root.left)  
            result.append(root.val)          
            recursion(root.right)
        recursion(root)
        for i in range(1, len(result)):
            min_val = min(result[i]- result[i-1], min_val)
        return min_val
        