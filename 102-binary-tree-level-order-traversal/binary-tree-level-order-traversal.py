# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        1. Level order traversal of binary tree 
        2. Add the root node to the queue
        3. Traverse the children from left to right
        4. Remove the ndoes form the queue 
        5. Again add the nodes for each level
        6. store these nodes in an array
        """
        helper_queue = []
        final_list=[]
        if root is None:
            return None
        helper_queue.append(root)
        while helper_queue:
            size = len(helper_queue)
            result_order_list = []
            for i in range(size):
                polled_node = helper_queue.pop(0)
                if polled_node.left:
                    helper_queue.append(polled_node.left)
                if polled_node.right:
                    helper_queue.append(polled_node.right)
                result_order_list.append(polled_node.val)
            final_list.append(result_order_list)
        return final_list
