# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest_value = float("inf")
        diff = float("inf")

        def helper(root: Optional[TreeNode], target: float) -> int:
            nonlocal closest_value, diff
            if not root:
                return 
            current_diff = abs(target - root.val)
            if current_diff < diff:
                diff = current_diff
                closest_value = root.val
            if current_diff == diff:
                closest_value = min(closest_value, root.val)
            helper(root.left, target)
            helper(root.right, target)
        helper(root, target)
        return closest_value
            
        