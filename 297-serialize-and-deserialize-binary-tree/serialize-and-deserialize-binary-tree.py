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
        def serialize_string(root, encoded_str):
            if not root:
                return encoded_str + "null,"
            encoded_str += str(root.val) + ","
            encoded_str = serialize_string(root.left, encoded_str)
            encoded_str = serialize_string(root.right, encoded_str)
            return encoded_str
        return serialize_string(root, "")
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        result = data.split(",")
        def decoded_string(result):
            if result:
                if result[0] == 'null':
                    result.pop(0)
                    return None
                root = TreeNode(result[0])
                result.pop(0)
                root.left = decoded_string(result)
                root.right = decoded_string(result)
                return root
        
        return decoded_string(result)
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))