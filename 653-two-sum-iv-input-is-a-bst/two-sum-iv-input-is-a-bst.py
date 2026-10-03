# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        new_set = set()
        result = [False]
        def recursion(root,k):
            if not root:
                return
            if (k - root.val in new_set):
                result[0] = True
            new_set.add(root.val)
            recursion(root.left, k)
            recursion(root.right, k)
            return 
        recursion(root, k)
        return result[0]



        