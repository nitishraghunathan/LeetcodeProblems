# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if not root or not p:
            return None
        stack = []
        flag = False
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            if flag:
                return node
            if node.val == p.val:
                flag =True
            if node.right:
                root = node.right
        return None
        