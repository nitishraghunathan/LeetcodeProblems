# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        max_value = -1
        def dfs(root: Optional[TreeNode], map_dict: dict):
            if root is None:
                return
            nonlocal max_value
            if root.val not in map_dict:
                map_dict[root.val] = 0
            map_dict[root.val] +=1
            max_value = max(map_dict[root.val], max_value)
            dfs(root.left, map_dict)
            dfs(root.right, map_dict)
        map_dict = {}
        dfs(root, map_dict)
        result = []
        for key, value in map_dict.items():
            if value == max_value:
                result.append(key)
        return result