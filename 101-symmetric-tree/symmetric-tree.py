class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def is_mirror(left: TreeNode | None, right: TreeNode | None) -> bool:
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (
                left.val == right.val
                and is_mirror(left.left, right.right)
                and is_mirror(left.right, right.left)
            )

        return not root or is_mirror(root.left, root.right)