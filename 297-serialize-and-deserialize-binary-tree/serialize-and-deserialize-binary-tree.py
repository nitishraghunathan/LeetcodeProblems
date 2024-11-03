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
        encoded_str = ""
        def dfs(root):
            nonlocal encoded_str
            if not root:
                encoded_str += 'null,'
                return
            encoded_str += str(root.val) + ','
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return encoded_str 
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print(data)
        encoded_list = data.split(",")
        def dfs(encoded_list):
            if not encoded_list:
                return None
            if encoded_list[0] == 'null':
                encoded_list.pop(0)
                return None
            root = TreeNode(int(encoded_list[0]))
            encoded_list.pop(0)
            root.left = dfs(encoded_list)
            root.right = dfs(encoded_list)
            return root
        return dfs(encoded_list)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))