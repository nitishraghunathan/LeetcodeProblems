"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        map_dict = {}
        def dfs(node):
            if not node:
                return None
            if node.val in map_dict:
                new_node = map_dict[node.val]
                return new_node
            else:
                new_node = Node(node.val)
                map_dict[node.val] = new_node
            for nodes in node.neighbors:
                new_node.neighbors.append(dfs(nodes))
            return new_node
        return dfs(node)

        