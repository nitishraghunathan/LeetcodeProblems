# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        queue = []
        min_val = float('inf')
        tree_node = None
        while root or queue:
            while root:
                queue.append(root)
                root = root.left
            node = queue.pop()
            if node.val > p.val:
                if not tree_node or tree_node.val > node.val:
                    tree_node = node
            root = node.right
        return tree_node

                