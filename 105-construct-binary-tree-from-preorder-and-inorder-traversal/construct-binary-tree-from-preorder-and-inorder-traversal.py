# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
       
        def dfs(left, right):
            nonlocal preorder_index
            if left > right:
                return None
            val = preorder[preorder_index]
            root = TreeNode(val)
            preorder_index +=1
            index = inorder.index(val)
            root.left = dfs(left, index-1)
            root.right = dfs(index+1, right)
            return root
        preorder_index = 0
        return dfs(0, len(preorder)-1)