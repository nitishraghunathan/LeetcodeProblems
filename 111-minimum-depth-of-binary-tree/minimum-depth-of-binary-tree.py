# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        min_value = [float('inf')]
        def depth(root: Optional[TreeNode], counter):
            if not root:
                return
            if not root.left and not root.right:
                min_value[0] = min(min_value[0], counter)
                return
            depth(root.left, counter+1)
            depth(root.right, counter+1)
        depth(root,1)
        return min_value[0] if min_value[0] != float('inf') else 0
            
        
        

        