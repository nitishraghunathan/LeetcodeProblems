class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not p and not q:
            return None 
        while root.val != p.val and root.val != q.val:
            if root.val > p.val and root.val > q.val:
                root= root.left 
            elif root.val < p.val and root.val < q.val:
                root=root.right
            else:
                return root 
        return root