"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        """
        1. First Understand the core problem statement
        2. A quad tree is a data structure which has 4 children
            a. Divide the quadrant into 4 children
            b. Iterate between the dimesnions of each quadrant and validate if all values are same
                1. if yes return it as a lead node
                2. if no we need to recurse further and compute the tree nodes meaning divide the quadtreenode into smaller quad tree nodes
                3. We do that till we reach the end of the dimensions
        """

        def dfs(n, r, c):
            all_values = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r+i][c+j]:
                        all_values = False
                        break
            if all_values:
                return Node(grid[r][c], True)
            n = n//2
            tl = dfs(n, r, c)
            tr = dfs(n, r, c+n)
            bl = dfs(n, r+n, c)
            br = dfs(n, r+n, c+n)
            return Node(0, False, tl, tr, bl, br)
        return dfs(len(grid),0,0)

        