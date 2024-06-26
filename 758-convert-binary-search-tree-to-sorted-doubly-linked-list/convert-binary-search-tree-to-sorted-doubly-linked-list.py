"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        first, last = None, None 
        if not root:
            return
        def dfs(root):
            nonlocal last, first
            if not root:
                return 
            dfs(root.left)
            if last:
                last.right = root
                root.left = last 
            else:
                first = root 
            last = root
            dfs(root.right)
        dfs(root)
        last.right = first 
        first.left = last 
        return first
        