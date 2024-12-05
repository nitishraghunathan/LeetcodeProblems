class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.right, self.left = Node(0,0), Node(0,0)
        self.right.prev , self.left.next = self.left, self.right
        self.cache = {}
        

    def insert(self, node: Optional['Node']):
        prev, next = self.right.prev, self.right
        node.next, node.prev = next, prev
        prev.next, next.prev = node, node

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) == self.capacity:
                node = self.left.next
                self.remove(node)
                self.cache.pop(node.key)
            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)
        else:
            node = self.cache[key]
            self.remove(node)
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.insert(new_node)
        
class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)