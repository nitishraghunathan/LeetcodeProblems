# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def recursion(nums, low, high):
            if low > high:
                return None
            mid = low + (high-low)//2
            root = TreeNode(nums[mid])
            root.left = recursion(nums, low, mid-1)
            root.right = recursion(nums, mid+1, high)
            return root
        return recursion(nums,0, len(nums)-1)
        