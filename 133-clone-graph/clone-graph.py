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
        visited = set()
        def clone_graph(node: Optional['Node']):
            nonlocal map_dict
            if not node:
                return None
            new_node = None
            if node.val in map_dict:
                return  map_dict[node.val]
            else:
                map_dict[node.val] = Node(node.val)
                new_node = map_dict[node.val]
            new_node = map_dict[node.val]
            for child in node.neighbors:
                new_node.neighbors.append(clone_graph(child))
            return new_node
        return clone_graph(node) 
                
        