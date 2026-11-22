# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        queue = []
        queue.append(root)
        while queue:
            size = len(queue)
            result = []
            for i in range(len(queue)):
                node = queue.pop(0)
                if not node:
                    result.append(float('-inf'))
                    continue
                result.append(node.val)
                if node.left:
                    queue.append(node.left)
                else:
                    queue.append(None)
                if node.right:
                    queue.append(node.right)
                else:
                    queue.append(None)
            left, right = 0, len(result)-1
            while left < right:
                if result[left]!=result[right]:
                    return False
                left+=1
                right-=1
        return True
            
        