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
        def helper(root, encoded_str:str):
            if not root:
                return encoded_str + "null,"
            encoded_str += str(root.val) + ","
            encoded_str = helper(root.left, encoded_str)
            encoded_str = helper(root.right, encoded_str)
            return encoded_str
        return helper(root, "")

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        def helper(data):
            if not data:
                return None
            node = data.pop(0)
            if node == 'null' :
                return None
            root = TreeNode(node)
            root.left = helper(data)
            root.right = helper(data)
            return root
        return helper(data)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))