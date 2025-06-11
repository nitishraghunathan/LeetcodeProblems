# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        The concept used is here is that we construct a graph from a tree and then use a bfs and gather all nodes with distance K
        """
        graph_dict = {}
        def construct_graph(child:TreeNode, parent: TreeNode):
            if not child:
                return None
            if parent:
                if child.val not in graph_dict:
                    graph_dict[child.val] = []
                if parent.val not in graph_dict:
                    graph_dict[parent.val] = []
                graph_dict[child.val].append(parent.val)
                graph_dict[parent.val].append(child.val)
            construct_graph(child.left, child)
            construct_graph(child.right, child)
        construct_graph(root, None)
        visited = set()
        queue = []
        queue.append(target.val)
        visited.add(target.val)
        counter = 0
        result = []
        while queue:
            size = len(queue)
            for i in range(size):
                val = queue.pop(0)
                if counter == k:
                    result.append(val)
                for values in graph_dict.get(val, []):
                    if values not in visited:
                        visited.add(values)
                        queue.append(values)

            counter +=1
        return result

        