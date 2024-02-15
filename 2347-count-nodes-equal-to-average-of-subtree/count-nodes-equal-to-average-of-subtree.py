# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Count number of nodes wehre value of nodes = number of trees, return [sum, count]
    each node will return [sum+val, count of nodes per subtree, global count]
    """
    def averageOfSubtree(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, array: List[int]):
            if not root:
                return array
            left_array = dfs(root.left, list(array))
            right_array = dfs(root.right, list(array))
            new_array = [right_array[i] + left_array[i] for i in range(3)]
            new_array[0] += root.val
            new_array[1] += 1
            if root.val == math.floor(new_array[0]/new_array[1]):
                new_array[2] +=1
            return new_array
        return dfs(root, [0,0,0])[2]
        