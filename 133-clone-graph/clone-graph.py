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
        def recursion(node: Optional['Node'], map_dict: dict):
            if not node:
                return None
            if node.val in map_dict:
                return map_dict[node.val]
            new_node = Node(node.val)
            map_dict[new_node.val] = new_node
            for neighbor in node.neighbors:
                new_node.neighbors.append(recursion(neighbor, map_dict))
            return new_node
        return recursion(node, {})
            
                
        