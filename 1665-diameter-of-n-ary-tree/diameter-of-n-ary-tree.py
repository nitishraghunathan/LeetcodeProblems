"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        max_diameter = 0
        def dfs(root):
            nonlocal max_diameter
            if len(root.children) == 0:
                return 0
            max_height_one, max_height_two = 0, 0
            for index, children in enumerate(root.children):
                parent_height = dfs(children) + 1
                if parent_height > max_height_one:
                    max_height_one, max_height_two = parent_height, max_height_one
                elif parent_height > max_height_two:
                    max_height_two = parent_height
            max_diameter = max(max_diameter, max_height_one + max_height_two)
            return max_height_one
        dfs(root)
        return max_diameter