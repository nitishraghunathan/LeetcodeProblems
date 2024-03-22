# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(root, new_string):
            if not root:
                new_string += 'null,'
                return new_string
                return
            new_string += str(root.val) + ','
            new_string = dfs(root.left, new_string)
            new_string = dfs(root.right, new_string)
            return new_string
        return dfs(root, '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        new_list = data.split(',')
        def dfs(result):
            if result[0] == 'null':
                result.pop(0)
                return None
            root = TreeNode(int(result[0]))
            result.pop(0)
            root.left = dfs(result)
            root.right = dfs(result)
            return root
        return dfs(new_list)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))