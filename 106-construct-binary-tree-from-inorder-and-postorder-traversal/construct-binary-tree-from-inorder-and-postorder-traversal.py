# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def create_binary_tree(inorder, postorder):
            if not postorder or not inorder:
                return None
            root = TreeNode(postorder[-1])
            index = inorder.index(postorder[-1])
            root.left = create_binary_tree(inorder[:index], postorder[:index])
            root.right = create_binary_tree(inorder[index+1:], postorder[index:-1])
            return root

        root_node = postorder[-1]

        return create_binary_tree(inorder, postorder)
