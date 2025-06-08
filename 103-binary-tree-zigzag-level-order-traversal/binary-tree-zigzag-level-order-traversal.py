# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = []
        result = []
        queue.append(root)
        flag = False
        while queue:
            size = len(queue)
            new_queue = []
            for i in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                new_queue.append(node.val)
            if flag:
                result.append(list(reversed(new_queue)))
            else:
                result.append(list(new_queue))
            flag = not flag
        return result