# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = []
        queue.append(root)
        average = []
        while queue:
            size = len(queue)
            total_sum = 0
            for i in range(size):
                node = queue.pop(0)
                total_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            average.append(total_sum/size)
        return average