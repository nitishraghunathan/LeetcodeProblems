# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if root is None or root.val == x or root.val == y:
            return False 
        queue = []
        queue.append(root)
        level = 0
        level_x = -1 
        level_y = -1 
        parent_x = -1
        parent_y = -1
        while queue:
            size = len(queue)
            for i in range(size):
                temp = queue.pop(0)
                if temp.left:
                    queue.append(temp.left)
                    if temp.left.val == x:
                        parent_x = temp.val
                        level_x = level
                    if temp.left.val == y:
                        parent_y = temp.val
                        level_y = level
                if temp.right:
                    queue.append(temp.right)
                    if temp.right.val == x:
                        parent_x = temp.val
                        level_x = level
                    if temp.right.val == y:
                        parent_y = temp.val
                        level_y = level
            if parent_x != -1 and parent_y !=-1:
                return level_x == level_y and parent_x != parent_y
            level +=1
        return False