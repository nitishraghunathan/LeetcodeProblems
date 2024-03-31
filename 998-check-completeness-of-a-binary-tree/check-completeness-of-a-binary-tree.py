# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = []
        flag =False
        queue.append(root)
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if not node:
                    flag =True
                    continue
                else:
                    if flag:
                        return False
                    queue.append(node.left)
                    queue.append(node.right)
        return True
