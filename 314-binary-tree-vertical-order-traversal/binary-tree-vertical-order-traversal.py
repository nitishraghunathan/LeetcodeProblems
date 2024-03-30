# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        map_dict = {}
        result= []
        if not root:
            return result
        queue = []
        queue.append((root,0))
        new_queue = []
        heapq.heapify(new_queue)
        while queue:
            size = len(queue)
            for i in range(size):
                node, index = queue.pop(0)
                if node.left:
                    queue.append((node.left, index-1))
                if node.right:
                    queue.append((node.right, index+1))
                if index not in map_dict:
                    map_dict[index] = []
                    heapq.heappush(new_queue, index)
                map_dict[index].append(node.val)

        while new_queue:
            result.append(map_dict[heapq.heappop(new_queue)])
        return result