# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = []
        queue.append([root, 0])
        max_width = float('-inf')
        while queue:
            size = len(queue)
            start_point = queue[0][1]
            for i in range(size):
                node, direction  = queue.pop(0)
                if node.left:
                    queue.append([node.left, 2*direction])
                if node.right:
                    queue.append([node.right, 2*direction+1])
                max_width = max(max_width, abs(start_point - direction) +1)
        return max_width

            

        