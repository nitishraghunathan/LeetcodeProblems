class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        Construct a graph from teh tree and find all nodes at distance K
        """
        graph_dict = {}
        def dfs_graph_construct(root, parent):
            if not root:
                return
            if parent:
                if root.val not in graph_dict:
                    graph_dict[root.val] = []
                if parent.val not in graph_dict:
                    graph_dict[parent.val] = []
                graph_dict[root.val].append(parent.val)
                graph_dict[parent.val].append(root.val)
            dfs_graph_construct(root.left, root)
            dfs_graph_construct(root.right, root)
            return
        dfs_graph_construct(root, None)
        queue = []
        visited = set()
        result = []
        queue.append(target.val)
        visited.add(target.val)
        while queue and k > -1:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if k == 0:
                    result.append(node)
                for neighbor in graph_dict.get(node, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            k-=1
            if k == -1:
                return result
        return result


            