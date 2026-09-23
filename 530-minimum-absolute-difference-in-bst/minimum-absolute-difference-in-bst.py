# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = float('inf')
        result = []
        def recursion(root:Optional[TreeNode], value:int):
            nonlocal min_diff
            if not root:
                return
            recursion(root.left, root.val)
            result.append(root.val)
            recursion(root.right, root.val)
        recursion(root, float('inf'))
        for i in range(1, len(result)):
            min_diff = min(min_diff, result[i]- result[i-1])
        return min_diff
        
            

        